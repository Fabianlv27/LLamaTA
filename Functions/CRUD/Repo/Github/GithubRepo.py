import requests
import tkinter as tk
from tkinter import messagebox
import uuid

from Data.GetUserData import GetReposInfo, ModifyReposInfo
from Functions.CRUD.Repo.CompareRepos import CompareRepos
from Functions.Encript import Decifre

def get_repos(username, token):
    url = "https://api.github.com/user/repos"
    token = Decifre(token)
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        NoRepeat= CompareRepos(response.json())
        return NoRepeat
    else:
        messagebox.showerror("Error", f"Failed to fetch repositories: {response.status_code}")
        return []

def GithubRepo(username, refresh, token):
    repos = get_repos(username, token)
    if not repos:
        return

    root = tk.Tk()
    root.title("Your GitHub Repositories")

    # Crear un marco contenedor
    frame = tk.Frame(root, bg="black")
    frame.pack(fill=tk.BOTH, expand=True)

    # Crear un canvas, sin forzarlo a expandir horizontalmente
    canvas = tk.Canvas(frame, bg="black")
    canvas.pack(side=tk.LEFT, fill=tk.Y)

    # Barra de desplazamiento vertical
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Contenedor dentro del canvas para los repositorios
    repo_frame = tk.Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=repo_frame, anchor="n")

    # Función para desplazar el canvas con la rueda del ratón
    def _on_mousewheel(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
    canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))

    def on_repo_click(repo_url, name):
        newData = {
            "Id": str(uuid.uuid4()),
            "Name": name,
            "Link": repo_url,
            "Directories": []
        }
        Repos = GetReposInfo()
        Repos["Repos"].append(newData)
        Repos["Amount"] += 1
        ModifyReposInfo(Repos, up=True)
        refresh()
        root.destroy()

    # Mostrar repositorios centrados con color celeste
    for repo in repos:
        repo_name = repo['name']
        label = tk.Label(repo_frame, text=repo_name, fg="#00BFFF", bg="black",
                         cursor="hand2", font=("Arial", 12, "bold"))
        label.pack(padx=10, pady=5, anchor="center")
        label.bind("<Button-1>", lambda event, url=repo['clone_url'], name=repo['name']: on_repo_click(url, name))

    # Actualiza el tamaño del frame interno y ajusta el ancho del canvas según el contenido
    repo_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.config(width=repo_frame.winfo_reqwidth())

    root.mainloop()
