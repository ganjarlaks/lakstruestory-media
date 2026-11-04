from lib import *
from final import final
B='193:240:63:0'
# S0 cold open: real blast audio cut 6.2-10.3
c0=[(1.9,3.9,"5 May 1980.\\NBritain was watching TV."),(2.0,4.1,"")]
caps0=[(0.0,2.0,"5 May 1980. Britain was watching TV."),(2.0,4.1,"Then the screen cut to this.")]
render_seg('A0',CUT,6.2,4.1,[(BBC,148.9,4.1,B)],caps0,[(0.0,4.1,"BBC One · 5 May 1980")])
# S2 story: cut 380.75 -> 404.75, off = -380.75
P=[(0.0,3.0),(8.0,3.0),(14.8,2.6),(17.0,2.2),(156.3,3.0),(159.3,2.5),(224.0,3.7),(227.7,3.8)]
pics=[(BBC,s,d,B) for s,d in P]; dur=sum(d for _,d in P); print('A2 dur',dur)
caps=chunk_caps(380.75,380.75+dur,-380.75)
render_seg('A2',CUT,380.75,dur,pics,caps,[(0,dur,"BBC One · 5 May 1980")])
final('EMB_SHORT_A2.mp4',['A0','A2'])
