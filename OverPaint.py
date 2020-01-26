####Need Python 3.8 and PyGame 1.9.6#####################



from pygame import *
import math
from random import *
from tkinter import *
from tkinter import filedialog


fps=time.Clock()


root=Tk()
root.withdraw()

init()

musicList=[("music/Overwatch League 2019 Soundtrack - "+str(i)+".mp3") for i in range(1,35)]



display.set_caption("OverPaint")


width,height=display.Info().current_w,display.Info().current_h
screen=display.set_mode((width,height),FULLSCREEN)


LC=False

timeSlider=False

getColour=False

canvas=Surface((width,height),SRCALPHA).convert_alpha()
canvas.fill((0,0,0,0))

hl=Surface((int(height*(50/1080)),int(height*(50/1080))),SRCALPHA).convert_alpha()
hl.fill((0,0,0,0))

def insideCircle(a,b,h,k,r):
    if math.sqrt((a-h)**2+(b-k)**2)<=r:
        return True

        
def ratioScaling(img,nw,nh):
    imgw,imgh=img.get_size()
    if imgw>imgh:
        ratio=nw/imgw
        h=ratio*imgh
        if h>nh:
            ratio=nh/imgh
            w=ratio*imgw
            h=nh
        else:
            w=nw
    else:
        ratio=nh/imgh
        w=ratio*imgw
        if w>nw:
            ratio=nw/imgw
            w=nw
            h=ratio*imgh
        else:
            h=nh

    return transform.scale(img,(int(w),int(h)))

def sprayCan():
    if mb[0]==1:
        dx=mx-omx
        dy=my-omy
        dist=math.hypot(dx,dy)
        if int(dist)==0:
            for i in range(30):
                randx=randint(-thickSpray,thickSpray)
                randy=randint(-thickSpray,thickSpray)
                if insideCircle(mx+randx,my+randy,mx,my,thickSpray):
                    draw.circle(canvas,col,(mx+randx,my+randy),0)

        
        else:
            for i in range(1,int(dist)):
                cx=int(omx+i*dx/dist)
                cy=int(omy+i*dy/dist)
                for y in range(10):
                    randx=randint(-thickSpray,thickSpray)
                    randy=randint(-thickSpray,thickSpray)
                    if insideCircle(cx+randx,cy+randy,cx,cy,thickSpray):
                        draw.circle(canvas,col,(cx+randx,cy+randy),0)

def brush():
    if mb[0]==1:
        dx=mx-omx
        dy=my-omy
        dist=math.hypot(dx,dy)
        if int(dist)==0 or int(dist)==1 or int(dist)==2:
            draw.circle(canvas,col,(mx,my),thickB)
            draw.circle(canvas,col,(omx,omy),thickB)
        else:
            for i in range(1,int(dist)):
                draw.circle(canvas,col,(mx,my),thickB)
                draw.circle(canvas,col,(omx,omy),thickB)
                cx=int(omx+i*dx/dist)
                cy=int(omy+i*dy/dist)
                draw.circle(canvas,col,(cx,cy),thickB)


def eraser():
    if mb[0]==1:
        dx=mx-omx
        dy=my-omy
        dist=math.hypot(dx,dy)
        if int(dist)==0 or int(dist)==1 or int(dist)==2:
            draw.circle(canvas,(0,0,0,0),(mx,my),thickE)
            draw.circle(canvas,(0,0,0,0),(omx,omy),thickE)
        else:
            for i in range(1,int(dist)):
                draw.circle(canvas,(0,0,0,0),(mx,my),thickE)
                draw.circle(canvas,(0,0,0,0),(omx,omy),thickE)
                cx=int(omx+i*dx/dist)
                cy=int(omy+i*dy/dist)
                draw.circle(canvas,(0,0,0,0),(cx,cy),thickE)


def highlighter():
    if mb[0]==1:
        dx=mx-omx
        dy=my-omy
        dist=math.hypot(dx,dy)
        draw.circle(hl,(col[0],col[1],col[2],4),(int(height*(25/1080)),int(height*(25/1080))),thickHL)

        for i in range(1,int(dist)):
                cx=int(omx+i*dx/dist)
                cy=int(omy+i*dy/dist)
                canvas.blit(hl,(cx-int(height*(25/1080)),cy-int(height*(25/1080))))
        hl.fill((0,0,0,0))

RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)

filterFont=font.SysFont("comicsansms",int(height*(5/96)*0.71))
musicFont=font.SysFont("comicsansms",int(height*(40/1080)*0.71))


#Loading Images
colourPicker=image.load("image/colour picker.png")
shade=image.load("image/shades.png")
background=image.load("image/background.png")
pencilPic=image.load("image/pencil.png")
eraserPic=image.load("image/eraser.png")
brushPic=image.load("image/brush.png")
redoPic=image.load("image/redo.png")
undoPic=transform.flip(redoPic,True,False)
savePic=image.load("image/save.png")
openPic=image.load("image/open.png")
beforePic=image.load("image/before.png")
shufflePic=image.load("image/shuffle.png")
pausePic=image.load("image/pause.png")
playPic=image.load("image/play.png")
nextPic=image.load("image/next.png")
rectPic=image.load("image/rect.png")
circlePic=image.load("image/circle.png")
linePic=image.load("image/line.png")
hlPic=image.load("image/highlighter.png")
sprayPic=image.load("image/spray.png")
bucketPic=image.load("image/bucket.png")
polyPic=image.load("image/polygon.png")
edPic=image.load("image/ed.png")
tbPic=image.load("image/textBox.png")
cropPic=image.load("image/crop.png")
proPic=image.load("image/pro.png")


background=transform.scale(background,(width,height))
pencilPic=transform.scale(pencilPic,(int(1/15*height-2),int(1/15*height-2)))
eraserPic=transform.scale(eraserPic,(int(1/15*height-2),int(1/15*height-2)))
brushPic=transform.scale(brushPic,(int(1/15*height-2),int(1/15*height-2)))
colourPicker=transform.scale(colourPicker,(int(width*(270/1920)),int(width*(270/1920))))
shade=transform.scale(shade,(int(height*(20/1080)),int(width*(270/1920))))
redoPic=transform.scale(redoPic,(int(height*(5/96)-2),int(height*(5/96)-2)))
undoPic=transform.scale(undoPic,(int(height*(5/96)-2),int(height*(5/96)-2)))
savePic=transform.scale(savePic,(int(height*(5/96)-2),int(height*(5/96)-2)))
openPic=transform.scale(openPic,(int(height*(5/96)-2),int(height*(5/96)-2)))
pausePic=transform.scale(pausePic,(int(height*(5/96)),int(height*(5/96))))
playPic=transform.scale(playPic,(int(height*(5/96)),int(height*(5/96))))
nextPic=transform.scale(nextPic,(int(height*(5/96)),int(height*(5/96))))
rectPic=transform.scale(rectPic,(int(52/1080*height),int(52/1080*height)))
circlePic=transform.scale(circlePic,(int(1/15*height),int(1/15*height)))
linePic=transform.scale(linePic,(int(1/15*height),int(1/15*height)))
hlPic=transform.scale(hlPic,(int(1/15*height),int(1/15*height)))
sprayPic=transform.scale(sprayPic,(int(1/15*height),int(1/15*height)))
bucketPic=transform.scale(bucketPic,(int(1/15*height),int(1/15*height)))
polyPic=transform.scale(polyPic,(int(1/15*height),int(1/15*height)))
edPic=transform.scale(edPic,(int(1/15*height),int(1/15*height)))
tbPic=transform.scale(tbPic,(int(1/15*height),int(1/15*height)))
cropPic=transform.scale(cropPic,(int(1/15*height),int(1/15*height)))
proPic=transform.scale(proPic,(int(1/15*height),int(1/15*height)))

#Rect



colourPickerRect=colourPicker.get_rect()
colourPickerRect.x,colourPickerRect.y=3,height-int(width*(270/1920))-3
shadeRect=shade.get_rect()
shadeRect.x,shadeRect.y=int(width*(270/1920))+3,height-int(width*(270/1920))-3

ccRect=Rect(0,height-int(width*(270/1920))-6,int(width*(270/1920))+6+int(height*(20/1080)),int(width*(270/1920))+6)

undoRect=Rect(0,0,int(height*(5/96)),int(height*(5/96)))
redoRect=Rect(int(height*(5/96)+2),0,int(height*(5/96)),int(height*(5/96)))
canvasRect=Rect(int(width*0.1875),int(height*(1/6)),int(width-width*0.25),int(height-height*(1/3)))
pencilRect=Rect(int(1/40*width),int(1/6*height),int(1/15*height),int(1/15*height))
eraserRect=Rect(int(7/80*width),int(1/6*height),int(1/15*height),int(1/15*height))
brushRect=Rect(int(1/40*width),int(1/4*height),int(1/15*height),int(1/15*height))
rectRect=Rect(int(7/80*width),int(1/4*height),int(1/15*height),int(1/15*height))
saveRect=Rect(width-int(height*(5/96)),0,int(height*(5/96)),int(height*(5/96)))
openRect=Rect(width-(int(height*(5/96))*2)-2,0,int(height*(5/96)),int(height*(5/96)))
circleRect=Rect(int(1/40*width),int(1/3*height),int(1/15*height),int(1/15*height))
lineRect=Rect(int(7/80*width),int(1/3*height),int(1/15*height),int(1/15*height))
hlRect=Rect(int(1/40*width),int(5/12*height),int(1/15*height),int(1/15*height))
sprayRect=Rect(int(7/80*width),int(5/12*height),int(1/15*height),int(1/15*height))
bucketRect=Rect(int(1/40*width),int(1/2*height),int(1/15*height),int(1/15*height))
polyRect=Rect(int(7/80*width),int(1/2*height),int(1/15*height),int(1/15*height))
eyeDropperRect=Rect(int(1/40*width),int(7/12*height),int(1/15*height),int(1/15*height))
tbRect=Rect(int(7/80*width),int(7/12*height),int(1/15*height),int(1/15*height))
cropRect=Rect(int(1/40*width),int(2/3*height),int(1/15*height),int(1/15*height))
proRect=Rect(int(7/80*width),int(2/3*height),int(1/15*height),int(1/15*height))

tRects=[pencilRect,eraserRect,pencilRect,eraserRect,brushRect,rectRect,circleRect,lineRect,hlRect,sprayRect,bucketRect,polyRect,eyeDropperRect,tbRect,cropRect,proRect]


GC=False

col=BLACK

omx,omy,mx,my=0,0,0,0

running=True

tool="no tool"


mInd=0

mixer.music.set_volume(0.5)

mixer.music.load(musicList[mInd])
mixer.music.play()



#Filters
def sepia():
    for x in range(int(width*0.1875),int(width*0.1875)+int(width-width*0.25)):
        for y in range(int(height*(1/6)),int(height*(1/6))+int(height-height*(1/3))):
            r,g,b,a=screen.get_at((x,y))
            nr = min(0.393*r + 0.769*g + 0.189*b,255)
            ng = min(0.349*r + 0.686*g + 0.168*b,255)
            nb = min(0.272*r + 0.534*g + 0.131*b,255)
            screen.set_at((x,y),(int(nr),int(ng),int(nb)))
            R,G,B,A=canvas.get_at((x,y))
            if (R,G,B,A)!=(0,0,0,0):
                NR = min(0.393*R + 0.769*G + 0.189*B,255)
                NG = min(0.349*R + 0.686*G + 0.168*B,255)
                NB = min(0.272*R + 0.534*G + 0.131*B,255)
                canvas.set_at((x,y),(int(NR),int(NG),int(NB)))
            
def greyscale():
    for x in range(int(width*0.1875),int(width*0.1875)+int(width-width*0.25)):
        for y in range(int(height*(1/6)),int(height*(1/6))+int(height-height*(1/3))):
            r,g,b,a=screen.get_at((x,y))
            na=(0.3 * b) + (0.59 * g) + (0.11 * b)
            screen.set_at((x,y),(int(na),int(na),int(na)))
            R,G,B,A=canvas.get_at((x,y))
            if (R,G,B,A)!=(0,0,0,0):
                NA=(0.3 * B) + (0.59 * G) + (0.11 * B)
                canvas.set_at((x,y),(int(NA),int(NA),int(NA)))

filterS=filterFont.render("Sepia",True,BLACK)
sepiaRect=Rect(int(height*(5/96)*2)+4,0,filterS.get_width(),int(height*(5/96)))


filterGs=filterFont.render("Grey Scale",True,BLACK)
gsRect=Rect(int(height*(5/96)*2)+6+filterS.get_width(),0,filterGs.get_width(),int(height*(5/96)))

setBGRect=Rect(width-(int(height*(5/96))*2)-2,int(height*(5/96))+2,int(height*(5/96))*2,int(height*(5/96)))

shuffle=False
shufflePic=transform.scale(shufflePic,(int(height*(5/96)),int(height*(5/96))))
shuffleRect=Rect(int(height*(5/96)*2)+8+filterS.get_width()+filterGs.get_width(),0,int(height*(5/96)),int(height*(5/96)))



beforePic=transform.scale(beforePic,(int(height*(5/96)),int(height*(5/96))))
beforeRect=Rect(int(height*(5/96)*2)+10+filterS.get_width()+filterGs.get_width()+int(height*(5/96)),0,int(height*(5/96)),int(height*(5/96)))

playRect=Rect(int(height*(5/96)*2)+12+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*2,0,int(height*(5/96)),int(height*(5/96)))

nextRect=Rect(int(height*(5/96)*2)+14+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*3,0,int(height*(5/96)),int(height*(5/96)))

c=Surface((int(width-width*0.25),int(height-height*(1/3))),SRCALPHA).convert_alpha()
c.fill(WHITE)

moveRect=Rect(int(height*(5/96)*2)+19+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4,int(height*(5/96))//2-int(height*(8/1080))//2,int(height*(150/1080)),int(height*(8/1080)))
sliderRect=Rect(int(height*(5/96)*2)+19+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))//2-int(height*(10/1080))//2,int(height*(4/1080)),int(height*(10/1080)),int(height*(5/96))-int(height*(4/1080)))
timeRect=Rect(int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080)),int(height*(5/96))//2-int(height*(8/1080))//2,int(height*(150/1080)),int(height*(8/1080)))
hahaRect=Rect(int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))-int(height*(10/1080))//2,int(height*(14/1080)),int(height*(10/1080)),int(height*(5/96))-int(height*(25/1080)))



setBG=filterFont.render("BG",True,BLACK)

play=True

undo=[canvas]
cundo=[c]
redo=[]
credo=[]

firstss=False
first=False
start=False


sliding=False


before=[0]
ns=[]

songTime=[127,245,65,155,158,157,326,270,101,148,157,172,150,106,68,268,176,83,129,103,165,77,147,122,104,180,315,195,193,240,193,140,193,194]


thickC=0
thickL=1
thickB=1
thickE=1
thickR=0
thickHL=20
thickSpray=int(height*(25/1080))

ts=0

adding=[(1,0),(-1,0),(0,-1),(0,1)]

polying=False

cleanOnce=False



firstPoint=False
secPoint=False
angPoint=False
checkAngle=False


stickerUsing=[(image.load("sticker/"+str(i)+".png")) for i in range(1,13)]

stickerPics=[(ratioScaling(stickerUsing[i],int(1/12*height),int(1/12*height))) for i in range(len(stickerUsing))]

stickerRects=[(Rect(int(width*0.1875)+int((120/1920*width)*i),int(height*(1/6))+int(height-height*(1/3))+int(height*45/1080),int(1/12*height),int(1/12*height))) for i in range(len(stickerPics))]

bgUsing=[(image.load("bg/"+str(i)+".png")) for i in range(1,7)]
bgPics=[(transform.scale(bgUsing[i],(int((width-width*0.25)*0.14),int((height-height*(1/3))*0.14)))) for i in range(len(bgUsing))]
bgRects=[(Rect(int(width*0.1875)+int((247/1920*width)*i),int(height*5/96)+int(height*15/1080),int((width-width*0.25)*0.14),int((height-height*(1/3))*0.14))) for i in range(len(bgPics))]

writing=False
can=False

cCrop=False

crosshair=False


transb=Surface((int(1/15*height),int(1/15*height)),SRCALPHA)
transb.fill((193,230,223,100))


while running:



    screen.fill(WHITE)
    screen.blit(background,(0,0))
    draw.rect(screen,((0,0,0,0)),canvasRect)
    screen.blit(cundo[-1],(int(width*0.1875),int(height*(1/6))))
    
    if firstss==False:
        screen.blit(undo[-1],(0,0))
    else:
        screen.blit(canvas,(0,0))

        



    if timeSlider==False:
        hahaRect.x=int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))-int(height*(10/1080))//2+int(mixer.music.get_pos()/1000/songTime[before[-1]%34]*height*(150/1080))+ts


    draw.rect(screen,col,ccRect)
    draw.rect(screen,(255,255,255,255),colourPickerRect)
    screen.blit(colourPicker,(3,height-int(width*(270/1920))-3))

    for tRect in tRects:
        screen.blit(transb,tRect)
    
    screen.blit(pencilPic,(int(1/40*width+2),int(1/6*height+2)))
    screen.blit(eraserPic,(int(7/80*width+2),int(1/6*height+2)))
    screen.blit(brushPic,(int(1/40*width+2),int(1/4*height+2)))
    draw.rect(screen,(255,255,255,255),shadeRect)
    screen.blit(shade,(int(width*(270/1920))+3,height-int(width*(270/1920))-3))

    if crosshair==True:
        draw.line(screen,(66,245,221),(chx-5,chy),(chx-2,chy),1)
        draw.line(screen,(66,245,221),(chx+5,chy),(chx+2,chy),1)
        draw.line(screen,(66,245,221),(chx,chy-5),(chx,chy-2),1)
        draw.line(screen,(66,245,221),(chx,chy+5),(chx,chy+2),1)

    screen.blit(openPic,(width-int(height*(5/96))*2-1,1))
    screen.blit(savePic,(width-int(height*(5/96))+1,1))
    screen.blit(redoPic,(int(height*(5/96)+3),1))
    screen.blit(undoPic,(1,1))
    draw.rect(screen,GREY,openRect,2)
    draw.rect(screen,GREY,saveRect,2)
    draw.rect(screen,GREY,undoRect,2)
    draw.rect(screen,GREY,redoRect,2)
    screen.blit(filterS,(int(height*(5/96)*2)+4,0))
    draw.rect(screen,GREY,sepiaRect,2)
    screen.blit(filterGs,(int(height*(5/96)*2)+6+filterS.get_width(),0))
    draw.rect(screen,GREY,gsRect,2)
    screen.blit(shufflePic,(int(height*(5/96)*2)+8+filterS.get_width()+filterGs.get_width(),0))
    draw.rect(screen,GREY,shuffleRect,2)
    screen.blit(beforePic,(int(height*(5/96)*2)+10+filterS.get_width()+filterGs.get_width()+int(height*(5/96)),0))
    draw.rect(screen,GREY,beforeRect,2)
    draw.rect(screen,GREY,setBGRect,2)
    screen.blit(setBG,((width-(int(height*(5/96))*2)-2)+int(height*(5/96))-setBG.get_width()//2,int(height*(5/96))))
    




    if play==True:
        screen.blit(pausePic,(int(height*(5/96)*2)+12+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*2,0))
    elif play==False:
        screen.blit(playPic,(int(height*(5/96)*2)+12+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*2,0))

    draw.rect(screen,GREY,playRect,2)

    screen.blit(nextPic,(int(height*(5/96)*2)+14+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*3,0))
    draw.rect(screen,GREY,nextRect,2)
    draw.rect(screen,GREY,moveRect)
    draw.rect(screen,BLACK,sliderRect)
    draw.rect(screen,GREY,rectRect,2)
    screen.blit(rectPic,(int(178/1920*width),int(280/1080*height)))
    screen.blit(circlePic,(int(1/40*width),int(1/3*height)))
    screen.blit(linePic,(int(7/80*width),int(1/3*height)))
    screen.blit(hlPic,(int(1/40*width),int(5/12*height)))



    draw.rect(screen,GREY,timeRect)
    draw.rect(screen,BLACK,hahaRect)
    songName=musicFont.render("OWL OST "+str(before[-1]%34+1),True,(76,221,237),(252,171,104))
    screen.blit(songName,(0,int(height*5/96)))
    hehe=int((hahaRect.x-(int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))-int(height*(10/1080))//2))/int(height*(150/1080))*songTime[before[-1]%34])
    songDuration=musicFont.render("   {:02d}:{:02d}/{:02d}:{:02d}".format(hehe//60,hehe%60,songTime[before[-1]%34]//60,songTime[before[-1]%34]%60),True,(76,221,237),(252,171,104))
    screen.blit(songDuration,(songName.get_width(),int(height*5/96)))

    if tool=="pro":
        if checkAngle==False:
            angle=musicFont.render("None",True,(76,221,237),(252,171,104))
            screen.blit(angle,(0,int(height*5/96+songName.get_height())))
        else:
            angle=musicFont.render(str(abs(degree)),True,(76,221,237),(252,171,104))
            screen.blit(angle,(0,int(height*5/96+songName.get_height())))

##    for stRect in stickerRects:
##        draw.rect(screen,(194,240,220),stRect)

    screen.blit(sprayPic,(int(7/80*width),int(5/12*height)))
    screen.blit(bucketPic,(int(1/40*width),int(1/2*height)))
    screen.blit(polyPic,(int(7/80*width),int(1/2*height)))
    screen.blit(edPic,(int(1/40*width),int(7/12*height)))
    screen.blit(tbPic,(int(7/80*width),int(7/12*height)))
    screen.blit(cropPic,(int(1/40*width),int(2/3*height)))
    screen.blit(proPic,(int(7/80*width),int(2/3*height)))



    for i in range(len(stickerPics)):
        screen.blit(stickerPics[i],((int(width*0.1875)+int((120/1920*width)*i))+int(1/12*height)//2-stickerPics[i].get_width()//2,(int(height*(1/6))+int(height-height*(1/3))+int(height*45/1080))+int(1/12*height)//2-stickerPics[i].get_height()//2))

    for i in range(len(bgPics)):
        screen.blit(bgPics[i],(int(width*0.1875)+int((247/1920*width)*i),int(height*5/96)+int(height*15/1080)))

    if writing==True:
        
        firstss=True
        canvas.fill((0,0,0,0))
        canvas.blit(undo[-1],(0,0))
        txt=txtF.render(ntxt,True,col)
        canvas.blit(txt,(startx,starty))

    

    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:

                if canvasRect.collidepoint(mx,my):
                    if tool!="bucket" and tool!="poly" and tool!="ed" and tool!="tb" and tool!="crop" and tool!="pro":
                        start=True
                    if tool=="rect" or tool=="circle" or tool=="line" or tool[:7]=="sticker" or tool=="tb" or tool=="crop":
                        sx,sy=mx,my

                for i in range(len(bgRects)):
                    if bgRects[i].collidepoint(mx,my) and writing==False and checkAngle==False:
                        nBG=transform.scale(bgUsing[i],(int(width-width*0.25),int(height-height*(1/3))))
                        cundo.append(nBG.copy())
                        canvas.fill((0,0,0,0))
                        undo.append(canvas.copy())




                if tool=="bucket" and canvasRect.collidepoint(mx,my):
                    if screen.get_at((mx,my))!=col:
                        oldC=screen.get_at((mx,my))
                        bucketS=Surface((width,height),SRCALPHA).convert_alpha()
                        bucketS.fill((0,0,0,0))
                        bucketS.blit(screen.subsurface(canvasRect).copy(),(int(width*0.1875),int(height*(1/6))))
                        pos=[(mx,my)]
                        while len(pos)!=0:
                            cpos=pos.pop()
                            for add in adding:
                                npos=(cpos[0]+add[0],cpos[1]+add[1])
                                if int(width*0.1875)<=npos[0]<=int(width*0.1875)+int(width-width*0.25) and int(height*(1/6))<=npos[1]<=int(height*(1/6))+int(height-height*(1/3)):
                                    if bucketS.get_at(npos)==oldC:
                                        bucketS.set_at(npos,col)
                                        pos.append(npos)
                        canvas.fill((0,0,0,0))
                        canvas.blit(bucketS,(0,0))
                        cundo.append(cundo[-1].copy())
                        undo.append(canvas.copy())

                                
                if writing==False and checkAngle==False:
                    if pencilRect.collidepoint(mx,my):
                        tool="pencil"
                    if eraserRect.collidepoint(mx,my):
                        tool="eraser"
                    if brushRect.collidepoint(mx,my):
                        tool="brush"
                    if rectRect.collidepoint(mx,my):
                        tool="rect"
                    if circleRect.collidepoint(mx,my):
                        tool="circle"
                    if lineRect.collidepoint(mx,my):
                        tool="line"
                    if hlRect.collidepoint(mx,my):
                        tool="highlighter"
                    if sprayRect.collidepoint(mx,my):
                        tool="spray"
                    if bucketRect.collidepoint(mx,my):
                        tool="bucket"
                    if polyRect.collidepoint(mx,my):
                        tool="poly"
                    if eyeDropperRect.collidepoint(mx,my):
                        tool="ed"
                    if tbRect.collidepoint(mx,my):
                        tool="tb"
                    if cropRect.collidepoint(mx,my):
                        tool="crop"
                    if proRect.collidepoint(mx,my):
                        tool="pro"
                    for i in range(len(stickerRects)):
                        if stickerRects[i].collidepoint(mx,my):
                            tool="sticker "+str(i)
                
                if colourPickerRect.collidepoint(mx,my):
                    getColour=True

                if tool=="pro" and canvasRect.collidepoint(mx,my):
                    if firstPoint==False:
                        fpx,fpy=mx,my
                        firstPoint=True
                    elif secPoint==False:
                        firstss=True
                        spx,spy=mx,my
                        draw.line(canvas,col,(fpx,fpy),(spx,spy),2)
                        secPoint=True
                        angless=canvas.copy()
                    elif firstPoint and secPoint:
                        canvas.fill((0,0,0,0))
                        canvas.blit(angless,(0,0))
                        apx,apy=mx,my
                        draw.line(canvas,col,(fpx,fpy),(apx,apy),2)
                        distX1=apx-fpx
                        distY1=apy-fpy
                        degree1=round(math.degrees(math.atan2(distY1,distX1)))
                        distX2=spx-fpx
                        distY2=spy-fpy
                        degree2=round(math.degrees(math.atan2(distY2,distX2)))
                        degree=degree1-degree2
                        checkAngle=True
                        
                if tool=="poly" and canvasRect.collidepoint(mx,my):
                    firstss=True
                    if polying==False:
                        saved=canvas.copy()
                        savedB=cundo[-1].copy()
                        polying=True
                        poly=[(mx,my)]
                    elif polying==True:
                        poly.append((mx,my))
                        for i in range(len(poly)-1):
                            draw.line(canvas,col,poly[i],poly[i+1],3)
                            
                if hahaRect.collidepoint(mx,my):
                    timeSlider=True
                    if play==True:
                        play=False
                        alreadyPaused=False
                    else:
                        alreadyPaused=True
                    ov=mixer.music.get_volume()
                    mixer.music.set_volume(0)
    
                if sepiaRect.collidepoint(mx,my) and writing==False and checkAngle==False:
                    sepia()
                    undo.append(canvas.copy())
                    cundo.append(screen.subsurface(canvasRect).copy())
                if gsRect.collidepoint(mx,my) and writing==False and checkAngle==False:
                    greyscale()
                    undo.append(canvas.copy())
                    cundo.append(screen.subsurface(canvasRect).copy())
                if undoRect.collidepoint(mx,my) and writing==False and checkAngle==False:
                    if len(undo)>1:
                        credo.append(cundo[-1])
                        del cundo[-1]
                        screen.blit(cundo[-1],(int(width*0.1875),int(height*(1/6))))
                        
                        redo.append(undo[-1])
                        del undo[-1]
                        canvas.fill((0,0,0,0))
                        canvas.blit(undo[-1],(0,0))
                    else:
                        draw.rect(screen,RED,undoRect,2)
                        
                if redoRect.collidepoint(mx,my) and writing==False and checkAngle==False:
                    if len(redo)>0:
                        screen.blit(credo[-1],(int(width*0.1875),int(height*(1/6))))
                        cundo.append(credo[-1])
                        del credo[-1]
                        canvas.fill((0,0,0,0))
                        canvas.blit(redo[-1],(0,0))
                        undo.append(redo[-1])
                        del redo[-1]
                        
                if openRect.collidepoint(mx,my) and writing==False and checkAngle==False:
                    try:
                        fname=filedialog.askopenfilename()
                        myPic=image.load(fname)
                        myPic=transform.scale(myPic,(int(width-width*0.25),int(height-height*(1/3))))
                        canvas.blit(myPic,(int(width*0.1875),int(height*(1/6))))
                        undo.append(canvas.copy())
                        cundo.append(cundo[-1])
                    except:
                        print("Load error")
                if saveRect.collidepoint(mx,my) and writing==False and checkAngle==False:
                    try:
                        fname=filedialog.asksaveasfilename(defaultextension=".png")
                        image.save(screen.subsurface(canvasRect).copy(),fname)
                    except:
                        print("Saving error")
                if setBGRect.collidepoint(mx,my)and writing==False and checkAngle==False:
                    try:
                        fname=filedialog.askopenfilename()
                        myPic=image.load(fname)
                        myPic=transform.scale(myPic,(int(width-width*0.25),int(height-height*(1/3))))
                        cundo.append(myPic.copy())
                        canvas.fill((0,0,0,0))
                        undo.append(canvas.copy())
                    except:
                        print("Load error") 
                if shuffleRect.collidepoint(mx,my):
                    if shuffle==False:
                        shuffle=True
                        before=[before[-1]]
                        ns.clear()
                    elif shuffle==True:
                        shuffle=False
                        before=[before[-1]]
                        ns.clear()
                if playRect.collidepoint(mx,my):
                    if play==True:
                        mixer.music.pause()
                        play=False
                    elif play==False:
                        mixer.music.unpause()
                        play=True

                if nextRect.collidepoint(mx,my):
                    play=True
                    if shuffle==True:
                        if len(ns)==0:
                            rand=0
                            while True:
                                rand=randint(0,33)
                                if rand!=before[-1]:
                                    break
                            before.append(rand)
                            mixer.music.load(musicList[rand])
                            mixer.music.play()
                            ts=0
                        else:
                            before.append(ns[-1])
                            del ns[-1]
                            mixer.music.load(musicList[before[-1]])
                            mixer.music.play()
                            ts=0
                    if shuffle==False:
                        before.append(before[-1]+1)
                        mixer.music.load(musicList[before[-1]%34])
                        mixer.music.play()
                        ts=0


                if beforeRect.collidepoint(mx,my):
                    play=True
                    if shuffle==True:
                        if len(before)==1:
                            ns.append(before[-1])
                            del before[-1]
                            rand=randint(0,33)
                            before.append(rand)
                            mixer.music.load(musicList[rand])
                            mixer.music.play()
                            ts=0
                        else:
                            ns.append(before[-1])
                            del before[-1]
                            mixer.music.load(musicList[before[-1]])
                            mixer.music.play()
                            ts=0
                    if shuffle==False:
                        before.append(before[-1]-1)
                        mixer.music.load(musicList[before[-1]%34])
                        mixer.music.play()
                        ts=0
                        
                if sliderRect.collidepoint(mx,my):
                    sliding=True

            if evt.button==2:
                if polying==True:
                    poly.append(poly[-1])
                    draw.polygon(canvas,col,poly)
                    cundo.append(cundo[-1].copy())
                    undo.append(canvas.copy())
                    polying=False
                if tool[:7]=="sticker":
                    stickerUsing[int(tool[7:])]=transform.flip(stickerUsing[int(tool[7:])],1,0)

                
            if evt.button==3:
                if setBGRect.collidepoint(mx,my):
                    cundo.append(cundo[-1].copy())
                    cundo[-1].fill(col)
                    canvas.fill((0,0,0,0))
                    undo.append(canvas.copy())
                if eraserRect.collidepoint(mx,my):
                    cundo.append(cundo[-1].copy())
                    canvas.fill((0,0,0,0))
                    undo.append(canvas.copy())

                if polying==True:
                    poly.append(poly[-1])
                    draw.polygon(canvas,col,poly,3)
                    cundo.append(cundo[-1].copy())
                    undo.append(canvas.copy())
                    polying=False
                if tool=="crop":
                    sx,sy=mx,my
                if tool=="pro" and checkAngle==True:
                    canvas.fill((0,0,0,0))
                    canvas.blit(undo[-1],(0,0))
                    firstPoint=False
                    secPoint=False
                    checkAngle=False
                    firstss=False
            
            if evt.button==4:
                if tool=="brush" and thickB<int(height*(50/1080)):
                    if keys[K_LSHIFT] and thickB+5<int(height*(50/1080)):
                        thickB+=5
                    else:
                        thickB+=1
                if tool=="eraser" and thickE<int(height*(50/1080)):
                    if keys[K_LSHIFT] and thickE+5<int(height*(50/1080)):
                        thickE+=5
                    else:
                        thickE+=1
                if tool=="rect" and thickR<int(height*(200/1080)):
                    if keys[K_LSHIFT] and thickR+5<int(height*(200/1080)):
                        thickR+=5
                    else:
                        thickR+=1
                if tool=="circle" and thickC<int(height*(200/1080)):
                    if keys[K_LSHIFT] and thickC+5<int(height*(200/1080)):
                        thickC+=5
                    else:
                        thickC+=1
                if tool=="line" and thickL<int(height*(100/1080)):
                    if keys[K_LSHIFT] and thickL+5<int(height*(100/1080)):
                        thickL+=5
                    else:
                        thickL+=1
                if tool=="highlighter" and thickHL<int(height*(50/1080)):
                    if keys[K_LSHIFT] and thickHL+5<int(height*(50/1080)):
                        thickHL+=5
                    else:
                        thickHL+=1
                if tool=="spray" and thickSpray<int(height*(50/1080)):
                    if keys[K_LSHIFT] and thickSpray+5<int(height*(50/1080)):
                        thickSpray+=5
                    else:
                        thickSpray+=1
                if tool[:7]=="sticker":
                    stickerUsing[int(tool[7:])]=transform.rotate(stickerUsing[int(tool[7:])],90)
                    
            if evt.button==5:
                if tool=="brush" and thickB>1:
                    if keys[K_LSHIFT] and thickB-5>1:
                        thickB-=5
                    else:
                        thickB-=1
                if tool=="eraser" and thickE>1:
                    if keys[K_LSHIFT] and thickE-5>1:
                        thickE-=5
                    else:
                        thickE-=1
                if tool=="rect" and thickR>0:
                    if keys[K_LSHIFT] and thickR-5>0:
                        thickR-=5
                    else:
                        thickR-=1
                if tool=="circle" and thickC>0:
                    if keys[K_LSHIFT] and thickC-5>0:
                        thickC-=5
                    else:
                        thickC-=1
                if tool=="line" and thickL>1:
                    if keys[K_LSHIFT] and thickL-5>1:
                        thickL-=5
                    else:
                        thickL-=1
                if tool=="highlighter" and thickHL>1:
                    if keys[K_LSHIFT] and thickHL-5>1:
                        thickHL-=5
                    else:
                        thickHL-=1
                if tool=="spray" and thickSpray>1:
                    if keys[K_LSHIFT] and thickSpray-5>1:
                        thickSpray-=5
                    else:
                        thickSpray-=1
                if tool[:7]=="sticker":
                    stickerUsing[int(tool[7:])]=transform.rotate(stickerUsing[int(tool[7:])],-90)
                    
        if evt.type==MOUSEBUTTONUP:
            if evt.button==1:
                if start:
                    if len(undo)==1:
                        if tool!="eraser":
                            cundo.append(cundo[-1])
                            undo.append(canvas.copy())

                            start=False
                            firstss=False
                    else:
                        cundo.append(cundo[-1])
                        undo.append(canvas.copy())
                        start=False
                        firstss=False
                if getColour:
                    getColour=False
                    
                if sliding:
                    sliding=False
                    
                if writing==False and tool=="tb" and can==True:
                    canvas.fill((0,0,0,0))
                    canvas.blit(undo[-1],(0,0))
                    writing=True
                    cant=True
                    ntxt=""

                    th=abs(sy-my)
                    txtF=font.SysFont("comicsansms",int(th*0.71))
                    if mx-sx>0 and my-sy>0:
                        startx=sx
                        starty=sy
                    elif mx-sx<0 and my-sy<0:
                        startx=mx
                        starty=my
                    elif mx-sx<0 and my-sy>0:
                        startx=mx
                        starty=sy
                    elif mx-sx>0 and my-sy<0:
                        startx=sx
                        starty=my



                    if mx<int(width*0.1875):
                        if mx-sx<0 and my-sy<0:
                            startx=int(width*0.1875)
                        elif mx-sx<0 and my-sy>0:
                            startx=int(width*0.1875)
                        

                        
                    if my>int(height*(1/6))+int(height-height*(1/3)):
                        th=abs(sy-(int(height*(1/6))+int(height-height*(1/3))))
                    elif my<int(height*(1/6)):
                        if mx-sx<0 and my-sy<0:
                            starty=int(height*(1/6))
                        elif mx-sx>0 and my-sy<0:
                            starty=int(height*(1/6))
                        th=abs(sy-int(height*(1/6)))
                    else:
                        th=abs(sy-my)
                        
                if tool=="crop" and cCrop==True:
                    canvas.fill((0,0,0,0))
                    canvas.blit(undo[-1],(0,0))
                    cCrop=False


                    
                    if mx-sx>0 and my-sy>0:
                        stx=sx
                        sty=sy
                    elif mx-sx<0 and my-sy<0:
                        stx=mx
                        sty=my
                    elif mx-sx<0 and my-sy>0:
                        stx=mx
                        sty=sy
                    elif mx-sx>0 and my-sy<0:
                        stx=sx
                        sty=my

                    
                    if mx>int(width*0.1875)+int(width-width*0.25):
                        cropW=abs(sx-(int(width*0.1875)+int(width-width*0.25)))
                    elif mx<int(width*0.1875):
                        if mx-sx<0 and my-sy<0:
                            stx=int(width*0.1875)
                        elif mx-sx<0 and my-sy>0:
                            stx=int(width*0.1875)
                        cropW=abs(sx-int(width*0.1875))
                    else:
                        cropW=abs(sx-mx)

                    if my>int(height*(1/6))+int(height-height*(1/3)):
                        cropH=abs(sy-(int(height*(1/6))+int(height-height*(1/3))))
                    elif my<int(height*(1/6)):
                        if mx-sx<0 and my-sy<0:
                            sty=int(height*(1/6))
                        elif mx-sx>0 and my-sy<0:
                            sty=int(height*(1/6))
                        cropH=abs(sy-int(height*(1/6)))
                    else:
                        cropH=abs(sy-my)

                        
                    nBackg=cundo[-1].subsurface((stx-int(width*0.1875),sty-int(height*(1/6)),cropW,cropH)).copy()
                    cundo.append(transform.scale(nBackg,(int(width-width*0.25),int(height-height*(1/3)))))


                    nCanvas=undo[-1].subsurface((stx,sty,cropW,cropH)).copy()
                    nCanvas=transform.scale(nCanvas,(int(width-width*0.25),int(height-height*(1/3))))
                    
                    nSurf=Surface((width,height),SRCALPHA)
                    nSurf.fill((0,0,0,0))
                    
                    nSurf.blit(nCanvas,(int(width*0.1875),int(height*(1/6))))
                    undo.append(nSurf.copy())
                    canvas.fill((0,0,0,0))
                    canvas.blit(undo[-1],(0,0))

                
                if cleanOnce:
                    cleanOnce=False
                
                if timeSlider:
                    timeSlider=False
                    if alreadyPaused==False:
                        play=True
                    mixer.music.set_volume(ov)
                    ts+=hahaRect.x-(int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))-int(height*(10/1080))//2+int(mixer.music.get_pos()/1000/songTime[before[-1]%34]*height*(150/1080))+ts)


            if evt.button==3:
                if tool=="crop" and cCrop==True:
                    canvas.fill((0,0,0,0))
                    canvas.blit(undo[-1],(0,0))
                    cCrop=False
                    
                    nSurf=Surface((width,height),SRCALPHA)
                    nSurf.fill((0,0,0,0))
                    
                    if mx>sx and my>sy:
                        stx=sx
                        sty=sy 
                    elif mx<sx and my<sy:
                        stx=sx-rectW
                        sty=sy-rectH
                    elif mx<sx and my>sy:
                        stx=sx-rectW
                        sty=sy
                    elif mx>sx and my<sy:
                        stx=sx
                        sty=sy-rectH

                    
                    nBackg=cundo[-1].subsurface((stx-int(width*0.1875),sty-int(height*(1/6)),int(rectW),int(rectH))).copy()

                    cundo.append(transform.scale(nBackg,(int(width-width*0.25),int(height-height*(1/3)))))
                    
                    nCanvas=undo[-1].subsurface((stx,sty,int(rectW),int(rectH))).copy()
                    nCanvas=transform.scale(nCanvas,(int(width-width*0.25),int(height-height*(1/3))))
                    nSurf.blit(nCanvas,(int(width*0.1875),int(height*(1/6))))
                    undo.append(nSurf.copy())
                    
                    canvas.fill((0,0,0,0))
                    canvas.blit(undo[-1],(0,0))

        if evt.type==KEYDOWN:
            if writing==True:
                if evt.key==K_RETURN:
                    writing=False
                    can=False
                    firstss=False
                    cundo.append(cundo[-1].copy())
                    undo.append(canvas.copy())
                    
                elif evt.key==K_BACKSPACE:
                    if len(ntxt)>0:
                        ntxt=ntxt[:-1]
                else:
                    if txt.get_width()+startx<int(width*0.1875)+int(width-width*0.25)-th*0.5:
                        ntxt+=evt.unicode
            
        
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    keys=key.get_pressed()

    if keys[K_ESCAPE]:
        running=False


    if mixer.music.get_busy()==False:
        if shuffle==False:
            before.append(before[-1]+1)
            mixer.music.load(musicList[before[-1]%34])
            mixer.music.play()
            ts=0
        elif shuffle==True:
            if len(ns)==0:
                rand=0
                while True:
                    rand=randint(0,33)
                    if rand!=before[-1]:
                        break
                before.append(rand)
                mixer.music.load(musicList[rand])
                mixer.music.play()
                ts=0
            else:
                before.append(ns[-1])
                del ns[-1]
                mixer.music.load(musicList[before[-1]])
                mixer.music.play()
                ts=0

    if colourPickerRect.collidepoint(mx,my) and getColour==True:
        col=screen.get_at((mx,my))
        chx=mx
        chy=my
        crosshair=True
        draw.line(screen,(66,245,221),(chx-5,chy),(chx-2,chy),1)
        draw.line(screen,(66,245,221),(chx+5,chy),(chx+2,chy),1)
        draw.line(screen,(66,245,221),(chx,chy-5),(chx,chy-2),1)
        draw.line(screen,(66,245,221),(chx,chy+5),(chx,chy+2),1)
    
    if shadeRect.collidepoint(mx,my) and getColour==True:
        col=screen.get_at((mx,my))
        chx=mx
        chy=my
        crosshair=True
        draw.line(screen,(66,245,221),(chx-5,chy),(chx-2,chy),1)
        draw.line(screen,(66,245,221),(chx+5,chy),(chx+2,chy),1)
        draw.line(screen,(66,245,221),(chx,chy-5),(chx,chy-2),1)
        draw.line(screen,(66,245,221),(chx,chy+5),(chx,chy+2),1)


    if tool!="pencil":
        draw.rect(screen,GREY,pencilRect,2)
    else:
        draw.rect(screen,GREEN,pencilRect,2)
    if tool!="eraser":
        draw.rect(screen,GREY,eraserRect,2)
    else:
        draw.rect(screen,GREEN,eraserRect,2)
    if tool!="brush":
        draw.rect(screen,GREY,brushRect,2)
    else:
        draw.rect(screen,GREEN,brushRect,2)
    if tool!="rect":
        draw.rect(screen,GREY,rectRect,2)
    else:
        draw.rect(screen,GREEN,rectRect,2)
    if tool!="circle":
        draw.rect(screen,GREY,circleRect,2)
    else:
        draw.rect(screen,GREEN,circleRect,2)

    if tool!="line":
        draw.rect(screen,GREY,lineRect,2)
    else:
        draw.rect(screen,GREEN,lineRect,2)
        
    if tool!="highlighter":
        draw.rect(screen,GREY,hlRect,2)
    else:
        draw.rect(screen,GREEN,hlRect,2)

    if tool!="spray":
        draw.rect(screen,GREY,sprayRect,2)
    else:
        draw.rect(screen,GREEN,sprayRect,2)

    if tool!="bucket":
        draw.rect(screen,GREY,bucketRect,2)
    else:
        draw.rect(screen,GREEN,bucketRect,2)

    if tool!="poly":
        draw.rect(screen,GREY,polyRect,2)
    else:
        draw.rect(screen,GREEN,polyRect,2)

    if tool!="ed":
        draw.rect(screen,GREY,eyeDropperRect,2)
    else:
        draw.rect(screen,GREEN,eyeDropperRect,2)

    if tool!="tb":
        draw.rect(screen,GREY,tbRect,2)
    else:
        draw.rect(screen,GREEN,tbRect,2)

    if tool!="crop":
        draw.rect(screen,GREY,cropRect,2)
    else:
        draw.rect(screen,GREEN,cropRect,2)

    if tool!="pro":
        draw.rect(screen,GREY,proRect,2)
    else:
        draw.rect(screen,GREEN,proRect,2)

    for i in range(len(stickerRects)):
        if tool!="sticker "+str(i):
            draw.rect(screen,GREY,stickerRects[i],2)
        else:
            draw.rect(screen,GREEN,stickerRects[i],2)


    #Hovering
    if pencilRect.collidepoint(mx,my) and tool!="pencil":
        draw.rect(screen,RED,pencilRect,2)
    if eraserRect.collidepoint(mx,my) and tool!="eraser":
        draw.rect(screen,RED,eraserRect,2)
    if brushRect.collidepoint(mx,my) and tool!="brush":
        draw.rect(screen,RED,brushRect,2)
    if rectRect.collidepoint(mx,my) and tool!="rect":
        draw.rect(screen,RED,rectRect,2)
    if circleRect.collidepoint(mx,my) and tool!="circle":
        draw.rect(screen,RED,circleRect,2)
    if lineRect.collidepoint(mx,my) and tool!="line":
        draw.rect(screen,RED,lineRect,2)
    if hlRect.collidepoint(mx,my) and tool!="highlighter":
        draw.rect(screen,RED,hlRect,2)
    if sprayRect.collidepoint(mx,my) and tool!="spray":
        draw.rect(screen,RED,sprayRect,2)
    if bucketRect.collidepoint(mx,my) and tool!="bucket":
        draw.rect(screen,RED,bucketRect,2)
    if polyRect.collidepoint(mx,my) and tool!="poly":
        draw.rect(screen,RED,polyRect,2)
    if eyeDropperRect.collidepoint(mx,my) and tool!="ed":
        draw.rect(screen,RED,eyeDropperRect,2)
    if tbRect.collidepoint(mx,my) and tool!="tb":
        draw.rect(screen,RED,tbRect,2)
    if cropRect.collidepoint(mx,my) and tool!="crop":
        draw.rect(screen,RED,cropRect,2)
    if proRect.collidepoint(mx,my) and tool!="pro":
        draw.rect(screen,RED,proRect,2)
    

    for i in range(len(stickerRects)):
        if stickerRects[i].collidepoint(mx,my) and tool!="sticker "+str(i):
            draw.rect(screen,RED,stickerRects[i],2)


    for i in range(len(bgRects)):
        if bgRects[i].collidepoint(mx,my):
            draw.rect(screen,YELLOW,bgRects[i],2)
            if mb[0]==1:
                draw.rect(screen,GREEN,bgRects[i],2)
        else:
            draw.rect(screen,GREY,bgRects[i],2)


    if undoRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,undoRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,undoRect,2)
    else:
        draw.rect(screen,GREY,undoRect,2)


    if sepiaRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,sepiaRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,sepiaRect,2)
    else:
        draw.rect(screen,GREY,sepiaRect,2)



    if gsRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,gsRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,gsRect,2)
    else:
        draw.rect(screen,GREY,gsRect,2)


    
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,redoRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,redoRect,2)
    else:
        draw.rect(screen,GREY,redoRect,2)

    if saveRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,saveRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,saveRect,2)
    else:
        draw.rect(screen,GREY,saveRect,2)

    if openRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,openRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,openRect,2)
    else:
        draw.rect(screen,GREY,openRect,2)

    if setBGRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,setBGRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,setBGRect,2)
        if mb[2]==1:
            draw.rect(screen,BLUE,setBGRect,2)
    else:
        draw.rect(screen,GREY,setBGRect,2)

    if shuffle==True:
        draw.rect(screen,GREEN,shuffleRect,2)

    if shuffle==False:
        draw.rect(screen,RED,shuffleRect,2)


    if beforeRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,beforeRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,beforeRect,2)
    else:
        draw.rect(screen,GREY,beforeRect,2)



    if playRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,playRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,playRect,2)
    else:
        draw.rect(screen,GREY,playRect,2)

    if nextRect.collidepoint(mx,my):
        draw.rect(screen,YELLOW,nextRect,2)
        if mb[0]==1:
            draw.rect(screen,GREEN,nextRect,2)
    else:
        draw.rect(screen,GREY,nextRect,2)

###########################################################

    if canvasRect.collidepoint(mx,my):
        if mb[0]==1:
            canvas.set_clip(canvasRect)
            if tool=="pencil":
                firstss=True
                draw.line(canvas,col,(omx,omy),(mx,my))
            if tool=="eraser":
                firstss=True
                eraser()
            if tool=="brush":
                firstss=True
                brush()
            if tool=="highlighter":
                firstss=True
                highlighter()
            if tool=="spray":
                firstss=True
                sprayCan()


            if tool=="rect":
                firstss=True
                canvas.fill((0,0,0,0))
                canvas.blit(undo[-1],(0,0))

                if keys[K_LSHIFT]:
                    squareS=min(abs(mx-sx),abs(my-sy))
                    if mx>sx and my>sy:
                        draw.rect(canvas,col,(sx,sy,int(squareS),int(squareS)),thickR)
                        if thickR>0:
                            draw.rect(canvas,col,(int(sx+squareS-thickR/2),int(sy+squareS-thickR/2),thickR,thickR))
                            draw.rect(canvas,col,(int(sx-thickR/2)+1,int(sy-thickR/2)+1,thickR,thickR))
                            draw.rect(canvas,col,(int(sx+squareS-thickR/2),int(sy-thickR/2)+1,thickR,thickR))
                            draw.rect(canvas,col,(int(sx-thickR/2)+1,int(sy+squareS-thickR/2),thickR,thickR))
                    elif mx<sx and my<sy:
                        draw.rect(canvas,col,(sx,sy,int(-squareS),int(-squareS)),thickR)
                        if thickR>0:
                            draw.rect(canvas,col,(int(sx-squareS-thickR/2),int(sy-squareS-thickR/2),thickR,thickR))
                            draw.rect(canvas,col,(int(sx-thickR/2)+1,int(sy-thickR/2)+1,thickR,thickR))
                            draw.rect(canvas,col,(int(sx-squareS-thickR/2),int(sy-thickR/2)+1,thickR,thickR))
                            draw.rect(canvas,col,(int(sx-thickR/2)+1,int(sy-squareS-thickR/2),thickR,thickR))
                    elif mx<sx and my>sy:
                        draw.rect(canvas,col,(sx,sy,int(-squareS),int(squareS)),thickR)
                        if thickR>0:
                            draw.rect(canvas,col,(int(sx-squareS-thickR/2),int(sy+squareS-thickR/2),thickR,thickR))
                            draw.rect(canvas,col,(int(sx-thickR/2)+1,int(sy-thickR/2)+1,thickR,thickR))
                            draw.rect(canvas,col,(int(sx-squareS-thickR/2),int(sy-thickR/2)+1,thickR,thickR))
                            draw.rect(canvas,col,(int(sx-thickR/2)+1,int(sy+squareS-thickR/2),thickR,thickR))
                    elif mx>sx and my<sy:
                        draw.rect(canvas,col,(sx,sy,int(squareS),int(-squareS)),thickR)
                        if thickR>0:
                            draw.rect(canvas,col,(int(sx+squareS-thickR/2),int(sy-squareS-thickR/2),thickR,thickR))
                            draw.rect(canvas,col,(int(sx-thickR/2)+1,int(sy-thickR/2)+1,thickR,thickR))
                            draw.rect(canvas,col,(int(sx+squareS-thickR/2),int(sy-thickR/2)+1,thickR,thickR))
                            draw.rect(canvas,col,(int(sx-thickR/2)+1,int(sy-squareS-thickR/2),thickR,thickR))

                else:
                    draw.rect(canvas,col,(sx,sy,mx-sx,my-sy),thickR)
                    if thickR>0:
                        draw.rect(canvas,col,(int(mx-thickR/2),int(my-thickR/2),thickR,thickR))
                        draw.rect(canvas,col,(int(sx-thickR/2)+1,int(sy-thickR/2)+1,thickR,thickR))
                        draw.rect(canvas,col,(int(mx-thickR/2),int(sy-thickR/2)+1,thickR,thickR))
                        draw.rect(canvas,col,(int(sx-thickR/2)+1,int(my-thickR/2),thickR,thickR))


            if tool=="tb" and writing==False:
                firstss=True
                can=True
                canvas.fill((0,0,0,0))
                canvas.blit(undo[-1],(0,0))
                draw.rect(canvas,col,(sx,sy,mx-sx,my-sy),1)
  
                
            if tool[:7]=="sticker":
                firstss=True
                canvas.fill((0,0,0,0))
                canvas.blit(undo[-1],(0,0))
                
                if keys[K_LSHIFT]:
                    if mx>sx and my>sy:
                        nSticker=ratioScaling(stickerUsing[int(tool[7:])],abs(mx-sx),abs(my-sy))
                        canvas.blit(nSticker,(sx,sy))
                    elif mx<sx and my<sy:
                        nSticker=ratioScaling(stickerUsing[int(tool[7:])],abs(mx-sx),abs(my-sy))
                        canvas.blit(nSticker,(sx-nSticker.get_width(),sy-nSticker.get_height()))

                    elif mx<sx and my>sy:
                        nSticker=ratioScaling(stickerUsing[int(tool[7:])],abs(sx-mx),abs(my-sy))
                        canvas.blit(nSticker,(sx-nSticker.get_width(),sy))

                    elif mx>sx and my<sy:
                        nSticker=ratioScaling(stickerUsing[int(tool[7:])],abs(sx-mx),abs(my-sy))
                        canvas.blit(nSticker,(sx,sy-nSticker.get_height()))

                else:
                    if mx>sx and my>sy:
                        canvas.blit(transform.scale(stickerUsing[int(tool[7:])],(abs(mx-sx),abs(my-sy))),(sx,sy))
                    elif mx<sx and my<sy:
                        canvas.blit(transform.scale(stickerUsing[int(tool[7:])],(abs(mx-sx),abs(my-sy))),(mx,my))

                    elif mx<sx and my>sy:
                        canvas.blit(transform.scale(stickerUsing[int(tool[7:])],(abs(sx-mx),abs(my-sy))),(mx,sy))

                    elif mx>sx and my<sy:
                        canvas.blit(transform.scale(stickerUsing[int(tool[7:])],(abs(sx-mx),abs(my-sy))),(sx,my))
                        
         


            if tool=="circle":
                firstss=True
                canvas.fill((0,0,0,0))
                canvas.blit(undo[-1],(0,0))
                
                if keys[K_LSHIFT]:
                    try:
                        squareS=min(abs(mx-sx),abs(my-sy))
                        if mx>sx and my>sy:
                            circleR=Rect(sx,sy,int(squareS),int(squareS))
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx+1,sy,int(squareS),int(squareS))
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx,sy+1,int(squareS),int(squareS))
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx-1,sy,int(squareS),int(squareS))
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx,sy-1,int(squareS),int(squareS))
                            draw.ellipse(canvas,col,circleR,thickC)
                        elif mx<sx and my<sy:
                            circleR=Rect(sx,sy,int(-squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx+1,sy,int(-squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx,sy+1,int(-squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx-1,sy,int(-squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx,sy-1,int(-squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                        elif mx<sx and my>sy:
                            circleR=Rect(sx,sy,int(-squareS),int(squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx+1,sy,int(-squareS),int(squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx,sy+1,int(-squareS),int(squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx-1,sy,int(-squareS),int(squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx,sy-1,int(-squareS),int(squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                        elif mx>sx and my<sy:
                            circleR=Rect(sx,sy,int(squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx+1,sy,int(squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx,sy+1,int(squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx-1,sy,int(squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            circleR=Rect(sx,sy-1,int(squareS),int(-squareS)); circleR.normalize();
                            draw.ellipse(canvas,col,circleR,thickC)
                            
                    except:
                        pass

                elif keys[K_LCTRL]:
                    cdistX=mx-sx
                    cdistY=my-sy
                    Rad=math.hypot(cdistY,cdistX)
                    try:
                        draw.circle(canvas,col,(sx,sy),int(Rad),thickC)
                    except:
                        pass
                    
                else:  
                    try:
                        circleR=Rect(sx,sy,mx-sx,my-sy); circleR.normalize();
                        draw.ellipse(canvas,col,circleR,thickC)
                        circleR=Rect(sx+1,sy,mx-sx,my-sy); circleR.normalize();
                        draw.ellipse(canvas,col,circleR,thickC)
                        circleR=Rect(sx-1,sy,mx-sx,my-sy); circleR.normalize();
                        draw.ellipse(canvas,col,circleR,thickC)
                        circleR=Rect(sx,sy+1,mx-sx,my-sy); circleR.normalize();
                        draw.ellipse(canvas,col,circleR,thickC)
                        circleR=Rect(sx,sy-1,mx-sx,my-sy); circleR.normalize();
                        draw.ellipse(canvas,col,circleR,thickC)
                    except:
                        pass

            if tool=="line":
                firstss=True
                canvas.fill((0,0,0,0))
                canvas.blit(undo[-1],(0,0))
                draw.line(canvas,col,(sx,sy),(mx,my),thickL)

            if tool=="crop":
                firstss=True
                cCrop=True
                canvas.fill((0,0,0,0))
                canvas.blit(undo[-1],(0,0))
                draw.rect(canvas,col,(sx,sy,mx-sx,my-sy),1)
                

            
            if tool=="ed":
                if crosshair!=False:
                    crosshair=False
                col=screen.get_at((mx,my))

            canvas.set_clip(None)

            
        if tool=="crop" and mb[2]==1:
            canvas.set_clip(canvasRect)
            firstss=True
            cCrop=True
            canvas.fill((0,0,0,0))
            canvas.blit(undo[-1],(0,0))


            rto=width/height
            if mx>int(width*0.1875)+int(width-width*0.25):
                rw=abs(sx-(int(width*0.1875)+int(width-width*0.25)))
            elif mx<int(width*0.1875):
                rw=abs(sx-int(width*0.1875))
            else:
                rw=abs(sx-mx)

            if my>int(height*(1/6))+int(height-height*(1/3)):
                rh=abs(sy-(int(height*(1/6))+int(height-height*(1/3))))
            elif my<int(height*(1/6)):
                rh=abs(sy-int(height*(1/6)))
            else:
                rh=abs(sy-my)

            if width>height:
                rto=rw/width
                rectH=rto*height
                if rectH>rh:
                    rto=rh/height
                    rectW=rto*width
                    rectH=rh
                else:
                    rectW=rw
            else:
                rto=rh/height
                rectW=rto*width
                if rectW>rw:
                    rto=rw/width
                    rectW=rw
                    rectH=rto*height
                else:
                    rectH=rh

            if mx>sx and my>sy:
                draw.rect(canvas,BLACK,(sx,sy,int(rectW),int(rectH)),1)
            elif mx<sx and my<sy:
                draw.rect(canvas,BLACK,(sx-rectW,sy-rectH,int(rectW),int(rectH)),1)
            elif mx<sx and my>sy:
                draw.rect(canvas,BLACK,(sx-rectW,sy,int(rectW),int(rectH)),1)
            elif mx>sx and my<sy:
                draw.rect(canvas,BLACK,(sx,sy-rectH,int(rectW),int(rectH)),1)
                
            canvas.set_clip(None)

            
        if tool=="eraser" and mb[0]==0:
            if cleanOnce==False:
                cleanOnce=True
            firstss=True
            screen.set_clip(canvasRect)
            canvas.fill((0,0,0,0))
            canvas.blit(undo[-1],(0,0))
            draw.circle(canvas,(0,0,0,0),(mx,my),thickE)
            screen.set_clip(None)
        if tool=="brush" and mb[0]==0:
            screen.set_clip(canvasRect)
            draw.circle(screen,col,(mx,my),thickB)
            screen.set_clip(None)
        if tool=="highlighter" and mb[0]==0:
            screen.set_clip(canvasRect)
            draw.circle(hl,(col[0],col[1],col[2],4),(int(height*(25/1080)),int(height*(25/1080))),thickHL)
            screen.blit(hl,(mx-int(height*(25/1080)),my-int(height*(25/1080))))
            hl.fill((0,0,0,0))
            screen.set_clip(None)
        if tool[:7]=="sticker" and mb[0]==0:
            screen.set_clip(canvasRect)
            demo=ratioScaling(stickerUsing[int(tool[7:])],1/15*height,1/15*height)
            screen.blit(demo,(mx-demo.get_width()//2,my-demo.get_height()//2))
            screen.set_clip(None)
        if tool=="ed" and mb[0]==0:
            screen.set_clip(canvasRect)
            draw.line(screen,(66,245,221),(mx-5,my),(mx-2,my),1)
            draw.line(screen,(66,245,221),(mx+5,my),(mx+2,my),1)
            draw.line(screen,(66,245,221),(mx,my-5),(mx,my-2),1)
            draw.line(screen,(66,245,221),(mx,my+5),(mx,my+2),1)
            screen.set_clip(None)
        if tool=="spray" and mb[0]==0:
            screen.set_clip(canvasRect)
            draw.circle(screen,col,(mx,my),thickSpray,1)
            screen.set_clip(None)
        

    if sliding==True:
        if mx>int(height*(5/96)*2)+19+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080)):
            sliderRect.x=int(height*(5/96)*2)+19+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))-int(height*(10/1080)//2)
            mixer.music.set_volume(1)

        elif mx<int(height*(5/96)*2)+19+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4:
            sliderRect.x=int(height*(5/96)*2)+19+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4-int(height*(10/1080))//2
            mixer.music.set_volume(0)

        else:
            sliderRect.x=mx-int(height*(10/1080))//2
            mixer.music.set_volume((mx-(int(height*(5/96)*2)+19+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4))/int(height*(150/1080)))

    if timeSlider==True:
        if mx>int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))*2:
            hahaRect.x=int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))*2-int(height*(10/1080)//2)
            mixer.music.rewind()
            mixer.music.set_pos(songTime[before[-1]%34]-1)
        elif mx<int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080)):
            hahaRect.x=int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))-int(height*(10/1080)//2)
            mixer.music.rewind()
            
        else:
            hahaRect.x=mx-int(height*(10/1080))//2
            perc=(mx-(int(height*(5/96)*2)+30+filterS.get_width()+filterGs.get_width()+int(height*(5/96))*4+int(height*(150/1080))))/int(height*(150/1080))
            mixer.music.rewind()
            mixer.music.set_pos(int(songTime[before[-1]%34]*perc))

    if cleanOnce and canvasRect.collidepoint(mx,my)==False:
        if mb[0]==1:
            temp=canvas.copy()
            canvas.fill((0,0,0,0))
            canvas.blit(temp,(0,0))
        else:
            canvas.fill((0,0,0,0))
            canvas.blit(undo[-1],(0,0))
            
    display.flip()
    omx,omy=mx,my
    fps.tick(300)
quit()
