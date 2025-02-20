import tkinter as tk
from tkinter import ttk
from Functions.Verifiers.GitLoginVerifier import GitIsLoginVerifier
from Functions.Verifiers.LocalLoginVerifier import isLocalVerifier
from Pages.LoginPage import LoginPage
from Pages.MenuPage import MenuPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TeleArchiver")
        self.geometry("400x390")
        self.resizable(False, True)
        self.configure(bg="black")
        # Aplicamos estilos globales
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.iconbitmap("Llama.ico")
        self.style.configure(
            "TButton",
            font=("Arial", 14),
            background="black",
            foreground="#00BFFF",  # Celeste
            activebackground="#005f99",
            padding=5,
        )
        self.style.configure(
            "TLabel",
            font=("Arial", 18, "bold"),
            background="black",
            foreground="white",  # Blanco para las etiquetas
            padding=10,
        )

        # Configuración de Canvas y Scrollbar
        self.canvas = tk.Canvas(self, bg="black", borderwidth=50, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="black")

        # Configurar el scroll y expansión del canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Empaquetar el Canvas y Scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Configurar expansión para scrollable_frame
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Diccionario para almacenar las páginas
        self.frames = {}

        # Crear y mostrar la página inicial
        self.create_pages()
        self.show_initial_page()
        
    def PagesCreator(self,Page):
        page_name = Page.__name__
        frame = Page(parent=self.scrollable_frame, controller=self)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def create_pages(self):
        """Crea todas las páginas y las almacena en el diccionario de frames."""
        for Page in (LoginPage, MenuPage):
            self.PagesCreator(Page)
  

    def show_initial_page(self):
        """Determina qué página mostrar al inicio."""
        try:
            LocalVerify = isLocalVerifier()
            if GitIsLoginVerifier() and LocalVerify["status"]:
                self.show_frame("MenuPage")
            else:
                self.show_frame("LoginPage")
        except Exception as e:
            # Manejo de errores si algo falla en las verificaciones
            print(f"Error al verificar el inicio de sesión: {e}")
            self.show_frame("LoginPage")

    def show_frame(self, page_name):
        """Muestra el frame deseado."""
        frame = self.frames[page_name]
        frame.tkraise()
        
    def RefreshMenu(self):
        del self.frames["MenuPage"]
        self.PagesCreator(MenuPage)