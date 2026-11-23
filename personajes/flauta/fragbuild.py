import numpy as np,sys
from PIL import Image
from scipy import ndimage
def key(path):
    a=np.asarray(Image.open(path).convert('RGB')).astype(float);r,g,b=a[...,0],a[...,1],a[...,2]
    al=np.clip((140-(np.minimum(r,b)-g))/80,0,1)
    m=np.minimum(r,b);sp=np.maximum(0,m-g)*(1-al)  # despill
    r2=r-sp*.5;b2=b-sp*.8
    out=np.dstack([r2,g,b2,al*255]).clip(0,255).astype(np.uint8);return out
d='/home/claude/piethepiper/personajes/flauta/'
# icon
ic=key(d+'flauta-fragmento.png');A=ic[...,3]>20;ys,xs=np.where(A);ic=ic[ys.min():ys.max()+1,xs.min():xs.max()+1]
Image.fromarray(ic).save(d+'flauta-fragmento-recorte.png');I=Image.fromarray(ic);I.thumbnail((256,256),Image.LANCZOS);I.save('frag_icon.webp',quality=88);print('icon',I.size)
g=key(d+'flauta-fragmento-giro.png');al=g[...,3]>30
lab,n=ndimage.label(ndimage.binary_dilation(al,iterations=12));
objs=ndimage.find_objects(lab);sizes=ndimage.sum(al,lab,range(1,n+1))
big=[(i,o) for i,(o,sz) in enumerate(zip(objs,sizes)) if sz>2000];print(len(big))
cents=[]
for i,o in big:
    m=(lab[o]==i+1)&al[o];ys,xs=np.where(m);cents.append(((o[0].start+ys.mean()),(o[1].start+xs.mean()),i,o))
# sort by row then col
cents.sort(key=lambda c:(int(c[0]//341.4),c[1]))
S=0
for cy,cx,i,o in cents:S=max(S,o[0].stop-o[0].start,o[1].stop-o[1].start)
S+=8;fr=[]
for cy,cx,i,o in cents:
    c=np.zeros((S,S,4),np.uint8);sub=g[o].copy();sub[lab[o]!=i+1]=0
    # center by bbox center
    hh,ww=sub.shape[:2];y0=(S-hh)//2;x0=(S-ww)//2;c[y0:y0+hh,x0:x0+ww]=sub;fr.append(Image.fromarray(c))
k=128/S;s2=round(S*k)
strip=Image.new('RGBA',(s2*len(fr),s2))
for j,f in enumerate(fr):strip.paste(f.resize((s2,s2),Image.LANCZOS),(j*s2,0))
strip.save('frag_spin.webp',quality=88,method=6);Image.new('RGBA',(S*len(fr),S)).save('/dev/null','PNG')
full=Image.new('RGBA',(S*len(fr),S));[full.paste(f,(j*S,0)) for j,f in enumerate(fr)];full.save(d+'flauta-fragmento-giro-tira.png')
print('frames',len(fr),'S',S,'cell',s2)
