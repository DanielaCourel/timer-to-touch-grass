import tkinter as tk

def show_message_with_countdown(duration):
    #modificar esta linea para agregar listas de mensajes diferentes
    message = "Es hora de hacer una pausa. \n Levántate y estira las piernas por 1 min.\n"

    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    popup = tk.Toplevel(root)
    popup.title("Time to Touch Grass")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    popup_width = int(screen_width * 0.8)  # Ajustar el ancho de la ventana al 80% de la pantalla
    popup_height = int(screen_height * 0.8)  # Ajustar el alto de la ventana al 80% de la pantalla

    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2

    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    #modificar esta linea para poner diferentes fondos
    popup.configure(background="red")

    popup.overrideredirect(True)  # Eliminar la barra de título y los bordes
    popup.attributes('-topmost', True)  # Mantener la ventana en primer plano

    label = tk.Label(popup, text=message, fg="white", bg="red", font=("Verdana", 20))
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centrar el texto
    label.config(justify=tk.CENTER)  # Alinear el texto al centro

    def countdown(remaining):
        if remaining <= 0:
            root.deiconify()  # Mostrar la ventana principal
            popup.destroy()
            return
        label['text'] = f"{message} {remaining} segundos"
        remaining -= 1
        popup.after(1000, countdown, remaining)

    countdown(duration)
    popup.after(duration * 1000, popup.destroy)  # Terminar la ejecución después de `duration` segundos
    root.after(duration * 1000, root.quit)

    root.mainloop()
