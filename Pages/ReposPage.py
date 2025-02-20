import tkinter as tk
from tkinter import ttk
from Data.GetUserData import GetReposInfo
from Pages.ReposMenu import ReposMenu  # Asegúrate de importar la clase ReposMenu correctamente

class ReposPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="black") 
        self.Data = GetReposInfo()  # Obtiene la información de los repositorios
        self.frames = {}  # Diccionario para almacenar los frames de repositorios

        # Título de la página
        label = ttk.Label(self, text="Your Repositories", style="TLabel")
        label.pack(pady=20)
        RefreshButtom=ttk.Button(
         self, 
         text="Refresh",
        style="TButton",
        command=lambda:self.controller.Refresh()
        )
        RefreshButtom.pack(pady=5) 
        # Contenedor principal para los frames de repositorios
        self.page_container = tk.Frame(self, bg="black")
        self.page_container.pack(fill="both", expand=True)

        # Renderizar los repositorios
        self.RenderRepos()

    def RenderRepos(self):
        """Renderiza cada repositorio como un frame independiente."""
        for i in range(self.Data["Amount"]):  # Iterar por la cantidad de repositorios
            repo_frame = ReposMenu(
                parent=self.page_container, 
                controller=self.controller, 
                Element=i
            )
            repo_frame.grid(row=i, column=0, sticky="nsew")  # Ubicar cada frame en una fila diferente

            # Almacenar el frame en el diccionario para referencia futura
            self.frames[self.Data["Repos"][i]["Name"]] = repo_frame

        # Configuración del grid para expandir los frames correctamente
        for i in range(self.Data["Amount"]):
            self.page_container.grid_rowconfigure(i, weight=0)  # Hacer que las filas crezcan
        self.page_container.grid_columnconfigure(0, weight=1)  # Hacer que la única columna crezca
