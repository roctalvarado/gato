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
        password_encrypt = encrypt(password)

        sql = "INSERT INTO user (name, curp, account, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, curp_encrypt, account, password_encrypt))
        connection.commit()

        cursor.close()
        connection.close()

    def get_users():
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT idm bame, curp, account, password FROM user"

        cursor.execute(sql)
        rows = cursor.fetchall()

        return [
            User(
                id = row["id"],
                name = row["name"],
                account = row["account"],
                curp = decrypt(row["curp"]),
                password = row["password"]
            )
            for row in rows
        ]
    