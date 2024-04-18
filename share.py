import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import PASSWD_JSON

def get_file_id_by_name(drive_service, file_name):
    try:
        result = drive_service.files().list(q=f"name='{file_name}'").execute()
        files = result.get('files', [])
        if files:
            return files[0]['id']
    except HttpError as e:
        print(f"Erro ao procurar arquivo: {e}")
    return None

def share_file(file_id, email, role):
    credentials = service_account.Credentials.from_service_account_file(
        PASSWD_JSON,
        scopes=['https://www.googleapis.com/auth/drive.file']
    )

    drive_service = build('drive', 'v3', credentials=credentials)

    permission = {
        'type': 'user',
        'role': role,
        'emailAddress': email,
    }

    try:
        drive_service.permissions().create(fileId=file_id, body=permission).execute()
        print(f"Permissão concedida para {email} com papel de {role}")
    except HttpError as e:
        print(f"Erro ao conceder permissão: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python3 share.py nomedoarquivo email_leitura email_escrita")
    else:
        file_name = sys.argv[1]
        email_leitura = sys.argv[2]
        email_escrita = sys.argv[3]

        credentials = service_account.Credentials.from_service_account_file(
            PASSWD_JSON,
            scopes=['https://www.googleapis.com/auth/drive.file']
        )
        drive_service = build('drive', 'v3', credentials=credentials)

        file_id = get_file_id_by_name(drive_service, file_name)

        if file_id:
            share_file(file_id, email_leitura, 'reader')
            share_file(file_id, email_escrita, 'writer')
        else:
            print(f"Arquivo '{file_name}' não encontrado no Google Drive.")
