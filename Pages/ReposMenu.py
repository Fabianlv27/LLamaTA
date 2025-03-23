import tkinter as tk
from tkinter import ttk
from Alerts.SingleRepoMenu import SingleRepoMenu
from Data.GetUserData import GetReposInfo,GetUserInfo

class ReposMenu(tk.Frame):
    def __init__(self,parent,controller,Element):
        super().__init__(parent)
        self.controller=controller
        self.configure(bg="black",pady=0) 
        self.UserData=GetUserInfo()
        self.Data=GetReposInfo()
        self.Element=Element
        self.Belong=self.isHere(self.Data["Repos"][Element],self.UserData)
        self.Empty=self.isEmpty(self.Data["Repos"][Element])
        self.Directory=self.GetDirectory(Element)
        print(self.Belong)   
        
        buttonContainer=tk.Frame(self)
        buttonContainer.pack(anchor="w",pady=0,padx=2)
        
        User=ttk.Label(buttonContainer,text=self.Data["Repos"][Element]["Name"],font=("Arial",12),foreground="#00BFFF" if self.Belong else "grey",cursor="hand2")
        User.pack(side="left",padx=0)
        User.bind("<Button-1>",lambda event:SingleRepoMenu(self,self.Data["Repos"][self.Element],self.UserData,self.Belong,self.Directory,self.controller.Refresh,self.Empty))

    def GetDirectory(self,Element):
            for direc in self.Data["Repos"][Element]["Directories"]:
                if direc["IDMachine"]==self.UserData["CodeMachineId"]:
                    return direc["Directory"]

    def isHere(self,e,UserData):
        for direc in e["Directories"]:
            if direc["IDMachine"]==UserData["CodeMachineId"]:
                return True
        return False
    def isEmpty(self,Element):
        if len(Element["Directories"])==0:
            return True
        return False     