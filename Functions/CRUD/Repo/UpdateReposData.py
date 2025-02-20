import requests
import base64
import json
from Alerts.AlertBox import Show_popup
from Data.GetUserData import ModifyReposInfo
from Functions.Encript import Decifre

def UpdateReposData(Url,Token):
    DecifredToken=Decifre(Token)
    headers={"Authorization":f"token {DecifredToken}"}
    response=requests.get(Url,headers=headers)
    if response.status_code==200:
        content=response.json()
        FileContent=base64.b64decode(content["content"]).decode("utf-8")
        JsonData=json.loads(FileContent)
        ModifyReposInfo(JsonData,False)
        return
    else:
        Show_popup("Error Updating ReposData")
        return