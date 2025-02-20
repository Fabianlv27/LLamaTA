import requests
from Functions.Encript import Decifre

def CheckReposData(EncripToken):
    GitHub_Token=Decifre(EncripToken)
    Github_Api_Url=f"https://api.github.com/user/repos"

    Headers={
    "Authorization":f"Bearer {GitHub_Token}"
}

    Params={
    "visibility":"all",
    "per_page":100
}
    response=requests.get(Github_Api_Url,headers=Headers,params=Params)

    if response.status_code==200:
        repos=response.json()
        for repo in repos:
            if repo["name"]=="ReposData":
                return True
        return False

    else:
        print(f"Error {response.status_code}: {response.json().get('message', 'Algo salió mal')}")
        return False
    
