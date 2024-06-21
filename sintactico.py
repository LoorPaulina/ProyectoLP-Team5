import ply.yacc as yacc
from lexico import tokens

def p_cuerpo(p):
    '''cuerpo : expression
            | impresion
            | tupla
            | declaracion'''

#Loor Paulina
#impresion - funcion
def p_impresion_vacia(p):
    'impresion : PRINT PARENTESIS_IZ PARENTESIS_DER'

def p_impresion(p):
    'impresion : PRINT PARENTESIS_IZ expression PARENTESIS_DER'

#estructura de control - if
def p_estructura_if(p):
    'estructura_if : IF CONDITION VALOR ELSE VALOR' 
    
#estructura de datos - hash
