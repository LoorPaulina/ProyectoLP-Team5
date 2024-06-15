import ply.lex as lex

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
    "end": "END"
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
    'PARENTESIS_L',
    'PARENTESIS_R',
    'IGUAL_DOBLEP',
    'IGUAL',
    'COMA',
    'OR_SIGNO',
    'AND_SIGNO',
    'MAYOR_QUE',
    'MENOR_QUE',
    'MAYOR_IGUAL_QUE',
    'MENOR_IGUAL_QUE',
    'EXCLAMACION_LOW',
    'EXCLAMACION_HIGH',
    'DIFERENTE',
    'COMENTARIO',
    'COMENTARIO_MULTI',
    #Paulina Loor
    'SIMBOLO',
    'COMILLA_S',
    'COMILLA_D',
    'LLAVE_L',
    'LLAVE_R',
    'PORCENTAJE',
    'PIPELINE',
    'MULTIPLICACION',
    'EXPONENCIACION',
    'CORCHETE_L',
    'CORCHETE_R'
    
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

t_AND_SIGNO=r'&&'
t_COMA=r','
t_OR_SIGNO=r'\|\|'
t_MAYOR_QUE=r'>'
t_MAYOR_IGUAL_QUE=r'>='
t_MENOR_IGUAL_QUE=r'<='
t_MENOR_QUE=r'<'
t_EXCLAMACION_LOW=r'!'
t_EXCLAMACION_HIGH=r'¡'
t_DIFERENTE=r'!='
t_IGUAL=r'='
t_IGUAL_DOBLEP=r':'
t_MAS= r'\+'
t_MENOS= r'-'
t_DIVISION= r'/'
t_PARENTESIS_L= r'\('
t_PARENTESIS_R= r'\)'
#Loor Paulina
t_MULTIPLICACION=r'\*'
t_COMILLA_D=r'\"'
t_COMILLA_S=r'\''
t_LLAVE_R=r'}'
t_LLAVE_L=r'{'
t_PORCENTAJE=r'%'
t_PIPELINE=r'\|'
t_EXPONENCIACION=r'\*\*'
t_CORCHETE_L=r'\['
t_CORCHETE_R=r'\]'

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


lexer_ruiz=lex.lex()

data_ruiz = """
    # Definición de una clase con métodos y atributos 
    class Vehiculo 
    attr_accessor :marca, :modelo, :velocidad 
    def initialize(marca, modelo, velocidad = 
    0) 
        @marca = marca 
        @modelo = modelo 
        @velocidad = velocidad 
    end 
    
    def acelerar(incremento) 
        @velocidad += incremento 
    end 
    
    def frenar(decremento) 
        @velocidad -= decremento 
        @velocidad = 0 if @velocidad < 0 
    end 
    
    def estado 
        "El #{@marca} #{@modelo} va a #{@velocidad} km/h." 
    end 
    end 
    
    # Creación de un objeto 
    vehiculo1 = Vehiculo.new("Toyota", 
    "Corolla") 
    puts vehiculo1.estado 
    
    # Uso de un array 
    marcas = ["Ford", "Chevrolet", "Honda"] 
    marcas << vehiculo1.marca 
    
    # Uso de un diccionario (hash) 
    modelos = { "Ford" => "Focus", "Chevrolet" 
    => "Malibu", "Honda" => "Civic" } 
    modelos[vehiculo1.marca] = vehiculo1.modelo 
    
    # Ciclo for 
    puts "Marcas en la lista:" 
    for marca in marcas 
    puts marca 
    end 
    
    # Ciclo while 
    contador = 0 
    while contador < marcas.length 
    puts "Marca #{contador + 1}: 
    #{marcas[contador]}" 
    contador += 1 
    end 
    
    # Condicionales y expresiones booleanas 
    puts "Condicionales y expresiones 
    booleanas:" 
    marcas.each do |marca| 
    if modelos[marca] 
        puts "El modelo de #{marca} es #{modelos[marca]}." 
    else 
        puts "Modelo no registrado para #{marca}." 
    end 
    end 
    
    # Uso de case 
    puts "Uso de case:" 
    marcas.each do |marca| 
    case modelos[marca] 
    when "Focus" 
        puts "#{marca} tiene el modelo Focus." 
    when "Malibu" 
        puts "#{marca} tiene el modelo Malibu." 
    when "Civic" 
        puts "#{marca} tiene el modelo Civic." 
    when vehiculo1.modelo 
        puts "#{marca} tiene el modelo #{vehiculo1.modelo}." 
    else 
        puts "Modelo desconocido para #{marca}." 
    end 
    end 
    
    # Expresiones aritméticas 
    puts "Expresiones aritméticas:" 
    vehiculo1.acelerar(50) 
    vehiculo1.frenar(20) 
    puts vehiculo1.estado 
    
    # Expresiones booleanas y operaciones con  arrays 
    puts "Operaciones con arrays y expresiones booleanas:" 
    marcas_duplicadas = ["Ford", "Chevrolet", 
    "Honda", "Toyota", "Ford"] 
    marcas_unicas = marcas_duplicadas.uniq 
    puts "Marcas únicas: #{marcas_unicas.join(', ')}" 
    
    # Uso de un método con parámetros y valores de retorno 
    def calcular_factorial(n) 
    return 1 if n <= 1 
    n * calcular_factorial(n - 1) 
    end 
    
    puts "Factorial de 5 es: #{calcular_factorial(5)}" """


lexer_ruiz.input(data_ruiz)

# Tokenize
while True:
    tok = lexer_ruiz.token() 
    if not tok:
        break  # No more input
    else:
        print(tok)
