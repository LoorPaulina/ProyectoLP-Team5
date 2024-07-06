
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ASIGNA_HASH BARRA BEGIN BREAK CADENA CASE CHOMP CLASS COMA COMENTARIO COMENTARIO_MULTI COMILLA_D COMILLA_S CONCAT CORCHETE_DER CORCHETE_IZ DEF DEFINED_QUESTION DIFERENTE DIVISION DO DOBLE_IGUAL EACH ELSE ELSEIF END ENSURE ENTERO EXCLAMACION_ALTO EXCLAMACION_BAJO EXPONENCIACION FALSE FLOTANTE FOR GETS ID_CLASE IF IGUAL IGUAL_DOBLEP IN INITIALIZE LLAVE_DER LLAVE_IZ MAS MAYOR_IGUAL_QUE MAYOR_QUE MENOR_IGUAL_QUE MENOR_QUE MENOS MODULE MODULO MULTIPLICACION NEXT NIL NOT OR O_SIGNO PARENTESIS_DER PARENTESIS_IZ PORCENTAJE PREGUNTA PRINT PRINTF PUNTO PUTS RAISE REDO RESCUE RETRY RETURN SELF SIMBOLO SORT SUPER TO_F TRES_PUNTOS TRIPLE_IGUAL TRUE UNTIL VARIABLE VARIABLECLASE WHEN WHILE YIELD Y_SIGNOcuerpo : operacionAritmetica\n              | concatenacionSimpleCadena\n              | asignacion\n              | impresion\n              | impresion_vacia\n              | expresiones_booleanas\n              | solicitudDatosTeclado\n              | hashes\n              | estructura_if\n              | funciones\n              | funcionesEstructuras\n              | array\n              | each_array\n              | comentarios\n              | each_hash\n              | sentencia_while\n              | sentencia_case\n              | sentencias_when\n              | sentencia_until\n              | definicion_clasevalorCadena : CADENA\n                   | VARIABLE concatenacionSimpleCadena : valorCadena MAS valorCadena\n                                 | concatenacionSimpleCadena MAS valorCadenavalorNumerico : FLOTANTE \n                     | ENTERO\n                     | VARIABLEsoloEnteros : ENTEROoperadores : MAS \n                  | MENOS\n                  | DIVISION\n                  | MULTIPLICACION\n                  | EXPONENCIACION \n                  | MODULOexpresionNumerica : valorNumerico\n                         | operacionAritmetica\n                         | PARENTESIS_IZ operacionAritmetica PARENTESIS_DERoperacionAritmetica : expresionNumerica operadores expresionNumericavalor_print : PRINT\n                   | PUTS valores : valor\n               | valor COMA valores\n               | valor estructura_ifUnaLineavalor : CADENA\n             | valorNumerico\n             | VARIABLE\n             | VARIABLECLASEimpresion : valor_print valoresasignacion : VARIABLE IGUAL CADENA\n                  | VARIABLE IGUAL expresionNumerica\n                  | VARIABLE IGUAL hashes\n                  | VARIABLE IGUAL arrayelementos_array : elemento_array COMA elementos_array\n                       | elemento_array elemento_array : CADENA\n                      | ENTERO\n                      | FLOTANTE\n                      | array\n                      | VARIABLEarray : CORCHETE_IZ elementos_array CORCHETE_DER\n             | CORCHETE_IZ CORCHETE_DEReach_array : VARIABLE PUNTO DO BARRA VARIABLE BARRA cuerpo_each ENDcuerpo_each : cuerpo\n                   | vaciovacio :  rangos : PARENTESIS_IZ soloEnteros TRES_PUNTOS soloEnteros PARENTESIS_DERcomentarios : COMENTARIO \n                    | COMENTARIO_MULTIimpresion_vacia : PRINT PARENTESIS_IZ PARENTESIS_DER\n                        | PUTS PARENTESIS_IZ PARENTESIS_DER\n                        | PUTSoperadoresComparacion : DOBLE_IGUAL\n                            | DIFERENTE\n                            | MAYOR_QUE\n                            | MENOR_QUE\n                            | MENOR_IGUAL_QUE\n                            | MAYOR_IGUAL_QUEfuncionesComparacion : AND\n                            | ORexpresiones_booleanas : valorNumerico operadoresComparacion valorNumerico  \n                            | rangos TRIPLE_IGUAL ENTERO\n                            | VARIABLE operadoresComparacion VARIABLE\n                            | VARIABLE operadoresComparacion valorNumerico\n                            | valorNumerico operadoresComparacion VARIABLEsolicitudDatosTeclado : GETS \n                            | GETS PUNTO funcionesFormatoImpresion funciones : DEF VARIABLE PARENTESIS_IZ PARENTESIS_DER END\n                 | DEF VARIABLE PARENTESIS_IZ argumentos PARENTESIS_DER ENDfuncionesArray : SORT\n                      | FOR EACHfuncionesFormatoImpresion : CHOMPfuncionesNumeros : TO_FfuncionesEstructuras : VARIABLE PUNTO funcionesArray\n                            | VARIABLE PUNTO funcionesNumerosargumentos : VARIABLE\n                    | VARIABLE COMA argumentoscondicionIf : expresiones_booleanas\n                | expresiones_booleanas funcionesComparacion expresiones_booleanasestructura_if : IF condicionIf declaracion ELSE declaracion END\n                    | IF condicionIf declaracion estructura_secundaria_ifestructura_ifUnaLinea : IF condicionIfestructura_secundaria_if : ELSEIF condicionIf declaracion ELSE declaracion END\n                                | ELSEIF condicionIf declaracion estructura_secundaria_ifdeclaracion : operacionAritmetica\n                    | asignacion\n                    | impresion\n                    | impresion_vacia\n                    | expresiones_booleanas\n                    | solicitudDatosTeclado\n                    | hashes\n                    | estructura_if\n                     sentencia_while : WHILE declaracion DO sentencia_while END\n                      | WHILE declaracion DO declaracion END sentencia_case : CASE declaracion sentencia_when ENDsentencias_when : sentencia_when\n                    | sentencia_when sentencias_whensentencia_when : WHEN declaracion IGUAL_DOBLEP declaracionsentencia_until : UNTIL declaracion DO declaracion ENDhashes : LLAVE_IZ elemento_hash LLAVE_DER\n              | LLAVE_IZ LLAVE_DERclaveValor : VARIABLE ASIGNA_HASH valorNumerico\n                  | VARIABLE ASIGNA_HASH CADENAelemento_hash : claveValor\n                    | claveValor COMA claveValoreach_hash : VARIABLE PUNTO EACH DO BARRA each_args_hash declaracion ENDeach_args_hash : VARIABLE COMA VARIABLE BARRA\n                 | VARIABLE BARRAdefinicion_clase : CLASS ID_CLASE DEF INITIALIZE PARENTESIS_IZ argumentos PARENTESIS_DER'
    
_lr_action_items = {'VARIABLE':([0,26,27,28,29,32,34,35,36,37,40,41,43,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,61,62,63,64,72,79,86,87,124,125,133,135,140,141,142,146,147,149,150,151,153,155,156,158,160,161,170,172,173,185,188,189,195,196,198,207,208,210,217,],[24,69,-39,77,-40,-26,85,89,91,99,109,109,109,-25,109,116,77,-29,-30,-31,-32,-33,-34,116,77,124,-72,-73,-74,-75,-76,-77,77,141,109,-97,-27,-83,69,89,-80,-27,-81,85,77,89,-78,-79,174,99,109,109,109,184,109,89,-98,197,109,174,174,24,109,214,-127,109,-126,]),'PRINT':([0,32,40,41,43,45,46,86,87,124,125,140,141,142,156,158,160,170,173,188,196,198,208,210,217,],[27,-26,27,27,27,-25,27,27,-97,-27,-83,-80,-27,-81,27,27,27,27,-98,27,27,27,-127,27,-126,]),'PUTS':([0,32,40,41,43,45,46,86,87,124,125,140,141,142,156,158,160,170,173,188,196,198,208,210,217,],[29,-26,29,29,29,-25,29,29,-97,-27,-83,-80,-27,-81,29,29,29,29,-98,29,29,29,-127,29,-126,]),'GETS':([0,32,40,41,43,45,46,86,87,124,125,140,141,142,156,158,160,170,173,188,196,198,208,210,217,],[33,-26,33,33,33,-25,33,33,-97,-27,-83,-80,-27,-81,33,33,33,33,-98,33,33,33,-127,33,-126,]),'LLAVE_IZ':([0,32,40,41,43,45,46,56,86,87,124,125,140,141,142,156,158,160,170,173,188,196,198,208,210,217,],[34,-26,34,34,34,-25,34,34,34,-97,-27,-83,-80,-27,-81,34,34,34,34,-98,34,34,34,-127,34,-126,]),'IF':([0,32,40,41,43,45,46,66,67,68,69,70,86,87,124,125,140,141,142,156,158,160,170,173,188,196,198,208,210,217,],[35,-26,35,35,35,-25,35,135,-44,-45,-27,-47,35,-97,-27,-83,-80,-27,-81,35,35,35,35,-98,35,35,35,-127,35,-126,]),'DEF':([0,113,196,],[36,159,36,]),'CORCHETE_IZ':([0,37,56,155,196,],[37,37,37,37,37,]),'COMENTARIO':([0,196,],[38,38,]),'COMENTARIO_MULTI':([0,196,],[39,39,]),'WHILE':([0,156,196,],[40,40,40,]),'CASE':([0,196,],[41,41,]),'UNTIL':([0,196,],[43,43,]),'CLASS':([0,196,],[44,44,]),'PARENTESIS_IZ':([0,27,28,29,32,35,40,41,43,45,46,48,49,50,51,52,53,54,56,72,86,87,91,124,125,135,140,141,142,149,150,151,156,158,160,170,172,173,182,188,196,198,208,210,217,],[28,71,72,78,-26,90,28,28,28,-25,28,72,-29,-30,-31,-32,-33,-34,72,72,28,-97,153,-27,-83,90,-80,-27,-81,90,-78,-79,28,28,28,28,90,-98,195,28,28,28,-127,28,-126,]),'CADENA':([0,26,27,29,37,47,55,56,133,147,155,196,],[25,67,-39,-40,95,25,25,120,67,169,95,25,]),'FLOTANTE':([0,26,27,28,29,32,35,37,40,41,43,45,46,48,49,50,51,52,53,54,56,57,59,60,61,62,63,64,72,79,86,87,124,125,133,135,140,141,142,147,149,150,151,155,156,158,160,170,172,173,188,196,198,208,210,217,],[45,45,-39,45,-40,-26,45,97,45,45,45,-25,45,45,-29,-30,-31,-32,-33,-34,45,45,-72,-73,-74,-75,-76,-77,45,45,45,-97,-27,-83,45,45,-80,-27,-81,45,45,-78,-79,97,45,45,45,45,45,-98,45,45,45,-127,45,-126,]),'ENTERO':([0,26,27,28,29,32,35,37,40,41,43,45,46,48,49,50,51,52,53,54,56,57,59,60,61,62,63,64,72,79,80,86,87,90,124,125,133,135,138,140,141,142,147,149,150,151,155,156,158,160,170,172,173,188,196,198,208,210,217,],[32,32,-39,75,-40,-26,32,96,32,32,32,-25,32,32,-29,-30,-31,-32,-33,-34,32,32,-72,-73,-74,-75,-76,-77,32,32,142,32,-97,152,-27,-83,32,32,152,-80,-27,-81,32,32,-78,-79,96,32,32,32,32,32,-98,32,32,32,-127,32,-126,]),'WHEN':([0,29,32,33,42,45,65,66,67,68,69,70,76,77,83,87,93,101,102,103,104,105,106,107,108,110,117,118,120,121,122,123,124,125,134,136,137,139,140,141,142,143,144,145,154,164,165,171,173,183,196,199,211,218,],[46,-71,-26,-85,46,-25,-48,-41,-44,-45,-27,-47,-35,-27,-120,-97,-61,-104,-105,-106,-107,-108,-109,-110,-111,46,-38,-36,-49,-50,-51,-52,-27,-83,-43,-69,-37,-70,-80,-27,-81,-86,-91,-119,-60,-42,-101,-100,-98,-117,46,-99,-103,-102,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,25,29,32,33,38,39,42,45,65,66,67,68,69,70,76,77,83,87,93,101,102,103,104,105,106,107,108,111,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,134,136,137,139,140,141,142,143,144,145,154,163,164,165,171,173,180,183,190,192,193,194,199,202,211,212,213,215,218,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-71,-26,-85,-67,-68,-115,-25,-48,-41,-44,-45,-27,-47,-35,-27,-120,-97,-61,-104,-105,-106,-107,-108,-109,-110,-111,-116,-24,-22,-38,-36,-23,-49,-50,-51,-52,-27,-83,-93,-94,-89,-92,-43,-69,-37,-70,-80,-27,-81,-86,-91,-119,-60,-90,-42,-101,-100,-98,-114,-117,-87,-113,-112,-118,-99,-88,-103,-128,-62,-125,-102,]),'END':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,25,29,32,33,38,39,42,45,65,66,67,68,69,70,76,77,83,87,93,101,102,103,104,105,106,107,108,111,115,116,117,118,119,120,121,122,123,124,125,126,127,130,132,134,136,137,139,140,141,142,143,144,145,154,157,163,164,165,171,173,175,178,179,180,181,183,187,190,191,192,193,194,196,199,202,204,205,206,209,211,212,213,215,216,218,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-71,-26,-85,-67,-68,-115,-25,-48,-41,-44,-45,-27,-47,-35,-27,-120,-97,-61,-104,-105,-106,-107,-108,-109,-110,-111,-116,-24,-22,-38,-36,-23,-49,-50,-51,-52,-27,-83,-93,-94,-89,-92,-43,-69,-37,-70,-80,-27,-81,-86,-91,-119,-60,180,-90,-42,-101,-100,-98,190,192,193,-114,194,-117,199,-87,202,-113,-112,-118,-65,-99,-88,213,-63,-64,215,-103,-128,-62,-125,218,-102,]),'MAS':([2,3,22,23,24,25,30,32,45,73,75,76,77,101,109,115,116,117,118,119,121,137,],[-36,47,49,55,-22,-21,-35,-26,-25,-36,-26,-35,-27,-36,-27,-24,-22,49,-36,-23,49,-37,]),'MENOS':([2,22,24,30,32,45,73,75,76,77,101,109,117,118,121,137,],[-36,50,-27,-35,-26,-25,-36,-26,-35,-27,-36,-27,50,-36,50,-37,]),'DIVISION':([2,22,24,30,32,45,73,75,76,77,101,109,117,118,121,137,],[-36,51,-27,-35,-26,-25,-36,-26,-35,-27,-36,-27,51,-36,51,-37,]),'MULTIPLICACION':([2,22,24,30,32,45,73,75,76,77,101,109,117,118,121,137,],[-36,52,-27,-35,-26,-25,-36,-26,-35,-27,-36,-27,52,-36,52,-37,]),'EXPONENCIACION':([2,22,24,30,32,45,73,75,76,77,101,109,117,118,121,137,],[-36,53,-27,-35,-26,-25,-36,-26,-35,-27,-36,-27,53,-36,53,-37,]),'MODULO':([2,22,24,30,32,45,73,75,76,77,101,109,117,118,121,137,],[-36,54,-27,-35,-26,-25,-36,-26,-35,-27,-36,-27,54,-36,54,-37,]),'IGUAL':([24,109,],[56,56,]),'PUNTO':([24,33,],[58,81,]),'DOBLE_IGUAL':([24,30,32,45,88,89,109,],[59,59,-26,-25,59,59,59,]),'DIFERENTE':([24,30,32,45,88,89,109,],[60,60,-26,-25,60,60,60,]),'MAYOR_QUE':([24,30,32,45,88,89,109,],[61,61,-26,-25,61,61,61,]),'MENOR_QUE':([24,30,32,45,88,89,109,],[62,62,-26,-25,62,62,62,]),'MENOR_IGUAL_QUE':([24,30,32,45,88,89,109,],[63,63,-26,-25,63,63,63,]),'MAYOR_IGUAL_QUE':([24,30,32,45,88,89,109,],[64,64,-26,-25,64,64,64,]),'VARIABLECLASE':([26,27,29,133,],[70,-39,-40,70,]),'DO':([29,32,33,45,58,65,66,67,68,69,70,76,77,83,87,93,100,101,102,103,104,105,106,107,108,112,117,118,120,121,122,123,124,125,129,134,136,137,139,140,141,142,143,144,145,154,164,165,171,173,199,211,218,],[-71,-26,-85,-25,128,-48,-41,-44,-45,-27,-47,-35,-27,-120,-97,-61,156,-104,-105,-106,-107,-108,-109,-110,-111,158,-38,-36,-49,-50,-51,-52,-27,-83,162,-43,-69,-37,-70,-80,-27,-81,-86,-91,-119,-60,-42,-101,-100,-98,-99,-103,-102,]),'IGUAL_DOBLEP':([29,32,33,45,65,66,67,68,69,70,76,77,83,87,93,101,102,103,104,105,106,107,108,114,117,118,120,121,122,123,124,125,134,136,137,139,140,141,142,143,144,145,154,164,165,171,173,199,211,218,],[-71,-26,-85,-25,-48,-41,-44,-45,-27,-47,-35,-27,-120,-97,-61,-104,-105,-106,-107,-108,-109,-110,-111,160,-38,-36,-49,-50,-51,-52,-27,-83,-43,-69,-37,-70,-80,-27,-81,-86,-91,-119,-60,-42,-101,-100,-98,-99,-103,-102,]),'ELSE':([29,32,33,45,65,66,67,68,69,70,76,77,83,87,93,101,102,103,104,105,106,107,108,117,118,120,121,122,123,124,125,134,136,137,139,140,141,142,143,144,145,148,154,164,165,171,173,199,200,211,218,],[-71,-26,-85,-25,-48,-41,-44,-45,-27,-47,-35,-27,-120,-97,-61,-104,-105,-106,-107,-108,-109,-110,-111,-38,-36,-49,-50,-51,-52,-27,-83,-43,-69,-37,-70,-80,-27,-81,-86,-91,-119,170,-60,-42,-101,-100,-98,-99,210,-103,-102,]),'ELSEIF':([29,32,33,45,65,66,67,68,69,70,76,77,83,87,93,101,102,103,104,105,106,107,108,117,118,120,121,122,123,124,125,134,136,137,139,140,141,142,143,144,145,148,154,164,165,171,173,199,200,211,218,],[-71,-26,-85,-25,-48,-41,-44,-45,-27,-47,-35,-27,-120,-97,-61,-104,-105,-106,-107,-108,-109,-110,-111,-38,-36,-49,-50,-51,-52,-27,-83,-43,-69,-37,-70,-80,-27,-81,-86,-91,-119,172,-60,-42,-101,-100,-98,-99,172,-103,-102,]),'TRIPLE_IGUAL':([31,186,],[80,-66,]),'COMA':([32,45,66,67,68,69,70,77,84,93,94,95,96,97,98,99,154,168,169,174,197,],[-26,-25,133,-44,-45,-27,-47,-27,146,-61,155,-55,-56,-57,-58,-59,-60,-121,-122,189,207,]),'PARENTESIS_DER':([32,45,71,73,76,77,78,117,118,137,152,153,166,174,176,201,203,],[-26,-25,136,137,-35,-27,139,-38,-36,-37,-28,175,186,-95,191,-96,212,]),'AND':([32,45,87,124,125,140,141,142,],[-26,-25,150,-27,-83,-80,-27,-81,]),'OR':([32,45,87,124,125,140,141,142,],[-26,-25,151,-27,-83,-80,-27,-81,]),'LLAVE_DER':([32,34,45,77,82,84,167,168,169,],[-26,83,-25,-27,145,-123,-124,-121,-122,]),'CORCHETE_DER':([37,92,93,94,95,96,97,98,99,154,177,],[93,154,-61,-54,-55,-56,-57,-58,-59,-60,-53,]),'ID_CLASE':([44,],[113,]),'EACH':([58,131,],[129,163,]),'SORT':([58,],[130,]),'FOR':([58,],[131,]),'TO_F':([58,],[132,]),'TRES_PUNTOS':([74,75,152,],[138,-28,-28,]),'CHOMP':([81,],[144,]),'ASIGNA_HASH':([85,],[147,]),'BARRA':([128,162,184,197,214,],[161,185,196,208,217,]),'INITIALIZE':([159,],[182,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,196,],[1,205,]),'operacionAritmetica':([0,28,40,41,43,46,48,56,72,86,156,158,160,170,188,196,198,210,],[2,73,101,101,101,101,118,118,73,101,101,101,101,101,101,2,101,101,]),'concatenacionSimpleCadena':([0,196,],[3,3,]),'asignacion':([0,40,41,43,46,86,156,158,160,170,188,196,198,210,],[4,102,102,102,102,102,102,102,102,102,102,4,102,102,]),'impresion':([0,40,41,43,46,86,156,158,160,170,188,196,198,210,],[5,103,103,103,103,103,103,103,103,103,103,5,103,103,]),'impresion_vacia':([0,40,41,43,46,86,156,158,160,170,188,196,198,210,],[6,104,104,104,104,104,104,104,104,104,104,6,104,104,]),'expresiones_booleanas':([0,35,40,41,43,46,86,135,149,156,158,160,170,172,188,196,198,210,],[7,87,105,105,105,105,105,87,173,105,105,105,105,87,105,7,105,105,]),'solicitudDatosTeclado':([0,40,41,43,46,86,156,158,160,170,188,196,198,210,],[8,106,106,106,106,106,106,106,106,106,106,8,106,106,]),'hashes':([0,40,41,43,46,56,86,156,158,160,170,188,196,198,210,],[9,107,107,107,107,122,107,107,107,107,107,107,9,107,107,]),'estructura_if':([0,40,41,43,46,86,156,158,160,170,188,196,198,210,],[10,108,108,108,108,108,108,108,108,108,108,10,108,108,]),'funciones':([0,196,],[11,11,]),'funcionesEstructuras':([0,196,],[12,12,]),'array':([0,37,56,155,196,],[13,98,123,98,13,]),'each_array':([0,196,],[14,14,]),'comentarios':([0,196,],[15,15,]),'each_hash':([0,196,],[16,16,]),'sentencia_while':([0,156,196,],[17,179,17,]),'sentencia_case':([0,196,],[18,18,]),'sentencias_when':([0,42,196,],[19,111,19,]),'sentencia_until':([0,196,],[20,20,]),'definicion_clase':([0,196,],[21,21,]),'expresionNumerica':([0,28,40,41,43,46,48,56,72,86,156,158,160,170,188,196,198,210,],[22,22,22,22,22,22,117,121,22,22,22,22,22,22,22,22,22,22,]),'valorCadena':([0,47,55,196,],[23,115,119,23,]),'valor_print':([0,40,41,43,46,86,156,158,160,170,188,196,198,210,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'valorNumerico':([0,26,28,35,40,41,43,46,48,56,57,72,79,86,133,135,147,149,156,158,160,170,172,188,196,198,210,],[30,68,76,88,30,30,30,30,76,76,125,76,140,30,68,88,168,88,30,30,30,30,88,30,30,30,30,]),'rangos':([0,35,40,41,43,46,86,135,149,156,158,160,170,172,188,196,198,210,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'sentencia_when':([0,42,110,196,],[42,42,157,42,]),'operadores':([22,117,121,],[48,48,48,]),'operadoresComparacion':([24,30,88,89,109,],[57,79,79,57,57,]),'valores':([26,133,],[65,164,]),'valor':([26,133,],[66,66,]),'soloEnteros':([28,90,138,],[74,74,166,]),'elemento_hash':([34,],[82,]),'claveValor':([34,146,],[84,167,]),'condicionIf':([35,135,172,],[86,165,188,]),'elementos_array':([37,155,],[92,177,]),'elemento_array':([37,155,],[94,94,]),'declaracion':([40,41,43,46,86,156,158,160,170,188,198,210,],[100,110,112,114,148,178,181,183,187,200,209,216,]),'funcionesArray':([58,],[126,]),'funcionesNumeros':([58,],[127,]),'estructura_ifUnaLinea':([66,],[134,]),'funcionesFormatoImpresion':([81,],[143,]),'funcionesComparacion':([87,],[149,]),'estructura_secundaria_if':([148,200,],[171,211,]),'argumentos':([153,189,195,],[176,201,203,]),'each_args_hash':([185,],[198,]),'cuerpo_each':([196,],[204,]),'vacio':([196,],[206,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> operacionAritmetica','cuerpo',1,'p_cuerpo','sintactico.py',13),
  ('cuerpo -> concatenacionSimpleCadena','cuerpo',1,'p_cuerpo','sintactico.py',14),
  ('cuerpo -> asignacion','cuerpo',1,'p_cuerpo','sintactico.py',15),
  ('cuerpo -> impresion','cuerpo',1,'p_cuerpo','sintactico.py',16),
  ('cuerpo -> impresion_vacia','cuerpo',1,'p_cuerpo','sintactico.py',17),
  ('cuerpo -> expresiones_booleanas','cuerpo',1,'p_cuerpo','sintactico.py',18),
  ('cuerpo -> solicitudDatosTeclado','cuerpo',1,'p_cuerpo','sintactico.py',19),
  ('cuerpo -> hashes','cuerpo',1,'p_cuerpo','sintactico.py',20),
  ('cuerpo -> estructura_if','cuerpo',1,'p_cuerpo','sintactico.py',21),
  ('cuerpo -> funciones','cuerpo',1,'p_cuerpo','sintactico.py',22),
  ('cuerpo -> funcionesEstructuras','cuerpo',1,'p_cuerpo','sintactico.py',23),
  ('cuerpo -> array','cuerpo',1,'p_cuerpo','sintactico.py',24),
  ('cuerpo -> each_array','cuerpo',1,'p_cuerpo','sintactico.py',25),
  ('cuerpo -> comentarios','cuerpo',1,'p_cuerpo','sintactico.py',26),
  ('cuerpo -> each_hash','cuerpo',1,'p_cuerpo','sintactico.py',27),
  ('cuerpo -> sentencia_while','cuerpo',1,'p_cuerpo','sintactico.py',28),
  ('cuerpo -> sentencia_case','cuerpo',1,'p_cuerpo','sintactico.py',29),
  ('cuerpo -> sentencias_when','cuerpo',1,'p_cuerpo','sintactico.py',30),
  ('cuerpo -> sentencia_until','cuerpo',1,'p_cuerpo','sintactico.py',31),
  ('cuerpo -> definicion_clase','cuerpo',1,'p_cuerpo','sintactico.py',32),
  ('valorCadena -> CADENA','valorCadena',1,'p_valorCadena','sintactico.py',38),
  ('valorCadena -> VARIABLE','valorCadena',1,'p_valorCadena','sintactico.py',39),
  ('concatenacionSimpleCadena -> valorCadena MAS valorCadena','concatenacionSimpleCadena',3,'p_concatenacionSimpleCadena','sintactico.py',68),
  ('concatenacionSimpleCadena -> concatenacionSimpleCadena MAS valorCadena','concatenacionSimpleCadena',3,'p_concatenacionSimpleCadena','sintactico.py',69),
  ('valorNumerico -> FLOTANTE','valorNumerico',1,'p_valorNumerico','sintactico.py',72),
  ('valorNumerico -> ENTERO','valorNumerico',1,'p_valorNumerico','sintactico.py',73),
  ('valorNumerico -> VARIABLE','valorNumerico',1,'p_valorNumerico','sintactico.py',74),
  ('soloEnteros -> ENTERO','soloEnteros',1,'p_soloEnteros','sintactico.py',83),
  ('operadores -> MAS','operadores',1,'p_operadores','sintactico.py',87),
  ('operadores -> MENOS','operadores',1,'p_operadores','sintactico.py',88),
  ('operadores -> DIVISION','operadores',1,'p_operadores','sintactico.py',89),
  ('operadores -> MULTIPLICACION','operadores',1,'p_operadores','sintactico.py',90),
  ('operadores -> EXPONENCIACION','operadores',1,'p_operadores','sintactico.py',91),
  ('operadores -> MODULO','operadores',1,'p_operadores','sintactico.py',92),
  ('expresionNumerica -> valorNumerico','expresionNumerica',1,'p_expresionNumerica','sintactico.py',96),
  ('expresionNumerica -> operacionAritmetica','expresionNumerica',1,'p_expresionNumerica','sintactico.py',97),
  ('expresionNumerica -> PARENTESIS_IZ operacionAritmetica PARENTESIS_DER','expresionNumerica',3,'p_expresionNumerica','sintactico.py',98),
  ('operacionAritmetica -> expresionNumerica operadores expresionNumerica','operacionAritmetica',3,'p_operacionAritmetica','sintactico.py',110),
  ('valor_print -> PRINT','valor_print',1,'p_valor_print','sintactico.py',139),
  ('valor_print -> PUTS','valor_print',1,'p_valor_print','sintactico.py',140),
  ('valores -> valor','valores',1,'p_valores','sintactico.py',143),
  ('valores -> valor COMA valores','valores',3,'p_valores','sintactico.py',144),
  ('valores -> valor estructura_ifUnaLinea','valores',2,'p_valores','sintactico.py',145),
  ('valor -> CADENA','valor',1,'p_valor','sintactico.py',147),
  ('valor -> valorNumerico','valor',1,'p_valor','sintactico.py',148),
  ('valor -> VARIABLE','valor',1,'p_valor','sintactico.py',149),
  ('valor -> VARIABLECLASE','valor',1,'p_valor','sintactico.py',150),
  ('impresion -> valor_print valores','impresion',2,'p_impresion','sintactico.py',157),
  ('asignacion -> VARIABLE IGUAL CADENA','asignacion',3,'p_asignacion','sintactico.py',165),
  ('asignacion -> VARIABLE IGUAL expresionNumerica','asignacion',3,'p_asignacion','sintactico.py',166),
  ('asignacion -> VARIABLE IGUAL hashes','asignacion',3,'p_asignacion','sintactico.py',167),
  ('asignacion -> VARIABLE IGUAL array','asignacion',3,'p_asignacion','sintactico.py',168),
  ('elementos_array -> elemento_array COMA elementos_array','elementos_array',3,'p_elementos_array','sintactico.py',177),
  ('elementos_array -> elemento_array','elementos_array',1,'p_elementos_array','sintactico.py',178),
  ('elemento_array -> CADENA','elemento_array',1,'p_elemento_array','sintactico.py',185),
  ('elemento_array -> ENTERO','elemento_array',1,'p_elemento_array','sintactico.py',186),
  ('elemento_array -> FLOTANTE','elemento_array',1,'p_elemento_array','sintactico.py',187),
  ('elemento_array -> array','elemento_array',1,'p_elemento_array','sintactico.py',188),
  ('elemento_array -> VARIABLE','elemento_array',1,'p_elemento_array','sintactico.py',189),
  ('array -> CORCHETE_IZ elementos_array CORCHETE_DER','array',3,'p_array','sintactico.py',196),
  ('array -> CORCHETE_IZ CORCHETE_DER','array',2,'p_array','sintactico.py',197),
  ('each_array -> VARIABLE PUNTO DO BARRA VARIABLE BARRA cuerpo_each END','each_array',8,'p_each_array','sintactico.py',205),
  ('cuerpo_each -> cuerpo','cuerpo_each',1,'p_cuerpo_each','sintactico.py',207),
  ('cuerpo_each -> vacio','cuerpo_each',1,'p_cuerpo_each','sintactico.py',208),
  ('vacio -> <empty>','vacio',0,'p_vacio','sintactico.py',210),
  ('rangos -> PARENTESIS_IZ soloEnteros TRES_PUNTOS soloEnteros PARENTESIS_DER','rangos',5,'p_rangos','sintactico.py',215),
  ('comentarios -> COMENTARIO','comentarios',1,'p_comentarios','sintactico.py',219),
  ('comentarios -> COMENTARIO_MULTI','comentarios',1,'p_comentarios','sintactico.py',220),
  ('impresion_vacia -> PRINT PARENTESIS_IZ PARENTESIS_DER','impresion_vacia',3,'p_impresion_vacia','sintactico.py',223),
  ('impresion_vacia -> PUTS PARENTESIS_IZ PARENTESIS_DER','impresion_vacia',3,'p_impresion_vacia','sintactico.py',224),
  ('impresion_vacia -> PUTS','impresion_vacia',1,'p_impresion_vacia','sintactico.py',225),
  ('operadoresComparacion -> DOBLE_IGUAL','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',229),
  ('operadoresComparacion -> DIFERENTE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',230),
  ('operadoresComparacion -> MAYOR_QUE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',231),
  ('operadoresComparacion -> MENOR_QUE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',232),
  ('operadoresComparacion -> MENOR_IGUAL_QUE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',233),
  ('operadoresComparacion -> MAYOR_IGUAL_QUE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',234),
  ('funcionesComparacion -> AND','funcionesComparacion',1,'p_funcionesComparacion','sintactico.py',237),
  ('funcionesComparacion -> OR','funcionesComparacion',1,'p_funcionesComparacion','sintactico.py',238),
  ('expresiones_booleanas -> valorNumerico operadoresComparacion valorNumerico','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',241),
  ('expresiones_booleanas -> rangos TRIPLE_IGUAL ENTERO','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',242),
  ('expresiones_booleanas -> VARIABLE operadoresComparacion VARIABLE','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',243),
  ('expresiones_booleanas -> VARIABLE operadoresComparacion valorNumerico','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',244),
  ('expresiones_booleanas -> valorNumerico operadoresComparacion VARIABLE','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',245),
  ('solicitudDatosTeclado -> GETS','solicitudDatosTeclado',1,'p_solicitudDatosTeclado','sintactico.py',275),
  ('solicitudDatosTeclado -> GETS PUNTO funcionesFormatoImpresion','solicitudDatosTeclado',3,'p_solicitudDatosTeclado','sintactico.py',276),
  ('funciones -> DEF VARIABLE PARENTESIS_IZ PARENTESIS_DER END','funciones',5,'p_funciones','sintactico.py',280),
  ('funciones -> DEF VARIABLE PARENTESIS_IZ argumentos PARENTESIS_DER END','funciones',6,'p_funciones','sintactico.py',281),
  ('funcionesArray -> SORT','funcionesArray',1,'p_funcionesArray','sintactico.py',284),
  ('funcionesArray -> FOR EACH','funcionesArray',2,'p_funcionesArray','sintactico.py',285),
  ('funcionesFormatoImpresion -> CHOMP','funcionesFormatoImpresion',1,'p_funcionesFormatoImpresion','sintactico.py',288),
  ('funcionesNumeros -> TO_F','funcionesNumeros',1,'p_funcionesNumeros','sintactico.py',291),
  ('funcionesEstructuras -> VARIABLE PUNTO funcionesArray','funcionesEstructuras',3,'p_funcionesEstructuras','sintactico.py',294),
  ('funcionesEstructuras -> VARIABLE PUNTO funcionesNumeros','funcionesEstructuras',3,'p_funcionesEstructuras','sintactico.py',295),
  ('argumentos -> VARIABLE','argumentos',1,'p_argumentos','sintactico.py',314),
  ('argumentos -> VARIABLE COMA argumentos','argumentos',3,'p_argumentos','sintactico.py',315),
  ('condicionIf -> expresiones_booleanas','condicionIf',1,'p_condicionIf','sintactico.py',319),
  ('condicionIf -> expresiones_booleanas funcionesComparacion expresiones_booleanas','condicionIf',3,'p_condicionIf','sintactico.py',320),
  ('estructura_if -> IF condicionIf declaracion ELSE declaracion END','estructura_if',6,'p_estructura_if','sintactico.py',323),
  ('estructura_if -> IF condicionIf declaracion estructura_secundaria_if','estructura_if',4,'p_estructura_if','sintactico.py',324),
  ('estructura_ifUnaLinea -> IF condicionIf','estructura_ifUnaLinea',2,'p_estructura_ifUnaLinea','sintactico.py',327),
  ('estructura_secundaria_if -> ELSEIF condicionIf declaracion ELSE declaracion END','estructura_secundaria_if',6,'p_estructura_secundaria_if','sintactico.py',330),
  ('estructura_secundaria_if -> ELSEIF condicionIf declaracion estructura_secundaria_if','estructura_secundaria_if',4,'p_estructura_secundaria_if','sintactico.py',331),
  ('declaracion -> operacionAritmetica','declaracion',1,'p_declaracion','sintactico.py',333),
  ('declaracion -> asignacion','declaracion',1,'p_declaracion','sintactico.py',334),
  ('declaracion -> impresion','declaracion',1,'p_declaracion','sintactico.py',335),
  ('declaracion -> impresion_vacia','declaracion',1,'p_declaracion','sintactico.py',336),
  ('declaracion -> expresiones_booleanas','declaracion',1,'p_declaracion','sintactico.py',337),
  ('declaracion -> solicitudDatosTeclado','declaracion',1,'p_declaracion','sintactico.py',338),
  ('declaracion -> hashes','declaracion',1,'p_declaracion','sintactico.py',339),
  ('declaracion -> estructura_if','declaracion',1,'p_declaracion','sintactico.py',340),
  ('sentencia_while -> WHILE declaracion DO sentencia_while END','sentencia_while',5,'p_sentencia_while','sintactico.py',346),
  ('sentencia_while -> WHILE declaracion DO declaracion END','sentencia_while',5,'p_sentencia_while','sintactico.py',347),
  ('sentencia_case -> CASE declaracion sentencia_when END','sentencia_case',4,'p_sentencia_case','sintactico.py',350),
  ('sentencias_when -> sentencia_when','sentencias_when',1,'p_sentencias_when','sintactico.py',353),
  ('sentencias_when -> sentencia_when sentencias_when','sentencias_when',2,'p_sentencias_when','sintactico.py',354),
  ('sentencia_when -> WHEN declaracion IGUAL_DOBLEP declaracion','sentencia_when',4,'p_sentencia_when','sintactico.py',357),
  ('sentencia_until -> UNTIL declaracion DO declaracion END','sentencia_until',5,'p_sentencia_until','sintactico.py',360),
  ('hashes -> LLAVE_IZ elemento_hash LLAVE_DER','hashes',3,'p_hashes','sintactico.py',364),
  ('hashes -> LLAVE_IZ LLAVE_DER','hashes',2,'p_hashes','sintactico.py',365),
  ('claveValor -> VARIABLE ASIGNA_HASH valorNumerico','claveValor',3,'p_claveValor','sintactico.py',368),
  ('claveValor -> VARIABLE ASIGNA_HASH CADENA','claveValor',3,'p_claveValor','sintactico.py',369),
  ('elemento_hash -> claveValor','elemento_hash',1,'p_elemento_hash','sintactico.py',372),
  ('elemento_hash -> claveValor COMA claveValor','elemento_hash',3,'p_elemento_hash','sintactico.py',373),
  ('each_hash -> VARIABLE PUNTO EACH DO BARRA each_args_hash declaracion END','each_hash',8,'p_each_hash','sintactico.py',377),
  ('each_args_hash -> VARIABLE COMA VARIABLE BARRA','each_args_hash',4,'p_each_args_hash','sintactico.py',380),
  ('each_args_hash -> VARIABLE BARRA','each_args_hash',2,'p_each_args_hash','sintactico.py',381),
  ('definicion_clase -> CLASS ID_CLASE DEF INITIALIZE PARENTESIS_IZ argumentos PARENTESIS_DER','definicion_clase',7,'p_definicion_clase','sintactico.py',384),
]
