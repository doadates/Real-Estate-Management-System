from database import get_connection

conn = get_connection()
if conn:
    print("Connected to database successfully.")
    conn.close()
else:
    print("Connection failed.")
    
