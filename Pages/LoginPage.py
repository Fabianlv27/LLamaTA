import tkinter as tk
from tkinter import ttk
from Data.SaveMI import MIExist, SaveMI
from DataTokenHandler import DataTokenHandler
from Functions.GitConsoleLogin import GitConsoleLogin
from Functions.Verifiers.CheckReposData import CheckReposData
from Functions.CRUD.ReposDataFile.ResposDataCreator import CreateNewReposData
from Functions.CRUD.ReposDataFile.GetReposData import CloneReposData
from Alerts.AlertBox import Show_popup
from Functions.SystemInf import GetOsInfo
import json
from Functions.Encript import Encripte
import uuid
from Pages.MenuPage import MenuPage

class LoginPage(tk.Frame):
    #definimos el constructor que se usara por App
    def __init__(self,parent,controller):
        DataTokenHandler()    
        #llamamos al constructor del padre (tk.Frame) para que coloque como atributo parent al parametro obtenido.
        super().__init__(parent)
        self.controller=controller
        self.configure(bg="black") 

        label=ttk.Label(self,text="Inicia sesion",style="TLabel")
        label.pack(pady=5)

        InfoText=ttk.Label(self,text="Use your Github user and email",font=("Arial,12"),foreground="white")
        InfoText.pack()
        #Declaramos las variables publicas para almacenar la data de los inputs
        self.username_var=tk.StringVar()
        self.email_var=tk.StringVar()
        self.token_var=tk.StringVar()
        #Para primera autenticacion
        UserName=ttk.Label(self,text="Username",font=("Arial", 12), foreground="#00BFFF") #de github
        UserName.pack()
        #Declara con self un atributo de una instancia de la clase loginPage(), hacen que sean publicos para ser usados por hadlesubmit
        entry=ttk.Entry(self,textvariable=self.username_var,style="TEntry",justify="center")
        entry.pack()
        #Para primera autenticacion
        UserEmail=ttk.Label(self,text="Email",font=("Arial", 12), foreground="#00BFFF") #de github
        UserEmail.pack()
        
        EmailEntry=ttk.Entry(self,textvariable=self.email_var,style="TEntry",justify="center")
        EmailEntry.pack()
        
        #Para el primer push
        TokenText=ttk.Label(self,text="Token",font=("Arial", 12), foreground="#00BFFF")
        TokenText.pack()
        TokenEntry=ttk.Entry(self,textvariable=self.token_var,style="TEntry",justify="center")
        TokenEntry.pack(pady=5)

        button=ttk.Button(
              self, 
          style="TButton",
          text="Sent",
            command=self.Handle_Submit
        )
        button.pack(pady=10)

    def Handle_Submit(self):
        
        ResponseLogin= GitConsoleLogin(self.username_var.get(),self.email_var.get())
        Link=str
        if ResponseLogin["response"]:
            self.token_var.set(Encripte(self.token_var.get()).decode())
            if CheckReposData(self.token_var.get()):
                RespClone=CloneReposData(self.token_var.get(),self.username_var.get(), True)
                if not RespClone["response"]:
                    Show_popup(RespClone["message"])
                    return
                Link=RespClone["link"]
            else:
                RespCreate= CreateNewReposData(self.token_var.get())
                Link=RespCreate["link"]
            try:
                with open("Data/UserData.json", "r") as file:
                 UserData = json.load(file)
            except FileNotFoundError:
                UserData = {}  # Si el archivo no existe, inicializa un diccionario vacío 
            ExistMi=MIExist()
            if ExistMi["status"]:
                Id=ExistMi["IDMachine"]
                print("Ya existe un ID")
            else:     
                SI=GetOsInfo()
                Id=str(uuid.uuid4())+"%%@_"+ SI["OS"]+"/"+SI["nodo"]
                print("No existe un ID")
                SaveMI(Id)
                
            UserData["UserData"]={
                "UserName":self.username_var.get(),
                "UserEmail":self.email_var.get(),
                "Token":self.token_var.get(),
                "CodeMachineId":Id,
                "ReposDataLink":Link

            } 
            with open("Data/UserData.json", "w") as file:
                json.dump(UserData, file, indent=4)
            
            #self.controller.PageCreator(MenuPage)
            Show_popup(ResponseLogin["message"])
            self.controller.RefreshMenu()
            self.controller.show_frame("MenuPage")
        else:
            Show_popup(ResponseLogin["message"])
        
            