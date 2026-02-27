from entities.user import User
from entities.card import Card
from getpass import getpass
from security.crypto import encrypt, decrypt

user_id = 0
def register_user():
    name = input("Nombre: ")
    account = input("Cuenta: ")
    
    if User.check_account_exists(account):
        print("Usuario ya existe.")
    else:
        curp = input("CURP: ")
        password = getpass("Contraseña: ")
        User.insert(name, curp, account, password)

def view_users():
    users = User.get_users()

def login():
    account = input("Cuenta: ")
    password = getpass("Contraseña: ")

    user = User.get_user_by_account(account)
    if user and user.password == password:
        global user_id
        user_id = user.id
        return True
    else:
        return 
    # return user and user.password == password
    
def register_card():
    number = input("Número de tarjeta: ")
    bank = input("Banco: ")
    print("Tipo de tarjeta: ")
    card_type_number = input("Ingrese 1 para Débito, 2 para Crédito: ")
    if card_type_number == '1':
        card_type = 'Débito'
    elif card_type_number == '2':
        card_type = 'Crédito'
    else:
        print('Ingrese un valor válido')
    Card.insert(number, bank, card_type, user_id)

def view_cards():
    cards = Card.get_cards_by_user_id(user_id)
    for c in cards:
        print(f"Número: {c.number}, Banco: {c.bank}, Tipo: {c.card_type}")

if __name__ == "__main__":
    print("Inicio de sesión")
    if login():
        print("Seleccione una opción del menú")
        print("1.- Registrar un usuario")
        print("2.- Consultar usuarios")
        print("3.- Registrar una tarjeta")
        print("4.- Consultar tarjetas")
        option = int(input())
        if option == 1:
            register_user()
        if option == 2:
            view_users()
        if option == 3:
            register_card()
        if option == 4:
            view_cards()
    else:
        print("Credenciales inválidas")