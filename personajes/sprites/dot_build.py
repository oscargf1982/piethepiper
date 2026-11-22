# Construye el atlas de animaciones de Il Dottore a partir de tiras con fondo magenta
import numpy as np, json, base64, io, sys, os
from PIL import Image
D='/mnt/project-files/pay-the-piper/personajes/sprites/'
# uso: python3 dot_build.py <carpeta_salida> [personaje] [altura]   (personaje: dottore | guardia)
CH=sys.argv[2] if len(sys.argv)>2 else 'dottore';OUT=('dot' if CH=='dottore' else CH[:3])
KINDS={k:CH+'-'+k+'-tira.png' for k in ['reposo','caminar','baston','incienso','farol','alabarda','golpe','derrota']}
NF={'reposo':4,'caminar':8,'baston':6,'incienso':6,'farol':6,'alabarda':6,'golpe':3,'derrota':4}
TARGET_H=int(sys.argv[3]) if len(sys.argv)>3 else 356  # altura de la figura en reposo (igual que el sprite antiguo)
frames={};scale=None
for k,f in KINDS.items():
    if not os.path.exists(D+f):continue
    a=np.array(Image.open(D+f).convert('RGB')).astype(float);r,g,b=a[...,0],a[...,1],a[...,2]
    mag=np.minimum(r,b)-g  # cuanto "magenta" tiene
    al=np.clip((140-mag)/80,0,1)  # 1 = opaco
    # quitar halo magenta (despill): resta el exceso de rojo+azul sobre el verde
    ex=np.clip(np.minimum(r,b)-g,0,None);a[...,0]=r-ex;a[...,2]=b-ex
    m=al>0.5
    from scipy import ndimage as nd
    lab,nl=nd.label(m,structure=np.ones((3,3)));sizes=nd.sum(m,lab,range(1,nl+1));sl=nd.find_objects(lab)
    n=NF.get(k,4);order=np.argsort(-sizes);big=[i for i in order if sizes[i]>0.3*sizes[order[0]]]
    figs=[lab==(i+1) for i in big]
    mains=None
    while len(figs)<n:  # figuras pegadas: partir la más ancha por su columna más vacía
        wi=max(range(len(figs)),key=lambda j:np.ptp(np.where(figs[j].any(0))[0]));f=figs.pop(wi);cs=f.sum(0);cc=np.where(cs>0)[0];a0,a1=cc.min(),cc.max();q=(a1-a0)//4
        cut=a0+q+int(np.argmin(cs[a0+q:a1-q]));L=f.copy();L[:,cut:]=0;Rr=f.copy();Rr[:,:cut]=0;figs+= [L,Rr]
    figs=figs[:n];figs.sort(key=lambda f:np.where(f.any(0))[0].min())
    fb=[(np.where(f.any(0))[0].min(),np.where(f.any(0))[0].max()) for f in figs]
    for i in range(nl):  # trozos sueltos (humo, chispas) al personaje más cercano
        if i in big[:n] or sizes[i]<25:continue
        c0,c1=sl[i][1].start,sl[i][1].stop-1
        d=[max(0,b0-c1,c0-b1) - (min(c1,b1)-max(c0,b0) if min(c1,b1)>max(c0,b0) else 0) for (b0,b1) in fb]
        figs[int(np.argmin(d))]|=(lab==i+1)
    rows=np.where(m.sum(1)>3)[0];foot=rows.max()
    hs=sorted(foot-np.where(f.any(1))[0].min() for f in figs);hl=[foot-np.where(f.any(1))[0].min() for f in figs]
    scale=TARGET_H/(hl[0] if k=='derrota' else hs[len(hs)//2] if k in('reposo','caminar') else hl[-1])
    if CH=='guardia':  # escala por el cuerpo (casco a pies), no por la alabarda
        def body_h(f):
            rc=f.sum(1);rw=rc[rc>0];thr=0.3*np.median(rw);return foot-np.where(rc>thr)[0].min()
        bh=[body_h(f) for f in figs];ref=bh[0] if k=='derrota' else sorted(bh)[len(bh)//2] if k in('reposo','caminar') else bh[-1]
        if k=='reposo':BODY_T=ref*scale
        scale=BODY_T/ref
    fl=[]
    for f in figs:
        keep=nd.binary_dilation(f,iterations=2);yy,xx=np.where(f);y0,x0,x1=yy.min(),xx.min(),xx.max()
        lab2,_=nd.label(f,structure=np.ones((3,3)));sz=np.bincount(lab2.ravel());sz[0]=0;body=lab2==np.argmax(sz)
        bl=body[foot-int((foot-y0)*.12):foot+1];bw=np.where(bl)[1]
        if len(bw)<20:bw=np.where(f[foot-int((foot-y0)*.12):foot+1])[1]
        ax=float(np.median(bw))-x0
        sub=a[y0:foot+1,x0:x1+1];alp=(al*keep)[y0:foot+1,x0:x1+1]*255
        im=Image.fromarray(np.dstack([sub,alp]).astype(np.uint8),'RGBA');W=max(1,round(im.width*scale));H=max(1,round(im.height*scale))
        fl.append((im.resize((W,H),Image.LANCZOS),round(ax*scale),H))
    frames[k]=fl;print(k,len(fl),'frames')
# empaquetar en filas
Wmax=2048;x=y=rowh=0;meta={};placed=[]
for k,fl in frames.items():
    meta[k]=[]
    for im,ax,ay in fl:
        if x+im.width>Wmax:x=0;y+=rowh+2;rowh=0
        placed.append((im,x,y));meta[k].append({'x':x,'y':y,'w':im.width,'h':im.height,'ax':ax,'ay':ay});x+=im.width+2;rowh=max(rowh,im.height)
at=Image.new('RGBA',(Wmax,y+rowh),(0,0,0,0))
for im,px,py in placed:at.paste(im,(px,py))
bb=at.getbbox();at=at.crop((0,0,bb[2],bb[3]))
b=io.BytesIO();at.save(b,'WEBP',quality=82);open(sys.argv[1]+OUT+'_atlas.b64','w').write(base64.b64encode(b.getvalue()).decode())
json.dump(meta,open(sys.argv[1]+OUT+'_meta.json','w'),separators=(',',':'));at.save(sys.argv[1]+OUT+'_atlas.png');print('atlas',at.size,len(b.getvalue()))
