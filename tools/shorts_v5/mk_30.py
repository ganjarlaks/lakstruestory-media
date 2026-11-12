from lib import *
B='193:240:63:0'; H='289:360:15:0'; C='289:360:97:0'; CR="National Geographic documentary"
# A2a / A2b
da=5.7
render_seg('A2a',CUT,380.75,da,[(BBC,0.0,3.0,B),(BBC,8.0,2.7,B)],chunk_caps(380.75,380.75+da,-380.75),[(0,da,"BBC One · 5 May 1980")])
db=12.66
render_seg('A2b',CUT,391.76,db,[(BBC,156.3,3.0,B),(BBC,159.3,2.5,B),(BBC,224.0,3.7,B),(BBC,227.7,3.46,B)],chunk_caps(391.76,391.76+db,-391.76),[(0,db,"BBC One · 5 May 1980")])
# B0 short hook
d0=4.9
render_seg('B0s',CUT,85.27,d0,[(NG,352.3,4.9,H)],chunk_caps(85.27,90.2,-85.27),[(0,d0,"Sim Harris, hostage · "+CR)])
