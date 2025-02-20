import requests

from Alerts.AlertBox import Show_popup
from Data.GetUserData import GetReposInfo, ModifyReposInfo
from Functions.Encript import Decifre

def DeleteRepo(Id,EToken,UserName,refresh,close):
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
        ModifyReposInfo(Repos,True)
        refresh()
        close()
        Show_popup(f"✅ Repository '{Name}' successfully deleted.")
        return {"message": f"Repository '{Name}' successfully deleted.", "status": True}
    else:
        Show_popup(f"❌ Error {response.status_code}: {response.json().get('message', 'Something went wrong')}")
        return {"message": f"Error {response.status_code}: {response.json().get('message', 'Something went wrong')}", "status": False}
