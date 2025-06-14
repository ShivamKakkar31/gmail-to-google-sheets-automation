import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/spreadsheets'
]

def authenticate_services():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    gmail = build('gmail', 'v1', credentials=creds)
    sheets = build('sheets', 'v4', credentials=creds)
    return gmail, sheets

def fetch_emails(gmail_service, max_results=5):
    emails = []
    result = gmail_service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = result.get('messages', [])
    for msg in messages:
        msg_data = gmail_service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')
        snippet = msg_data.get('snippet', '')
        emails.append([subject, sender, snippet])
    return emails

def push_to_sheet(sheet_service, sheet_id, data):
    sheet = sheet_service.spreadsheets()
    sheet.values().update(
        spreadsheetId=sheet_id,
        range="Sheet1!A1",
        valueInputOption="RAW",
        body={
            'values': [["Subject", "Sender", "Snippet"]] + data
        }
    ).execute()

if __name__ == '__main__':
    gmail, sheets = authenticate_services()
    email_data = fetch_emails(gmail)
    sheet_id = "1XjRZcWy-O5TkvaBqMolmgZL2IVJjYPipXPKdtS82oVI"
    push_to_sheet(sheets, sheet_id, email_data)
    print("✅ Emails pushed to Google Sheet successfully!")
