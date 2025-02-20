import subprocess

def GitConsoleLogin(username,email):
    try:
        result_Name=subprocess.run(
        ["git","config","--global","user.name",username],
        capture_output=True,
        text=True
            )
        if result_Name.returncode!=0:
            return {"message":"Git username set to"+username+"unsuccessfully.","response":False}
        
        result_Email=subprocess.run(
        ["git","config","--global","user.email",email],
        capture_output=True,
        text=True
            )
        if result_Email.returncode!=0:
            return {"message":"Git username set to"+email+"unsuccessfully.","response":False}

        return{"message":"Git successfully signed","response":True}
    except FileNotFoundError:
        print("Git is not installed or not available in the system PATH.")
        return {"message":"Git is not installed or not available in the system PATH.","response":False}
