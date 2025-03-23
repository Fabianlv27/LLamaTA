import tkinter as tk
from tkinter import ttk
import os
from Alerts.AlertBox import Show_popup
from Data.GetUserData import GetUserInfo
from Functions.CRUD.Repo.DeleteRepo import DeleteRepo
from Functions.CRUD.Repo.Local.DeleteLDirectory import DeleteLDirectory
from Functions.CRUD.Repo.Local.GetRepo import GetRepo
from Functions.CRUD.Repo.Local.RemoveRepo import RemoveRepo
from Functions.CRUD.Repo.Local.SaveChanges import SaveChanges
from Functions.CRUD.Repo.UpdateRepo import UpdateRepo

def SingleRepoMenu(parent, RepoElement, UserData, Belong, Directory,Refresh,Empty):
    # Crear la nueva ventana
    NewWindow = tk.Toplevel(parent)
    NewWindow.title(RepoElement["Name"])
    NewWindow.geometry("400x480")
    NewWindow.configure(bg="black")
    #Scroll configure
    canvas = tk.Canvas(NewWindow, bg="black",borderwidth=0,highlightthickness=0)
    scrollbar = ttk.Scrollbar(NewWindow, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="black")
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
   # print(Directory.replace("/","\\\\"))
    # Obtener información del usuario
    UserData = GetUserInfo()

    # Cargar imágenes (evitar recolección de basura)
    IUp = tk.PhotoImage(file="Media/Update.png").subsample(2, 2)
    ISa = tk.PhotoImage(file="Media/Save.png").subsample(2, 2)
    IStt = tk.PhotoImage(file="Media/Stettings.png").subsample(2, 2)
    ICl = tk.PhotoImage(file="Media/Clone.png").subsample(2, 2)
    IOp = tk.PhotoImage(file="Media/OpenFile.png").subsample(2, 2)
    IDel = tk.PhotoImage(file="Media/Delete.png").subsample(2, 2)
    IADel = tk.PhotoImage(file="Media/AllDelete.png").subsample(2, 2)
    IRem = tk.PhotoImage(file="Media/Remove.png").subsample(2, 2)

    # Etiqueta con el nombre del repositorio
    label = ttk.Label(scrollable_frame, text=RepoElement["Name"], wraplength=280, background="black", foreground="white")
    label.pack(pady=2)

    # Contenedor de botones
    button_frame = tk.Frame(scrollable_frame, bg="black")
    button_frame.pack(pady=10)

    # Botón de actualizar
    Update = ttk.Button(
        button_frame,
        image=IUp,
        command=lambda: UpdateRepo(Directory,False)
    )
    Update.image = IUp  # Evita recolección de basura
    Update.pack(side="left", padx=5)

    # Botón de guardar cambios
    Save = ttk.Button(
        button_frame,
        image=ISa,
        command=lambda: SaveChanges(Directory, UserData["UserEmail"], False)
    )
    Save.image = ISa
    Save.pack(side="left", padx=5) 
    
    GetB = ttk.Button(
        button_frame,
        image=ICl,
        command=lambda: GetRepo(RepoElement["Link"],UserData["CodeMachineId"],UserData["ReposDataLink"],RepoElement["Id"],RepoElement["Name"],Refresh,NewWindow.destroy)
    )
    GetB.image=ICl
    GetB.pack(side="left", padx=5) 
    
    Open = ttk.Button(
        button_frame,
        image=IOp,
        command=lambda: os.startfile(Directory.replace("/","\\\\")) if os.path.exists(Directory.replace("/","\\\\")) else Show_popup("Path does not exist or was moved")
    )
    Open.image=IOp
    Open.pack(side="left", padx=5)
    

    DirectoriesFrame=tk.Frame(NewWindow,bg="Black")
    DirectoriesFrame.pack(pady=5,fill="both",expand=True)
    
    
    IWindows=tk.PhotoImage(file="Media/OS/Windows.png").subsample(2,2)
    ILinux=tk.PhotoImage(file="Media/OS/Linux.png").subsample(2,2)
    IMac=tk.PhotoImage(file="Media/OS/Mac.png").subsample(2,2)
    
    ttk.Label(scrollable_frame,text="Dengerous Zone",wraplength=280,background="black",foreground="red").pack(padx=1)

    Row1=tk.Frame(scrollable_frame,bg="black")
    Row1.pack(anchor="w",padx=10,fill="x")
    
    Del=ttk.Button(
        Row1,
        image=IDel,
        command=lambda:DeleteLDirectory(RepoElement["Id"],UserData["CodeMachineId"],Refresh,NewWindow.destroy)
    )
    Del.image=IDel
    Del.pack(side="left",padx=1)
    
    ttk.Label(Row1,text="Delete from the device",wraplength=280,font=("Arial",10),background="black",foreground="red").pack(side="left")
    
    Row2=tk.Frame(scrollable_frame,bg="black")
    Row2.pack(anchor="w",padx=10,fill="x")
    
    ADel=ttk.Button(
        Row2,
        image=IADel,
        command=lambda:DeleteRepo(RepoElement["Id"],UserData["Token"],UserData["UserName"],Refresh,NewWindow.destroy,Directory)
    )
    ADel.image=IADel
    ADel.pack(side="left")
    
    ttk.Label(Row2,text="Delete from the server",wraplength=280,font=("Arial",10),background="black",foreground="red").pack(side="left")
    Row3 = tk.Frame(scrollable_frame, bg="black")
    Row3.pack(anchor="w", padx=10, fill="x")
    Rem=ttk.Button(
        Row3,
        image=IRem,
        command=lambda:RemoveRepo(RepoElement["Id"],Refresh,NewWindow.destroy)
    )
    Rem.image=IRem
    Rem.pack(side="left")
    
    ttk.Label(Row3,text="Remove from LLamaTA",wraplength=280,font=("Arial",10),background="black",foreground="red").pack(side="left")
    
        # Deshabilitar botones si el usuario no es dueño del repositorio
    if not Belong:
        Save.config(state=tk.DISABLED)
        Update.config(state=tk.DISABLED)
        Del.config(state=tk.DISABLED)
        Open.config(state=tk.DISABLED)
    if not Empty:
        Rem.config(state=tk.DISABLED)
        
    ttk.Label(scrollable_frame,text="Directories", wraplength=250, background="black", foreground="white").pack(padx=1)
    
    for i,direc in enumerate(RepoElement.get("Directories",[])) :
        OsData=direc['IDMachine'].split('%%@_')[1].split("/")
        Os=IWindows
        
        if OsData[0]=="Windows":
            Os=IWindows
        elif OsData[0]=="Linux":
            Os=ILinux
        else:
            Os=IMac
            
        frame=tk.Frame(scrollable_frame,bg="black")
        frame.pack(anchor="w", padx=20, pady=2, fill="x")
        
        img_label = ttk.Label(frame, image=Os, background="black")
        img_label.image =Os  # Evitar recolección de basura
        img_label.pack(side="left", padx=1)
        ttk.Label(frame,text=f"{i+1}: {OsData[1]}").pack(side="left",padx=5)
        

    # Mantener imágenes en la memoria
    NewWindow.IUp = IUp
    NewWindow.ISa = ISa
    NewWindow.IStt = IStt
    NewWindow.IOp=IOp
    NewWindow.ICl=ICl
    NewWindow.IDel=IDel
    NewWindow.IADel=IADel
    NewWindow.IRem=IRem
