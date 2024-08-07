import tkinter as tk
import sintactico as s
from lexico import lexer
import lexico as l
from PIL import Image,ImageTk

def validar():
    #tomar lo del la textbox 
    #guarda en code_output
    save_to_file()
    # text_code1.delete("1.0", tk.END)
    # #manda output al parser
    # #parser guarda en validation y lo carga en la pantalla 
    load_from_file()
    print(s.tabla_variables)
        
    pass

def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    help_window.geometry("700x600")
    help_label_3 = tk.Label(help_window, text="Ejemplo", padx=20, pady=20)
    help_label_3.pack()

    #ayuda
    imageHelp=Image.open("help.PNG")
    imageHelp=imageHelp.resize((700,400),Image.Resampling.LANCZOS)
    photoHelp = ImageTk.PhotoImage(imageHelp)


    label_help=tk.Label(help_window,image=photoHelp,bg="#1A1A1A")
    label_help.pack(side=tk.LEFT, padx=10, pady=10)
    help_label_2.pack()
    help_label_2 = tk.Label(help_window, text="Ejemplo: \n a=3 \n\n if a>3 \n puts 5 \n end", padx=20, pady=20)

def load_from_file():
    s.tabla_variables.clear()
    s.errores_semanticos.clear()
    l.noReconocidos.clear()
    s.errors.clear()
    stringAnalisis=""
    codigo=open("code_output.txt","r")
    for linea in codigo.readlines():
        stringAnalisis = stringAnalisis + " "+ linea.strip()
          
    with open("code_output.txt", "w") as file:
        file.write(stringAnalisis)
    
    file=open("code_output.txt","r")
    for linea in file.readlines():
        lexer.input(linea)
        s.pruebasSemanticoInterfaz(linea)

    try:
        with open("code_validation.txt", "r") as file:
            file_content = file.read()
        text_code1.delete("1.0", tk.END)
        text_code1.insert(tk.END, file_content)

        
    except FileNotFoundError:
        text_code1.delete("1.0", tk.END)
        text_code1.insert(tk.END, "No se encontró el archivo 'code_validation.txt'.")

def clean():
    text_code.delete("1.0", tk.END)
    text_code1.delete("1.0", tk.END)
    pass

def save_to_file():
    code_content = text_code.get("1.0", tk.END)
    with open("code_output.txt", "w") as file:
        file.write(code_content)

# Crear la ventana principal
root = tk.Tk()
root.title("RubyAnalyzer")
root.configure(bg="#1A1B26")
root.geometry("1000x600")

# Crear la barra de navegación (navbar)
navbar = tk.Frame(root, bg="#1A1A1A", height=50)
navbar.pack(side=tk.TOP, fill=tk.X)
#logo
image=Image.open("logo.png")
image=image.resize((60,60),Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)


label_img=tk.Label(navbar,image=photo,bg="#1A1A1A")
label_img.pack(side=tk.LEFT, padx=10, pady=10)

# Etiqueta en la barra de navegación
label_navbar = tk.Label(navbar, text="RubyAnalyzer", fg="white", font=("Arial", 18, "bold"),bg="#1A1A1A") 
label_navbar.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

# Crear los tres recuadros
frame_recuadros = tk.Frame(root, padx=20, pady=20, bg="#1A1B26")
frame_recuadros.pack()
#recuadros
recuadro1 = tk.Frame(frame_recuadros, bg="#1A1B26", padx=10, pady=10,  width=40, height=200)
recuadro1.grid(row=0, column=0, padx=10, pady=10)

title1= tk.LabelFrame(recuadro1, text="Code", bg="#C630FB", fg="white", padx=10, pady=10, width=250, height=40)
title1.pack(fill=tk.BOTH, expand=True)
text_frame=tk.Frame(title1)
text_frame.pack(fill=tk.BOTH, expand=True)
text_code = tk.Text(text_frame, width=50, height=20,)
text_code.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Crear la Scrollbar vertical
scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_code.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Configurar el widget Text para usar la Scrollbar
text_code.config(yscrollcommand=scrollbar.set)

recuadro2 = tk.Frame(frame_recuadros, bg="#1A1B26", padx=10, pady=10,  width=40, height=200)
recuadro2.grid(row=0, column=1, padx=10, pady=10)

title2= tk.LabelFrame(recuadro2, text="Result", bg="#C630FB", fg="white", padx=10, pady=10, width=250, height=40)
title2.pack(fill=tk.BOTH, expand=True)
text_frame1=tk.Frame(title2)
text_frame1.pack(fill=tk.BOTH, expand=True)
text_code1 = tk.Text(text_frame1, width=50, height=20,)
text_code1.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
# Crear la Scrollbar vertical
scrollbar1 = tk.Scrollbar(text_frame1, orient=tk.VERTICAL, command=text_code.yview)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
# Configurar el widget Text para usar la Scrollbar
text_code1.config(yscrollcommand=scrollbar1.set)
# Crear la barra de botones
button = tk.Frame(root, bg="#1A1B26",width=100, height=50)
button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

container = tk.Frame(button, bg="#1A1B26")
container.pack(expand=True)

# Crear los botones en la barra de botones
btn_validar = tk.Button(container, text="Validate", command=validar, bg="#C630FB", fg="white", width=20,height=2 )
btn_validar.pack(side=tk.LEFT, padx=10, pady=5)

btn_clean = tk.Button(container, text="Clean", command=clean, bg="#C630FB", fg="white", width=20, height=2)
btn_clean.pack(side=tk.LEFT, padx=10, pady=5)

recuadro3 = tk.Frame(frame_recuadros, bg="#1A1B26", padx=10, pady=10, width=40, height=200)
recuadro3.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

title3 = tk.LabelFrame(recuadro3, text="Instructions", bg="#C630FB", fg="white", padx=10, pady=10, width=250, height=40)
title3.pack(fill=tk.BOTH, expand=True)

instruction_label = tk.Label(title3, text="Para validar, escribir el código dentro del recuadro Code.", bg="#1A1B26", fg="white", font=("Arial", 14))
instruction_label.pack(fill=tk.BOTH, expand=True)

btn_help = tk.Button(navbar, text="Help", command=show_help, bg="#C630FB", fg="white", width=10, height=2)
btn_help.pack(side=tk.RIGHT, padx=10, pady=5)
# Ejecutar el bucle principal de la aplicación
root.mainloop()

