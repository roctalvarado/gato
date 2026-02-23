import mysql.connector as mysql

def get_connection():
    return mysql.connect(
        host="localhost",
        user="root",
        password="admin",
        database="gatodb",
        use_pure=True
    )