import requests
from Functions.Encript import Decifre
from Functions.CRUD.ReposDataFile.UpdateRReposData import UpdateRReposData

def CreateNewReposData(EncryToken):
    GitHub_Token=Decifre(EncryToken)
    Github_Api_Url="https://api.github.com/user/repos"

    Headers={
        "Authorization":f"token {GitHub_Token}",
        "Content-Type":"application/json"
    }

    RepoData={
        "name":"ReposData",
        "description":"Here we will save your Repositories",
        "private":True,
        "auto_init":True,
    }

    response=requests.post(Github_Api_Url,headers=Headers,json=RepoData)

    if response.status_code==201:
        repo_info=response.json()
        print(repo_info)
        print(f"Repository successfully created: {repo_info['html_url']}")
    else:
        print(f"Error {response.status_code}: {response.json().get('message', 'Something went wrong')}")
        return
    #Crea el archivo json
    
    owner=response.json()["owner"]["login"]
    repo=response.json()["name"]
    file_path="ReposInfo.json"
    link=f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    upload_response=UpdateRReposData([],link)
    return upload_response

  
    