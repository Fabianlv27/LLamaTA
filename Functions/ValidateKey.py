import base64
import os
try:
    key = os.environ["ENCRYPTION_KEY"]
    print(key)
    decoded_key = base64.b64decode(key)
    print(f"Clave decodificada válida: {decoded_key}")
except Exception as ex:
    print(f"Error en la clave de cifrado: {ex}")
