README: Gmail to Google Sheets Automation Script

Project Name:

Email Extraction and Google Sheets Automation

🔧 Technologies Used:

- Python 3
- Gmail API
- Google Sheets API
- Google OAuth 2.0
- Required Libraries: `google-auth`, `google-auth-oauthlib`, `google-api-python-client`

Project Description:
This script reads emails from your Gmail inbox (using Gmail API), extracts basic information (subject, sender, date, snippet), and writes them into a Google Sheet (using Google Sheets API). This Python script connects to Gmail and Google Sheets using Google APIs. It extracts the latest 5 emails from the user's inbox and writes the subject, sender, and snippet into a Google Sheet using secure OAuth authentication.

This is a part of a demo assignment for automating quotation extraction from emails into Google Sheets.

Files Included:
- main.py : Main script
- token.json :Auto-generated token file after first login
- credentials.json : Not included due to security reasons

How to Run:
1. Set Up API
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a project
   - Enable:
     - Gmail API
     - Google Sheets API
   - Create OAuth 2.0 Credentials (Desktop App)
   - Download credentials.json

2. Place credentials.json
   - Put the file in the same directory as `main.py`

3. Install Required Libraries
   Run this in terminal:

   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
