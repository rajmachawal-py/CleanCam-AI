# ♻️ CleanCam AI

### Smart Cleanliness Monitoring using Computer Vision

> AI-powered garbage detection, severity scoring, and automated civic complaint workflow.

---

## 🚀 Overview

CleanCam AI is a **Smart City AI project** that detects garbage accumulation from images or CCTV feeds and automatically triggers complaint workflows, sends email alerts, and logs data into Google Sheets for monitoring and analytics.

This project demonstrates how **AI + Automation + CivicTech** can help cities maintain cleanliness without relying on manual reporting.

---

## 🌍 Problem Statement

Urban areas frequently suffer from garbage overflow because reporting is manual and inconsistent. Citizens often:

* Ignore waste accumulation
* Don’t know where to report
* Avoid the effort of filing complaints

This leads to:

* Health hazards
* Poor sanitation
* Environmental pollution

**CleanCam AI automates the entire reporting pipeline.**

---

## 💡 Solution

CleanCam AI combines **Computer Vision + Automation** to automatically:

1. Detect garbage from images or cameras
2. Predict severity of garbage accumulation
3. Trigger complaint workflow when severity is high
4. Send evidence via email
5. Store records in Google Sheets
6. Display data on a dashboard

Supported inputs:

* CCTV cameras
* Mobile images
* Drone footage

---

## 🧠 Key Features

### 🗑️ Garbage Detection

YOLO-based detection model identifies garbage in images.

### 📊 Severity Classification

Garbage is categorized into:

* Low
* Medium
* High
* Critical

### 📧 Automated Complaint Filing

When severity reaches **High/Critical**:

* Complaint message generated
* Image evidence attached
* Email sent automatically
* Data stored in Google Sheets

### 📊 Dashboard Monitoring

Tracks complaint history and analytics.

---

## 🏗️ System Architecture

```
User Image / CCTV Feed
        ↓
Garbage Detection Model (YOLO)
        ↓
Severity Prediction Model
        ↓
Decision Engine
        ↓
Automation Workflow (n8n / Webhooks)
        ↓
Email + Google Sheets Logging
        ↓
Dashboard Tracking
```

---

## 📁 Project Structure

```
src/
 ┣ dashboard_api/
 ┃ ┣ services/
 ┃ ┃ ┗ sheets_services.py
 ┃ ┣ static/css/
 ┃ ┣ templates/
 ┃ ┃ ┗ dashboard.html
 ┃ ┗ main.py
 ┣ detect_severity.py
 ┗ requirements.txt
```

---

## ⚙️ Tech Stack

### 👨‍💻 Backend

* Python
* FastAPI / Flask

### 🤖 Machine Learning

* YOLO Object Detection
* OpenCV
* NumPy
* Pandas

### 🔗 Automation & Cloud

* Webhooks
* n8n + Docker
* Google Cloud APIs
* Gmail Automation
* Google Sheets API

### 🗄️ Database (Planned)

* MongoDB

---

## 🔄 Workflow

1. Upload image / capture frame
2. Detect garbage using YOLO
3. Predict garbage severity
4. If severity ≥ threshold → trigger complaint
5. Send email with image evidence
6. Store data in Google Sheets
7. Update dashboard

---

## 🧪 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rajmachawal-py/CleanCam-AI.git
cd CleanCam-AI
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Dashboard API

```bash
cd src/dashboard_api
python main.py
```

---

## 🎯 Use Cases

* Smart Cities
* Municipal Corporations
* Housing Societies
* College Campuses
* Industrial Areas

---

## 🌟 Why This Project Matters

* Encourages cleaner cities
* Reduces manual effort
* Speeds up civic response
* Demonstrates AI for social good

---

## 🔮 Future Improvements

* Live CCTV real‑time monitoring
* Mobile app for citizens
* Garbage hotspot heatmaps
* Multilingual complaint generation
* Real-time analytics dashboard

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

