
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCOMMAleftEQUALPLUSEQUALMINUSEQUALleftSEMInonassocISEQUALDEQUALnonassocLESSLESSEQUALGREATERGREATEREQUALleftPLUSMINUSrightLBRACKETleftELSIFleftELSEALIAS AMPERSANT APOSTROPHE BEGIN BREAK CASE CLASS COLON COMMA COMMENTS COMMENTS_C99 DEF DEFINED DEQUAL DISTINT DIVIDE DO DOT DOT_DOT ELSE ELSIF END ENSURE EQUAL FALSE FLOAT FOR GETS GREATER GREATEREQUAL HASHTAG IDVAR IF IN INT ISEQUAL LBLOCK LBRACKET LESS LESSEQUAL LPAREN MINUS MINUSEQUAL MINUSMINUS MODULE NEXT NIL NOT OPEN PLUS PLUSEQUAL PLUSPLUS PUTS QUOTES RBLOCK RBRACKET REDO RESCUE RETRY RETURN RPAREN SELF SEMI STRING SUPER THEN TIME TIMES TIMESTIMES TREU UNDEF UNLESS UNTIL VARIABLE VARINST VOID WHEN WHILE YIELDprogram : contsDecl  contsDecl : contsDecl declaration \n                  | declarationdeclaration : str_declaration\n                   | var_declaration\n                   | iffor_declaration \n                   | comt_declaration\n                   | def_declaration \n                   | end_declarationstr_declaration : PUTS STRING\n                       | PUTS VARIABLE\n                       | PUTS VARIABLE PLUS VARIABLEvar_declaration : VARIABLE EQUAL STRING\n                       | VARIABLE EQUAL INT\n                       | VARIABLE EQUAL VARIABLE\n                       | VARIABLE EQUAL FLOAT\n                       | VARIABLE EQUAL FLOAT PLUS FLOAT\n                       | VARIABLE EQUAL INT PLUS INT\n                       | VARIABLE EQUAL VARIABLE PLUS INT\n                       | VARIABLE PLUS EQUAL INT\n                       | VARIABLE PLUS EQUAL VARIABLE\n                       | VARIABLE MINUS EQUAL INTiffor_declaration : IF VARIABLE ISEQUAL STRING str_declaration\n                         | ELSE str_declaration\n                         | ELSE\n                         | IF VARIABLE LESSEQUAL STRING str_declaration \n                         | IF VARIABLE LESSEQUAL VARIABLE \n                         | IF VARIABLE LESSEQUAL STRING var_declaration str_declaration \n                         | IF VARIABLE LESSEQUAL STRING empty comt_declaration : COMMENTSdef_declaration : DEF VARIABLE LPAREN VARIABLE COMMA VARIABLE RPAREN str_declaration\n                       | DEF VARIABLE LPAREN VARIABLE COMMA VARIABLE RPAREN str_declaration iffor_declaration\n                       | VARIABLE LPAREN VARIABLE COMMA VARIABLE RPAREN end_declaration : ENDempty :'
    
_lr_action_items = {'PUTS':([0,2,3,4,5,6,7,8,9,13,14,16,17,18,19,25,28,29,30,31,38,42,43,44,46,47,48,50,51,52,54,56,57,58,60,61,63,64,65,],[10,10,-3,-4,-5,-6,-7,-8,-9,-25,-30,-34,-2,-10,-11,-24,-15,-13,-14,-16,-12,-21,-20,-22,10,-27,10,-19,-18,-17,-23,-26,10,-29,-33,-28,10,-31,-32,]),'VARIABLE':([0,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,23,25,27,28,29,30,31,32,36,37,38,42,43,44,45,47,48,50,51,52,54,56,58,59,60,61,64,65,],[11,11,-3,-4,-5,-6,-7,-8,-9,19,24,-25,-30,26,-34,-2,-10,-11,28,34,-24,38,-15,-13,-14,-16,42,47,49,-12,-21,-20,-22,53,-27,55,-19,-18,-17,-23,-26,-29,62,-33,-28,-31,-32,]),'IF':([0,2,3,4,5,6,7,8,9,13,14,16,17,18,19,25,28,29,30,31,38,42,43,44,47,48,50,51,52,54,56,58,60,61,64,65,],[12,12,-3,-4,-5,-6,-7,-8,-9,-25,-30,-34,-2,-10,-11,-24,-15,-13,-14,-16,-12,-21,-20,-22,-27,-35,-19,-18,-17,-23,-26,-29,-33,-28,12,-32,]),'ELSE':([0,2,3,4,5,6,7,8,9,13,14,16,17,18,19,25,28,29,30,31,38,42,43,44,47,48,50,51,52,54,56,58,60,61,64,65,],[13,13,-3,-4,-5,-6,-7,-8,-9,-25,-30,-34,-2,-10,-11,-24,-15,-13,-14,-16,-12,-21,-20,-22,-27,-35,-19,-18,-17,-23,-26,-29,-33,-28,13,-32,]),'COMMENTS':([0,2,3,4,5,6,7,8,9,13,14,16,17,18,19,25,28,29,30,31,38,42,43,44,47,48,50,51,52,54,56,58,60,61,64,65,],[14,14,-3,-4,-5,-6,-7,-8,-9,-25,-30,-34,-2,-10,-11,-24,-15,-13,-14,-16,-12,-21,-20,-22,-27,-35,-19,-18,-17,-23,-26,-29,-33,-28,-31,-32,]),'DEF':([0,2,3,4,5,6,7,8,9,13,14,16,17,18,19,25,28,29,30,31,38,42,43,44,47,48,50,51,52,54,56,58,60,61,64,65,],[15,15,-3,-4,-5,-6,-7,-8,-9,-25,-30,-34,-2,-10,-11,-24,-15,-13,-14,-16,-12,-21,-20,-22,-27,-35,-19,-18,-17,-23,-26,-29,-33,-28,-31,-32,]),'END':([0,2,3,4,5,6,7,8,9,13,14,16,17,18,19,25,28,29,30,31,38,42,43,44,47,48,50,51,52,54,56,58,60,61,64,65,],[16,16,-3,-4,-5,-6,-7,-8,-9,-25,-30,-34,-2,-10,-11,-24,-15,-13,-14,-16,-12,-21,-20,-22,-27,-35,-19,-18,-17,-23,-26,-29,-33,-28,-31,-32,]),'$end':([1,2,3,4,5,6,7,8,9,13,14,16,17,18,19,25,28,29,30,31,38,42,43,44,47,48,50,51,52,54,56,58,60,61,64,65,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-25,-30,-34,-2,-10,-11,-24,-15,-13,-14,-16,-12,-21,-20,-22,-27,-35,-19,-18,-17,-23,-26,-29,-33,-28,-31,-32,]),'STRING':([10,20,35,36,],[18,29,46,48,]),'EQUAL':([11,21,22,55,],[20,32,33,20,]),'PLUS':([11,19,28,30,31,55,],[21,27,39,40,41,21,]),'MINUS':([11,55,],[22,22,]),'LPAREN':([11,26,],[23,37,]),'INT':([20,32,33,39,40,],[30,43,44,50,51,]),'FLOAT':([20,41,],[31,52,]),'ISEQUAL':([24,],[35,]),'LESSEQUAL':([24,],[36,]),'COMMA':([34,49,],[45,59,]),'RPAREN':([53,62,],[60,63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'contsDecl':([0,],[2,]),'declaration':([0,2,],[3,17,]),'str_declaration':([0,2,13,46,48,57,63,],[4,4,25,54,56,61,64,]),'var_declaration':([0,2,48,],[5,5,57,]),'iffor_declaration':([0,2,64,],[6,6,65,]),'comt_declaration':([0,2,],[7,7,]),'def_declaration':([0,2,],[8,8,]),'end_declaration':([0,2,],[9,9,]),'empty':([48,],[58,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> contsDecl','program',1,'p_program','ProgramaRubyAn_Sint.py',21),
  ('contsDecl -> contsDecl declaration','contsDecl',2,'p_contsDecl','ProgramaRubyAn_Sint.py',25),
  ('contsDecl -> declaration','contsDecl',1,'p_contsDecl','ProgramaRubyAn_Sint.py',26),
  ('declaration -> str_declaration','declaration',1,'p_declaration','ProgramaRubyAn_Sint.py',30),
  ('declaration -> var_declaration','declaration',1,'p_declaration','ProgramaRubyAn_Sint.py',31),
  ('declaration -> iffor_declaration','declaration',1,'p_declaration','ProgramaRubyAn_Sint.py',32),
  ('declaration -> comt_declaration','declaration',1,'p_declaration','ProgramaRubyAn_Sint.py',33),
  ('declaration -> def_declaration','declaration',1,'p_declaration','ProgramaRubyAn_Sint.py',34),
  ('declaration -> end_declaration','declaration',1,'p_declaration','ProgramaRubyAn_Sint.py',35),
  ('str_declaration -> PUTS STRING','str_declaration',2,'p_str_declaration','ProgramaRubyAn_Sint.py',40),
  ('str_declaration -> PUTS VARIABLE','str_declaration',2,'p_str_declaration','ProgramaRubyAn_Sint.py',41),
  ('str_declaration -> PUTS VARIABLE PLUS VARIABLE','str_declaration',4,'p_str_declaration','ProgramaRubyAn_Sint.py',42),
  ('var_declaration -> VARIABLE EQUAL STRING','var_declaration',3,'p_var_declaration','ProgramaRubyAn_Sint.py',46),
  ('var_declaration -> VARIABLE EQUAL INT','var_declaration',3,'p_var_declaration','ProgramaRubyAn_Sint.py',47),
  ('var_declaration -> VARIABLE EQUAL VARIABLE','var_declaration',3,'p_var_declaration','ProgramaRubyAn_Sint.py',48),
  ('var_declaration -> VARIABLE EQUAL FLOAT','var_declaration',3,'p_var_declaration','ProgramaRubyAn_Sint.py',49),
  ('var_declaration -> VARIABLE EQUAL FLOAT PLUS FLOAT','var_declaration',5,'p_var_declaration','ProgramaRubyAn_Sint.py',50),
  ('var_declaration -> VARIABLE EQUAL INT PLUS INT','var_declaration',5,'p_var_declaration','ProgramaRubyAn_Sint.py',51),
  ('var_declaration -> VARIABLE EQUAL VARIABLE PLUS INT','var_declaration',5,'p_var_declaration','ProgramaRubyAn_Sint.py',52),
  ('var_declaration -> VARIABLE PLUS EQUAL INT','var_declaration',4,'p_var_declaration','ProgramaRubyAn_Sint.py',53),
  ('var_declaration -> VARIABLE PLUS EQUAL VARIABLE','var_declaration',4,'p_var_declaration','ProgramaRubyAn_Sint.py',54),
  ('var_declaration -> VARIABLE MINUS EQUAL INT','var_declaration',4,'p_var_declaration','ProgramaRubyAn_Sint.py',55),
  ('iffor_declaration -> IF VARIABLE ISEQUAL STRING str_declaration','iffor_declaration',5,'p_iffor_declaration','ProgramaRubyAn_Sint.py',59),
  ('iffor_declaration -> ELSE str_declaration','iffor_declaration',2,'p_iffor_declaration','ProgramaRubyAn_Sint.py',60),
  ('iffor_declaration -> ELSE','iffor_declaration',1,'p_iffor_declaration','ProgramaRubyAn_Sint.py',61),
  ('iffor_declaration -> IF VARIABLE LESSEQUAL STRING str_declaration','iffor_declaration',5,'p_iffor_declaration','ProgramaRubyAn_Sint.py',62),
  ('iffor_declaration -> IF VARIABLE LESSEQUAL VARIABLE','iffor_declaration',4,'p_iffor_declaration','ProgramaRubyAn_Sint.py',63),
  ('iffor_declaration -> IF VARIABLE LESSEQUAL STRING var_declaration str_declaration','iffor_declaration',6,'p_iffor_declaration','ProgramaRubyAn_Sint.py',64),
  ('iffor_declaration -> IF VARIABLE LESSEQUAL STRING empty','iffor_declaration',5,'p_iffor_declaration','ProgramaRubyAn_Sint.py',65),
  ('comt_declaration -> COMMENTS','comt_declaration',1,'p_comt_declaration','ProgramaRubyAn_Sint.py',69),
  ('def_declaration -> DEF VARIABLE LPAREN VARIABLE COMMA VARIABLE RPAREN str_declaration','def_declaration',8,'p_def_declaration','ProgramaRubyAn_Sint.py',73),
  ('def_declaration -> DEF VARIABLE LPAREN VARIABLE COMMA VARIABLE RPAREN str_declaration iffor_declaration','def_declaration',9,'p_def_declaration','ProgramaRubyAn_Sint.py',74),
  ('def_declaration -> VARIABLE LPAREN VARIABLE COMMA VARIABLE RPAREN','def_declaration',6,'p_def_declaration','ProgramaRubyAn_Sint.py',75),
  ('end_declaration -> END','end_declaration',1,'p_end_declaration','ProgramaRubyAn_Sint.py',79),
  ('empty -> <empty>','empty',0,'p_empty','ProgramaRubyAn_Sint.py',83),
]