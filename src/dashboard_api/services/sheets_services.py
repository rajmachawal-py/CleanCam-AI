import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

SHEET_NAME = "CleanCam Data"   # EXACT sheet name

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDS_PATH = os.path.join(BASE_DIR, "..", "service_account.json")

def _get_sheet():
    try:
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        print("Using credentials at:", CREDS_PATH)

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            CREDS_PATH, scope
        )

        client = gspread.authorize(creds)
        spreadsheet = client.open(SHEET_NAME)
        sheet = spreadsheet.sheet1

        return sheet

    except Exception as e:
        print("❌ Google Sheets error:", e)
        raise e   # VERY IMPORTANT


def get_all_complaints():
    sheet = _get_sheet()
    return sheet.get_all_records()


def get_latest_complaint():
    records = get_all_complaints()
    return records[-1] if records else {}
