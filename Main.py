from Pages.App import App
#Ejecutamos la App
#Obtenemos el nombre del modulo o script que se esta ejecutando, si es un modulo obtendriamos su nombre , si el mismo archivo se obtiene __main__


if __name__=="__main__":
    app=App()
    app.mainloop()