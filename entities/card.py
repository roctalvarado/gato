from persistence.db import get_connection
from security.crypto import encrypt, decrypt

class Card:

    def __init__(self, id:int, number:str, bank:str, card_type:str):
        self.id = id
        self.number = number
        self.bank = bank
        self.card_type = card_type
    
    def insert(number, bank, card_type, id_user):
        connection = get_connection()
        cursor = connection.cursor()

        number_encrypt = encrypt(number)

        sql = "INSERT INTO card (number, bank, card_type, id_user) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (number_encrypt, bank, card_type, id_user))
        connection.commit()

        cursor.close()
        connection.close()

    def get_cards_by_user_id(id_user):
        connection = get_connection()
        cursor = connection.cursor()

        sql = "SELECT id, number, bank, card_type, id_user FROM card WHERE id_user = %s"
        cursor.execute(sql, (id_user,))
        rows = cursor.fetchall()

        return [
            Card(
                id = row["id"],
                number = decrypt(row["number"]),
                bank = row["bank"],
                card_type = row["card_type"],
                id_user = row["id_user"]
            )
            for row in rows
        ]