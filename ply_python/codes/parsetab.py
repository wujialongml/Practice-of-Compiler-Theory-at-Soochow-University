
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "NUMBER PRINT VARIABLEprogram : statementsstatements : statements statement\n                  | statement statement : assignment\n                  | operation\n                  | printassignment : VARIABLE '=' NUMBERoperation : VARIABLE '=' expr\n    expr : expr '+' term\n            | expr '-' term\n            | term\n    term : term '*' factor\n            | term '/' factor\n            | factor\n    factor : VARIABLE\n            | NUMBER\n    print : PRINT '(' values ')'\n    values : VARIABLE\n                | values ',' VARIABLE\n    "
    
_lr_action_items = {'VARIABLE':([0,2,3,4,5,6,9,10,11,12,13,14,15,16,19,20,21,22,23,24,25,26,27,28,29,],[7,7,-3,-4,-5,-6,-2,12,18,-15,-7,-8,-11,-14,12,12,12,12,-17,30,-9,-16,-10,-12,-13,]),'PRINT':([0,2,3,4,5,6,9,12,13,14,15,16,23,25,26,27,28,29,],[8,8,-3,-4,-5,-6,-2,-15,-7,-8,-11,-14,-17,-9,-16,-10,-12,-13,]),'$end':([1,2,3,4,5,6,9,12,13,14,15,16,23,25,26,27,28,29,],[0,-1,-3,-4,-5,-6,-2,-15,-7,-8,-11,-14,-17,-9,-16,-10,-12,-13,]),'=':([7,],[10,]),'(':([8,],[11,]),'NUMBER':([10,19,20,21,22,],[13,26,26,26,26,]),'*':([12,13,15,16,25,26,27,28,29,],[-15,-16,21,-14,21,-16,21,-12,-13,]),'/':([12,13,15,16,25,26,27,28,29,],[-15,-16,22,-14,22,-16,22,-12,-13,]),'+':([12,13,14,15,16,25,26,27,28,29,],[-15,-16,19,-11,-14,-9,-16,-10,-12,-13,]),'-':([12,13,14,15,16,25,26,27,28,29,],[-15,-16,20,-11,-14,-9,-16,-10,-12,-13,]),')':([17,18,30,],[23,-18,-19,]),',':([17,18,30,],[24,-18,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,],[2,]),'statement':([0,2,],[3,9,]),'assignment':([0,2,],[4,4,]),'operation':([0,2,],[5,5,]),'print':([0,2,],[6,6,]),'expr':([10,],[14,]),'term':([10,19,20,],[15,25,27,]),'factor':([10,19,20,21,22,],[16,16,16,28,29,]),'values':([11,],[17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','main.py',63),
  ('statements -> statements statement','statements',2,'p_statements','main.py',70),
  ('statements -> statement','statements',1,'p_statements','main.py',71),
  ('statement -> assignment','statement',1,'p_statement','main.py',82),
  ('statement -> operation','statement',1,'p_statement','main.py',83),
  ('statement -> print','statement',1,'p_statement','main.py',84),
  ('assignment -> VARIABLE = NUMBER','assignment',3,'p_assignment','main.py',91),
  ('operation -> VARIABLE = expr','operation',3,'p_operation','main.py',100),
  ('expr -> expr + term','expr',3,'p_expr','main.py',113),
  ('expr -> expr - term','expr',3,'p_expr','main.py',114),
  ('expr -> term','expr',1,'p_expr','main.py',115),
  ('term -> term * factor','term',3,'p_term','main.py',126),
  ('term -> term / factor','term',3,'p_term','main.py',127),
  ('term -> factor','term',1,'p_term','main.py',128),
  ('factor -> VARIABLE','factor',1,'p_factor','main.py',139),
  ('factor -> NUMBER','factor',1,'p_factor','main.py',140),
  ('print -> PRINT ( values )','print',4,'p_print','main.py',152),
  ('values -> VARIABLE','values',1,'p_values','main.py',161),
  ('values -> values , VARIABLE','values',3,'p_values','main.py',162),
]
