# ♻️ CleanCam AI

**AI-Powered Garbage Detection & Automated Complaint System**

CleanCam AI is a computer vision–based smart civic solution that detects garbage accumulation in public areas and automatically registers complaints to the appropriate government portal when the situation becomes severe.

---

## 🌍 Problem Statement

Urban areas frequently face garbage overflow issues due to delayed reporting and manual complaint processes. Citizens often:

* Ignore waste accumulation
* Don’t know where to report
* Avoid the effort required to file complaints

This leads to:

* Health hazards
* Poor sanitation
* Environmental pollution

**CleanCam AI solves this by automating the entire complaint pipeline.**

---

## 💡 Solution Overview

CleanCam AI uses:

* Computer Vision to detect garbage in images
* Machine Learning to classify severity
* Automation to register complaints when needed

The system can work with:

* CCTV cameras
* Mobile images
* Drone footage

Once garbage crosses a defined severity threshold, the AI automatically sends a complaint to the government portal.

---

## 🚀 Key Features

### 🧠 Garbage Detection

Detects garbage presence from images using ML models.

### 📊 Severity Classification

Classifies garbage into levels:

* Low
* Medium
* High
* Critical

### 🤖 Automated Complaint Filing

When severity reaches **High or Critical**, the system:

1. Generates a complaint message
2. Sends image evidence
3. Send Complaint to the official Mail, and stores data in Google Sheet


### 📡 Real-Time Monitoring (Future)

Will implement this in cameras for live and real time video feeds.

---

## 🏗️ Project Architecture

```
User Image / CCTV Feed
        ↓
Garbage Detection Model
        ↓
Severity Prediction Model
        ↓
Decision Engine
        ↓
Complaint Automation API
        ↓
Send Mail and Sore Data in Sheet
        ↓
Update the information on Dashboard
```

---

## 📁 Project Structure

```
📦src
 ┣ 📂dashboard_api
 ┃ ┣ 📂services
 ┃ ┃ ┣ 📜sheets_services.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂static
 ┃ ┃ ┗ 📂css
 ┃ ┃ ┃ ┗ 📜dashboard.css
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📜dashboard.html
 ┃ ┣ 📜main.py
 ┣ 📜detect_severity.py
 ┣ 📜requirements.txt

```

---

## ⚙️ Tech Stack

### 🖥️ Backend

* Python
* FastAPI / Flask

### 🤖 Machine Learning

* Yolo Detection Model
* OpenCV
* NumPy
* Pandas

### ☁️ Automation & APIs

* Webhooks
* n8n / Docker
* Google Cloud APIs

### 🗄️ Database (Planned)

* MongoDB

---

## 🔄 Workflow

1. User uploads an image OR camera sends frame.
2. AI detects garbage presence.
3. Severity model predicts garbage level.
4. If severity ≥ threshold → complaint triggered.
5. Complaint + image sent via webhook.
6. Complaint logged for tracking.
7. Complaint information saved on Google Sheet

---

## 📌 Use Cases

* Smart Cities
* Municipal Corporations
* Housing Societies
* College Campuses
* Industrial Areas

---

## 🎯 Why This Project Matters

* Encourages cleaner cities
* Reduces manual effort
* Enables faster government response
* Promotes AI for social good

---

## 🔮 Future Scope

* Live CCTV monitoring
* Mobile app for citizens
* Heatmap of garbage hotspots
* Integration with Smart City dashboards
* Multilingual complaint generation
* Real-time analytics dashboard



## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
