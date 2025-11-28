from PIL import Image, ImageDraw
import random 
size = (200,200)

def create(A:int,B:int,nV:int):
    x1 = random.randint(A,B)
    x2 = random.randint(A,B)
    y1 = random.randint(x1,B)
    y2 = random.randint(x2,B)
    if nV == 2 :
        return (x1,x2)
    elif nV == 3 :
        x3 = random.randint(A,B)
        return (x1,x2,x3)
    return (int(x1),int(x2),int(y1),int(y2))

def draw_in_im(im):
    draw = ImageDraw.Draw(im, "RGBA")
    rect = create(0,size[0],4)
    draw.rectangle(rect,create(0,255,4))

for i in range(10):
    im = Image.new("RGB" , size, "white")
    while (random.randint(1,5) != 5) :
        draw_in_im(im)
    im.save("image1"+str(i)+".png")

