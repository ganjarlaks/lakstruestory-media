import subprocess,os
S='/tmp/claude-0/-home-claude/a7987d7b-ff4e-55a3-a72f-03f553db811a/scratchpad'
BBC=S+'/emb_src/emb5.mp4'; NG=S+'/emb_src/emb46.mp4'
CUT=S+'/media/review/embassy_long_cut3/embassy_long_cut3_review_720p.mp4'
SRT=S+'/media/review/embassy_long_cut3/embassy_long_cut3_captions_en_DRAFT.srt'
def run(c): subprocess.run(c,shell=True,check=True)
def tt(x):
    h,m,r=x.split(':');s,ms=r.split(',');return int(h)*3600+int(m)*60+int(s)+int(ms)/1000
def ts(x):
    h=int(x//3600);m=int(x%3600//60);s=x%60;return f'{h}:{m:02d}:{s:05.2f}'
def srt_caps(lo,hi):
    out=[]
    for b in open(SRT).read().strip().split('\n\n'):
        l=b.split('\n');a,c=l[1].split(' --> ');a=tt(a);c=tt(c)
        if lo-0.05<=a<hi: out.append((a,min(c,hi),' '.join(l[2:])))
    return out
def split(txt,maxc=50):
    w=txt.split();n=-(-len(txt)//maxc)
    if n<=1: return [txt]
    tgt=len(txt)/n;out=[];cur=[]
    for x in w:
        cur.append(x)
        if len(' '.join(cur))>=tgt-6 and len(out)<n-1: out.append(' '.join(cur));cur=[]
    if cur: out.append(' '.join(cur))
    return out
def two(x):
    w=x.split()
    if len(x)<=27: return x
    best=None
    for i in range(1,len(w)):
        a=' '.join(w[:i]);b=' '.join(w[i:]);sc=max(len(a),len(b))
        if best is None or sc<best[0]: best=(sc,a,b)
    return best[1]+'\\N'+best[2]
HEAD='''[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Cap,Poppins,95.3,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,8,90,90,1380,1
Style: Cred,Poppins,53,&H00C0C0C0,&H00C0C0C0,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,8,90,90,1600,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
'''
def render_seg(name,src_audio,a_ss,dur,pieces,caps,credits):
    """pieces: (src,start,len,crop) ; caps: list (t0,t1,text) in seg time (already-chunked ok) ; credits: (t0,t1,text)"""
    os.makedirs(name,exist_ok=True)
    parts=[]
    for k,(src,s,d,crop) in enumerate(pieces):
        p=f'{name}/p{k}.mp4'
        run(f'ffmpeg -y -v error -ss {s:.3f} -t {d:.3f} -i {src} -vf "fps=30,crop={crop},scale=1080:1344:flags=lanczos,unsharp=5:5:0.7,format=yuv420p" -an -c:v libx264 -preset fast -crf 17 {p}')
        parts.append(p)
    open(f'{name}/l.txt','w').write(''.join(f"file 'p{k}.mp4'\n" for k in range(len(parts))))
    run(f'ffmpeg -y -v error -f concat -safe 0 -i {name}/l.txt -c copy {name}/band.mp4')
    ass=HEAD
    for a,b,x in caps: ass+=f'Dialogue: 0,{ts(a)},{ts(b)},Cap,,0,0,0,,{two(x)}\n'
    for a,b,x in credits: ass+=f'Dialogue: 0,{ts(a)},{ts(b)},Cred,,0,0,0,,{x}\n'
    open(f'{name}/cap.ass','w').write(ass)
    run(f'ffmpeg -y -v error -i {name}/band.mp4 -vf "pad=1080:1920:0:0:black,ass={name}/cap.ass:fontsdir=/usr/share/fonts/truetype/google-fonts,format=yuv420p" -c:v libx264 -crf 17 -preset fast {name}/v.mp4')
    run(f'ffmpeg -y -v error -ss {a_ss} -t {dur} -i {src_audio} -vn -ar 48000 -ac 2 -af "afade=t=in:d=0.03,afade=t=out:st={dur-0.05:.3f}:d=0.05" {name}/a.wav')
    tot=sum(p[2] for p in pieces); print(name,'pics',round(tot,2),'audio',dur)
def chunk_caps(lo,hi,offset):
    ev=[]
    for a,c,txt in srt_caps(lo,hi):
        ch=split(txt);tl=sum(len(x) for x in ch);t=a
        for x in ch:
            d=(c-a)*len(x)/tl;ev.append((t+offset,t+d+offset,x));t+=d
    return ev
def assemble(out,segs,total_tail=3.5):
    """segs: list of dirs in order: seg0, card, seg2..., then closing"""
    # video list
    run(f'ffmpeg -y -v error -loop 1 -t 2 -i open.png -vf "fps=30,format=yuv420p" -c:v libx264 -crf 17 open.mp4')
    run(f'ffmpeg -y -v error -loop 1 -t {total_tail} -i close.png -vf "fps=30,fade=t=in:d=0.3,fade=t=out:st={total_tail-0.5}:d=0.5,format=yuv420p" -c:v libx264 -crf 17 close.mp4')
