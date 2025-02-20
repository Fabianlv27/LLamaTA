from cryptography.fernet import Fernet
import os


def Encripte(e):
    with open("Data/keyfile.key","rb") as Keyfile:
        EncryKey=Keyfile.read()
    cipher=Fernet(EncryKey)
    #Cifrar la clave:
    Encripted=cipher.encrypt(e.encode())
    return Encripted

def Decifre(e):
     print(e)
     with open("Data/keyfile.key","rb") as Keyfile:
        EncryKey=Keyfile.read()
     cipher=Fernet(EncryKey)
     #Desifrar la clave:
     UnCripted=cipher.decrypt(e).decode()
     return UnCripted

