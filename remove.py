import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import PASSWD_JSON

def get_file_id_by_name(drive_service, file_name):
    results = drive_service.files().list(q=f"name = '{file_name}'").execute()
    files = results.get('files', [])

    if files:
        return files[0]['id']
    else:
        return None

def remove_files_by_name(drive_service, file_names):
    try:
        for file_name in file_names:
            file_id = get_file_id_by_name(drive_service, file_name)
            if file_id:
                drive_service.files().delete(fileId=file_id).execute()
                print(f'O arquivo com o nome "{file_name}" foi removido com sucesso.')
            else:
                print(f'Não foi possível encontrar o arquivo com o nome "{file_name}".')
    except Exception as e:
        print(f'Ocorreu um erro ao tentar excluir os arquivos: {str(e)}')

if __name__ == "__main__":
    credentials_path = PASSWD_JSON

    scopes = ['https://www.googleapis.com/auth/drive.file']

    try:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path, scopes=scopes
        )

        drive_service = build('drive', 'v3', credentials=credentials)
    except Exception as e:
        print(f'Ocorreu um erro ao autenticar as credenciais: {str(e)}')
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Uso: python3 remove.py <file_name1> <file_name2> ...")
        sys.exit(1)

    file_names = sys.argv[1:]

    remove_files_by_name(drive_service, file_names)
