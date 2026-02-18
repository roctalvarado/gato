from cryptography.fernet import Fernet # >.<

key = b'Zpg8MtBy8ZX1dwgYCIaEizHnzT6Oc6DXbBm7lvBy4kk='

fernet = Fernet(key)

def encrypt(value):
    return fernet.encrypt(value.encode()).decode()

def decrypt(value):
    return fernet.decrypt(value.encode()).decode()