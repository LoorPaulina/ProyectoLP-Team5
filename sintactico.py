import ply.yacc as yacc
from lexico import tokens
import datetime

tabla_variables={}
errors = []
ruta_carpeta="logs"
ruta_algoritmos="algoritmos"

def p_cuerpo(p):
    '''cuerpo : operacionAritmetica
              | asignacion
              | impresion
              | impresion_vacia
              | expresiones_booleanas
              | solicitudDatosTeclado
              | hashes
              | estructura_if
              | funciones
              | funcionesEstructuras'''
    #p[0] = p[1]
    
# Operaciones
#Dafne Ruiz
def p_valorNumerico(p):
    """valorNumerico : FLOTANTE 
                     | ENTERO"""
    p[0] = float(p[1])

def p_soloEnteros(p):
    """soloEnteros : ENTERO"""
    p[0] = int(p[1])

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

#AGREGAR CON PUTS Y + DE 1 ARGUMENTO
def p_impresion(p):
    """impresion : PRINT PARENTESIS_IZ expresionNumerica PARENTESIS_DER
                 | PRINT PARENTESIS_IZ VARIABLE PARENTESIS_DER """
    if  p[3] in tabla_variables:
        p[0]=tabla_variables[p[3]]  
    else:
        p[0]=p[3]
    

def p_asignacion(p):
    """asignacion : VARIABLE IGUAL expresionNumerica
                  | VARIABLE IGUAL CADENA
                  | VARIABLE IGUAL hashes"""
    tabla_variables[p[1]]=p[3]
    p[0]= (p[1],p[3])


#Paulina Loor
#corregir espacios
def p_rangos(p):
    '''rangos : PARENTESIS_IZ soloEnteros TRES_PUNTOS soloEnteros PARENTESIS_DER'''
    p[0] = (p[2], p[4])

def p_impresion_vacia(p):
    '''impresion_vacia : PRINT PARENTESIS_IZ PARENTESIS_DER
                        | PUTS PARENTESIS_IZ PARENTESIS_DER
                        | PUTS'''
    
def p_operadoresComparacion(p):
    '''operadoresComparacion : DOBLE_IGUAL
                            | DIFERENTE
                            | MAYOR_QUE
                            | MENOR_QUE
                            | MENOR_IGUAL_QUE
                            | MAYOR_IGUAL_QUE'''

def p_funcionesComparacion(p):
    '''funcionesComparacion : AND
                            | OR'''

def p_expresiones_booleanas(p):
    '''expresiones_booleanas : valorNumerico operadoresComparacion valorNumerico  
                            | rangos TRIPLE_IGUAL ENTERO
                            | VARIABLE operadoresComparacion VARIABLE
                            | VARIABLE operadoresComparacion valorNumerico
                            | valorNumerico operadoresComparacion VARIABLE''' 

def p_solicitudDatosTeclado(p):
    '''solicitudDatosTeclado : GETS '''
    p[0] = input()

def p_funciones(p):
    '''funciones : DEF VARIABLE PARENTESIS_IZ PARENTESIS_DER END
                | DEF VARIABLE PARENTESIS_IZ argumentos PARENTESIS_DER END'''   

def p_funcionesArray(p):
    '''funcionesArray : SORT'''

def p_funcionesNumeros(p):
    '''funcionesNumeros : TO_F'''

def p_funcionesEstructuras(p):
    '''funcionesEstructuras : VARIABLE PUNTO funcionesArray
                            | VARIABLE PUNTO funcionesNumeros'''

def p_argumentos(p):
    '''argumentos : VARIABLE
                    | VARIABLE COMA argumentos'''

#Estructuras de Control
def p_condicionIf(p):
    '''condicionIf : expresiones_booleanas
                | expresiones_booleanas funcionesComparacion expresiones_booleanas'''

def p_estructura_if(p):
    '''estructura_if : IF condicionIf declaracion ELSE declaracion END
                    | IF condicionIf declaracion estructura_secundaria_if'''

def p_estructura_secundaria_if(p):
    '''estructura_secundaria_if : ELSEIF condicionIf declaracion ELSE declaracion END
                                | ELSEIF condicionIf declaracion estructura_secundaria_if'''

def p_declaracion(p):
    '''declaracion : operacionAritmetica
                    | asignacion
                    | impresion
                    | impresion_vacia
                    | expresiones_booleanas
                    | solicitudDatosTeclado
                    | hashes
                    | estructura_if '''

#estructura de datos -> hash
def p_hashes(p):
    '''hashes : LLAVE_IZ elemento_hash LLAVE_DER'''

def p_claveValor(p):
    '''claveValor : VARIABLE ASIGNA_HASH valorNumerico
                  | VARIABLE ASIGNA_HASH CADENA'''
    
def p_elemento_hash(p):
    '''elemento_hash : claveValor
                    | claveValor COMA claveValor'''
    
def p_error(p):
    if p:
        message="Error de sintaxis en token:", p.type
        errors.append(message)
        #yacc.errok()
    '''else:
        print("Syntax error at EOF")'''


'''
#Dafne Ruiz
parser = yacc.yacc()

while True:
   try:
       s = input('ruby>')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)'''


#por terminar
def pruebas_loor():
    errors=[]
    parser = yacc.yacc()
    algoritmo_file="algoritmo_loor.txt"
    archivo = f"{ruta_algoritmos}/{algoritmo_file}"
    result=''
    
    with open(archivo, "r") as file:
        data = file.read()

    parser.errors = errors
    parser.parse(data)

    ahora = datetime.datetime.now()
    log_prefix = "sintactico-LoorPaulina"
    fecha_hora = ahora.strftime("%Y%m%d-%H%M%S") 
    nombre_archivo = f"{log_prefix}-{fecha_hora}.txt"


    ruta_archivo = f"{ruta_carpeta}/{nombre_archivo}"

    with open(ruta_archivo, "a+") as log_file:
        for error in errors:
            log_file.write(error + "\n")
            print (error)

    print(f"Resultado guardado en {ruta_archivo}")
    

pruebas_loor()