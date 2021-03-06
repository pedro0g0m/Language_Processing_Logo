
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "INT back bk fd forward home left lt pd pendown penup pu right rt setpencolor setpos setx setxy sety  program  :   command    program  :  program command    command  :  fd len   command  :  forward len   command  :  bk len   command  :  back len   command  :  lt deg   command  :  left deg   command  :  rt deg   command  :  right deg   command  :  setpos coordinate   command  :  setxy coordinate   command  :  sety y   command  :  setx x   command  :  home  command  :  pendown   command  :  pd   command  :  penup   command  :  pu    command  :  setpencolor color   color : '[' INT  INT  INT ']'   len : INT   deg : INT   x : INT   y : INT   coordinate : '[' INT  INT ']'\n                        | INT  INT  "
    
_lr_action_items = {'fd':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[3,3,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'forward':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[4,4,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'bk':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[5,5,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'back':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[6,6,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'lt':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[7,7,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'left':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[8,8,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'rt':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[9,9,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'right':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[10,10,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'setpos':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[11,11,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'setxy':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[12,12,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'sety':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[13,13,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'setx':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[14,14,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'home':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[15,15,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'pendown':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[16,16,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'pd':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[17,17,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'penup':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[18,18,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'pu':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[19,19,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'setpencolor':([0,1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[20,20,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'$end':([1,2,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,40,43,47,49,],[0,-1,-15,-16,-17,-18,-19,-2,-3,-22,-4,-5,-6,-7,-23,-8,-9,-10,-11,-12,-13,-25,-14,-24,-20,-27,-26,-21,]),'INT':([3,4,5,6,7,8,9,10,11,12,13,14,33,34,41,42,44,46,],[23,23,23,23,28,28,28,28,34,34,37,39,42,43,44,45,46,48,]),'[':([11,12,20,],[33,33,41,]),']':([45,48,],[47,49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'command':([0,1,],[2,21,]),'len':([3,4,5,6,],[22,24,25,26,]),'deg':([7,8,9,10,],[27,29,30,31,]),'coordinate':([11,12,],[32,35,]),'y':([13,],[36,]),'x':([14,],[38,]),'color':([20,],[40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> command','program',1,'p_program0','Parser.py',34),
  ('program -> program command','program',2,'p_program1','Parser.py',38),
  ('command -> fd len','command',2,'p_command0','Parser.py',44),
  ('command -> forward len','command',2,'p_command1','Parser.py',48),
  ('command -> bk len','command',2,'p_command2','Parser.py',52),
  ('command -> back len','command',2,'p_command3','Parser.py',56),
  ('command -> lt deg','command',2,'p_command4','Parser.py',60),
  ('command -> left deg','command',2,'p_command5','Parser.py',64),
  ('command -> rt deg','command',2,'p_command6','Parser.py',68),
  ('command -> right deg','command',2,'p_command7','Parser.py',72),
  ('command -> setpos coordinate','command',2,'p_command8','Parser.py',76),
  ('command -> setxy coordinate','command',2,'p_command9','Parser.py',81),
  ('command -> sety y','command',2,'p_command10','Parser.py',86),
  ('command -> setx x','command',2,'p_command11','Parser.py',90),
  ('command -> home','command',1,'p_command12','Parser.py',94),
  ('command -> pendown','command',1,'p_command13','Parser.py',99),
  ('command -> pd','command',1,'p_command14','Parser.py',104),
  ('command -> penup','command',1,'p_command15','Parser.py',109),
  ('command -> pu','command',1,'p_command16','Parser.py',114),
  ('command -> setpencolor color','command',2,'p_command17','Parser.py',119),
  ('color -> [ INT INT INT ]','color',5,'p_color','Parser.py',124),
  ('len -> INT','len',1,'p_len','Parser.py',128),
  ('deg -> INT','deg',1,'p_deg','Parser.py',132),
  ('x -> INT','x',1,'p_x','Parser.py',136),
  ('y -> INT','y',1,'p_y','Parser.py',140),
  ('coordinate -> [ INT INT ]','coordinate',4,'p_coordinate0','Parser.py',144),
  ('coordinate -> INT INT','coordinate',2,'p_coordinate0','Parser.py',145),
]
