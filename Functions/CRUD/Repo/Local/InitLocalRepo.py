import subprocess
import json

def InitLocalRepo(directory,name):
    directory= directory.replace("\\","/")
    #Crea el Servidor Local
    try:
        subprocess.run(["git","init"],cwd=directory,check=True)
    except subprocess.CalledProcessError as err:
        return {"message":f"Error initializing Git repo: {err}","status":False}
    except FileNotFoundError:
        return{"message":"Git is not installed or the Path was not found","status":False}
    
    try:
        subprocess.run(["git","branch","-m","master","main"],cwd=directory,check=True)
    except subprocess.CalledProcessError as err:
        return {"message":f"Error change master branch in local Git repo: {err}","status":False}
    except FileNotFoundError:
        return{"message":"Git is not installed or the Path was not found","status":False}
    #Vincula con el servidor en la nube
    with open("Data/UserData.json","r") as file:
        UserData=json.load(file)
    try:
        link=f"https://github.com/{UserData["UserData"]["UserName"]}/{name}.git"
        subprocess.run(["git","remote","add","origin",link],cwd=directory,check=True)
        #UpdateLReposData(UserData["UserData"]["UserName"],link,directory,UserData["UserData"]["CodeMachineId"])
    except subprocess.CalledProcessError as err:
        return {"message":f"Error linking Git repo: {err}","status":False}
    except FileNotFoundError:
        return{"message":"Git is not installed or the Path was not found","status":False}
    return{"message":"Local Git repository was successfully created and linked","status":True}