import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

import datetime
weeknumber = datetime.date.today().isocalendar()[1]

# Replace with your credentials file path
credentials_file = '../secretJSON/disctrack-fb3802d26c26.json'
# Replace with the path to the file you want to upload
file_to_upload = 'output/disctrack_w' + str(weeknumber) + '.xlsx'

# Authenticate using the credentials file
creds = service_account.Credentials.from_service_account_file(credentials_file, scopes=['https://www.googleapis.com/auth/drive'])


# Create the Google Drive API client
drive_service = build('drive', 'v3', credentials=creds)

# File metadata
file_metadata = {
    'name': os.path.basename(file_to_upload),
    'parents': ['1XWvZBsWlrlzLq-I-mEAT51Tdpme6wEz-']  # Replace with the folder ID where you want to store the file
}

# Upload the file
media = MediaFileUpload(file_to_upload, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

print(f'File ID: {uploaded_file.get("id")}')
