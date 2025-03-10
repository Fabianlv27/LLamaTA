import subprocess
import tkinter as tk
from tkinter import messagebox

def UpdateRepo(Directory):
    Directory = Directory.replace("\\", "/")
    
    try:
        # Intenta hacer pull de la rama 'main'
        subprocess.run(["git", "pull", "origin", "main"], cwd=Directory, check=True)
        return {"message": "Repository updated successfully", "status": True}
    
    except subprocess.CalledProcessError as err:
        # Si ocurre un error, muestra el mensaje y pregunta qué hacer
        print(f"Error updating Git repo: {err}")
        
        # Mostrar los archivos con conflicto usando git status
        status_result = subprocess.run(["git", "status"], cwd=Directory, check=True, capture_output=True, text=True)
        conflicted_files = status_result.stdout
        
        # Si hay archivos en conflicto, muestra la ventana gráfica
        if "both modified" in conflicted_files:
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
            
            def choose_remote():
                root.destroy()  # Cierra la ventana
                subprocess.run(["git", "pull", "origin", "main", "-s", "recursive", "-X", "theirs"], cwd=Directory, check=True)
                messagebox.showinfo("Succes", "Repository updated, remote changes prioritized.")
            
            # Botones para elegir local o remoto
            local_button = tk.Button(root, text="local", command=choose_local, width=30, height=2)
            local_button.pack(pady=5)

            remote_button = tk.Button(root, text="remote", command=choose_remote, width=30, height=2)
            remote_button.pack(pady=5)

            root.mainloop()  # Muestra la ventana gráfica
        
        else:
            return {"message": f"Error updating the repository {err}", "status": False}
    
    except FileNotFoundError:
        return {"message": "Git is not installed or was not found in the path", "status": False}
