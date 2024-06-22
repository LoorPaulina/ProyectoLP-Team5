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
    #Loor Paulina
    'VARIABLECLASE',
    #Dafne Ruiz
    'VARIABLE',
    'CADENA',
    'FLOTANTE',
    'ENTERO',
    'MAS',
    'MENOS',
    'DIVISION',
    'MODULO',
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
    #Daniel Picon
    'PREGUNTA',
    
]+list(reserved.values())

#expresiones regulares para los tokens 
#Dafne Ruiz
#cadenas

#flotantes 
def t_FLOTANTE(t):
    r'[-]?(0|[1-9]\d*)?\.{1}\d*'
    t.value=float(t.value)
    return t 


#enteros
def t_ENTERO(t):
    r'[-]?[0-9]+'
    t.value=int(t.value)
    return t 

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
t_MODULO= r'%'
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
t_PREGUNTA=r'\?'

#simbolos 

t_SIMBOLO=r'[:][a-z](\w)*'

#variables

#Ruiz Dafne y Loor Paulina
def t_VARIABLECLASE(t):
    r'[$@]{2}[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.strip("@"), 'VARIABLECLASE')
    return t

def t_VARIABLE(t):
    r'[$@]?[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.strip("@$"), 'VARIABLE')
    return t

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t.type = reserved.get(t.value, 'CADENA')
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

lexer = lex.lex()

def log_function(lexer_instance, algoritmo_file, log_prefix):
    string = ""
    archivo = f"{ruta_algoritmos}/{algoritmo_file}"
    ahora = datetime.datetime.now()
    fecha_hora = ahora.strftime("%Y%m%d-%H%M%S") 
    nombre_archivo = f"{log_prefix}-{fecha_hora}.txt"
    
    with open(archivo, 'r') as f:
        contenido = f.read().strip()
        lexer_instance.input(contenido)
    
    ruta_archivo = f"{ruta_carpeta}/{nombre_archivo}"
    
    while True:
        tok = lexer_instance.token()
        if not tok:
            break
        tipo = tok.type
        valor = tok.value
        valor_str = valor if isinstance(valor, str) else str(valor)
        string = f"Token: tipo={tipo}, valor='{valor_str}'"
        
        with open(ruta_archivo, "a+") as archivo_log:
            archivo_log.write(string + '\n')
    
    print(f"Resultado guardado en {ruta_archivo}")

def pruebas_ruiz():
    lexer_ruiz = lex.lex()
    log_function(lexer_ruiz, "algoritmo_ruiz.txt", "lexico-taizruiz")

def pruebas_loor():
    lexer_loor = lex.lex()
    log_function(lexer_loor, "algoritmo_loor.txt", "lexico-LoorPaulina")

def pruebas_picon():
    lexer_picon = lex.lex()
    log_function(lexer_picon, "algoritmo_picon.txt", "lexico-PiconDaniel")

# Uncomment to run tests
# pruebas_ruiz()
# pruebas_loor()
# pruebas_picon()