import ply.yacc as yacc
from lexico import tokens

def p_cuerpo(p):
    '''cuerpo : expression
            | impresion
            | tupla
            | declaracion
            | operacionSuma'''

#Loor Paulina
#impresion - funcion
def p_impresion_vacia(p):
    'impresion : PRINT PARENTESIS_IZ PARENTESIS_DER'

def p_impresion(p):
    'impresion : PRINT PARENTESIS_IZ expression PARENTESIS_DER'

#estructura de control - if
#def p_estructura_if(p):
#    'estructura_if : IF CONDITION VALOR ELSE VALOR' 
    
#estructura de datos - hash
#Dafne Ruiz
#operaciones aritmeticas
def p_valorNumerico(p):
    """valorNumerico : FLOTANTE 
                     | ENTERO """
def p_operadores(p):
    """operadores : MAS 
                  | MENOS
                  | DIVISION
                  | MULTIPLICACION
                  | EXPONENCIACION """
def p_operacionSuma(p):
    """operacionSuma : valorNumerico operadores valorNumerico """

#estructura de datos-Array 
parser = yacc.yacc()

while True:
    try:
        s = input('lp > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
