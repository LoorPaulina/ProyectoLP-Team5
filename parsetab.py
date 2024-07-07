
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ASIGNA_HASH BARRA BEGIN BREAK CADENA CASE CHOMP CLASS COMA COMENTARIO COMENTARIO_MULTI COMILLA_D COMILLA_S CONCAT CORCHETE_DER CORCHETE_IZ DEF DEFINED_QUESTION DIFERENTE DIVISION DO DOBLE_IGUAL EACH ELSE ELSEIF END ENSURE ENTERO EXCLAMACION_ALTO EXCLAMACION_BAJO EXPONENCIACION FALSE FLOTANTE FOR GETS ID_CLASE IF IGUAL IGUAL_DOBLEP IN INITIALIZE LLAVE_DER LLAVE_IZ MAS MAYOR_IGUAL_QUE MAYOR_QUE MENOR_IGUAL_QUE MENOR_QUE MENOS MODULE MODULO MULTIPLICACION NEXT NIL NOT OR O_SIGNO PARENTESIS_DER PARENTESIS_IZ PORCENTAJE PREGUNTA PRINT PRINTF PUNTO PUTS RAISE REDO RESCUE RETRY RETURN SELF SIMBOLO SORT SUPER TO_F TRES_PUNTOS TRIPLE_IGUAL TRUE UNTIL VARIABLE VARIABLECLASE WHEN WHILE YIELD Y_SIGNOcuerpo : operacionAritmetica\n              | comparacion_simbolo\n              | input_concatenacion\n              | asignacion\n              | impresion\n              | impresion_vacia\n              | expresiones_booleanas\n              | solicitudDatosTeclado\n              | hashes\n              | estructura_if\n              | funciones\n              | funcionesEstructuras\n              | array\n              | each_array\n              | comentarios\n              | each_hash\n              | sentencia_while\n              | sentencia_case\n              | sentencias_when\n              | sentencia_until\n              | definicion_clasevalorSimbolo : SIMBOLO \n                    | VARIABLE comparacion_simbolo : valorSimbolo IGUAL_DOBLEP valorSimbolo \n                            | valorSimbolo DIFERENTE valorSimbolo  input_concatenacion : concatenacionSimpleCadena\n                            | concatenacion_funcion  concatenacion_funcion : VARIABLE PUNTO CONCAT PARENTESIS_IZ valorCadena PARENTESIS_DER  valorCadena : CADENA\n                    | VARIABLE concatenacionSimpleCadena : valorCadena MAS valorCadena\n                                 | concatenacionSimpleCadena MAS valorCadenavalorNumerico : FLOTANTE \n                     | ENTERO\n                     | VARIABLEsoloEnteros : ENTEROoperadores : MAS \n                  | MENOS\n                  | DIVISION\n                  | MULTIPLICACION\n                  | EXPONENCIACION \n                  | MODULOexpresionNumerica : valorNumerico\n                         | operacionAritmetica\n                         | PARENTESIS_IZ operacionAritmetica PARENTESIS_DERoperacionAritmetica : expresionNumerica operadores expresionNumericavalor_print : PRINT\n                   | PUTS valores : valor\n               | valor COMA valores\n               | valor estructura_ifUnaLineavalor : CADENA\n             | valorNumerico\n             | VARIABLE\n             | VARIABLECLASE\n             | SIMBOLOimpresion : valor_print valoresasignacion : VARIABLE IGUAL CADENA\n                  | VARIABLE IGUAL expresionNumerica\n                  | VARIABLE IGUAL hashes\n                  | VARIABLE IGUAL SIMBOLO\n                  | VARIABLE IGUAL array\n                  | VARIABLE IGUAL input_concatenacionelementos_array : elemento_array COMA elementos_array\n                       | elemento_array elemento_array : CADENA\n                      | ENTERO\n                      | FLOTANTE\n                      | array\n                      | VARIABLEarray : CORCHETE_IZ elementos_array CORCHETE_DER\n             | CORCHETE_IZ CORCHETE_DEReach_array : VARIABLE PUNTO DO BARRA VARIABLE BARRA cuerpo_each ENDcuerpo_each : cuerpo\n                   | vaciovacio :  rangos : PARENTESIS_IZ soloEnteros TRES_PUNTOS soloEnteros PARENTESIS_DERcomentarios : COMENTARIO \n                    | COMENTARIO_MULTIimpresion_vacia : PRINT PARENTESIS_IZ PARENTESIS_DER\n                        | PUTS PARENTESIS_IZ PARENTESIS_DER\n                        | PUTSoperadoresComparacion : IGUAL_DOBLEP\n                             | DIFERENTE\n                             | MAYOR_QUE\n                             | MENOR_QUE\n                             | MENOR_IGUAL_QUE\n                             | MAYOR_IGUAL_QUEfuncionesComparacion : AND\n                            | ORexpresiones_booleanas : valorNumerico operadoresComparacion valorNumerico\n                             | rangos TRIPLE_IGUAL ENTERO\n                             | VARIABLE operadoresComparacion VARIABLE\n                             | VARIABLE operadoresComparacion valorNumerico\n                             | valorNumerico operadoresComparacion VARIABLEsolicitudDatosTeclado : GETS \n                            | GETS PUNTO funcionesFormatoImpresion funciones : DEF VARIABLE PARENTESIS_IZ PARENTESIS_DER END\n                 | DEF VARIABLE PARENTESIS_IZ argumentos PARENTESIS_DER ENDfuncionesArray : SORT\n                      | FOR EACHfuncionesFormatoImpresion : CHOMPfuncionesNumeros : TO_FfuncionesEstructuras : VARIABLE PUNTO funcionesArray\n                            | VARIABLE PUNTO funcionesNumerosargumentos : VARIABLE\n                    | VARIABLE COMA argumentoscondicionIf : expresiones_booleanas\n                | expresiones_booleanas funcionesComparacion expresiones_booleanasestructura_if : IF condicionIf declaracion ELSE declaracion END\n                    | IF condicionIf declaracion estructura_secundaria_ifestructura_ifUnaLinea : IF condicionIfestructura_secundaria_if : ELSEIF condicionIf declaracion ELSE declaracion END\n                                | ELSEIF condicionIf declaracion estructura_secundaria_ifdeclaracion : operacionAritmetica\n                    | asignacion\n                    | impresion\n                    | impresion_vacia\n                    | expresiones_booleanas\n                    | solicitudDatosTeclado\n                    | hashes\n                    | estructura_if\n                     sentencia_while : WHILE declaracion DO sentencia_while END\n                      | WHILE declaracion DO declaracion END sentencia_case : CASE declaracion sentencia_when ENDsentencias_when : sentencia_when\n                    | sentencia_when sentencias_whensentencia_when : WHEN declaracion IGUAL_DOBLEP declaracionsentencia_until : UNTIL declaracion DO declaracion ENDhashes : LLAVE_IZ elemento_hash LLAVE_DER\n              | LLAVE_IZ LLAVE_DERclaveValor : VARIABLE ASIGNA_HASH valorNumerico\n                  | VARIABLE ASIGNA_HASH CADENAelemento_hash : claveValor\n                     | claveValor COMA claveValoreach_hash : VARIABLE PUNTO EACH DO BARRA each_args_hash declaracion ENDeach_args_hash : VARIABLE COMA VARIABLE BARRA\n                      | VARIABLE BARRAdefinicion_clase : CLASS ID_CLASE DEF INITIALIZE PARENTESIS_IZ argumentos PARENTESIS_DER'
    
_lr_action_items = {'VARIABLE':([0,30,31,32,33,36,38,39,40,41,44,45,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,68,69,70,79,86,93,94,121,137,138,147,149,154,155,156,160,161,163,164,165,167,169,170,172,175,177,179,187,189,190,202,206,207,213,214,216,226,227,229,236,],[27,75,-47,84,-48,-34,92,96,98,106,116,116,116,-33,116,84,-37,-38,-39,-40,-41,-42,126,126,129,130,137,-83,-84,-85,-86,-87,-88,84,155,116,-108,129,-35,-94,75,96,-91,-35,-92,92,84,96,-89,-90,191,106,116,116,116,201,129,116,96,-109,215,116,191,191,27,116,233,-138,116,-137,]),'PRINT':([0,36,44,45,47,50,51,93,94,137,138,154,155,156,170,172,175,187,190,206,214,216,227,229,236,],[31,-34,31,31,31,-33,31,31,-108,-35,-94,-91,-35,-92,31,31,31,31,-109,31,31,31,-138,31,-137,]),'PUTS':([0,36,44,45,47,50,51,93,94,137,138,154,155,156,170,172,175,187,190,206,214,216,227,229,236,],[33,-34,33,33,33,-33,33,33,-108,-35,-94,-91,-35,-92,33,33,33,33,-109,33,33,33,-138,33,-137,]),'GETS':([0,36,44,45,47,50,51,93,94,137,138,154,155,156,170,172,175,187,190,206,214,216,227,229,236,],[37,-34,37,37,37,-33,37,37,-108,-35,-94,-91,-35,-92,37,37,37,37,-109,37,37,37,-138,37,-137,]),'LLAVE_IZ':([0,36,44,45,47,50,51,62,93,94,137,138,154,155,156,170,172,175,187,190,206,214,216,227,229,236,],[38,-34,38,38,38,-33,38,38,38,-108,-35,-94,-91,-35,-92,38,38,38,38,-109,38,38,38,-138,38,-137,]),'IF':([0,36,44,45,47,50,51,72,73,74,75,76,77,93,94,137,138,154,155,156,170,172,175,187,190,206,214,216,227,229,236,],[39,-34,39,39,39,-33,39,149,-52,-53,-35,-55,-56,39,-108,-35,-94,-91,-35,-92,39,39,39,39,-109,39,39,39,-138,39,-137,]),'DEF':([0,120,214,],[40,173,40,]),'CORCHETE_IZ':([0,41,62,169,214,],[41,41,41,41,41,]),'COMENTARIO':([0,214,],[42,42,]),'COMENTARIO_MULTI':([0,214,],[43,43,]),'WHILE':([0,170,214,],[44,44,44,]),'CASE':([0,214,],[45,45,]),'UNTIL':([0,214,],[47,47,]),'CLASS':([0,214,],[48,48,]),'PARENTESIS_IZ':([0,31,32,33,36,39,44,45,47,50,51,52,53,54,55,56,57,58,62,79,93,94,98,137,138,143,149,154,155,156,163,164,165,170,172,175,187,189,190,199,206,214,216,227,229,236,],[32,78,79,85,-34,97,32,32,32,-33,32,79,-37,-38,-39,-40,-41,-42,79,79,32,-108,167,-35,-94,179,97,-91,-35,-92,97,-89,-90,32,32,32,32,97,-109,213,32,32,32,-138,32,-137,]),'SIMBOLO':([0,30,31,33,59,60,62,147,214,],[29,77,-47,-48,29,29,134,77,29,]),'FLOTANTE':([0,30,31,32,33,36,39,41,44,45,47,50,51,52,53,54,55,56,57,58,62,63,65,66,67,68,69,70,79,86,93,94,137,138,147,149,154,155,156,161,163,164,165,169,170,172,175,187,189,190,206,214,216,227,229,236,],[50,50,-47,50,-48,-34,50,104,50,50,50,-33,50,50,-37,-38,-39,-40,-41,-42,50,50,-83,-84,-85,-86,-87,-88,50,50,50,-108,-35,-94,50,50,-91,-35,-92,50,50,-89,-90,104,50,50,50,50,50,-109,50,50,50,-138,50,-137,]),'ENTERO':([0,30,31,32,33,36,39,41,44,45,47,50,51,52,53,54,55,56,57,58,62,63,65,66,67,68,69,70,79,86,87,93,94,97,137,138,147,149,152,154,155,156,161,163,164,165,169,170,172,175,187,189,190,206,214,216,227,229,236,],[36,36,-47,82,-48,-34,36,103,36,36,36,-33,36,36,-37,-38,-39,-40,-41,-42,36,36,-83,-84,-85,-86,-87,-88,36,36,156,36,-108,166,-35,-94,36,36,166,-91,-35,-92,36,36,-89,-90,103,36,36,36,36,36,-109,36,36,36,-138,36,-137,]),'WHEN':([0,25,26,28,33,36,37,46,50,71,72,73,74,75,76,77,83,84,90,94,100,108,109,110,111,112,113,114,115,117,123,124,128,129,130,131,132,133,134,135,136,137,138,148,150,151,153,154,155,156,157,158,159,168,174,181,182,188,190,200,214,217,218,230,237,],[51,-26,-27,-29,-82,-34,-96,51,-33,-57,-49,-52,-53,-35,-55,-56,-43,-35,-131,-108,-72,-115,-116,-117,-118,-119,-120,-121,-122,51,-46,-44,-32,-30,-35,-58,-59,-60,-61,-62,-63,-35,-94,-51,-80,-45,-81,-91,-35,-92,-97,-102,-130,-71,-31,-50,-112,-111,-109,-128,51,-28,-110,-114,-113,]),'CADENA':([0,30,31,33,41,61,62,121,147,161,169,179,214,],[28,73,-47,-48,102,28,131,28,73,186,102,28,28,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,26,28,29,33,36,37,42,43,46,50,71,72,73,74,75,76,77,83,84,90,94,100,108,109,110,111,112,113,114,115,118,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,144,146,148,150,151,153,154,155,156,157,158,159,168,174,180,181,182,188,190,197,200,208,210,211,212,217,218,221,230,231,232,234,237,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-26,-27,-29,-22,-82,-34,-96,-78,-79,-126,-33,-57,-49,-52,-53,-35,-55,-56,-43,-35,-131,-108,-72,-115,-116,-117,-118,-119,-120,-121,-122,-127,-46,-44,-24,-23,-25,-32,-30,-35,-58,-59,-60,-61,-62,-63,-35,-94,-104,-105,-100,-103,-51,-80,-45,-81,-91,-35,-92,-97,-102,-130,-71,-31,-101,-50,-112,-111,-109,-125,-128,-98,-124,-123,-129,-28,-110,-99,-114,-139,-73,-136,-113,]),'END':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,25,26,28,29,33,36,37,42,43,46,50,71,72,73,74,75,76,77,83,84,90,94,100,108,109,110,111,112,113,114,115,118,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,144,146,148,150,151,153,154,155,156,157,158,159,168,171,174,180,181,182,188,190,192,195,196,197,198,200,205,208,209,210,211,212,214,217,218,221,223,224,225,228,230,231,232,234,235,237,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-26,-27,-29,-22,-82,-34,-96,-78,-79,-126,-33,-57,-49,-52,-53,-35,-55,-56,-43,-35,-131,-108,-72,-115,-116,-117,-118,-119,-120,-121,-122,-127,-46,-44,-24,-23,-25,-32,-30,-35,-58,-59,-60,-61,-62,-63,-35,-94,-104,-105,-100,-103,-51,-80,-45,-81,-91,-35,-92,-97,-102,-130,-71,197,-31,-101,-50,-112,-111,-109,208,210,211,-125,212,-128,218,-98,221,-124,-123,-129,-76,-28,-110,-99,232,-74,-75,234,-114,-139,-73,-136,237,-113,]),'MAS':([2,23,25,27,28,34,36,49,50,80,82,83,84,108,116,123,124,128,129,130,131,132,151,174,],[-44,53,61,-30,-29,-43,-34,121,-33,-44,-34,-43,-35,-44,-35,53,-44,-32,-30,-30,-29,53,-45,-31,]),'MENOS':([2,23,27,34,36,50,80,82,83,84,108,116,123,124,130,132,151,],[-44,54,-35,-43,-34,-33,-44,-34,-43,-35,-44,-35,54,-44,-35,54,-45,]),'DIVISION':([2,23,27,34,36,50,80,82,83,84,108,116,123,124,130,132,151,],[-44,55,-35,-43,-34,-33,-44,-34,-43,-35,-44,-35,55,-44,-35,55,-45,]),'MULTIPLICACION':([2,23,27,34,36,50,80,82,83,84,108,116,123,124,130,132,151,],[-44,56,-35,-43,-34,-33,-44,-34,-43,-35,-44,-35,56,-44,-35,56,-45,]),'EXPONENCIACION':([2,23,27,34,36,50,80,82,83,84,108,116,123,124,130,132,151,],[-44,57,-35,-43,-34,-33,-44,-34,-43,-35,-44,-35,57,-44,-35,57,-45,]),'MODULO':([2,23,27,34,36,50,80,82,83,84,108,116,123,124,130,132,151,],[-44,58,-35,-43,-34,-33,-44,-34,-43,-35,-44,-35,58,-44,-35,58,-45,]),'IGUAL_DOBLEP':([24,25,26,27,28,29,33,34,36,37,50,71,72,73,74,75,76,77,83,84,90,94,95,96,100,108,109,110,111,112,113,114,115,116,122,123,124,128,129,130,131,132,133,134,135,136,137,138,148,150,151,153,154,155,156,157,158,159,168,174,181,182,188,190,217,218,230,237,],[59,-26,-27,65,-29,-22,-82,65,-34,-96,-33,-57,-49,-52,-53,-35,-55,-56,-43,-35,-131,-108,65,65,-72,-115,-116,-117,-118,-119,-120,-121,-122,65,175,-46,-44,-32,-30,-35,-58,-59,-60,-61,-62,-63,-35,-94,-51,-80,-45,-81,-91,-35,-92,-97,-102,-130,-71,-31,-50,-112,-111,-109,-28,-110,-114,-113,]),'DIFERENTE':([24,27,29,34,36,50,95,96,116,],[60,66,-22,66,-34,-33,66,66,66,]),'DO':([25,26,28,33,36,37,50,64,71,72,73,74,75,76,77,83,84,90,94,100,107,108,109,110,111,112,113,114,115,119,123,124,128,129,130,131,132,133,134,135,136,137,138,142,148,150,151,153,154,155,156,157,158,159,168,174,181,182,188,190,217,218,230,237,],[-26,-27,-29,-82,-34,-96,-33,141,-57,-49,-52,-53,-35,-55,-56,-43,-35,-131,-108,-72,170,-115,-116,-117,-118,-119,-120,-121,-122,172,-46,-44,-32,-30,-35,-58,-59,-60,-61,-62,-63,-35,-94,178,-51,-80,-45,-81,-91,-35,-92,-97,-102,-130,-71,-31,-50,-112,-111,-109,-28,-110,-114,-113,]),'ELSE':([25,26,28,33,36,37,50,71,72,73,74,75,76,77,83,84,90,94,100,108,109,110,111,112,113,114,115,123,124,128,129,130,131,132,133,134,135,136,137,138,148,150,151,153,154,155,156,157,158,159,162,168,174,181,182,188,190,217,218,219,230,237,],[-26,-27,-29,-82,-34,-96,-33,-57,-49,-52,-53,-35,-55,-56,-43,-35,-131,-108,-72,-115,-116,-117,-118,-119,-120,-121,-122,-46,-44,-32,-30,-35,-58,-59,-60,-61,-62,-63,-35,-94,-51,-80,-45,-81,-91,-35,-92,-97,-102,-130,187,-71,-31,-50,-112,-111,-109,-28,-110,229,-114,-113,]),'ELSEIF':([25,26,28,33,36,37,50,71,72,73,74,75,76,77,83,84,90,94,100,108,109,110,111,112,113,114,115,123,124,128,129,130,131,132,133,134,135,136,137,138,148,150,151,153,154,155,156,157,158,159,162,168,174,181,182,188,190,217,218,219,230,237,],[-26,-27,-29,-82,-34,-96,-33,-57,-49,-52,-53,-35,-55,-56,-43,-35,-131,-108,-72,-115,-116,-117,-118,-119,-120,-121,-122,-46,-44,-32,-30,-35,-58,-59,-60,-61,-62,-63,-35,-94,-51,-80,-45,-81,-91,-35,-92,-97,-102,-130,189,-71,-31,-50,-112,-111,-109,-28,-110,189,-114,-113,]),'IGUAL':([27,116,],[62,62,]),'PUNTO':([27,37,130,],[64,88,176,]),'MAYOR_QUE':([27,34,36,50,95,96,116,],[67,67,-34,-33,67,67,67,]),'MENOR_QUE':([27,34,36,50,95,96,116,],[68,68,-34,-33,68,68,68,]),'MENOR_IGUAL_QUE':([27,34,36,50,95,96,116,],[69,69,-34,-33,69,69,69,]),'MAYOR_IGUAL_QUE':([27,34,36,50,95,96,116,],[70,70,-34,-33,70,70,70,]),'PARENTESIS_DER':([28,36,50,78,80,83,84,85,123,124,129,151,166,167,183,191,193,203,220,222,],[-29,-34,-33,150,151,-43,-35,153,-46,-44,-30,-45,-36,192,204,-106,209,217,-107,231,]),'VARIABLECLASE':([30,31,33,147,],[76,-47,-48,76,]),'TRIPLE_IGUAL':([35,204,],[87,-77,]),'COMA':([36,50,72,73,74,75,76,77,84,91,100,101,102,103,104,105,106,168,185,186,191,215,],[-34,-33,147,-52,-53,-35,-55,-56,-35,160,-72,169,-66,-67,-68,-69,-70,-71,-132,-133,207,226,]),'AND':([36,50,94,137,138,154,155,156,],[-34,-33,164,-35,-94,-91,-35,-92,]),'OR':([36,50,94,137,138,154,155,156,],[-34,-33,165,-35,-94,-91,-35,-92,]),'LLAVE_DER':([36,38,50,84,89,91,184,185,186,],[-34,90,-33,-35,159,-134,-135,-132,-133,]),'CORCHETE_DER':([41,99,100,101,102,103,104,105,106,168,194,],[100,168,-72,-65,-66,-67,-68,-69,-70,-71,-64,]),'ID_CLASE':([48,],[120,]),'EACH':([64,145,],[142,180,]),'CONCAT':([64,176,],[143,143,]),'SORT':([64,],[144,]),'FOR':([64,],[145,]),'TO_F':([64,],[146,]),'TRES_PUNTOS':([81,82,166,],[152,-36,-36,]),'CHOMP':([88,],[158,]),'ASIGNA_HASH':([92,],[161,]),'BARRA':([141,178,201,215,233,],[177,202,214,227,236,]),'INITIALIZE':([173,],[199,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,214,],[1,224,]),'operacionAritmetica':([0,32,44,45,47,51,52,62,79,93,170,172,175,187,206,214,216,229,],[2,80,108,108,108,108,124,124,80,108,108,108,108,108,108,2,108,108,]),'comparacion_simbolo':([0,214,],[3,3,]),'input_concatenacion':([0,62,214,],[4,136,4,]),'asignacion':([0,44,45,47,51,93,170,172,175,187,206,214,216,229,],[5,109,109,109,109,109,109,109,109,109,109,5,109,109,]),'impresion':([0,44,45,47,51,93,170,172,175,187,206,214,216,229,],[6,110,110,110,110,110,110,110,110,110,110,6,110,110,]),'impresion_vacia':([0,44,45,47,51,93,170,172,175,187,206,214,216,229,],[7,111,111,111,111,111,111,111,111,111,111,7,111,111,]),'expresiones_booleanas':([0,39,44,45,47,51,93,149,163,170,172,175,187,189,206,214,216,229,],[8,94,112,112,112,112,112,94,190,112,112,112,112,94,112,8,112,112,]),'solicitudDatosTeclado':([0,44,45,47,51,93,170,172,175,187,206,214,216,229,],[9,113,113,113,113,113,113,113,113,113,113,9,113,113,]),'hashes':([0,44,45,47,51,62,93,170,172,175,187,206,214,216,229,],[10,114,114,114,114,133,114,114,114,114,114,114,10,114,114,]),'estructura_if':([0,44,45,47,51,93,170,172,175,187,206,214,216,229,],[11,115,115,115,115,115,115,115,115,115,115,11,115,115,]),'funciones':([0,214,],[12,12,]),'funcionesEstructuras':([0,214,],[13,13,]),'array':([0,41,62,169,214,],[14,105,135,105,14,]),'each_array':([0,214,],[15,15,]),'comentarios':([0,214,],[16,16,]),'each_hash':([0,214,],[17,17,]),'sentencia_while':([0,170,214,],[18,196,18,]),'sentencia_case':([0,214,],[19,19,]),'sentencias_when':([0,46,214,],[20,118,20,]),'sentencia_until':([0,214,],[21,21,]),'definicion_clase':([0,214,],[22,22,]),'expresionNumerica':([0,32,44,45,47,51,52,62,79,93,170,172,175,187,206,214,216,229,],[23,23,23,23,23,23,123,132,23,23,23,23,23,23,23,23,23,23,]),'valorSimbolo':([0,59,60,214,],[24,125,127,24,]),'concatenacionSimpleCadena':([0,62,214,],[25,25,25,]),'concatenacion_funcion':([0,62,214,],[26,26,26,]),'valor_print':([0,44,45,47,51,93,170,172,175,187,206,214,216,229,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'valorNumerico':([0,30,32,39,44,45,47,51,52,62,63,79,86,93,147,149,161,163,170,172,175,187,189,206,214,216,229,],[34,74,83,95,34,34,34,34,83,83,138,83,154,34,74,95,185,95,34,34,34,34,95,34,34,34,34,]),'rangos':([0,39,44,45,47,51,93,149,163,170,172,175,187,189,206,214,216,229,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'sentencia_when':([0,46,117,214,],[46,46,171,46,]),'valorCadena':([0,61,62,121,179,214,],[49,128,49,174,203,49,]),'operadores':([23,123,132,],[52,52,52,]),'operadoresComparacion':([27,34,95,96,116,],[63,86,86,63,63,]),'valores':([30,147,],[71,181,]),'valor':([30,147,],[72,72,]),'soloEnteros':([32,97,152,],[81,81,183,]),'elemento_hash':([38,],[89,]),'claveValor':([38,160,],[91,184,]),'condicionIf':([39,149,189,],[93,182,206,]),'elementos_array':([41,169,],[99,194,]),'elemento_array':([41,169,],[101,101,]),'declaracion':([44,45,47,51,93,170,172,175,187,206,216,229,],[107,117,119,122,162,195,198,200,205,219,228,235,]),'funcionesArray':([64,],[139,]),'funcionesNumeros':([64,],[140,]),'estructura_ifUnaLinea':([72,],[148,]),'funcionesFormatoImpresion':([88,],[157,]),'funcionesComparacion':([94,],[163,]),'estructura_secundaria_if':([162,219,],[188,230,]),'argumentos':([167,207,213,],[193,220,222,]),'each_args_hash':([202,],[216,]),'cuerpo_each':([214,],[223,]),'vacio':([214,],[225,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> operacionAritmetica','cuerpo',1,'p_cuerpo','sintactico.py',13),
  ('cuerpo -> comparacion_simbolo','cuerpo',1,'p_cuerpo','sintactico.py',14),
  ('cuerpo -> input_concatenacion','cuerpo',1,'p_cuerpo','sintactico.py',15),
  ('cuerpo -> asignacion','cuerpo',1,'p_cuerpo','sintactico.py',16),
  ('cuerpo -> impresion','cuerpo',1,'p_cuerpo','sintactico.py',17),
  ('cuerpo -> impresion_vacia','cuerpo',1,'p_cuerpo','sintactico.py',18),
  ('cuerpo -> expresiones_booleanas','cuerpo',1,'p_cuerpo','sintactico.py',19),
  ('cuerpo -> solicitudDatosTeclado','cuerpo',1,'p_cuerpo','sintactico.py',20),
  ('cuerpo -> hashes','cuerpo',1,'p_cuerpo','sintactico.py',21),
  ('cuerpo -> estructura_if','cuerpo',1,'p_cuerpo','sintactico.py',22),
  ('cuerpo -> funciones','cuerpo',1,'p_cuerpo','sintactico.py',23),
  ('cuerpo -> funcionesEstructuras','cuerpo',1,'p_cuerpo','sintactico.py',24),
  ('cuerpo -> array','cuerpo',1,'p_cuerpo','sintactico.py',25),
  ('cuerpo -> each_array','cuerpo',1,'p_cuerpo','sintactico.py',26),
  ('cuerpo -> comentarios','cuerpo',1,'p_cuerpo','sintactico.py',27),
  ('cuerpo -> each_hash','cuerpo',1,'p_cuerpo','sintactico.py',28),
  ('cuerpo -> sentencia_while','cuerpo',1,'p_cuerpo','sintactico.py',29),
  ('cuerpo -> sentencia_case','cuerpo',1,'p_cuerpo','sintactico.py',30),
  ('cuerpo -> sentencias_when','cuerpo',1,'p_cuerpo','sintactico.py',31),
  ('cuerpo -> sentencia_until','cuerpo',1,'p_cuerpo','sintactico.py',32),
  ('cuerpo -> definicion_clase','cuerpo',1,'p_cuerpo','sintactico.py',33),
  ('valorSimbolo -> SIMBOLO','valorSimbolo',1,'p_valorSimbolo','sintactico.py',38),
  ('valorSimbolo -> VARIABLE','valorSimbolo',1,'p_valorSimbolo','sintactico.py',39),
  ('comparacion_simbolo -> valorSimbolo IGUAL_DOBLEP valorSimbolo','comparacion_simbolo',3,'p_comparacion_simbolo','sintactico.py',65),
  ('comparacion_simbolo -> valorSimbolo DIFERENTE valorSimbolo','comparacion_simbolo',3,'p_comparacion_simbolo','sintactico.py',66),
  ('input_concatenacion -> concatenacionSimpleCadena','input_concatenacion',1,'p_input_concatenacion','sintactico.py',78),
  ('input_concatenacion -> concatenacion_funcion','input_concatenacion',1,'p_input_concatenacion','sintactico.py',79),
  ('concatenacion_funcion -> VARIABLE PUNTO CONCAT PARENTESIS_IZ valorCadena PARENTESIS_DER','concatenacion_funcion',6,'p_concatenacion_funcion','sintactico.py',84),
  ('valorCadena -> CADENA','valorCadena',1,'p_valorCadena','sintactico.py',96),
  ('valorCadena -> VARIABLE','valorCadena',1,'p_valorCadena','sintactico.py',97),
  ('concatenacionSimpleCadena -> valorCadena MAS valorCadena','concatenacionSimpleCadena',3,'p_concatenacionSimpleCadena','sintactico.py',129),
  ('concatenacionSimpleCadena -> concatenacionSimpleCadena MAS valorCadena','concatenacionSimpleCadena',3,'p_concatenacionSimpleCadena','sintactico.py',130),
  ('valorNumerico -> FLOTANTE','valorNumerico',1,'p_valorNumerico','sintactico.py',148),
  ('valorNumerico -> ENTERO','valorNumerico',1,'p_valorNumerico','sintactico.py',149),
  ('valorNumerico -> VARIABLE','valorNumerico',1,'p_valorNumerico','sintactico.py',150),
  ('soloEnteros -> ENTERO','soloEnteros',1,'p_soloEnteros','sintactico.py',159),
  ('operadores -> MAS','operadores',1,'p_operadores','sintactico.py',163),
  ('operadores -> MENOS','operadores',1,'p_operadores','sintactico.py',164),
  ('operadores -> DIVISION','operadores',1,'p_operadores','sintactico.py',165),
  ('operadores -> MULTIPLICACION','operadores',1,'p_operadores','sintactico.py',166),
  ('operadores -> EXPONENCIACION','operadores',1,'p_operadores','sintactico.py',167),
  ('operadores -> MODULO','operadores',1,'p_operadores','sintactico.py',168),
  ('expresionNumerica -> valorNumerico','expresionNumerica',1,'p_expresionNumerica','sintactico.py',172),
  ('expresionNumerica -> operacionAritmetica','expresionNumerica',1,'p_expresionNumerica','sintactico.py',173),
  ('expresionNumerica -> PARENTESIS_IZ operacionAritmetica PARENTESIS_DER','expresionNumerica',3,'p_expresionNumerica','sintactico.py',174),
  ('operacionAritmetica -> expresionNumerica operadores expresionNumerica','operacionAritmetica',3,'p_operacionAritmetica','sintactico.py',186),
  ('valor_print -> PRINT','valor_print',1,'p_valor_print','sintactico.py',215),
  ('valor_print -> PUTS','valor_print',1,'p_valor_print','sintactico.py',216),
  ('valores -> valor','valores',1,'p_valores','sintactico.py',219),
  ('valores -> valor COMA valores','valores',3,'p_valores','sintactico.py',220),
  ('valores -> valor estructura_ifUnaLinea','valores',2,'p_valores','sintactico.py',221),
  ('valor -> CADENA','valor',1,'p_valor','sintactico.py',227),
  ('valor -> valorNumerico','valor',1,'p_valor','sintactico.py',228),
  ('valor -> VARIABLE','valor',1,'p_valor','sintactico.py',229),
  ('valor -> VARIABLECLASE','valor',1,'p_valor','sintactico.py',230),
  ('valor -> SIMBOLO','valor',1,'p_valor','sintactico.py',231),
  ('impresion -> valor_print valores','impresion',2,'p_impresion','sintactico.py',249),
  ('asignacion -> VARIABLE IGUAL CADENA','asignacion',3,'p_asignacion','sintactico.py',256),
  ('asignacion -> VARIABLE IGUAL expresionNumerica','asignacion',3,'p_asignacion','sintactico.py',257),
  ('asignacion -> VARIABLE IGUAL hashes','asignacion',3,'p_asignacion','sintactico.py',258),
  ('asignacion -> VARIABLE IGUAL SIMBOLO','asignacion',3,'p_asignacion','sintactico.py',259),
  ('asignacion -> VARIABLE IGUAL array','asignacion',3,'p_asignacion','sintactico.py',260),
  ('asignacion -> VARIABLE IGUAL input_concatenacion','asignacion',3,'p_asignacion','sintactico.py',261),
  ('elementos_array -> elemento_array COMA elementos_array','elementos_array',3,'p_elementos_array','sintactico.py',270),
  ('elementos_array -> elemento_array','elementos_array',1,'p_elementos_array','sintactico.py',271),
  ('elemento_array -> CADENA','elemento_array',1,'p_elemento_array','sintactico.py',278),
  ('elemento_array -> ENTERO','elemento_array',1,'p_elemento_array','sintactico.py',279),
  ('elemento_array -> FLOTANTE','elemento_array',1,'p_elemento_array','sintactico.py',280),
  ('elemento_array -> array','elemento_array',1,'p_elemento_array','sintactico.py',281),
  ('elemento_array -> VARIABLE','elemento_array',1,'p_elemento_array','sintactico.py',282),
  ('array -> CORCHETE_IZ elementos_array CORCHETE_DER','array',3,'p_array','sintactico.py',289),
  ('array -> CORCHETE_IZ CORCHETE_DER','array',2,'p_array','sintactico.py',290),
  ('each_array -> VARIABLE PUNTO DO BARRA VARIABLE BARRA cuerpo_each END','each_array',8,'p_each_array','sintactico.py',298),
  ('cuerpo_each -> cuerpo','cuerpo_each',1,'p_cuerpo_each','sintactico.py',300),
  ('cuerpo_each -> vacio','cuerpo_each',1,'p_cuerpo_each','sintactico.py',301),
  ('vacio -> <empty>','vacio',0,'p_vacio','sintactico.py',303),
  ('rangos -> PARENTESIS_IZ soloEnteros TRES_PUNTOS soloEnteros PARENTESIS_DER','rangos',5,'p_rangos','sintactico.py',308),
  ('comentarios -> COMENTARIO','comentarios',1,'p_comentarios','sintactico.py',312),
  ('comentarios -> COMENTARIO_MULTI','comentarios',1,'p_comentarios','sintactico.py',313),
  ('impresion_vacia -> PRINT PARENTESIS_IZ PARENTESIS_DER','impresion_vacia',3,'p_impresion_vacia','sintactico.py',316),
  ('impresion_vacia -> PUTS PARENTESIS_IZ PARENTESIS_DER','impresion_vacia',3,'p_impresion_vacia','sintactico.py',317),
  ('impresion_vacia -> PUTS','impresion_vacia',1,'p_impresion_vacia','sintactico.py',318),
  ('operadoresComparacion -> IGUAL_DOBLEP','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',322),
  ('operadoresComparacion -> DIFERENTE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',323),
  ('operadoresComparacion -> MAYOR_QUE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',324),
  ('operadoresComparacion -> MENOR_QUE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',325),
  ('operadoresComparacion -> MENOR_IGUAL_QUE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',326),
  ('operadoresComparacion -> MAYOR_IGUAL_QUE','operadoresComparacion',1,'p_operadoresComparacion','sintactico.py',327),
  ('funcionesComparacion -> AND','funcionesComparacion',1,'p_funcionesComparacion','sintactico.py',330),
  ('funcionesComparacion -> OR','funcionesComparacion',1,'p_funcionesComparacion','sintactico.py',331),
  ('expresiones_booleanas -> valorNumerico operadoresComparacion valorNumerico','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',334),
  ('expresiones_booleanas -> rangos TRIPLE_IGUAL ENTERO','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',335),
  ('expresiones_booleanas -> VARIABLE operadoresComparacion VARIABLE','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',336),
  ('expresiones_booleanas -> VARIABLE operadoresComparacion valorNumerico','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',337),
  ('expresiones_booleanas -> valorNumerico operadoresComparacion VARIABLE','expresiones_booleanas',3,'p_expresiones_booleanas','sintactico.py',338),
  ('solicitudDatosTeclado -> GETS','solicitudDatosTeclado',1,'p_solicitudDatosTeclado','sintactico.py',368),
  ('solicitudDatosTeclado -> GETS PUNTO funcionesFormatoImpresion','solicitudDatosTeclado',3,'p_solicitudDatosTeclado','sintactico.py',369),
  ('funciones -> DEF VARIABLE PARENTESIS_IZ PARENTESIS_DER END','funciones',5,'p_funciones','sintactico.py',373),
  ('funciones -> DEF VARIABLE PARENTESIS_IZ argumentos PARENTESIS_DER END','funciones',6,'p_funciones','sintactico.py',374),
  ('funcionesArray -> SORT','funcionesArray',1,'p_funcionesArray','sintactico.py',377),
  ('funcionesArray -> FOR EACH','funcionesArray',2,'p_funcionesArray','sintactico.py',378),
  ('funcionesFormatoImpresion -> CHOMP','funcionesFormatoImpresion',1,'p_funcionesFormatoImpresion','sintactico.py',381),
  ('funcionesNumeros -> TO_F','funcionesNumeros',1,'p_funcionesNumeros','sintactico.py',384),
  ('funcionesEstructuras -> VARIABLE PUNTO funcionesArray','funcionesEstructuras',3,'p_funcionesEstructuras','sintactico.py',387),
  ('funcionesEstructuras -> VARIABLE PUNTO funcionesNumeros','funcionesEstructuras',3,'p_funcionesEstructuras','sintactico.py',388),
  ('argumentos -> VARIABLE','argumentos',1,'p_argumentos','sintactico.py',407),
  ('argumentos -> VARIABLE COMA argumentos','argumentos',3,'p_argumentos','sintactico.py',408),
  ('condicionIf -> expresiones_booleanas','condicionIf',1,'p_condicionIf','sintactico.py',412),
  ('condicionIf -> expresiones_booleanas funcionesComparacion expresiones_booleanas','condicionIf',3,'p_condicionIf','sintactico.py',413),
  ('estructura_if -> IF condicionIf declaracion ELSE declaracion END','estructura_if',6,'p_estructura_if','sintactico.py',416),
  ('estructura_if -> IF condicionIf declaracion estructura_secundaria_if','estructura_if',4,'p_estructura_if','sintactico.py',417),
  ('estructura_ifUnaLinea -> IF condicionIf','estructura_ifUnaLinea',2,'p_estructura_ifUnaLinea','sintactico.py',420),
  ('estructura_secundaria_if -> ELSEIF condicionIf declaracion ELSE declaracion END','estructura_secundaria_if',6,'p_estructura_secundaria_if','sintactico.py',423),
  ('estructura_secundaria_if -> ELSEIF condicionIf declaracion estructura_secundaria_if','estructura_secundaria_if',4,'p_estructura_secundaria_if','sintactico.py',424),
  ('declaracion -> operacionAritmetica','declaracion',1,'p_declaracion','sintactico.py',426),
  ('declaracion -> asignacion','declaracion',1,'p_declaracion','sintactico.py',427),
  ('declaracion -> impresion','declaracion',1,'p_declaracion','sintactico.py',428),
  ('declaracion -> impresion_vacia','declaracion',1,'p_declaracion','sintactico.py',429),
  ('declaracion -> expresiones_booleanas','declaracion',1,'p_declaracion','sintactico.py',430),
  ('declaracion -> solicitudDatosTeclado','declaracion',1,'p_declaracion','sintactico.py',431),
  ('declaracion -> hashes','declaracion',1,'p_declaracion','sintactico.py',432),
  ('declaracion -> estructura_if','declaracion',1,'p_declaracion','sintactico.py',433),
  ('sentencia_while -> WHILE declaracion DO sentencia_while END','sentencia_while',5,'p_sentencia_while','sintactico.py',439),
  ('sentencia_while -> WHILE declaracion DO declaracion END','sentencia_while',5,'p_sentencia_while','sintactico.py',440),
  ('sentencia_case -> CASE declaracion sentencia_when END','sentencia_case',4,'p_sentencia_case','sintactico.py',443),
  ('sentencias_when -> sentencia_when','sentencias_when',1,'p_sentencias_when','sintactico.py',446),
  ('sentencias_when -> sentencia_when sentencias_when','sentencias_when',2,'p_sentencias_when','sintactico.py',447),
  ('sentencia_when -> WHEN declaracion IGUAL_DOBLEP declaracion','sentencia_when',4,'p_sentencia_when','sintactico.py',450),
  ('sentencia_until -> UNTIL declaracion DO declaracion END','sentencia_until',5,'p_sentencia_until','sintactico.py',453),
  ('hashes -> LLAVE_IZ elemento_hash LLAVE_DER','hashes',3,'p_hashes','sintactico.py',457),
  ('hashes -> LLAVE_IZ LLAVE_DER','hashes',2,'p_hashes','sintactico.py',458),
  ('claveValor -> VARIABLE ASIGNA_HASH valorNumerico','claveValor',3,'p_claveValor','sintactico.py',461),
  ('claveValor -> VARIABLE ASIGNA_HASH CADENA','claveValor',3,'p_claveValor','sintactico.py',462),
  ('elemento_hash -> claveValor','elemento_hash',1,'p_elemento_hash','sintactico.py',465),
  ('elemento_hash -> claveValor COMA claveValor','elemento_hash',3,'p_elemento_hash','sintactico.py',466),
  ('each_hash -> VARIABLE PUNTO EACH DO BARRA each_args_hash declaracion END','each_hash',8,'p_each_hash','sintactico.py',470),
  ('each_args_hash -> VARIABLE COMA VARIABLE BARRA','each_args_hash',4,'p_each_args_hash','sintactico.py',473),
  ('each_args_hash -> VARIABLE BARRA','each_args_hash',2,'p_each_args_hash','sintactico.py',474),
  ('definicion_clase -> CLASS ID_CLASE DEF INITIALIZE PARENTESIS_IZ argumentos PARENTESIS_DER','definicion_clase',7,'p_definicion_clase','sintactico.py',477),
]
