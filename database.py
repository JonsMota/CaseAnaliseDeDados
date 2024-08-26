import pyodbc

def get_connection():
    server = 'your_server.database.windows.net'
    database = 'survey_data'
    username = 'adminuser'
    password = 'SenhaSegura123!'
    connection = pyodbc.connect(
        f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    )
    return connection