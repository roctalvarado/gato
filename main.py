from entities.user import User
from getpass import getpass
from security.crypto import encrypt, decrypt

def register_user():
    name = input("Nombre: ")
    account = input("Cuenta: ")
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
        return True
    else:
        return 
    
    # return user and user.password == password

if __name__ == "__main__":
    #gfdgdfhdrd
    print("Inicio de sesión")
    if login():
        print("Seleccione una opción del menú")
        print("1.- Registrar un usuario")
        print("2.- Consultar usuarios")
        option = int(input())
        if option == 1:
            register_user()
        if option == 2:
            view_users()
    else:
        print("Credenciales inválidas")