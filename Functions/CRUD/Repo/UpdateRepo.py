import subprocess
import json

def UpdateRepo(Directory):
    Directory=Directory.replace("\\","/")
    try:
        subprocess.run(["git","pull","origin","main"],cwd=Directory,check=True)
    except subprocess.CalledProcessError as err:
        return {"message":f"Error updating Git repo: {err}","status":False}
    except FileNotFoundError:
        return{"message":"Git is not installed or the Path was not found","status":False}
