import os
import shutil
import stat

def on_rm_error(func, path, exc_info):
    """Change the permission of the file and retry deletion"""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def DeleteDirectory(directory):
    print(directory)
    if os.path.exists(directory):
        print("Directory successfully deleted")
        shutil.rmtree(directory, onerror=on_rm_error)  # Use on_rm_error to handle permission issues
        return {"message": "Directory successfully deleted", "status": True}
    else:
        print("Directory Unsuccessfully deleted")
        return {"message": "Directory does not exist or was moved", "status": False}
