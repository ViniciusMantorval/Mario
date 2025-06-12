import tkinter as tk

telaWidth=800
telaHeight=600
tela=tk.Tk()
tela.geometry(f"{telaWidth}x{telaHeight}")
tela.title("Mario")

xvelocity=10
yvelocity=0
isOnFloor=False
canva = tk.Canvas(tela,width=telaWidth,height=telaHeight,bg="black")
def gravity(obj):
    global x,xvelocity,yvelocity,isOnFloor
    grav=4
    cordinates = canva.coords(obj)
    if cordinates[3]>telaHeight and not isOnFloor:
        yvelocity=0
        canva.coords(mario,(x/2)-tamanho,y-tamanho,x/2,y)
        isOnFloor=True
    else:
        if yvelocity<20 and not isOnFloor:
            yvelocity+=grav
        canva.move(obj,xvelocity,yvelocity)
    canva.after(50,lambda:gravity(mario))
x=telaWidth
y=telaHeight
tamanho=20
def jump(event):
    global yvelocity, isOnFloor
    yvelocity=-25   
    isOnFloor=False

def left(event):
    global x,xvelocity
    x-=xvelocity
def right(event):
    global x,xvelocity
    x+=xvelocity
# def on_key_release(event):
#     global xvelocity
#     if event.keysym == "a" or event.keysym == "d":
#         xvelocity=0
# mario = canva.create_rectangle((x/2)-tamanho,y-tamanho,x/2,y,fill="red")
mario = canva.create_rectangle((x/2)-tamanho,0,x/2,tamanho,fill="red")
canva.pack()
gravity(mario)
tela.bind("<space>", jump)
tela.bind("<a>", left)
tela.bind("<d>", right)
# tela.bind("<KeyRelease>", on_key_release)
tela.mainloop()
