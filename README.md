
# Python Google Drive

Automatização de upload de arquivos pro Google através de scripts em python com o Google API.

## Instalação

Para utilizar os scripts em python é necessário adicionar o Google API
```
pip install google-api-python-client
pip install google-api
```
    
## Variáveis de Ambiente

Para rodar esse projeto, será necessário utilizar uma conta no Google Console (https://console.cloud.google.com/), ativar e gerar uma credencial (em JSON) no Google Drive API. Posteriormente adicione as informações no arquivo credentials.json.

A credencial obtida do Google API tem esse padrão:

```
{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "drive-api@...iam.gserviceaccount.com",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "",
  "universe_domain": "googleapis.com"
}
```

## Arquivo de configuração

As variaveis estão descritas no arquivo config.py.
## Uso dos scripts:

```
## Cria o arquivo dentro do Google Drive API
python3 create.py nome-do-arquivo

## Realiza o update das informações no arquivo*
python3 update.py nome-do-arquivo

*O nome do arquivo local deve ser o mesmo que foi criado no Drive, a leitura dos arquivos a serem importados para o drive ficam dentro do diretório "dados", podendo ser alterado no arquivo config.py

## Lista todos os arquivos criados dentro do Google Drive API
python3 list.py

## Caso necessite remover algum arquivo listado anterior
python3 remove.py nome-do-arquivo

## Para compartilhar o arquivo com outro usuário, tendo um controle de quem pode ler ou escrever no arquivo
python3 share.py nome-do-arquivo email-leitura email-escrita
```

