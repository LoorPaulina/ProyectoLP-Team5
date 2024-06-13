import ply.lex as lex
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
    'CADENA'
    
    
)

#expresiones regulares para los tokens 
t_IGUAL=r'='
t_ENTERO= r'^[-]?[0-9]*$'
t_MAS= r'\+'
t_MAS= r'-'
t_DIVISION= r'/'
t_PARENTESIS_L= r'('
t_PARENTESIS_R= r')'
t_VARIABLE=r'^[$@]?[a-zA-Z]{1,}\w*$'
t_FLOTANTE=r'^[-]?(0|[1-9]\d*)?\.{1}\d*$'
t_CADENA=r'^"[^"]*"$'

