import ply.lex as lex
#escritura_a_carpeta_log
import datetime
ruta_carpeta="logs"
ruta_algoritmos="algoritmos"
#palabras reservadas
reserved = {
    #Dafne Ruiz
    "true":"TRUE",
    "false":"FALSE",
    "if":"IF",
    "else":"ELSE",
    "while":"WHILE",
    "class":"CLASS",
    "module":"MODULE",
    "return":"RETURN",
    "nil":"NIL",
    "super":"SUPER",
    "self":"SELF",
    "begin":"BEGIN",
    "rescue":"RESCUE",
    "ensure":"ENSURE",
    "retry":"RETRY",
    "raise":"RAISE",
    "and":"AND",
    "or":"OR",
    "not":"NOT",
    "break":"BREAK",
    "next":"NEXT",
    "redo":"REDO",
    "alias":"ALIAS",
    "defined?":"DEFINED_QUESTION",
    "yield":"YIELD",
    #Loor Paulina
    "elseif": "ELSEIF",
    "until":"UNTIL",
    "for": "FOR",
    "in": "IN",
    "case": "CASE",
    "def": "DEF",
    "end": "END",
    "return": "RETURN",
    "each":"EACH",
    "sort": "SORT",
    "puts": "PUTS",
    "print": "PRINT",
    "printf": "PRINTF",
    "gets": "GETS",
    "chomp": "CHOMP",
    "to_f": "TO_F",
    "concat": "CONCAT"
}

tokens=[
    #Dafne Ruiz
    'VARIABLE',
    'CADENA',
    'FLOTANTE',
    'ENTERO',
    'MAS',
    'MENOS',
    'DIVISION',
    'PARENTESIS_IZ',
    'PARENTESIS_DER',
    'IGUAL_DOBLEP',
    'IGUAL',
    'COMA',
    'O_SIGNO',
    'Y_SIGNO',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MAYOR_IGUAL_QUE',
    'MENOR_IGUAL_QUE',
    'EXCLAMACION_BAJO',
    'EXCLAMACION_ALTO',
    'DIFERENTE',
    'COMENTARIO',
    'COMENTARIO_MULTI',
    #Paulina Loor
    'SIMBOLO',
    'COMILLA_S',
    'COMILLA_D',
    'LLAVE_IZ',
    'LLAVE_DER',
    'PORCENTAJE',
    'BARRA',
    'MULTIPLICACION',
    'EXPONENCIACION',
    'CORCHETE_IZ',
    'CORCHETE_DER',
    'TRIPLE_IGUAL',
    'ASIGNA_HASH',
    
]+list(reserved.values())

#expresiones regulares para los tokens 
#Dafne Ruiz
#cadenas

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t.type = reserved.get(t.value, 'CADENA')
    return t

#flotantes 

t_FLOTANTE=r'[-]?(0|[1-9]\d*)?\.{1}\d*'

#enteros

t_ENTERO=r'[-]?[0-9]+'

#operadores y delimitadores

#Ruiz Dafne

t_Y_SIGNO=r'&&'
t_COMA=r','
t_O_SIGNO=r'\|\|'
t_MAYOR_QUE=r'>'
t_MAYOR_IGUAL_QUE=r'>='
t_MENOR_IGUAL_QUE=r'<='
t_MENOR_QUE=r'<'
t_EXCLAMACION_BAJO=r'!'
t_EXCLAMACION_ALTO=r'¡'
t_DIFERENTE=r'!='
t_IGUAL=r'='
t_IGUAL_DOBLEP=r':'
t_MAS= r'\+'
t_MENOS= r'-'
t_DIVISION= r'/'
t_PARENTESIS_IZ= r'\('
t_PARENTESIS_DER= r'\)'
#Loor Paulina
t_MULTIPLICACION=r'\*'
t_COMILLA_D=r'\"'
t_COMILLA_S=r'\''
t_LLAVE_DER=r'}'
t_LLAVE_IZ=r'{'
t_PORCENTAJE=r'%'
t_BARRA=r'\|'
t_EXPONENCIACION=r'\*\*'
t_CORCHETE_IZ=r'\['
t_CORCHETE_DER=r'\]'
t_TRIPLE_IGUAL=r'==='
t_ASIGNA_HASH=r'=>'

#simbolos 

t_SIMBOLO=r'[:][a-z](\w)*'

#variables

#Ruiz Dafne y Loor Paulina
def t_VARIABLE(t):
    r'[$@]?[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.strip("@$"), 'VARIABLE')
    return t

def t_COMENTARIO(t):
    r'\#.*'
    t.value = t.value[1:].strip()  
    return t

# Comentario multilínea - Detecta el inicio de un comentario multilínea
def t_COMENTARIO_MULTI(t):
    
    r'=begin(?!.*(?:=begin[\s\S]*?=end))[\s\S]*?=end'
    return t



#ignorar espacios

t_ignore = ' \t'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejar errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer_loor=lex.lex()
data_loor="""  
# Variables globales 
$global_var = "Soy una variable global" 
 
# Clase Persona 
class Persona 
  # Variable de clase 
  @@total_personas = 0 
 
  # Constructor 
  def initialize(nombre, edad) 
    @nombre = nombre      # Variable de 
instancia 
    @edad = edad          # Variable de 
instancia 
    @@total_personas += 1 # Incrementa el 
contador de personas 
  end 
 
  # Método de instancia 
  def presentarse 
    puts "Hola, mi nombre es #{@nombre} y 
tengo #{@edad} años." 
  end 
 
  # Método de clase 
  def self.total_personas 
    @@total_personas 
  end 
end 
 
# Clase Estudiante que hereda de Persona 
class Estudiante < Persona 
  def initialize(nombre, edad, grado) 
    super(nombre, edad)   # Llama al 
constructor de la clase base 
    @grado = grado        # Variable de 
instancia 
  end 
 
  # Sobreescribe el método presentarse 
  def presentarse 
    super() 
    puts "Estoy en el grado #{@grado}." 
  end 
end 
 
# Función para pedir datos por teclado 
def pedir_datos(mensaje) 
  print mensaje 
  gets.chomp 
end 
 
# Programa principal 
puts $global_var 
 
# Pedir nombre y edad 
nombre = pedir_datos("Por favor, ingresa tu 
nombre: ") 
edad = pedir_datos("Por favor, ingresa tu 
edad: ").to_i 
 
# Crear instancia de Persona 
persona = Persona.new(nombre, edad) 
persona.presentarse 
 
# Pedir grado y crear instancia de Estudiante 
grado = pedir_datos("Por favor, ingresa tu 
grado: ") 
estudiante = Estudiante.new(nombre, edad, 
grado) 
estudiante.presentarse 
 
# Comparaciones lógicas 
puts "Eres mayor de edad" if edad >= 18 
 
# Diccionario (Hash) con símbolos 
informacion = { 
  nombre: nombre, 
  edad: edad, 
  grado: grado 
} 
 
puts "Información: #{@informacion}" 
 
# Array 
numeros = [1, 2, 3, 4, 5] 
 
# Iterar sobre el array con `each` 
numeros.each do |num| 
  puts "Número: #{num}" 
end 
 
# Operaciones aritméticas 
suma = numeros.reduce(:+) 
promedio = suma.to_f / numeros.size 
 
puts "Suma: #{@suma}, Promedio: #{@promedio}" 
 
# Caso `case` 
valor = pedir_datos("Ingresa un número del 1 
al 3: ").to_i 
 
case valor 
when 1 
  puts "Elegiste uno" 
when 2 
  puts "Elegiste dos" 
when 3 
  puts "Elegiste tres" 
else 
  puts "Valor fuera del rango" 
end 
 
# Booleanos y operaciones 
booleano1 = true 
booleano2 = false 
 
if booleano1 && !booleano2 
  puts "Booleano1 es verdadero y Booleano2 
es falso" 
end 
 
puts "Total de personas: 
#{Persona.total_personas}"
"""

#lexer_loor.input(data_loor)

#log ruiz
def pruebas_ruiz():
  lexer_ruiz=lex.lex()
  string=""
  archivo = ruta_algoritmos+"/algoritmo_ruiz.txt"
  ahora = datetime.datetime.now()
  fecha_hora = ahora.strftime("%Y%m%d-%H%M%S") 
  nombre_archivo = f"lexico-taizruiz-{fecha_hora}.txt"
  with open(archivo, 'r') as f:
    contenido = f.read().strip()
    lexer_ruiz.input(contenido)
  while True:
    tok = lexer_ruiz.token() 
    if tok is not None:
      tipo = tok.type
      valor = tok.value
      # Convertir el valor del token a cadena si es necesario
      if isinstance(valor, str):
          valor_str = valor
      else:
          valor_str = str(valor)
    string=f"Token: tipo={tipo}, valor='{valor_str}'"
    if not tok:
        break  # No more input
    else:  
        ruta_archivo = ruta_carpeta+"/"+nombre_archivo
        with open(ruta_archivo, "a+") as archivo_log:
            archivo_log.write(string + '\n')  # Escribir el resultado en el archivo

  print(f"Resultado guardado en {ruta_archivo}")

pruebas_ruiz();

