import os
import googleapiclient.discovery
import googleapiclient.errors
import send_mail_with_pdf

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


scopes = ['https://www.googleapis.com/auth/drive']

def get_document_infos():
    document_infos = []
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = googleapiclient.discovery.build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10).execute()
    items = results.get('files', [])

    if not items:
        print('No file found!')
    else:
        for item in items:
            document_infos.append(item)
        return document_infos

def convert_2_pdf(document_id):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = googleapiclient.discovery.build('drive', 'v3', credentials=creds)

    request =   service.files().export_media(fileId=document_id,   mimeType='application/pdf')

    response = request.execute()
    with open("temp.pdf", "wb") as wer:
        wer.write(response)


if __name__ == '__main__':
    document_infos = get_document_infos()
    for item in document_infos:
        print(item)


    convert_2_pdf(document_infos[0]['id'])
    
    send_mail_with_pdf.sendMail(<recipient-email-adress>, 'temp.pdf', document_infos[0]['name'])