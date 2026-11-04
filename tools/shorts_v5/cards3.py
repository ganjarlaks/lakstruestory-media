from PIL import Image, ImageDraw, ImageFont
import sys
W,H=1080,1920
SERIF="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS="/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
f=lambda p,s:ImageFont.truetype(p,s)
def wrap(d,t,font,mw):
    L=[];c=''
    for w in t.split():
        x=(c+' '+w).strip()
        if d.textlength(x,font=font)<=mw:c=x
        else:L.append(c);c=w
    L.append(c);return L
def cl(d,lines,font,y,fill,gap=14):
    for ln in lines:
        w=d.textlength(ln,font=font);d.text(((W-w)/2,y),ln,font=font,fill=fill);y+=font.size+gap
    return y
def close(title,out):
    im=Image.new('RGB',(W,H),0);d=ImageDraw.Draw(im)
    tf=f(SERIF,84);y=cl(d,wrap(d,title,tf,940),tf,420,(255,255,255),16)
    d.rectangle(((W-160)/2,y+34,(W+160)/2,y+42),fill=(255,210,0))
    av=Image.open('../channel_avatar.jpg').convert('RGB').resize((260,260))
    m=Image.new('L',(260,260),0);ImageDraw.Draw(m).ellipse((0,0,259,259),fill=255)
    im.paste(av,(410,1130),m)
    cl(d,["Full video at our channel"],f(SERIF,60),1430,(255,255,255))
    im.save(out)
close("Iranian Embassy Siege: Britain Watched It Live",'close_A.png')
close("Iranian Embassy Siege: The Hostage Said It Was “Mice”",'close_B.png')
