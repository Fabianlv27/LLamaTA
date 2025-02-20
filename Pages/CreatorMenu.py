import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import os
from Alerts.AlertBox import Show_popup
from Functions.CRUD.Directory.CreateDirectory import CreateDirectory
from Functions.CRUD.Directory.HandlerDirectory import OpenDirectory
from Functions.CRUD.Repo.CreateRepo import CreateRepo
from Data.GetUserData import GetUserInfo
from Functions.CRUD.Repo.Local.InitLocalRepo import InitLocalRepo
from Functions.CRUD.ReposDataFile.UpdateLReposData import UpdateLReposData
from Functions.CRUD.ReposDataFile.UpdateRReposData import UpdateRReposData

class CreatorMenu(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        self.configure(bg="black") 
        
        style=ttk.Style()
        style.configure(
            "TFIle",
            font=("Arial",12),
            background="#black",
            foreground="#00BFFF",
        )
        
        label = ttk.Label(self, text="Create a New TeleArchiver", style="TLabel")
        label.pack(pady=20)

        self.SaveOption="Create a new directory"
        options=["Create a new directory","Select a created directory"]
        combo=ttk.Combobox(self,values=options,state="readonly")
        combo.set("Create a new directory")
        combo.pack(pady=10)
        

        def OnSelect(e):
            self.SaveOption=combo.get()
            
        combo.bind("<<ComboboxSelected>>",OnSelect) 
               
        def DirectoryHandler():
            if self.SaveOption=="Create a new directory":
                CDData=CreateDirectory()
                if CDData["status"]:
                    Directory=CDData["path"]
                    DName=CDData["name"]
                else:
                    Show_popup(CDData["message"])
                    return
            else:
                Directory=OpenDirectory()
                DName=os.path.basename(Directory)
                
            Desciption=simpledialog.askstring("Description","Write a description (opcional)")
            CreateRepoData= CreateRepo(DName,Desciption if Desciption !=None else "")
            if CreateRepoData["status"]:
               InitLocalRepoRes= InitLocalRepo(Directory,DName)
               if InitLocalRepoRes["status"]:
                   UpdateLReposDataResp=UpdateLReposData(DName,CreateRepoData["link"],Directory,GetUserInfo()["CodeMachineId"],"NoId")
                   print("Uploading")
                   UpdateRReposData(UpdateLReposDataResp["content"],GetUserInfo()["ReposDataLink"])     
                   controller.Refresh()         
            else:
                Show_popup(CreateRepoData["message"])
                return
            
        User=ttk.Label(self,text="Select the directory",font=("Arial,12"),foreground="white")
        User.pack(pady=10)
        
        button = ttk.Button(
            self,
            text="Open FileExplorer",
            style="TButton",
            command=lambda: DirectoryHandler()
        )
        button.pack(pady=20)
        button.pack(pady=20)