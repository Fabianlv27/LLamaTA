import json
import uuid

def UpdateLReposData(name,link,Directory,CodeMachineId,Id):
    NewDirectoryData={
        "IDMachine":CodeMachineId,
        "Directory":Directory
    }
    with open("Data/ReposInfo.json","r") as file:
        ReposInfo=json.load(file)
        
    existRepo=False
    RepoFoundOrNew=object
    for repo in ReposInfo["Repos"]:
        if repo["Id"]==Id:
            existRepo=True
            repo["Directories"].append(NewDirectoryData)
    if not existRepo:
        print("no existe")
        NewRepo={
            "Id":str(uuid.uuid4()),
            "Name":name,
            "Link":link,
            "Directories":[]
        }
        NewRepo["Directories"].append(NewDirectoryData)
        if ReposInfo["Amount"]==0:
            print("colocando objeto")
            ReposInfo["Repos"]=[NewRepo]
            ReposInfo["Amount"]+=1
        else:
            ReposInfo["Repos"].append(NewRepo)
            ReposInfo["Amount"]+=1
            
    print("AA")
    print(ReposInfo["Repos"],ReposInfo["Amount"])
    
    #Content=[] if ReposInfo["Repos"]==None else ReposInfo["Repos"]
    #print(Content)
    with open("Data/ReposInfo.json","w") as file:
        json.dump(ReposInfo,file,indent=4)
        
    return{"status":True,"content":ReposInfo}