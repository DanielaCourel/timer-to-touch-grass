import tkinter as tk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")

def show_message_with_countdown(message, duration):
    root = tk.Tk()
    root.title("Time to Touch Grass")
    root.withdraw()  # Ocultar la ventana principal

    popup = tk.Toplevel(root)
    popup.title("Time to Touch Grass")
    popup.geometry("900x200")  # Establecer el tamaño
    center_window(popup, 900, 200)  # Centrar la ventana

    popup.configure(bg="red")

    label = tk.Label(popup, text=message, fg="white", bg="red", font=("Verdana", 15))
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
    popup.after(duration * 1000, popup.destroy)  # Terminar la ejecución después de 6 segundos
    root.after(duration * 1000, root.quit)

    root.mainloop()