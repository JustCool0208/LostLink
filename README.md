# 🔍 LostLink AI — Smart Lost & Found System

LostLink AI is a fully functional, AI-powered Lost & Found web application that helps users report, browse, and claim lost or found items using intelligent matching algorithms and real-time communication support.

Built with love ❤️ and logic by [Rohith](https://github.com/JustCool0208) and [Rohan](https://github.com/RohanAM-286).

---

## 🚀 Features

- 🔐 **User Authentication** (JWT-based)
- 📝 Report **Lost** or **Found** items with image uploads
- 🧠 **AI Matching** using:
  - **Gemini API** (Google)
  - **Sentence-Transformers** (semantic similarity)
- 🎯 **Priority Flag** to lower match threshold for critical reports
- 📨 **Email alerts** + 📞 **AI agent call support** (Twilio-ready)
- 👨‍💼 Admin Dashboard to manage claims and submissions
- 📊 Realtime Stats on total/lost/found items
- 💬 Feedback system to collect user input
- ✅ Minimal frontend: HTML + CSS + JS
- ⚙️ FastAPI backend with MongoDB
- 🧼 Clean UI & responsive design

---

## 🛠️ Tech Stack

| Layer      | Tools Used                                   |
|------------|----------------------------------------------|
| Frontend   | HTML, CSS, JavaScript (no frameworks)        |
| Backend    | Python, FastAPI                              |
| Database   | MongoDB                                      |
| AI Matching| Gemini API + Sentence-Transformers           |
| Auth       | JWT (via jose)                               |
| Storage    | Local file uploads (FastAPI static mount)    |
| Communication | Email + optional Twilio integration       |

---

## 🔁 API Overview

> FastAPI backend with 15+ endpoints  
> All routes are CORS-enabled and token protected where needed.

### Key Endpoints

| Method | Endpoint             | Description                          |
|--------|----------------------|--------------------------------------|
| `POST` | `/signup`            | Register user                        |
| `POST` | `/login`             | Get JWT token                        |
| `GET`  | `/browse`            | Browse unclaimed items               |
| `POST` | `/report_lost`       | Submit a lost item                   |
| `POST` | `/report_found`      | Submit a found item                  |
| `POST` | `/claim/{item_id}`   | Claim an item (AI matching runs)     |
| `GET`  | `/admin`             | View all unverified items (admin)    |
| `POST` | `/admin/approve/{id}`| Mark item as claimed                 |
| `POST` | `/feedback`          | Submit user feedback                 |
| `GET`  | `/stats`             | View total, lost, and found counts   |

_(Full list in code)_

---

## 🔒 Authentication

- JWT-based login/signup
- Token must be attached 

## 📸 Screenshots
![1751479924237](https://github.com/user-attachments/assets/a07b75f3-78a6-43d4-9fbd-3b7c20d54c9e)
![1751479924220](https://github.com/user-attachments/assets/39090ef8-3a27-4e4d-aca7-64c32a391d40)

![1751479924263](https://github.com/user-attachments/assets/0566edd4-74e6-4438-ad68-70c02f771aeb)

![1751479924241](https://github.com/user-attachments/assets/e523c883-130d-4b9d-bc29-84ffb2cdf3bd)
![1751479924224](https://github.com/user-attachments/assets/f60d3b2e-d7b0-45b2-8c20-a0420896c37e)
![1751479924228](https://github.com/user-attachments/assets/c38c7aa9-6c60-4eeb-8c5b-b13f53be8fb9)
![1751479924216](https://github.com/user-attachments/assets/55290fbe-b2d6-48d7-a21c-55680003fe7d)
[1751479924564](https://github.com/user-attachments/assets/bffa6789-b567-4005-8236-9a1182f3cc87)
[1751479924266](https://github.com/user-attachments/assets/e390e668-6ead-430e-af79-4e22fc53f70a)
[1751479924215](https://github.com/user-attachments/assets/d4f7fb17-fee4-49d6-be74-db4b6c30f14c)
![1751479924251](https://github.com/user-attachments/assets/0db6af72-d72d-4b6c-8b3c-ffd70f883d9c)


