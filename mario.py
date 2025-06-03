import tkinter as tk

telaWidth=800
telaHeight=600
tela=tk.Tk()
tela.geometry(f"{telaWidth}x{telaHeight}")
tela.title("Mario")

yvelocity=0
canva = tk.Canvas(tela,width=800,height=600,bg="black")
def gravity(obj):
    global yvelocity
    grav=2
    cordinates = canva.coords(obj)
    if cordinates[3]>telaHeight-tamanho:
        yvelocity=0
        canva.coords(mario,(x/2)-tamanho,y-tamanho,x/2,y)
    else:
        if yvelocity<20 and yvelocity!=0:
            yvelocity+=grav
        canva.move(obj,0,yvelocity)
    canva.after(50,lambda:gravity(mario))
x=telaWidth
y=telaHeight
tamanho=20
def jump(event):
    global yvelocity
    yvelocity=-25   

# mario = canva.create_rectangle((x/2)-tamanho,y-tamanho,x/2,y,fill="red")
mario = canva.create_rectangle((x/2)-tamanho,0,x/2,tamanho,fill="red")
canva.pack()
gravity(mario)
tela.bind("<space>", jump)
tela.mainloop()
