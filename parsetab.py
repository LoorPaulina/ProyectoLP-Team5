
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ASIGNA_HASH BARRA BEGIN BREAK CADENA CASE CHOMP CLASS COMA COMENTARIO COMENTARIO_MULTI COMILLA_D COMILLA_S CONCAT CORCHETE_DER CORCHETE_IZ DEF DEFINED_QUESTION DIFERENTE DIVISION EACH ELSE ELSEIF END ENSURE ENTERO EXCLAMACION_ALTO EXCLAMACION_BAJO EXPONENCIACION FALSE FLOTANTE FOR GETS IF IGUAL IGUAL_DOBLEP IN LLAVE_DER LLAVE_IZ MAS MAYOR_IGUAL_QUE MAYOR_QUE MENOR_IGUAL_QUE MENOR_QUE MENOS MODULE MULTIPLICACION NEXT NIL NOT OR O_SIGNO PARENTESIS_DER PARENTESIS_IZ PORCENTAJE PREGUNTA PRINT PRINTF PUTS RAISE REDO RESCUE RETRY RETURN SELF SIMBOLO SORT SUPER TO_F TRIPLE_IGUAL TRUE UNTIL VARIABLE VARIABLECLASE WHILE YIELD Y_SIGNOcuerpo : operacionAritmeticavalorNumerico : FLOTANTE \n                     | ENTERO operadores : MAS \n                  | MENOS\n                  | DIVISION\n                  | MULTIPLICACION\n                  | EXPONENCIACION expresionNumerica : valorNumerico\n                         | operacionAritmetica\n                         | PARENTESIS_IZ operacionAritmetica PARENTESIS_DERoperacionAritmetica : expresionNumerica operadores expresionNumerica'
    
_lr_action_items = {'PARENTESIS_IZ':([0,5,8,9,10,11,12,13,],[5,5,5,-4,-5,-6,-7,-8,]),'FLOTANTE':([0,5,8,9,10,11,12,13,],[6,6,6,-4,-5,-6,-7,-8,]),'ENTERO':([0,5,8,9,10,11,12,13,],[7,7,7,-4,-5,-6,-7,-8,]),'$end':([1,2,4,6,7,15,16,17,],[0,-1,-9,-2,-3,-12,-10,-11,]),'MAS':([2,3,4,6,7,14,15,16,17,],[-10,9,-9,-2,-3,-10,9,-10,-11,]),'MENOS':([2,3,4,6,7,14,15,16,17,],[-10,10,-9,-2,-3,-10,10,-10,-11,]),'DIVISION':([2,3,4,6,7,14,15,16,17,],[-10,11,-9,-2,-3,-10,11,-10,-11,]),'MULTIPLICACION':([2,3,4,6,7,14,15,16,17,],[-10,12,-9,-2,-3,-10,12,-10,-11,]),'EXPONENCIACION':([2,3,4,6,7,14,15,16,17,],[-10,13,-9,-2,-3,-10,13,-10,-11,]),'PARENTESIS_DER':([4,6,7,14,15,16,17,],[-9,-2,-3,17,-12,-10,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,],[1,]),'operacionAritmetica':([0,5,8,],[2,14,16,]),'expresionNumerica':([0,5,8,],[3,3,15,]),'valorNumerico':([0,5,8,],[4,4,4,]),'operadores':([3,15,],[8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> operacionAritmetica','cuerpo',1,'p_cuerpo','sintactico.py',5),
  ('valorNumerico -> FLOTANTE','valorNumerico',1,'p_valorNumerico','sintactico.py',11),
  ('valorNumerico -> ENTERO','valorNumerico',1,'p_valorNumerico','sintactico.py',12),
  ('operadores -> MAS','operadores',1,'p_operadores','sintactico.py',16),
  ('operadores -> MENOS','operadores',1,'p_operadores','sintactico.py',17),
  ('operadores -> DIVISION','operadores',1,'p_operadores','sintactico.py',18),
  ('operadores -> MULTIPLICACION','operadores',1,'p_operadores','sintactico.py',19),
  ('operadores -> EXPONENCIACION','operadores',1,'p_operadores','sintactico.py',20),
  ('expresionNumerica -> valorNumerico','expresionNumerica',1,'p_expresionNumerica','sintactico.py',23),
  ('expresionNumerica -> operacionAritmetica','expresionNumerica',1,'p_expresionNumerica','sintactico.py',24),
  ('expresionNumerica -> PARENTESIS_IZ operacionAritmetica PARENTESIS_DER','expresionNumerica',3,'p_expresionNumerica','sintactico.py',25),
  ('operacionAritmetica -> expresionNumerica operadores expresionNumerica','operacionAritmetica',3,'p_operacionAritmetica','sintactico.py',28),
]
