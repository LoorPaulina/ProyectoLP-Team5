import ply.yacc as yacc
from lexico import tokens
tabla_variables={}
def p_cuerpo(p):
    '''cuerpo : operacionAritmetica
              | asignacion
              | impresion'''
    p[0] = p[1]
    
# Operaciones
#Dafne Ruiz
def p_valorNumerico(p):
    """valorNumerico : FLOTANTE 
                     | ENTERO """
    p[0] = float(p[1])
    
def p_operadores(p):
    """operadores : MAS 
                  | MENOS
                  | DIVISION
                  | MULTIPLICACION
                  | EXPONENCIACION 
                  | MODULO"""
    p[0] = p[1]
def p_expresionNumerica(p):
    """expresionNumerica : valorNumerico
                         | operacionAritmetica
                         | PARENTESIS_IZ operacionAritmetica PARENTESIS_DER"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_operacionAritmetica(p):
    """operacionAritmetica : expresionNumerica operadores expresionNumerica"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]
    elif p[2] == '/':
        if p[3] != 0:
            p[0] = p[1] / p[3]
        else:
            print("Error: Division by zero")
            p[0] = None
    elif p[2] == '**':
        p[0] = p[1] ** p[3]
def p_impresion(p):
    """impresion : PRINT PARENTESIS_IZ expresionNumerica PARENTESIS_DER
                 | PRINT PARENTESIS_IZ VARIABLE PARENTESIS_DER """
    if  p[3] in tabla_variables:
        p[0]=tabla_variables[p[3]]  
    else:
        p[0]=p[3]
    

def p_asignacion(p):
    """asignacion : VARIABLE IGUAL expresionNumerica
                  | VARIABLE IGUAL CADENA"""
    tabla_variables[p[1]]=p[3]
    p[0]= (p[1],p[3])
#def p_estructura(p):
    
def p_error(p):
    if p:
        print("Error de sintaxis en token:", p.type)
        yacc.errok()
    else:
        print("Syntax error at EOF")
#Dafne Ruiz
parser = yacc.yacc()

while True:
   try:
       s = input('ruby> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)