import requests
import tkinter as tk
from tkinter import messagebox
import uuid

from Data.GetUserData import GetReposInfo, ModifyReposInfo

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"Failed to fetch repositories: {response.status_code}")
        return []

def GithubRepo(username,refresh):
    repos = get_repos(username)
    if not repos:
        return

    root = tk.Tk()
    root.title("Your GitHub Repositories")

    def on_repo_click(repo_url,name):
        print(repo_url)
        newData=        {
            "Id": str(uuid.uuid4()),
            "Name": name,
            "Link": repo_url,
            "Directories": [

            ]
        }
        Repos= GetReposInfo()
        Repos["Repos"].append(newData)
        Repos["Amount"]+=1
        ModifyReposInfo(Repos,up=True)
        refresh()
        root.destroy()
    for repo in repos:
        repo_name = repo['name']
        label = tk.Label(root, text=repo_name, fg="blue", cursor="hand2")  # Texto azul y cursor de enlace
        label.pack()
        label.bind("<Button-1>", lambda event,url=repo['html_url'],name=repo['name']: on_repo_click(url,name))  # Asigna la acción al clic

    root.mainloop()

