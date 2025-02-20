import subprocess

def GitIsLoginVerifier():
    result=subprocess.run(
        ["git","config","--global","user.email"],
        capture_output=True,
        text=True
    )
    if result.returncode==0:
        return True
    else:
        print("Error al obtener al Usuario")
        return False
    
