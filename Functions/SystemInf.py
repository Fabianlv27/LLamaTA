import platform

def GetOsInfo():
    print(f"Sistema operativo: {platform.system()}")
    print(f"Nombre del nodo: {platform.node()}")
    return{"OS":platform.system(),"nodo":platform.node()}

