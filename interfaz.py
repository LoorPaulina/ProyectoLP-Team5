import tkinter as tk

def validar():
    # Función para validar
    pass

def clean():
    # Función para limpiar
    pass

# Crear la ventana principal
root = tk.Tk()
root.title("RubyAnalyzer")
root.configure(bg="#1A1B26")

# Crear la barra de navegación (navbar)
navbar = tk.Frame(root, bg="#1A1A1A", height=50)
navbar.pack(side=tk.TOP, fill=tk.X)

# Crear la barra de botones
button = tk.Frame(root, bg="black", height=50)
button.pack(side=tk.TOP, fill=tk.X)

# Crear los botones en la barra de botones
btn_validar = tk.Button(button, text="Validate", command=validar, bg="#C630FB", fg="white")
btn_validar.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH, expand=True)

btn_clean = tk.Button(button, text="Clean", command=clean, bg="#C630FB", fg="white")
btn_clean.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH, expand=True)

# Etiqueta en la barra de navegación
label_navbar = tk.Label(navbar, text="RubyAnalyzer", fg="white", font=("Arial", 18, "bold"),bg="#1A1A1A") 
label_navbar.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

# Crear los tres recuadros
frame_recuadros = tk.Frame(root, padx=20, pady=20, bg="#1A1B26")
frame_recuadros.pack()

recuadro1 = tk.Frame(frame_recuadros, bg="black", padx=10, pady=10,  width=40, height=100)
recuadro1.grid(row=0, column=0, padx=10, pady=10)

title1= tk.LabelFrame(recuadro1, text="Code", bg="#C630FB", fg="white", padx=10, pady=10, width=250, height=40)
title1.pack(fill=tk.BOTH, expand=True)

text_code = tk.Text(recuadro1, width=50, height=10,)
text_code.pack(fill=tk.BOTH, expand=True)



# Ejecutar el bucle principal de la aplicación
root.mainloop()