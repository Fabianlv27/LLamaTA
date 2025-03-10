import os
import shutil
import requests
import stat
from Alerts.AlertBox import Show_popup
from Data.GetUserData import GetReposInfo, ModifyReposInfo
from Functions.Encript import Decifre

def DeleteRepo(Id,EToken,UserName,refresh,close,Directory):
    Repos=GetReposInfo()
    Token=Decifre(EToken) 
    Name=str
    for i,Repo in enumerate(Repos["Repos"]):
        if Repo["Id"]==Id:
           Name=Repo["Name"]           
           del Repos["Repos"][i]
           Repos["Amount"]-=1
                   
    url=f"https://api.github.com/repos/{UserName}/{Name}"
    
    headers = {
        "Authorization": f"token {Token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
  # Cambiar los permisos de los archivos y directorios   # Cambiar los permisos de los archivos y directorios dentro de .git
        git_dir = os.path.join(Directory, ".git")
        if os.path.exists(git_dir):
            for root, dirs, files in os.walk(git_dir):
                for dir in dirs:
                    os.chmod(os.path.join(root, dir), stat.S_IRWXU)
                for file in files:
                    os.chmod(os.path.join(root, file), stat.S_IRWXU)
            shutil.rmtree(git_dir)
        
        ModifyReposInfo(Repos, True)
        
        ModifyReposInfo(Repos, True)
        refresh()
        close()
        Show_popup(f"✅ Repository '{Name}' successfully deleted.")
        
        return {"message": f"Repository '{Name}' successfully deleted.", "status": True}
    else:
        Show_popup(f"❌ Error {response.status_code}: {response.json().get('message', 'Something went wrong')}")
        return {"message": f"Error {response.status_code}: {response.json().get('message', 'Something went wrong')}", "status": False}
