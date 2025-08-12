import psycopg2
#from estate_agent import connect_db
from database import get_connection



"""conn = get_connection()
if conn is None:
    print("Could not connect to the database.")
    exit()

cur = conn.cursor()"""

def insert_person():
    #conn = connect_db()
    conn = get_connection()
    cur = conn.cursor()

    first_name = input("Enter first name: ")
    name = input("Enter last name: ")
    address = input("Enter address: ")

    cur.execute("""
        INSERT INTO Person (first_name, name, address)
        VALUES (%s, %s, %s)
    """, (first_name, name, address))

    conn.commit()
    cur.close()
    conn.close()
    print("Person inserted successfully.")

from database import get_connection

def create_contract():
    conn = get_connection()
    cur = conn.cursor()
    
    print("\n--- Create New Contract ---")
    contract_no = input("Enter contract number: ")
    date = input("Enter date (YYYY-MM-DD): ")
    place = input("Enter place: ")
    person_id = input("Enter person ID: ")

    # --- Yeni ekleme: Person var mı diye kontrol et ---
    cur.execute("SELECT id FROM person WHERE id = %s", (person_id,))
    person = cur.fetchone()

    if not person:
        print(f"Error: No person found with ID {person_id}. Contract creation cancelled.")
        cur.close()
        conn.close()
        return
    # --------------------------------------------------

    try:
        cur.execute("""
            INSERT INTO contract (contract_no, date, place, person_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (contract_no, date, place, person_id))

        contract_id = cur.fetchone()[0]
        conn.commit()
        print(f"Contract created successfully with ID {contract_id}.")

    except Exception as e:
        print("Error while creating contract:", e)
        conn.rollback()

    finally:
        cur.close()
        conn.close()

def list_contracts():
    conn = get_connection()
    #conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT contract.id, contract_no, date, place, first_name, person.name
        FROM contract
        LEFT JOIN person ON Contract.person_id = person.id
        ORDER BY contract.id
    """)

    contracts = cur.fetchall()
    print("\n--- All Contracts ---")
    for contract in contracts:
        print(f"ID: {contract[0]} | No: {contract[1]} | Date: {contract[2]} | Place: {contract[3]} | Signed by: {contract[4]} {contract[5]}")

    conn.commit()
    cur.close()
    conn.close()
