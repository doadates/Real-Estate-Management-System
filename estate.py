import psycopg2
#from estate_agent import connect_db
from database import get_connection


conn = get_connection()
if conn is None:
    print("Could not connect to the database.")
    exit()

cur = conn.cursor()


def create_estate(agent_id):

    #conn = connect_db()
    conn = get_connection()
    cur = conn.cursor()

    # Step 1: Getting estate information
    """ putting the type of data before taking it as an input is important
        without data type sql and python data do not match and data can not be added to sql database"""
    
    print("\n --- Create New Estate ---")
    city = input("Enter city: ")
    postal_code = int(input("Enter postal code: ")) 
    street = input("Enter street: ")
    street_number = input("Enter street number: ")
    square_area = int(input("Enter square area: "))  

    # adding to estate table in sql 
    cur.execute("""
        INSERT INTO estate (city, postal_code, street, street_number, square_area, agent_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id 
    """, (city, postal_code, street, street_number, square_area, agent_id))
    estate_id = cur.fetchone()[0] #record of new estate id 

    print(f"Estate inserted to database with ID: {estate_id}")

    # Step 2: Choosing estate type (house or apartment)
    print("\nWhat type of estate do you want to create?")
    print("[1] Apartment")
    print("[2] House")
    choice = input("Choose an option: ")

    if choice == "1":
        # Getting apartment information
        floor = int(input("Enter floor number: "))  #INT
        rent = float(input("Enter rent: "))  #REAL
        rooms = int(input("Enter number of rooms: "))  #INT
        balcony = input("Does it have a balcony? (yes/no): ").lower() == "yes"
        built_in_kitchen = input("Does it have a built-in kitchen? (yes/no): ").lower() == "yes"

        # Adding to apartment table in sql
        cur.execute("""
            INSERT INTO apartment (id, floor, rent, rooms, balcony, built_in_kitchen)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (estate_id, floor, rent, rooms, balcony, built_in_kitchen))

        print("Apartment created successfully.")

    elif choice == "2":
        # Getting house information
        floor = int(input("Enter number of floors: "))  # INT
        price = float(input("Enter total price: "))  # REAL
        garden = input("Does it have a garden? (yes/no): ").lower() == "yes"   #1 veya 0 giremiyoruz

        # Adding to house table in sql
        cur.execute("""
            INSERT INTO house (id, floor, price, garden)
            VALUES (%s, %s, %s, %s)
        """, (estate_id, floor, price, garden))

        print("House created successfully.")

    else:
        print(" Invalid option.")

    conn.commit() #bu da kaydetmek için zaten
    cur.close() #veri gönderdik işim bitti kapat
    conn.close() #connection

    print("All changes committed to the database.")

#Changing (updating the estates)
def update_estate(agent_id):

    #conn = connect_db()
    conn = get_connection()
    cur = conn.cursor()

    estate_id = input("Enter the ID of the estate you want to update:")

    # Checking if the selected estate belongs to estate agent
    cur.execute("""
        SELECT id 
        FROM Estate 
        WHERE id = %s AND agent_id = %s
    """, (estate_id, agent_id))
    if not cur.fetchone():
        print("No such estate for your account.")
        return

    city = input("Enter city: ")
    postal_code = int(input("Enter postal code: ")) 
    street = input("Enter street: ")
    street_number = input("Enter street number: ")
    square_area = int(input("Enter square area: "))

    cur.execute("""
        UPDATE Estate
        SET city = %s, postal_code = %s, street = %s, street_number = %s, square_area = %s
        WHERE id = %s
    """, (city, postal_code, street, street_number, square_area, estate_id))

    conn.commit()
    cur.close()
    conn.close()
    print("Estate updated successfully.")

#Changing (deleting the estates)
def delete_estate(agent_id):

    #conn = connect_db()
    conn = get_connection()
    cur = conn.cursor()

    estate_id = input("Enter the ID of the estate you want to delete: ")

    # Check if the estate belongs to this agent
    cur.execute("""
        SELECT id 
        FROM Estate 
        WHERE id = %s AND agent_id = %s
    """, (estate_id, agent_id))
    if not cur.fetchone(): #eşleşen ilk sonuç gelir none dönmüşse koşul true olur
        print("No such estate for your account.")
        return

    cur.execute("""
        DELETE FROM Estate WHERE id = %s
    """, (estate_id,)) ##çok güzel bir açıklaması var virgülün

    conn.commit()
    cur.close()
    conn.close()
    print("Estate deleted successfully.")