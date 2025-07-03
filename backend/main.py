# at the top of main.py
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
from fastapi import FastAPI, Request, UploadFile, File, Form, Depends , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from auth import router as auth_router
from models import Item
from database import items_col,feedback_col
import os
import uuid
from ai_matcher import match_with_gemini

app = FastAPI()
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
UPLOAD_DIR = "uploads"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

@app.post("/report_found")
async def report_found(
    item_name: str = Form(...),
    description: str = Form(...),
    date: str = Form(...),
    time: str = Form(...),
    location: str = Form(...),
    contact_info: str = Form(...),
    priority: bool = Form(False),
    image: UploadFile = File(...)
):
    filename = f"{uuid.uuid4()}_{image.filename.replace(' ', '_')}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        content = await image.read()
        f.write(content)

    image_url = f"/uploads/{filename}"

    item = {
        "item_name": item_name,
        "description": description,
        "date": date,
        "time": time,
        "location": location,
        "contact_info": contact_info,
        "priority": priority,
        "image_url": image_url,
        "type": "found",
        "is_claimed": False
    }
    inserted = items_col.insert_one(item)

    # Run Gemini matching in background (pseudo for now)
    # match_with_gemini(item)

    return {"message": "Found item reported successfully"}

@app.get("/stats")
def get_stats():
    total = items_col.count_documents({})
    found = items_col.count_documents({"type": "found"})
    lost = items_col.count_documents({"type": "lost"})
    return {
        "total_items": total,
        "found_items": found,
        "lost_items": lost
    }

from fastapi import Depends
from auth import get_current_user  # or however you're getting current user

@app.post("/report_lost")
async def report_lost(
    item_name: str = Form(...),
    description: str = Form(...),
    date: str = Form(...),
    time: str = Form(...),
    location: str = Form(...),
    contact_info: str = Form(...),
    priority: bool = Form(False),
    image: UploadFile = File(...),
    wants_call: bool = Form(False),
    user: dict = Depends(get_current_user)  # ✅ Inject the current user from token
):
    filename = f"{uuid.uuid4()}_{image.filename.replace(' ', '_')}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        content = await image.read()
        f.write(content)

    image_url = f"/uploads/{filename}"

    item = {
        "item_name": item_name,
        "description": description,
        "date": date,
        "time": time,
        "location": location,
        "contact_info": contact_info,
        "priority": priority,
        "wants_call": wants_call,
        "image_url": image_url,
        "type": "lost",
        "is_claimed": False,
        "reporter_email": user["email"]  # ✅ Store who submitted it
    }

    items_col.insert_one(item)

    # Run AI match
    # match_with_gemini(item)

    return {"message": "Lost item reported successfully"}

from fastapi import Query
from typing import Optional
@app.get("/browse")
def get_unclaimed_found_items(user_email: Optional[str] = Query(None)):
    query = {"type": "found", "is_claimed": False}
    
    if user_email:
        query["reporter_email"] = {"$ne": user_email}

    items = list(items_col.find(query))
    for item in items:
        item["_id"] = str(item["_id"])
    return items



from bson import ObjectId
def sanitize_item(item):
    item["_id"] = str(item["_id"])
    return item

@app.get("/admin")

def get_admin_items():
    return [sanitize_item(item) for item in items_col.find({"is_claimed": False})]


from datetime import datetime



# POST: Collect feedback
@app.post("/feedback")
def submit_feedback(name: str = Form(...), email: str = Form(None), message: str = Form(...)):
    feedback = {
        "name": name,
        "email": email,
        "message": message,
        "date": datetime.utcnow()
    }
    feedback_col.insert_one(feedback)
    return {"message": "Thank you for your feedback!"}

# GET: Fetch all feedbacks
@app.get("/feedbacks")
def get_feedbacks():
    feedbacks = []
    for fb in feedback_col.find().sort("date", -1):  # latest first
        feedbacks.append({
            "id": str(fb.get("_id")),
            "name": fb.get("name", "Anonymous"),
            "email": fb.get("email"),
            "message": fb.get("message"),
            "date": fb.get("date").strftime("%Y-%m-%d %H:%M:%S") if fb.get("date") else "Unknown"
        })
    return feedbacks

from bson import ObjectId
from bson.errors import InvalidId
@app.post("/agent_request")
def agent_assist(item_id: str):
    try:
        item = items_col.find_one({"_id": ObjectId(item_id)})
        if not item:
            raise HTTPException(404, detail="Item not found")
    except InvalidId:
        raise HTTPException(400, detail="Invalid item ID format")

    response = model.generate_content(f"""
    You are an expert AI lost-and-found assistant. The user reported:
    {item['description']}
    
    Based on this, suggest any additional details they could provide to improve matching.
    """)
    
    return {"agent_response": response.text.strip()}

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os



# Serve index, login, signup directly
@app.get("/")
def read_index():
    return FileResponse("frontend/index.html")

@app.get("/login")
def serve_login():
    return FileResponse("frontend/login.html")

@app.get("/signup")
def serve_signup():
    return FileResponse("frontend/signup.html")

from fastapi import Body
from bson import ObjectId
from database import items_col  # assuming this is your Mongo collection
from notif import send_email  # make sure you have this utility

from fastapi import Form, UploadFile, File

@app.post("/claim/{item_id}")
async def claim_item(
    item_id: str,
    name: str = Form(...),
    contact: str = Form(...),
    proof: str = Form("")
):
    item = items_col.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found.")

    found_user_email = item["contact_info"]
    subject = f"[LostLink AI] Claim Request for: {item['item_name']}"
    message = f"""
    🔎 Someone has claimed the item you reported as FOUND!

    🧑 Claimer Name: {name}
    📞 Contact: {contact}
    📄 Proof: {proof or "Not provided"}

    Please reach out to verify.
    """

    send_email(to=found_user_email, subject=subject, body=message)
    return {"message": "Claim sent to item reporter."}


@app.post("/admin/approve/{item_id}")
def approve_item(item_id: str):
    result = items_col.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"is_claimed": True}}
    )
    if result.modified_count == 1:
        return {"msg": "Item marked as claimed"}
    raise HTTPException(status_code=404, detail="Item not found")
