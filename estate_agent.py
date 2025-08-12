from database import get_connection
import psycopg2
import getpass

""" To access this mode, the user has to enter a separate password, which is hard-coded in the application
for simplicity """
admin_password = "1234"  # Hardcoded admin password

"""
def connect_db():
    return psycopg2.connect(
        dbname="dis-2025",
        user="vsisp06",
        password="mb6HbaLL",
        host="vsisdb.informatik.uni-hamburg.de"
                )"""


"""conn = get_connection()
if conn is None:
    print("Could not connect to the database.")
    exit()

cur = conn.cursor()"""


def verify_admin_password():
    password = getpass.getpass("Enter admin password: ")
    return password == admin_password


def create_agent():

    #conn = connect_db()
    conn = get_connection()
    cur = conn.cursor()

    print("\n--- Create New Estate Agent Account ---")
    name = input("Enter name: ")
    address = input("Enter address: ")
    login = input("Enter username: ")
    password = input("Enter password: ")

    cur.execute("""
        INSERT INTO estate_agent (name, address, login, password)
        VALUES (%s, %s, %s, %s)
    """, (name, address, login, password))

    conn.commit()
    print("Estate agent account created successfully.")

    cur.close()
    conn.close()

def login_agent():
    conn = get_connection()
    if conn is None:
        print("Connection failed. Exiting.")
        return
    cur = conn.cursor()

    print("\n--- Estate Agent Login ---")
    login = input("Enter username: ")
    password = input("Enter password: ")

    cur.execute("""
        SELECT id, name 
        FROM estate_agent WHERE login = %s AND password = %s
    """, (login, password))

    agent = cur.fetchone()

    if agent:
        print(f"Login successful. Welcome {agent[1]}!")
        cur.close()
        conn.close()
        return agent[0] 
    else:
        print("Login failed.")
        cur.close()
        conn.close()
        return None

def delete_agent():

    conn = get_connection()
    cur = conn.cursor()

    print("\n--- Delete Estate Agent Account ---")
    login = input("Enter username to delete: ")

    cur.execute("""
        DELETE FROM estate_agent 
        WHERE login = %s
    """, (login,))

    if cur.rowcount > 0: # if there is a match then it is 1
        conn.commit()
        print("Account deleted successfully.")
    else:
        print("No such account found.")

    cur.close()
    conn.close()




