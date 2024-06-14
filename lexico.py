import ply.lex as lex
#palabras reservadas
reserved={
    'true':"TRUE",
    'false':"FALSE"
    }
#lista de nombres de tokens 
tokens=[
    'VARIABLE',
    'CADENA',
    'FLOTANTE',
    'ENTERO',
    'MAS',
    'MENOS',
    'DIVISION',
    'PARENTESIS_L',
    'PARENTESIS_R',
    'IGUAL'
    
]+list(reserved.values())

#expresiones regulares para los tokens 

t_FLOTANTE=r'[-]?(0|[1-9]\d*)?\.{1}\d*'
t_ENTERO= r'[-]?[0-9]+'
t_MAS= r'\+'
t_MENOS= r'-'
t_DIVISION= r'/'
t_PARENTESIS_L= r'\('
t_PARENTESIS_R= r'\)'
t_IGUAL=r'='
t_ignore = ' \t'


def t_VARIABLE(t):
    r'[$@]?[a-zA-Z]{1,}\w*'
    t.type = reserved.get(t.value.lstrip('$@'), 'VARIABLE')
    return t

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t.type = reserved.get(t.value, 'CADENA')
    return t
# Manejar nuevos líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejar errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer=lex.lex()
lexer = lex.lex()

data = ''' @false='cadena' '''

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)