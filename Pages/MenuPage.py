import tkinter as tk
from tkinter import ttk
from Data.GetUserData import GetUserInfo
from Functions.CRUD.Repo.UpdateReposData import UpdateReposData
from Functions.Verifiers.LocalLoginVerifier import isLocalVerifier
from Pages.ReposPage import ReposPage
from Pages.CreatorMenu import CreatorMenu

class MenuPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        self.configure(bg="black") 
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.Refresh=controller.RefreshMenu
        self.UserInfo=GetUserInfo()
        
        label = ttk.Label(self, text="Menú Principal", style="TLabel")
        label.pack(pady=20)
        LocalVerify=isLocalVerifier()
        if LocalVerify["status"]:
            UpdateReposData(self.UserInfo["ReposDataLink"],self.UserInfo["Token"])
            User=ttk.Label(self,text=LocalVerify["data"]["UserName"])
            User.pack(pady=10)
        
        CMButton=ttk.Button(
         self, 
         text="Create New",
        style="TButton",
        command=lambda:self.show_frame("CreatorMenu")
        )
        CMButton.pack(pady=5)
        
        ReposMenuB=ttk.Button(
         self, 
         text="My Repos",
        style="TButton",
        command=lambda:self.show_frame("ReposPage")
        )
        ReposMenuB.pack(pady=5)
        
        button= ttk.Button(
         self, 
         text="Login",
        style="TButton",
        command=lambda: controller.show_frame("LoginPage")
        )
        button.pack(pady=20)
        
        self.page_container = tk.Frame(self, bg="black")
        self.page_container.pack(fill="both", expand=True)


        # Diccionario para almacenar las páginas
        self.frames = {}

        # Crear y mostrar la página inicial
        self.create_pages()
        self.show_initial_page()

    def create_pages(self):
        """Crea todas las páginas y las almacena en el diccionario de frames."""
        for Page in (CreatorMenu, ReposPage):
            page_name = Page.__name__
            frame = Page(parent=self.page_container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
               # Configurar grid en el contenedor para expandir los frames
        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)
          
    def show_initial_page(self):
        self.show_frame("ReposPage")
        
    def show_frame(self, page_name):
        """Muestra el frame deseado."""
        frame = self.frames[page_name]
        frame.tkraise()      

                 