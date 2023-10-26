import os
import tkinter as tk
from tkinter import ttk

def borrar_archivos_temporales():
    try:
        ruta_temporal = os.environ['TEMP']
        archivos_a_borrar = os.listdir(ruta_temporal)
        total_archivos = len(archivos_a_borrar)
        archivos_borrados = 0
        archivos_omitidos = 0

        for archivo in archivos_a_borrar:
            archivo_ruta = os.path.join(ruta_temporal, archivo)
            if os.path.isfile(archivo_ruta):
                try:
                    os.remove(archivo_ruta)
                    archivos_borrados += 1
                except Exception as e:
                    archivos_omitidos += 1
                progreso_var.set(int((archivos_borrados + archivos_omitidos) / total_archivos * 100))
                cantidad_label.config(text=f"Archivos omitidos: {archivos_omitidos} - Archivos eliminados: {archivos_borrados}")
                root.update_idletasks()

        if archivos_borrados > 0:
            cantidad_label.config(text=f"Archivos omitidos: {archivos_omitidos} - Archivos eliminados: {archivos_borrados} - Archivos borrados con éxito")
            progreso_var.set(0)
        else:
            cantidad_label.config(text="No se encontraron archivos para eliminar")

    except Exception as e:
        cantidad_label.config(text="Error: No se pudieron borrar archivos temporales")

root = tk.Tk()
root.title("Borrar Archivos Temporales")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

progreso_var = tk.IntVar()
progreso = ttk.Progressbar(frame, variable=progreso_var, length=300, mode='determinate')
progreso.grid(row=0, column=0, padx=10, pady=10)

boton_borrar = ttk.Button(frame, text="Borrar Archivos", command=borrar_archivos_temporales)
boton_borrar.grid(row=1, column=0, padx=10, pady=10)

cantidad_label = ttk.Label(frame, text="Haga clic en 'Borrar Archivos' para comenzar.")
cantidad_label.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()

