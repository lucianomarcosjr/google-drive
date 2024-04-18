from googleapiclient.discovery import build
from google.oauth2 import service_account
from config import PASSWD_JSON

credentials = service_account.Credentials.from_service_account_file(
    PASSWD_JSON,
    scopes=['https://www.googleapis.com/auth/drive']
)

drive_service = build('drive', 'v3', credentials=credentials)

results = drive_service.files().list().execute()
files = results.get('files', [])

if not files:
    print('Nenhum arquivo encontrado.')
else:
    print('Arquivos no Google Drive:')
    for file in files:
        print(f'{file["name"]} ({file["id"]})')
