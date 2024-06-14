import ply.lex as lex

#palabras reservadas
reserved = {
    #Loor Paulina
    "if":"IF",
    "else":"ELSE",
    "elseif": "ELSEIF",
    "until":"UNTIL",
    "for": "FOR",
    "in": "IN",
    "case": "CASE",
    "def": "DEF",
    "end": "END"
}

#lista de nombres de tokens 
tokens=(
    'IGUAL',
    'ENTERO',
    'MAS',
    'MENOS',
    'DIVISION',
    'PARENTESIS_L',
    'PARENTESIS_R',
    'VARIABLE',
    'FLOTANTE',
    'CADENA',
    'ARRAY',
    'DICCIONARIO',
    'SIMBOLO',
    'VERDADERO',
    'FALSO',
    'COMILLA_S',
    'COMILLA_D',
    'LLAVE_L',
    'LLAVE_R',
    'PORCENTAJE',
    'PIPELINE',
    'MULTIPLICACION',
    'EXPONENCIACION',
    'CORCHETE_L',
    'CORCHETE_R')+ tuple(
              reserved.values()) 


#expresiones regulares para los tokens
#Ruiz Dafne
t_IGUAL=r'='
t_FLOTANTE=r'^[-]?(0|[1-9]\d*)?\.{1}\d*$'
t_MAS= r'\+'
t_MENOS= r'-'
t_DIVISION= r'/'
t_PARENTESIS_L= r'\('
t_PARENTESIS_R= r'\)'
t_CADENA=r'^"[^"]*"$'


#Loor Paulina
t_MULTIPLICACION=r'\*'
t_ARRAY=r'^[\[]\s*(([-]?(0|[1-9]\d*)?\.{1}\d+)[,]?|true[,]?|false[,]?|([-]?[0-9]*)[,]?|([a-zA-Z][,]?|[a-z][,]?|[A-Z][,]?)*|)*[^,]\]$'
t_VERDADERO=r'true'
t_FALSO=r'false'
t_DICCIONARIO=r'^{\s*(([-]?(0|[1-9]\d*)?\.{1}\d+)[=][>]|true[=][>]|false[=][>]|([-]?[0-9]*)[=][>]|([a-zA-Z]+)[=][>])+\s*(([-]?(0|[1-9]\d*)?\.{1}\d+)[,]?|true[,]?|false[,]?|([-]?[0-9]*)[,]?|([a-zA-Z]+[,]?))+[^>][^,]}$'
t_SIMBOLO=r'^[:][a-z](\w)*'
t_COMILLA_D=r'\"'
t_COMILLA_S=r'\''
t_LLAVE_R=r'}'
t_LLAVE_L=r'{'
t_PORCENTAJE=r'%'
t_PIPELINE=r'\|'
t_EXPONENCIACION=r'\*\*'
t_CORCHETE_L=r'\['
t_CORCHETE_R=r'\]'

#Ruiz Dafne y Loor Paulina
def t_VARIABLE(t):
    r'^[$@]?[a-zA-Z]{1,}\w*'
    t.type = reserved.get(t.value.strip(), 'VARIABLE')
    return t

def t_ENTERO(t):
    r'^[-]?[0-9]+$'
    t.value = int(t.value)
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la posición {t.lexpos}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

data = "[a,b,c]"

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
