import os
import pyodbc

# Connect to SQL Server
server = 'VIRTSQL-MDB122'
database = 'OMNI.Omni.sgh_nm'
username = 'username'
password = 'password'
driver = '{ODBC Driver 18 for SQL Server}'

# cnxn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}') 
cnxn = pyodbc.connect(f'Driver={driver};SERVER={server};DATABASE={database};TRUSTED_CONNECTION=yes')

# Get a cursor to interact with the database
cursor = cnxn.cursor()

# Define the folder path
folder_path = "N:\\DATA\\SGHNM\\Hermes_Sample\\AW\\48.P\\tmp"

status_id = 30

# Loop through all files in the folder
for filename in os.listdir(folder_path):
  # Insert the filename into the SQL Server table
  sql = "INSERT INTO sgh_nm (studyuid, status) VALUES (?, ?)"
  val = (filename, status_id)
  cursor.execute(sql, val)
  cnxn.commit()

# Close the SQL Server connection
cursor.close()
cnxn.close()
