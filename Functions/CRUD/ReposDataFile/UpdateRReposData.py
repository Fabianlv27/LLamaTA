import base64
import json
import requests
from datetime import datetime
from Functions.Encript import Decifre
from Data.GetUserData import GetUserInfo

def UpdateRReposData(content,link):
    print(content)
    token=GetUserInfo()["Token"]
    print(token)
    DecodeToken=Decifre(token)
   
    Headers={
        "Authorization":f"token {DecodeToken}",
        "Content-Type":"application/json",
    }
    shaResponse=requests.get(link,headers=Headers)
    if shaResponse.status_code==200:
        sha=shaResponse.json().get("sha")
    else:
        print(f"Error al obtener SHA: {shaResponse.status_code} - {shaResponse.json().get('message')}")
        return {"status": False, "message": f"Error al obtener SHA: {shaResponse.status_code}"}
    FileContent=content
    EncodeContent=base64.b64encode(json.dumps(FileContent).encode()).decode()
    Date=datetime.now()
    DateStr=Date.strftime("%Y-%m-%d %H:%M:%S")
    UploadData={
        "message":f"Here We will save your data, Repository updated at: {DateStr}",
        "content":EncodeContent,
        "sha":sha
    }
    print(UploadData,Headers)
    UploadResponse=requests.put(
        link,
        headers=Headers,
        json=UploadData
    )
    
    if UploadResponse.status_code == 200:
        print(f"Archivo subido: {UploadResponse.json()['content']['html_url']}")
        return{"status":True,"link":link}
    else:
        print(f"Error al subir archivo: {UploadResponse.status_code} - {UploadResponse.json().get('message')}")
        return{"status":False,"message":f"Error al subir archivo: {UploadResponse.status_code} - {UploadResponse.json().get('message')}"}