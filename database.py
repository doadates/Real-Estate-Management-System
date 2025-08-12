import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname='dis-2025',   
            user='vsisp06',
            password='mb6HbaLL',
            host='vsisdb.informatik.uni-hamburg.de'
        )
        return connection
    except psycopg2.Error as e:
        print("Error while connecting to database:", e)
        return None
