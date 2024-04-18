import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from config import PASSWD_JSON

def create_spreadsheet(file_name):
    credentials = service_account.Credentials.from_service_account_file(
        PASSWD_JSON,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    sheets_service = build('sheets', 'v4', credentials=credentials)
    spreadsheet_exists = False
    try:
        spreadsheet = sheets_service.spreadsheets().get(spreadsheetId=file_name).execute()
        spreadsheet_exists = True
    except HttpError as e:
        if 'spreadsheetNotFound' in str(e):
            spreadsheet_exists = False

    if spreadsheet_exists:
        print(f"A planilha '{file_name}' já existe no Google Sheets.")
    else:
        spreadsheet_metadata = {
            'properties': {
                'title': file_name
            },
            'sheets': [
                {
                    'properties': {
                        'title': 'Sheet1'
                    }
                }
            ]
        }

        try:
            created_spreadsheet = sheets_service.spreadsheets().create(
                body=spreadsheet_metadata,
                fields='spreadsheetId'
            ).execute()

            spreadsheet_id = created_spreadsheet['spreadsheetId']
            print(f"Nova planilha '{file_name}' criada no Google Sheets. ID: {spreadsheet_id}")
        except HttpError as e:
            print(f"Erro ao criar a planilha no Google Sheets: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 create.py nomedaplanilha")
    else:
        file_name = sys.argv[1]
        create_spreadsheet(file_name)
