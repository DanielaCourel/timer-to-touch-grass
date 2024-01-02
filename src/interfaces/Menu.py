import tkinter as tk

class SettingsWindow:
    def __init__(self):
        self.settings_window = tk.Tk()
        self.settings_window.title("Configurar tiempos")

        # Barra para obtener el tiempo de actividad
        self.activity_label = tk.Label(self.settings_window, text="Tiempo de actividad (segundos):")
        self.activity_label.pack()

        self.activity_time_entry = tk.Entry(self.settings_window)
        self.activity_time_entry.pack()

        # Barra para obtener el tiempo de pausa
        self.pause_label = tk.Label(self.settings_window, text="Tiempo de pausa (segundos):")
        self.pause_label.pack()

        self.pause_time_entry = tk.Entry(self.settings_window)
        self.pause_time_entry.pack()

        # Selección de si la actividad es interactiva o no
        self.interactive_label = tk.Label(self.settings_window, text="¿Es una tarea interactiva?")
        self.interactive_label.pack()

        self.interactive = tk.BooleanVar()  # Variable que almacenará el valor booleano
        self.interactive.set(False)  # Valor predeterminado

        # Configuración de botones de radio para seleccionar sí o no
        self.yes_button = tk.Radiobutton(self.settings_window, text="Sí", variable=self.interactive, value=True)
        self.yes_button.pack()

        self.no_button = tk.Radiobutton(self.settings_window, text="No", variable=self.interactive, value=False)
        self.no_button.pack()

        # Botón para establecer los valores
        self.set_button = tk.Button(self.settings_window, text="Establecer", command=self.set_values)
        self.set_button.pack()

        # Valores por defecto
        self.activity_time = None
        self.pause_time = None
        self.ready = False

    def set_values(self):
        """Obtener los valores y cerrar la ventana"""
        self.activity_time = int(self.activity_time_entry.get())
        self.pause_time = int(self.pause_time_entry.get())
        self.interactive = self.interactive.get()  # Obtener el valor booleano seleccionado
        self.ready = True
        self.settings_window.destroy()  # Cerrar la ventana después de obtener los datos

    def open_settings_window(self):
        """Abrir la ventana de configuración"""
        self.settings_window.mainloop()
