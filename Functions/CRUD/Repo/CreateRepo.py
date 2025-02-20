import requests
import json
from Functions.Encript import Decifre

def CreateRepo(Name,Desc):
    with open("Data/UserData.json","r") as file:
        UserData=json.load(file)
    Token=Decifre(UserData["UserData"]["Token"])
    print(f"el token: {Token}") 
    Github_Api_Url="https://api.github.com/user/repos"
    
    Headers={
        "Authorization":f"token {Token}",
        "Content-Type":"application/json"
    }
    
    RepoData={
        "name":Name,
        "description":f"TeleArchiver: {Desc}",
        "private":True,
        "auto_init":True,
    }
    
    response=requests.post(Github_Api_Url,headers=Headers,json=RepoData)
    print(response.status_code)
    if response.status_code==201:
        repoInfo=response.json()
        print(f"Repository successfully created: {repoInfo['html_url']}")
        return {"message":f"Repository successfully created: {repoInfo['html_url']}","status":True,"link":f"{repoInfo['html_url']}.git"}
    else:
        print(f"Error {response.status_code}: {response.json().get('message', 'Something went wrong')}")
        return {"message":f"Error {response.status_code}: {response.json().get('message', 'Something went wrong')}","status":False}