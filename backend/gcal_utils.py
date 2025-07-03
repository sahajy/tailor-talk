# backend/gcal_utils.py
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'service_account.json')  # <- Rename if needed
CALENDAR_ID = 'primary'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('calendar', 'v3', credentials=credentials)


def book_appointment(time_range: str) -> str:
    try:
        start_str, end_str = time_range.split(" to ")
        start = datetime.strptime(start_str.strip(), "%Y-%m-%d %H:%M")
        end = datetime.strptime(end_str.strip(), "%Y-%m-%d %H:%M")

        event = {
            'summary': 'Tailor Appointment',
            'start': {'dateTime': start.isoformat(), 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': end.isoformat(), 'timeZone': 'Asia/Kolkata'},
        }

        service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        return f"✅ Appointment booked from {start_str} to {end_str}"
    except Exception as e:
        return f"❌ Error in booking: Invalid time format: '{time_range}' | Error: {str(e)}"


def check_availability(time_range: str) -> str:
    try:
        start_str, end_str = time_range.split(" to ")
        start = datetime.strptime(start_str.strip(), "%Y-%m-%d %H:%M")
        end = datetime.strptime(end_str.strip(), "%Y-%m-%d %H:%M")

        events_result = service.events().list(
            calendarId=CALENDAR_ID,
            timeMin=start.isoformat() + 'Z',
            timeMax=end.isoformat() + 'Z',
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        if events:
            return f"❌ Time slot from {start_str} to {end_str} is not available."
        return f"✅ Time slot from {start_str} to {end_str} is available."
    except Exception as e:
        return f"❌ Error in checking availability: Invalid time format: '{time_range}' | Error: {str(e)}"
