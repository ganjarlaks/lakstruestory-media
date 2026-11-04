from lib import *
def final(out,segdirs,closepng,tail=3.0):
    run(f'ffmpeg -y -v error -loop 1 -t 2 -i open.png -vf "fps=30,format=yuv420p" -c:v libx264 -crf 17 open.mp4')
    run(f'ffmpeg -y -v error -loop 1 -t {tail} -i {closepng} -vf "fps=30,fade=t=in:d=0.3,fade=t=out:st={tail-0.5}:d=0.5,format=yuv420p" -c:v libx264 -crf 17 close_x.mp4')
    run(f'ffmpeg -y -v error -ss 557.3 -t 2 -i {CUT} -vn -ar 48000 -ac 2 -af "afade=t=in:d=0.5,afade=t=out:st=1.7:d=0.3" card.wav')
    run(f'ffmpeg -y -v error -ss 557.3 -t {tail} -i {CUT} -vn -ar 48000 -ac 2 -af "volume=0.3,afade=t=in:d=0.3,afade=t=out:st=1.8:d={tail-1.8}" tail_m.wav')
    run(f'ffmpeg -y -v error -i vo_fraser.wav -ar 48000 -ac 2 -af "adelay=500|500,volume=1.3,apad=whole_dur={tail}" vo_d.wav')
    run(f'ffmpeg -y -v error -i tail_m.wav -i vo_d.wav -filter_complex "amix=inputs=2:duration=first:normalize=0" tail_f.wav')
    vids=['open.mp4']+[f'{d}/v.mp4' for d in segdirs]+['close_x.mp4']
    auds=['card.wav']+[f'{d}/a.wav' for d in segdirs]+['tail_f.wav']
    open('vl.txt','w').write(''.join(f"file '{v}'\n" for v in vids))
    ins=' '.join(f'-i {a}' for a in auds);n=len(auds)
    run(f'ffmpeg -y -v error {ins} -filter_complex "'+''.join(f'[{i}]' for i in range(n))+f'concat=n={n}:v=0:a=1[o]" -map "[o]" all.wav')
    run(f'ffmpeg -y -v error -f concat -safe 0 -i vl.txt -i all.wav -c:v libx264 -crf 17 -preset fast -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart {out}')
import sys
w=sys.argv[1]
if w=='A': final('EMB_SHORT_A5.mp4',['A0','A2a','A2b'],'close_A.png')
else: final('EMB_SHORT_B5.mp4',['B0s','B2'],'close_B.png')
