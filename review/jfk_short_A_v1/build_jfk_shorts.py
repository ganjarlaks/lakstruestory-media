import sys, os, json, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.io import wavfile
from scipy.signal import resample_poly
S='/tmp/claude-0/-home-claude/a7987d7b-ff4e-55a3-a72f-03f553db811a/scratchpad/jfk'
RAW='/home/claude/work_jfk/raw/'; LONG='/home/claude/lakstruestory-media/review/jfk_long_v3/jfk_long_v3_review_720p.mp4'
VD='/home/claude/production-house/channels/laks-true-story/long-video/jfk/voice_data/'
SR=48000; TITLE='JFK : The Last Day In Dallas'
SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; POP="/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
INTER="/usr/share/fonts/opentype/inter/Inter-%s.otf"
def run(c):
    subprocess.run('nice -n 10 '+c,shell=True,check=True)
def ff(c): run('ffmpeg -y -v error -threads 2 '+c)
WT={x['n']:x['words'] for x in json.load(open(VD+'jfk_word_times.json'))}
ST={x['n']:x['start'] for x in json.load(open(VD+'sent_times.json'))}
def raw(n):
    sr,x=wavfile.read(RAW+n+'.wav'); x=x.astype(np.float64)/32768
    return resample_poly(x,SR,sr)
def words(n,a,b):
    s0=ST[n]; out=[]
    for w in WT[n]:
        s=w['s']-s0
        if (s>=a+0.01 or (a==0.0 and s>=-0.1)) and s<b-0.05: out.append((w['w'],max(s,a)-a,min(w['e']-s0,b)-a))
    return out
def lufs(x):
    p=S+'/w/_l.wav'; wavfile.write(p,SR,(np.clip(np.stack([x,x],1),-1,1)*32767).astype(np.int16))
    r=subprocess.run(f'ffmpeg -nostats -i {p} -af ebur128=peak=true -f null - 2>&1',shell=True,capture_output=True,text=True).stdout
    i=r.rfind('I:'); return float(r[i+2:].split('LUFS')[0])
def vlim(x,target=-16.0):
    g=10**((target-lufs(x))/20)
    for _ in range(4):
        wavfile.write(S+'/w/_i.wav',SR,(np.clip(x*g,-8,8).astype(np.float32)))
        subprocess.run(f'ffmpeg -y -v error -i {S}/w/_i.wav -af alimiter=limit=0.8:attack=5:release=60:level=0 -c:a pcm_f32le {S}/w/_o.wav',shell=True,check=True)
        y=wavfile.read(S+'/w/_o.wav')[1].astype(np.float64)
        L=lufs(y); 
        if abs(L-target)<0.15: break
        g*=10**((target-L)/20)
    print('vlim',L,np.abs(y).max()); return y
# ---------- cards
def fnt(p,s): return ImageFont.truetype(p,s)
def wrap(d,t,font,mw):
    L=[];c=''
    for w in t.split():
        x=(c+' '+w).strip()
        if d.textlength(x,font=font)<=mw:c=x
        else:L.append(c);c=w
    L.append(c);return L
def center(d,lines,font,y,fill,gap=16):
    for ln in lines:
        w=d.textlength(ln,font=font);d.text(((1080-w)/2,y),ln,font=font,fill=fill);y+=font.size+gap
    return y
def open_card(path,place):
    im=Image.new('RGB',(1080,1920),0);d=ImageDraw.Draw(im)
    center(d,['A TRUE STORY'],fnt(POP,40),705,(190,190,190))
    y=center(d,wrap(d,TITLE,fnt(SERIF,88),940),fnt(SERIF,88),810,(255,255,255))
    d.rectangle((460,y+14,620,y+22),fill=(255,210,0))
    center(d,[place],fnt(POP,48),y+60,(190,190,190)); im.save(path)
def close_card(path):
    im=Image.new('RGB',(1080,1920),0);d=ImageDraw.Draw(im)
    tf=fnt(SERIF,84);y=center(d,wrap(d,TITLE,tf,940),tf,420,(255,255,255))
    d.rectangle((460,y+18,620,y+26),fill=(255,210,0))
    lg=Image.open('/home/claude/lakstruestory-media/assets/brand/lts_journal_logo_2048.png').convert('RGBA').resize((260,260),Image.LANCZOS)
    im.paste(lg,(410,1130),lg)
    center(d,['Full video at our channel'],fnt(SERIF,60),1430,(255,255,255)); im.save(path)
# ---------- graphics (1080x1344)
BG=(24,26,29);GRID=(38,41,46);INK=(226,222,212);DIM=(130,132,136);ACC=(232,168,56)
def I(s,b=False): return ImageFont.truetype(INTER%('Bold' if b else 'Regular'),s)
def ease(t): t=max(0,min(1,t));return t*t*(3-2*t)
def bgimg():
    im=Image.new('RGB',(1080,1344),BG);d=ImageDraw.Draw(im)
    for x in range(0,1080,60): d.line([(x,0),(x,1344)],fill=GRID)
    for y in range(0,1344,60): d.line([(0,y),(1080,y)],fill=GRID)
    return im
def mix(c,a): return tuple(int(BG[i]+(c[i]-BG[i])*a) for i in range(3))
def gfx_frames(kind,dur,path):
    base=bgimg(); n=int(round(dur*30))
    p=subprocess.Popen(f'nice -n 10 ffmpeg -y -v error -threads 2 -f rawvideo -pix_fmt rgb24 -s 1080x1344 -r 30 -i - -c:v libx264 -preset veryfast -crf 17 -pix_fmt yuv420p {path}',shell=True,stdin=subprocess.PIPE)
    for f in range(n):
        t=f/30; im=base.copy(); d=ImageDraw.Draw(im)
        (clock if kind=='clock' else findings)(d,t)
        p.stdin.write(im.tobytes())
    p.stdin.close(); p.wait()
def head(d,t,kick,title):
    a=ease(t/0.5); d.rectangle((90,100,90+90*a,106),fill=ACC)
    d.text((90,124),kick,font=I(34,True),fill=mix(ACC,a)); d.text((90,176),title,font=I(66,True),fill=mix(INK,a))
def clock(d,t):
    head(d,t,'FRIDAY 22 NOVEMBER 1963','The clock before Dallas')
    d.text((90,262),'Fort Worth to Dallas, local time',font=I(34),fill=mix(DIM,ease(t/0.5)))
    nodes=[(0.15,500,'8:45 a.m.','Speech outside Hotel Texas, Fort Worth'),
           (3.6,760,'11:25 a.m.','Air Force One takes off'),
           (7.3,1030,'11:40 a.m.','Touchdown at Love Field, Dallas')]
    # line segments
    for i in range(len(nodes)-1):
        t0=nodes[i+1][0]-0.05; a=ease((t-t0)/0.6)
        y0=nodes[i][1]; y1=y0+(nodes[i+1][1]-y0)*a
        d.line([(170,y0),(170,y1)],fill=ACC,width=6)
    for k,(t0,y,tm,desc) in enumerate(nodes):
        a=ease((t-t0)/0.4)
        if a<=0: continue
        r=int(16+ (8 if k==2 else 0))
        d.ellipse((170-r,y-r,170+r,y+r),fill=mix((255,226,160) if k==2 else ACC,a))
        d.text((250,y-48),tm,font=I(70,True),fill=mix(ACC,a)); d.text((250,y+34),desc,font=I(40),fill=mix(INK,a))
    a=ease((t-6.5)/0.5)
    if a>0:
        d.line([(215,775),(235,775),(235,1015),(215,1015)],fill=mix(DIM,a),width=4)
        d.text((250,880),'Flight, about 13 minutes',font=I(38),fill=mix(DIM,a))
    d.text((90,1250),'Times as given by the Warren Report and NARA',font=I(26),fill=mix(DIM,0.8))
    d.text((90,1285),'(local Dallas clock). Schematic, not to scale.',font=I(26),fill=mix(DIM,0.8))
def findings(d,t):
    head(d,t,'CLAIMS, NOT PROOF','Two investigations,'); 
    d.text((90,250),'two answers',font=I(66,True),fill=mix(INK,ease(t/0.5)))
    def row(t0,y,yr,name,body):
        a=ease((t-t0)/0.5)
        if a<=0: return
        d.line([(90,y-24),(990,y-24)],fill=mix(GRID,a)if False else mix((60,63,68),a),width=2)
        d.text((90,y),yr,font=I(110,True),fill=mix(ACC,a)); d.text((90,y+134),name,font=I(38,True),fill=mix(INK,a))
        yy=y+190
        for ln in body: d.text((90,yy),ln,font=I(42),fill=mix((200,198,190),a)); yy+=58
    row(0.2,390,'1979','House Select Committee on Assassinations',['Oswald fired the shots that killed','the president. A conspiracy was','probable, mainly from a police','radio recording.'])
    row(11.9,880,'1982','National Academy of Sciences panel',['The recording did not support','that finding.'])
    d.text((90,1285),'Warren Report 1964, HSCA 1979, NAS panel 1982.',font=I(26),fill=mix(DIM,0.8))
    d.text((90,1250),'Findings are claims; the record is disputed.',font=I(26),fill=mix(DIM,0.8))
# ---------- captions
HEAD='''[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Cap,Poppins,95.3,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,8,90,90,1380,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
'''
def two(x):
    w=x.split()
    if len(x)<=27: return x
    best=None
    for i in range(1,len(w)):
        a=' '.join(w[:i]);b=' '.join(w[i:]);sc=max(len(a),len(b))
        if best is None or sc<best[0]: best=(sc,a,b)
    return best[1]+'\\N'+best[2]
def ts(x): return f'{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}'
def srt_ts(x): return f'{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{int(round((x%1)*1000)):03d}'
def chunks(wl):
    out=[];cur=[]
    for w,s,e in wl:
        cur.append((w,s,e)); txt=' '.join(c[0] for c in cur)
        if w.lower().strip(',.?') in ('the','a','in','of','to','at','that','and','on','than','from','he') and len(txt)<46: continue
        if (len(txt)>=34 and len(cur)>=3) or (w[-1] in ',.?' and len(txt)>=16) or len(txt)>=46:
            out.append(cur);cur=[]
    if cur:
        if out and len(cur)<2: out[-1]+=cur
        else: out.append(cur)
    ev=[]
    for i,c in enumerate(out):
        t=' '.join(x[0] for x in c); t=(t[0].upper()+t[1:]) if i==0 else t
        s=c[0][1]; e=(out[i+1][0][1] if i+1<len(out) else c[-1][2]+0.2)
        e=min(e,c[-1][2]+0.5) if i+1<len(out) else e
        ev.append([s,e,t])
    return ev
# ---------- build
def build(cfg):
    name=cfg['name']; os.makedirs(S+'/w/'+name,exist_ok=True); W=S+'/w/'+name+'/'
    GAP=0.3; t=0.0; nar=np.zeros(int(35*SR)); caps=[]; starts=[]
    for (n,a,b) in cfg['items']:
        x=raw(n)[int(a*SR):int(b*SR)].copy()
        k=int(0.03*SR); x[:k]*=np.linspace(0,1,k); x[-k:]*=np.linspace(1,0,k)
        i0=int(t*SR); nar[i0:i0+len(x)]+=x
        wl=[(w,s+t,e+t) for (w,s,e) in words(n,a,b)]
        caps+=chunks(wl); starts.append(t); t+=(b-a)+GAP
    # a1 ends w/ gap handled; story length
    story=cfg['story']; assert t-GAP<=story, (t,story)
    OPEN=2.0; CLOSE=3.0; total=OPEN+story+CLOSE; print(name,'total',total); assert total<=30.0
    # voice levels
    nar=vlim(nar[:int(story*SR)]); nar=np.concatenate([nar,np.zeros(int(35*SR))])
    vo=wavfile.read(S+'/w/vo_flat.wav')[1].astype(np.float64)/32768
    if vo.ndim>1: vo=vo.mean(1)
    vo=vlim(vo)
    # music
    sr_,m=None,None
    ff(f'-i {S}/mus/b.mp3 -ss {cfg["mus_off"]} -t {total+1} -ac 1 -ar {SR} {W}bed.wav')
    bed=wavfile.read(W+'bed.wav')[1].astype(np.float64)/32768
    bed=bed[:int(total*SR)]
    bed*=10**((lufs(bed)*-1-26)/20)  # bed to -26 LUFS
    N=int(total*SR); env=np.ones(N)*1.0
    # opening 0..2: music alone, slightly up (-22 => +4dB), fade in .5
    ts_=np.arange(N)/SR
    env[ts_<OPEN]=1.6
    env[(ts_>=OPEN-0.3)&(ts_<OPEN)]=np.linspace(1.6,1.0,int(0.3*SR))[:((ts_>=OPEN-0.3)&(ts_<OPEN)).sum()]
    cs=OPEN+story
    env[ts_>=cs]=1.0
    fi=np.clip(ts_/0.5,0,1); fo=np.clip((total-ts_)/1.5,0,1)
    mus=bed*env*fi*fo
    out=np.zeros(N); out+=mus
    o0=int(OPEN*SR); out[o0:o0+len(nar[:int(story*SR)])]+=nar[:int(story*SR)]
    c0=int((cs+0.5)*SR); out[c0:c0+len(vo)]+=vo[:N-c0]
    pk=np.abs(out).max(); print('peak',pk)
    out=vlim(out,-16.0); print('final mix LUFS',lufs(out),'peak',np.abs(out).max())
    stereo=np.stack([out,out],1)
    wavfile.write(W+'mix.wav',SR,(stereo*32767).astype(np.int16))
    # video
    open_card(W+'open.png',cfg['place']); close_card(W+'close.png')
    ff(f'-loop 1 -t {OPEN} -i {W}open.png -vf "fps=30,format=yuv420p" -c:v libx264 -preset veryfast -crf 17 {W}open.mp4')
    ff(f'-loop 1 -t {CLOSE} -i {W}close.png -vf "fps=30,fade=t=in:d=0.3,fade=t=out:st={CLOSE-0.5}:d=0.5,format=yuv420p" -c:v libx264 -preset veryfast -crf 17 {W}close.mp4')
    parts=[]
    for k,(kind,a,b,src,x) in enumerate(cfg['pic']):
        p=f'{W}p{k}.mp4'
        if kind=='gfx': gfx_frames(src,b-a,p)
        else: ff(f'-ss {src} -t {b-a:.3f} -i {LONG} -vf "fps=30,crop=523:650:{x}:70,scale=1080:1344:flags=lanczos,unsharp=5:5:0.6,format=yuv420p" -an -c:v libx264 -preset veryfast -crf 17 {p}')
        parts.append(p)
    assert abs(sum(b-a for _,a,b,_,_ in cfg['pic'])-story)<0.05
    open(W+'l.txt','w').write(''.join(f"file '{p}'\n" for p in parts))
    ff(f'-f concat -safe 0 -i {W}l.txt -c copy {W}band.mp4')
    ass=HEAD; srt=''
    for i,(s,e,tx) in enumerate(caps):
        s+=OPEN; e+=OPEN; ass+=f'Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{two(tx)}\n'
        srt+=f'{i+1}\n{srt_ts(s)} --> {srt_ts(e)}\n{tx}\n\n'
    srt+=f'{len(caps)+1}\n{srt_ts(cs+0.5)} --> {srt_ts(cs+2.5)}\nWatch the full video at our channel\n\n'
    open(W+'cap.ass','w').write(ass); open(W+f'{cfg["out"]}.srt','w').write(srt)
    ff(f'-i {W}band.mp4 -vf "pad=1080:1920:0:0:black,ass={W}cap.ass:fontsdir=/usr/share/fonts/truetype/google-fonts,format=yuv420p" -c:v libx264 -preset veryfast -crf 17 {W}story.mp4')
    open(W+'v.txt','w').write(f"file 'open.mp4'\nfile 'story.mp4'\nfile 'close.mp4'\n")
    ff(f'-f concat -safe 0 -i {W}v.txt -i {W}mix.wav -c:v libx264 -preset veryfast -crf 20 -maxrate 6M -bufsize 12M -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart {W}{cfg["out"]}.mp4')
    print('done',W)
A=dict(name='A',out='jfk_SHORT_A_v1_1080x1920',place='Dallas · 1963',mus_off=15,story=23.0,
 items=[('6.01',0.0,3.64),('2.07',3.745,6.92),('2.09',0.0,4.85),('3.01',0.0,4.90),('6.01',3.63,8.38)],
 pic=[('f',0,3.94,'166.5',250),('gfx',3.94,12.4,'clock',0),('f',12.4,15.4,'172.0',170),('f',15.4,18.4,'182.5',380),('f',18.4,21.0,'184.5',380),('f',21.0,23.0,'194.0',250)])
B=dict(name='B',out='jfk_SHORT_B_v1_1080x1920',place='Dallas · 1963',mus_off=60,story=23.3,
 items=[('5.07',0.0,6.30),('5.08',0.0,5.05),('5.09',0.0,6.90),('6.02',0.0,3.85)],
 pic=[('gfx',0,18.9,'findings',0),('f',18.9,23.3,'303.8',340)])
if __name__=='__main__':
    build({'A':A,'B':B}[sys.argv[1]])
