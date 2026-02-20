from entities.user import User
from getpass import getpass

def register_user():
    name = input("Nombre: ")
    account = input("Cuenta: ")
    curp = input("CURP: ")
    password = getpass("Contraseña: ")

    User.insert(name, curp, account, password)

def view_users():
    users = User.get_users()

if __name__ == "__main__":
    print()
    print("Seleccione una opción del menú")
    print("1.- Registrar un usuario")
    print("2.- Consultar usuarios")
    option = int(input())
    if option == 1:
        register_user()
    if option == 2:
        view_users()