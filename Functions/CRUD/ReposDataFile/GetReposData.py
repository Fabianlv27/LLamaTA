import requests
import base64
import json
from Functions.Encript import Decifre
def CloneReposData(EncripToken,owner,Save):
    GitHub_Token = Decifre(EncripToken)
    Github_Api_Url = "https://api.github.com"

    repo="ReposData"
    file_path="ReposInfo.json"

    Headers = {
        "Authorization": f"token {GitHub_Token}",
        "Content-Type": "application/json"
    }

    url = f"{Github_Api_Url}/repos/{owner}/{repo}/contents/{file_path}"

    response=requests.get(url,headers=Headers)

    if response.status_code==200:
        file_data=response.json()
        content=base64.b64decode(file_data["content"]).decode()
        print(f"Contenido del archivo '{file_path}':\n{content}")
        if Save:#save or update
            try:
                with open("Data/ReposInfo.json","r") as file:
                    Repos=json.load(file)
                Repos=json.loads(content)

            except FileNotFoundError:
                Repos={}
                return{"message":"Something went wrong(Not such a ReposInfo.json)","link":url,"response":False}             

            with open("Data/ReposInfo.json", "w") as file:
                json.dump(Repos, file, indent=4)
        return{"message":"Succefully ReposData Clone","link":url,"response":True}             
    else:
        print(f"Error {response.status_code}: {response.json().get('message', 'Algo salió mal')}")
        return{"message":f"Error {response.status_code}: {response.json().get('message', 'Something went wrong')}","response":False}             


