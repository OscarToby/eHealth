import os
import pyodbc

# Connect to SQL Server
server = 'yourserver'
database = 'yourdatabase'
username = 'yourusername'
password = 'yourpassword'
driver = '{ODBC Driver 18 for SQL Server}'
cnxn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Get a cursor to interact with the database
cursor = cnxn.cursor()

# Define the folder path
folder_path = "/path/to/your/folder"

status_id = 30

# Loop through all files in the folder
for filename in os.listdir(folder_path):
  # Insert the filename into the SQL Server table
  sql = "INSERT INTO sgh_nm (studyuid, status) VALUES (?, ?)"
  val = (studyuid, status_id)
  cursor.execute(sql, val)
  cnxn.commit()

# Close the SQL Server connection
cursor.close()
cnxn.close()
