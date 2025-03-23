
from Data.GetUserData import GetReposInfo

def CompareRepos(GHRepos):
    LocalRepos=GetReposInfo()["Repos"]
    NoRepeat=[]
    for Repo in GHRepos:
        Contains=False
        for LocalRepo in LocalRepos:
            if Repo["clone_url"]==LocalRepo["Link"]:
                print(Repo)
                Contains=True           
                break
        if not Contains:
            NoRepeat.append(Repo)
    #print(GHRepos)
    return NoRepeat
# Compare this snippet from Functions/CRUD/Repo/CompareRepos.py: