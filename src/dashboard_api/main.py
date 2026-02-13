from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

from services.sheets_services import get_all_complaints, get_latest_complaint

# ------------------ PATH SETUP ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EVIDENCE_DIR = os.path.join(BASE_DIR, "..", "detect_severity", "evidence")

# ------------------ APP ------------------
app = FastAPI(
    title="CleanCam AI Dashboard API",
    description="API for monitoring automated garbage complaints",
    version="1.0"
)

# ------------------ STATIC FILES ------------------
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static"
)

# ------------------ TEMPLATES ------------------
templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)

# ------------------ ROUTES ------------------
@app.get("/")
def health_check():
    return {"status": "CleanCam AI Dashboard API running"}

@app.get("/dashboard")
def dashboard(request: Request):
    complaints = get_all_complaints()
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "complaints": complaints}
    )

@app.get("/complaints")
def list_complaints():
    return get_all_complaints()

@app.get("/complaints/latest")
def latest_complaint():
    return get_latest_complaint()

@app.get("/evidence/{image_name}")
def get_evidence_image(image_name: str):
    if not image_name.lower().endswith(".jpg"):
        image_name += ".jpg"

    image_path = os.path.join(EVIDENCE_DIR, image_name)

    if not os.path.exists(image_path):
        return {"error": "Image not found"}

    return FileResponse(image_path)
