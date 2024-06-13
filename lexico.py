import ply.lex as lex
#lista de nombres de tokens 
tokens=(
    'NUMERO',
    'MAS',
    'MENOS',
    'DIVISION',
    'PARENTESIS_L'
    'PARENTESIS_R'
)

#expresiones regulares para los tokens 
t_NUMERO= r'^[-]?[0-9]*$'