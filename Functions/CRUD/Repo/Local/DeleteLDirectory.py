
from Alerts.AlertBox import Show_popup
from Data.GetUserData import GetReposInfo, ModifyReposInfo
from Functions.CRUD.Directory.DeleteDirectory import DeleteDirectory

def DeleteLDirectory(id,IDMachine,refresh,close):
   Repos=GetReposInfo()
   print(IDMachine)
   ElementtoDelete={"Repo":-1,"Element":-1}
   for i,Repo in enumerate(Repos["Repos"]):
       if Repo["Id"]==id:
           for j,direc in enumerate(Repo["Directories"]) :
               if direc["IDMachine"]==IDMachine:
                   DeleteDirectory(direc["Directory"])
                   ElementtoDelete["Repo"]=i
                   ElementtoDelete["Element"]=j
                   break
   print(ElementtoDelete)
   if not ElementtoDelete["Element"] ==-1:
        del Repos["Repos"][ElementtoDelete["Repo"]]["Directories"][ElementtoDelete["Element"]]
        print(Repos["Repos"][ElementtoDelete["Repo"]])
        print(Repos)
        ModifyReposInfo(Repos,True)
        refresh()
        close()
   else:
       Show_popup("Directory not found")
       
        