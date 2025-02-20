import subprocess
from Alerts.AlertBox import Show_popup

def SaveChanges(Directory,Email):
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
    
    #Git Commit
    StatusResult=RunCommand(["git","status","--porcelain"])
    if not StatusResult["status"]:
        Show_popup(StatusResult["message"])
        return
    
    ModifiedFile=StatusResult["output"].splitlines()
    if not ModifiedFile:
        Show_popup("No Changes to commit")
        return
    
    PullResult=RunCommand(["git","pull","origin","main"])
    if not PullResult["status"]:
        Show_popup(PullResult["message"])
        return
    
    AddResult=RunCommand(["git","add","."])
    if not AddResult["status"]:
        Show_popup(AddResult["message"])
        return
    
    fileList=[line[:3] for line in ModifiedFile]
    CommitResult=RunCommand(["git","commit","-m",f"Updated-Changes: {', '.join(fileList)}" ])
    if not CommitResult["status"]:
        Show_popup(CommitResult["message"])
        return

    EmailVerify=RunCommand(["git","config","--get","user.email"])
    if EmailVerify["output"]=="":
        EmailSet=RunCommand(["git","config","--global",Email])
        if not EmailSet["status"]:
            Show_popup(EmailSet["message"])
            return     
    print(EmailVerify)
    

    
    PushResult=RunCommand(["git","push","origin","main"])
    if not PushResult["status"]:
        Show_popup(PushResult["message"])
        return
    Show_popup(PushResult["message"])

