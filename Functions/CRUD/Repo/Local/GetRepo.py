import subprocess
import os
from Alerts.AlertBox import Show_popup
from Functions.CRUD.Directory.HandlerDirectory import OpenDirectory
from Functions.CRUD.ReposDataFile.UpdateLReposData import UpdateLReposData
from Functions.CRUD.ReposDataFile.UpdateRReposData import UpdateRReposData

def GetRepo(link,MachineID,ReposDataLink,id,Name,Refresh,Close):
    FilePath=OpenDirectory()
    print(FilePath)
    if os.path.exists(FilePath):
        try:
            subprocess.run(["git","clone",link],cwd=FilePath,check=True)
        except subprocess.CalledProcessError as err:
            Show_popup(f"Error initializing Git repo: {err}")
            return {"message":f"Error initializing Git repo: {err}","status":False}
        except FileNotFoundError:
            Show_popup("Git is not installed or the Path was not found")
            return{"message":"Git is not installed or the Path was not found","status":False}
        Show_popup("Proyect succefully cloned")
    
        UpdateLReposDataResp=UpdateLReposData("NoName","NoLink",FilePath+"/"+Name,MachineID,id)
        if UpdateLReposDataResp["status"]:
            UpdateRReposData(UpdateLReposDataResp["content"],ReposDataLink)
        else:
            return{"message":"Something went wrong Updating ReposData","status":False}   
                   
        Refresh()
        Close()
        return{"message":"Proyect succefully cloned","status":True}
    else:
        return
    