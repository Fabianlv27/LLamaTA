import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

from Alerts.AlertBox import Show_popup

def UpdateRepo(Directory,first):
    print('hello')
    Directory = Directory.replace("\\", "/")
    try:
        status_result = subprocess.run(["git", "status","--porcelain"], cwd=Directory, check=True, capture_output=True, text=True)
        
        print(status_result.stdout.strip())
        if status_result.stdout.strip():
            Show_popup("Commiting your changes")
            subprocess.run(["git", "add", "."], cwd=Directory, check=True)
            
            root = tk.Tk()
            root.withdraw()  # Ocultar la ventana principal
            commit_message = simpledialog.askstring("Commit Message", "Introduce a message for the commit")
            root.destroy()  # Destruir la ventana después de obtener el mensaje

            subprocess.run(["git","commit","-m",f"Updated-Changes: {commit_message if not first else 'First commit'}"], cwd=Directory, check=True)   
            
    except subprocess.CalledProcessError as err:
        Show_popup(f"Error commiting your changes from the repository {err}")
        return {"message": f"Error commiting your changes from the repository {err}", "status": False}
    
        # Mostrar los archivos con conflicto usando git status
    if not first:
        status_result = subprocess.run(["git", "status"], cwd=Directory, check=True, capture_output=True, text=True)
        conflicted_files = status_result.stdout
        if not conflicted_files.strip():
            return {"message": "No conflicts found", "status": True} 
        # Si hay archivos en conflicto, muestra la ventana gráfica   
        root = tk.Tk()
        root.title("Seleccionar Prioridad de Cambios")
            
            # Mostrar los archivos con conflicto
        conflict_label = tk.Label(root, text="Archivos con conflicto:\n", font=("Arial", 12))
        conflict_label.pack(pady=10)

        conflict_text = tk.Text(root, height=10, width=50)
        conflict_text.insert(tk.END, conflicted_files)
        conflict_text.config(state=tk.DISABLED)
        conflict_text.pack(pady=10)

            # Función para manejar la elección de prioridad
        def choose_local():
            root.destroy()  # Cierra la ventana
            subprocess.run(["git", "pull", "origin", "main", "-s", "recursive", "-X", "ours"], cwd=Directory, check=True)
            messagebox.showinfo("Succes", "Repository updated, local changes prioritized.")
            return {"message": "Repository updated, local changes prioritized.", "status": True}
            
        def choose_remote():
            root.destroy()  # Cierra la ventana
            subprocess.run(["git", "pull", "origin", "main", "-s", "recursive", "-X", "theirs"], cwd=Directory, check=True)
            messagebox.showinfo("Succes", "Repository updated, remote changes prioritized.")
            return {"message": "Repository updated, remote changes prioritized.", "status": True}
            
            # Botones para elegir local o remoto
        local_button = tk.Button(root, text="local", command=choose_local, width=30, height=2)
        local_button.pack(pady=5)

        remote_button = tk.Button(root, text="remote", command=choose_remote, width=30, height=2)
        remote_button.pack(pady=5)

        root.mainloop()  # Muestra la ventana gráfica
            