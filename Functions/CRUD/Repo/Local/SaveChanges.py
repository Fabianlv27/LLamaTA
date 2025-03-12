import subprocess
from Alerts.AlertBox import Show_popup
from Functions.CRUD.Repo.UpdateRepo import UpdateRepo

def SaveChanges(Directory,Email,first):
    Directory=Directory.replace("\\","/")
    
    #Git add
    def RunCommand(command):
        try:
           result=subprocess.run(command,cwd=Directory,check=True,text=True,capture_output=True)
           print(result)
        except subprocess.CalledProcessError as err:
            return {"message":f"Error executing :{' '.join(command)} {err}","status":False}
        except FileNotFoundError:
            return{"message":"Git is not installed or the Path was not found","status":False}
        print(result.stdout.strip())
        return{"message":"Changes Succefully Saved","status":True,"output":result.stdout.strip()}
    
    UResult= UpdateRepo(Directory,first)
    if not UResult["status"]:
        Show_popup(UResult["message"])
        return
    
    PushResult=RunCommand(["git","push","origin","main"])
    if not PushResult["status"]:
        Show_popup(PushResult["message"])
        return
    Show_popup(PushResult["message"])

