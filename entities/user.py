from persistence.db import get_connection
from security.crypto import encrypt, decrypt

class User:
    def __init__(self, id:int, name:str, curp:str, account:str, password:str):
        self.id = id
        self.name = name
        self.curp = curp
        self.account = account
        self.password = password

    def insert(name, curp, account, password):
        connection = get_connection()
        cursor = connection.cursor()

        curp_encrypt = encrypt(curp)

        sql = "INSERT INTO user (name, curp, account, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, curp_encrypt, account, password))
        connection.commit()

        cursor.close()
        connection.close()
        