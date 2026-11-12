from lib import *
from final import final
H='289:360:15:0'; C='289:360:97:0'
CR="National Geographic documentary"
# B0 hook: Harris real audio cut 77.97-90.17 (12.2s), src 345.0-357.2
d0=12.2
pics0=[(NG,345.0,5.0,H),(NG,1105.0,2.3,C),(NG,352.3,4.9,H)]
caps0=chunk_caps(78.0,90.2,-77.97)
render_seg('B0',CUT,77.97,d0,pics0,caps0,[(0,d0,"Sim Harris, hostage · "+CR)])
# B2: audio cut 168.09-186.2 (18.11)
d2=18.11
pics2=[(NG,385.6,1.9,C),(NG,1108.0,3.0,C),(NG,303.0,4.0,C),(NG,856.07,9.21,H)]
caps2=chunk_caps(168.09,186.25,-168.09)
render_seg('B2',CUT,168.09,d2,pics2,caps2,[(0,8.9,"Archive footage · "+CR),(8.9,d2,"Sim Harris, hostage · "+CR)])
# B3: audio cut 204.09-214.85 (10.76) cliffhanger
d3=10.76
pics3=[(NG,502.5,2.7,C),(NG,484.0,2.9,C),(NG,186.0,2.7,C),(NG,306.0,2.46,C)]
caps3=chunk_caps(204.09,214.85,-204.09)
render_seg('B3',CUT,204.09,d3,pics3,caps3,[(0,d3,"Archive footage · "+CR)])
final('EMB_SHORT_B2.mp4',['B0','B2','B3'])
