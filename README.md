# 🔍 LostLink AI — Smart Lost & Found System

## A powerful AI-driven Lost & Found system that makes item recovery 𝐬𝐦𝐚𝐫𝐭𝐞𝐫, 𝐟𝐚𝐬𝐭𝐞𝐫 and 𝐞𝐟𝐟𝐨𝐫𝐭𝐥𝐞𝐬𝐬.

LostLink AI is a fully functional, AI-powered Lost & Found web application that helps users report, browse, and claim lost or found items using intelligent matching algorithms and real-time communication support.

🔧 Every part of the system – from the frontend to the AI engine – was built from scratch, focusing on 𝐬𝐢𝐦𝐩𝐥𝐢𝐜𝐢𝐭𝐲, 𝐬𝐩𝐞𝐞𝐝, 𝐚𝐧𝐝 𝐮𝐬𝐚𝐛𝐢𝐥𝐢𝐭𝐲. No heavy frameworks, just 𝐜𝐥𝐞𝐚𝐧 𝐥𝐨𝐠𝐢𝐜 𝐚𝐧𝐝 𝐭𝐡𝐨𝐮𝐠𝐡𝐭𝐟𝐮𝐥 𝐝𝐞𝐬𝐢𝐠𝐧.

Built by [Rohith](https://github.com/JustCool0208) and [Rohan](https://github.com/RohanAM-286).

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


## 📸 Screenshots and feature highlights are added.

The attachments include the core website functions + admin dashboard and it includes screenshots of the mails and call done by AI agent.

![1751479924237](https://github.com/user-attachments/assets/a07b75f3-78a6-43d4-9fbd-3b7c20d54c9e)
![1751479924220](https://github.com/user-attachments/assets/39090ef8-3a27-4e4d-aca7-64c32a391d40)

![1751479924263](https://github.com/user-attachments/assets/0566edd4-74e6-4438-ad68-70c02f771aeb)

![1751479924241](https://github.com/user-attachments/assets/e523c883-130d-4b9d-bc29-84ffb2cdf3bd)
![1751479924224](https://github.com/user-attachments/assets/f60d3b2e-d7b0-45b2-8c20-a0420896c37e)
![1751479924228](https://github.com/user-attachments/assets/c38c7aa9-6c60-4eeb-8c5b-b13f53be8fb9)
![1751479924216](https://github.com/user-attachments/assets/55290fbe-b2d6-48d7-a21c-55680003fe7d)
![1751479924251](https://github.com/user-attachments/assets/1293d2dc-0596-4fff-b188-3da5f581b2a6)
![1751479924278](https://github.com/user-attachments/assets/77dfc568-e69a-4832-997f-9ae4d180635a)
![1751479924215](https://github.com/user-attachments/assets/af9503bb-1c2b-41ca-ae32-d155cdedf544)
![1751479924223](https://github.com/user-attachments/assets/72d17d14-6eaf-45ba-be52-72f7abd18f3f)
![1751479924299](https://github.com/user-attachments/assets/d629551f-3cd9-4ac4-a33d-ebf748ffbde9)
![1751479924266](https://github.com/user-attachments/assets/40ad8ef3-490d-4099-afc6-579a3e14ab90)
![1751479924564](https://github.com/user-attachments/assets/cea1b91c-6065-408c-a4ab-aaeb7a2a85c1)

![1751479924564](https://github.com/user-attachments/assets/8123cec9-fc92-4b9a-9f5a-b02463c4106c)
![1751479924208](https://github.com/user-attachments/assets/cecdb004-99b9-4757-9641-ee78652ae719)
![1751479924211](https://github.com/user-attachments/assets/68aef4d3-a2c5-480f-8770-bf4ad57b7f1e)
![1751479924197](https://github.com/user-attachments/assets/e5552d7a-d786-40ad-9657-308907d6f207)
