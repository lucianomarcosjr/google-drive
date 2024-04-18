import os
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from config import PASSWD_JSON, DADOS

def update_spreadsheet(file_name):
    credentials = service_account.Credentials.from_service_account_file(
        PASSWD_JSON,
        scopes=['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/spreadsheets']
    )

    drive_service = build('drive', 'v3', credentials=credentials)

    existing_files = drive_service.files().list(q=f"name='{file_name}'").execute()

    if 'files' in existing_files and existing_files['files']:
        file_id = existing_files['files'][0]['id']
        print(f"O arquivo '{file_name}' foi encontrado no Google Drive. ID: {file_id}")

        file_path = f'{DADOS}/{file_name}'
        if os.path.exists(file_path):
            file_metadata = {'name': file_name}

            try:
                media = MediaFileUpload(file_path, mimetype='application/octet-stream')
                updated_file = drive_service.files().update(
                    fileId=file_id,
                    body=file_metadata,
                    media_body=media
                ).execute()

                print(f"Arquivo '{file_name}' atualizado no Google Drive.")
            except HttpError as e:
                print(f"Erro ao atualizar o arquivo no Google Drive: {e}")
        else:
            print(f"O arquivo local '{DADOS}/{file_name}' não foi encontrado.")
    else:
        print(f"O arquivo '{file_name}' não foi encontrado no Google Drive. Execute o script de criação primeiro.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 update.py nomedoarquivo")
    else:
        file_name = sys.argv[1]
        update_spreadsheet(file_name)
