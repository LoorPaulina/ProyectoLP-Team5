import ply.lex as lex

#palabras reservadas
reserved = {
    #Dafne Ruiz
    "true":"TRUE",
    "false":"FALSE",
    "if":"IF",
    "else":"ELSE",
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
    'IGUAL',
    #Paulina Loor
    'ARRAY',
    'DICCIONARIO',
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
t_IGUAL=r'='
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

#colecciones

t_ARRAY=r'[\[]\s*(([-]?(0|[1-9]\d*)?\.{1}\d+)[,]?|true[,]?|false[,]?|([-]?[0-9]*)[,]?|([a-zA-Z][,]?|[a-z][,]?|[A-Z][,]?)*|)*[^,]\]'
t_DICCIONARIO=r'{\s*(([-]?(0|[1-9]\d*)?\.{1}\d+)[=][>]|true[=][>]|false[=][>]|([-]?[0-9]*)[=][>]|([a-zA-Z]+)[=][>])+\s*(([-]?(0|[1-9]\d*)?\.{1}\d+)[,]?|true[,]?|false[,]?|([-]?[0-9]*)[,]?|([a-zA-Z]+[,]?))+[^>][^,]}'

#simbolos 

t_SIMBOLO=r'[:][a-z](\w)*'

#variables

#Ruiz Dafne y Loor Paulina
def t_VARIABLE(t):
    r'[$@]?[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.strip("@$"), 'VARIABLE')
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


lexer=lex.lex()

data = ''' @false='cadena' '''



lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    else:
        print(tok)
