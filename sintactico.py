import ply.yacc as yacc
from lexico import tokens

def p_cuerpo(p):
    '''cuerpo : operacionSuma'''

#Loor Paulina
#impresion - funcion5 +
#def p_impresion_vacia(p):
#    'impresion : PRINT PARENTESIS_IZ PARENTESIS_DER'

#def p_impresion(p):
#    'impresion : PRINT PARENTESIS_IZ expression PARENTESIS_DER'

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
def p_error(p):
  if p:
    print("Error de sintaxis en token:", p.type)
    #sintactico.errok()
  else:
    print("Syntax error at EOF")
sintactico = yacc.yacc()

while True:
  try:
    s = input('ruby > ')
  except EOFError:
    break
  if not s: continue
  result = sintactico.parse(s)
  if result != None: print(result)

