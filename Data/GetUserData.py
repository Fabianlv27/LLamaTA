import json

from Alerts.AlertBox import Show_popup

def GetUserInfo():
    with open("Data/UserData.json","r") as file:
        Data=json.load(file)
    return Data["UserData"]

def GetReposInfo():
    with open("Data/ReposInfo.json","r") as file:
        Data=json.load(file)
    return Data

def ModifyReposInfo(content,up):
    from Functions.CRUD.ReposDataFile.UpdateRReposData import UpdateRReposData 
    try:
        with open("Data/ReposInfo.json","w",encoding="utf-8") as file:
            json.dump(content,file,indent=4)
        print("ReposInfo Succesfully updated")
    except FileNotFoundError:
        Show_popup("The file ReposInfo.json was not found")
    except PermissionError:
        Show_popup("You are not allowed to modify the file ReposInfo.json,check if the file es opened in another program")
    except Exception as err:
        Show_popup(f"Unexpected error ocurred: {err}")
        return
    if up:
        UpdateRReposData(content,GetUserInfo()["ReposDataLink"])
    
