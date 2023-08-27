import pypyodbc as odbc
import pandas  as pd 
from credential import username, password

server = 'connectiosneps.database.windows.net'
database = 'connectionpqr'
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:connectiosneps.database.windows.net,1433;Database=connectionpqr;Uid=CloudSA207c7bec;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = odbc.connect(connection_string)