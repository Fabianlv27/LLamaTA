import os
import sys
from cryptography.fernet import Fernet

def obtener_ruta_archivo(rel_path):
    # Si se está ejecutando desde el archivo .exe
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel_path)
    # Si se está ejecutando desde el código fuente
    return os.path.join(os.path.abspath("."), rel_path)

def DataTokenHandler():
    # Obtener la ruta correcta para el archivo
    absolute_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = obtener_ruta_archivo("Data/keyfile.key")  # Usar la función para obtener la ruta correcta

    if not os.path.exists(full_path):
        key = Fernet.generate_key()
        # Crear las carpetas necesarias si no existen
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "wb") as Keyfile:
            Keyfile.write(key)
        print(f"Clave generada y guardada en {full_path}")
        return
    else:
        with open(full_path, "rb") as Keyfile:
            key = Keyfile.read()
        print(f"Archivo ya existente: {full_path}")    
        return
