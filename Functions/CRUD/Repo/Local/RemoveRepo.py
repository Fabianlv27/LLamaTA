from Data.GetUserData import GetReposInfo, ModifyReposInfo

def RemoveRepo(Id,Refresh,Destroy):
    Repos=GetReposInfo()
    for i,Repo in enumerate(Repos["Repos"]):
        if Repo["Id"]==Id:          
           del Repos["Repos"][i]
           Repos["Amount"]-=1    
    ModifyReposInfo(Repos, True)
    Refresh()
    Destroy()
# Compare this snippet from Functions/CRUD/Repo/Local/RemoveRepo.py: