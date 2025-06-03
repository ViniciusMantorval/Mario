import tkinter as tk

telaWidth=800
telaHeight=600
tela=tk.Tk()
tela.geometry(f"{telaWidth}x{telaHeight}")

canva = tk.Canvas(tela,width=800,height=600,bg="black")
def gravity(obj):
    grav=5
    cordinates = canva.coords(obj)
    if cordinates[3]>=telaHeight-tamanho:
        canva.move(obj,0,telaHeight-tamanho)
    else:
        canva.move(obj,0,grav)
    canva.after(50,lambda:gravity(mario))
x=telaWidth
y=telaHeight
tamanho=20
# mario = canva.create_rectangle((x/2)-tamanho,y-tamanho,x/2,y,fill="red")
mario = canva.create_rectangle((x/2)-tamanho,0,x/2,tamanho,fill="red")
canva.pack()

gravity(mario)
tela.mainloop()