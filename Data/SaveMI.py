import os
import json
def SaveMI(Id):
    AppDataDir=os.path.join(os.getenv("APPDATA"),"LLamaTA")
    print(AppDataDir)
    if not os.path.exists(AppDataDir):
        os.makedirs(AppDataDir,exist_ok=True)
    
    FilePath=os.path.join(AppDataDir,"MachineId.json")
    
    data={"IDMachine":Id}
    with open(FilePath,"w") as file:
        json.dump(data,file,indent=4)
        
def MIExist():
    AppDataDir=os.path.join(os.getenv("APPDATA"),"LLamaTA")
    print(AppDataDir)
    if not os.path.exists(AppDataDir):
        return {"status":False,"message":"No such a AppDataDir"}
    FilePath=os.path.join(AppDataDir,"MachineId.json")
    if not os.path.exists(FilePath):
        return {"IDMachine":"None","status":False,"message":"No such a MachineId.json"}
    with open(FilePath,"r") as file:
        data=json.load(file)
    return {"IDMachine":data["IDMachine"],"status":True}