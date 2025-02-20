import json

with open("Data/UserData.json","r") as file:
    UserData=json.load(file)

def isLocalVerifier():
    if UserData["UserData"]=={}:
        return {"status":False}
    else:
        return {"status":True,"data":UserData["UserData"]}