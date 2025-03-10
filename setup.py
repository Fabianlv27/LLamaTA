from cx_Freeze import setup, Executable
import os

# Incluye archivos adicionales como datos, carpetas o configuraciones
include_files = [
    ('Alerts/', 'Alerts/'), # Incluye una carpeta completa
    ('Data/', 'Data/') , # Incluye una carpeta completa
    ('Functions/', 'Functions/'),  # Incluye una carpeta completa
    ('Media/', 'Media/'),  # Incluye una carpeta completa
    ('Pages/', 'Pages/'),  # Incluye una carpeta completa
    ('Functions/', 'Functions/'),
    ('DataTokenHandler.py/', 'DataTokenHandler.py/'),  # Incluye una carpeta completa
    ('Llama.ico', 'Llama.ico/')  # Incluye una carpeta completa
]

# Configuración del ejecutable
executables = [
    Executable(
        script="Main.py",  # Archivo principal de tu proyecto
        base="Win32GUI",   # Usa "Win32GUI" para aplicaciones sin consola o "Console" para mantener la consola
        target_name="LLamaTA.exe",  # Nombre del ejecutable
        icon="Llama.ico"
    )
]

# Configuración del proyecto
setup(
    name="LLamaTA",
    version="1.0",
    description="Easier way to transfer files using github",
    options={
        "build_exe": {
            "packages": ["os"],  # Lista de paquetes adicionales necesarios
            "include_files": include_files
        }
    },
    executables=executables
)
