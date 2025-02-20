import os
from tkinter import simpledialog
from Functions.CRUD.Directory.HandlerDirectory import OpenDirectory

def CreateDirectory():
                       
        filePath=OpenDirectory()
        if filePath:
            print(filePath)
        else:
            return{"status":False,"message":"Not directory selected"}
        
        DirectoryName=simpledialog.askstring("Directory Name","Set the Directory Name")
        if DirectoryName:
            print(DirectoryName)
        else:
            return{"status":False,"message":"No Directory Name"}
        
        CompleteRoot=filePath+"/"+DirectoryName
        print(CompleteRoot)
        try:
            os.mkdir(CompleteRoot)
        except FileExistsError:
            print(f"Error: The directory '{CompleteRoot}' already exists ")
            return{"message":f"Error: The directory '{CompleteRoot}' already exists ","status":False}
        except FileNotFoundError:
            print(f"Error: the parent route does not exists for'{CompleteRoot}'")
            return{"message":f"Error: the parent route does not exists for'{CompleteRoot}' ","status":False}
        except PermissionError:
            print(f"Error:You are no allowed to create directories in '{CompleteRoot}'")
            return{"message":f"Error:You are no allowed to create directories in '{CompleteRoot}' ","status":False}

        except Exception as e:
            print(f"Unexpected Error: {e}")
            return{"message":f"Unexpected Error: {e}","status":False}
    
        return {"message":"File was succesfully created","status":True,"name":DirectoryName,"path":CompleteRoot}