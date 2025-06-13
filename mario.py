import tkinter as tk

telaWidth=800
telaHeight=600
tela=tk.Tk()
tela.geometry(f"{telaWidth}x{telaHeight}")
tela.title("Mario")

xvelocity=0
yvelocity=0

x=telaWidth/2
y=telaHeight

aPressed=False
dPressed=False

isOnFloor=False

canva = tk.Canvas(tela,width=telaWidth,height=telaHeight,bg="black")
def gravity(obj):
    global x,xvelocity,yvelocity,isOnFloor
    grav=4
    cordinates = canva.coords(obj)
    if cordinates[3]>telaHeight and not isOnFloor:
        yvelocity=0
        canva.coords(mario,x-tamanho,y-tamanho,x,y)
        isOnFloor=True
    else:
        if yvelocity<20 and not isOnFloor:
            yvelocity+=grav
        x+=xvelocity
        canva.move(obj,xvelocity,yvelocity)
    canva.after(50,lambda:gravity(mario))

tamanho=20
def jump(event):
    global yvelocity, isOnFloor
    if isOnFloor:
        yvelocity=-25   
        isOnFloor=False

def left(event):
    global x,xvelocity,aPressed
    xvelocity=-10
    aPressed=True
def right(event):
    global x,xvelocity,dPressed
    xvelocity=10
    dPressed=True
def on_key_release(event):
    global xvelocity,aPressed,dPressed
    print(event)
    if event.keysym == "a" :
        aPressed=False
    elif event.keysym == "d":
        aPressed=False
    if aPressed and dPressed:
        xvelocity=0
    
# mario = canva.create_rectangle((x/2)-tamanho,y-tamanho,x/2,y,fill="red")
mario = canva.create_rectangle(x-tamanho,0,x,tamanho,fill="red")
block = canva.create_rectangle(600,400,800,400+tamanho,fill="#00F5E6")
canva.pack()
gravity(mario)
tela.bind("<KeyRelease>", on_key_release)
tela.bind("<space>", jump)
tela.bind("<a>", left)
tela.bind("<d>", right)
tela.mainloop()
