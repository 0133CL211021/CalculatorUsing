import tkinter
from tkinter import*


root = Tk()
root.geometry("570x600+100+200")
root.title("Calculator")
root.resizable(False,False)
root.configure(bg="#17161b")

eqution = ""

def show(value):
    global eqution
    eqution += value
    screen.config(text=eqution)

def clear():
    global eqution
    eqution = ""
    screen.config(text=eqution)

def calculate():
    global eqution
    result = ""
    if eqution != "":
        try:
            result = eval(eqution)
        except:
            result = "error"
            eqution = ""
        screen.config(text=result)

screen = Label(root, width=25,height=2 ,font =("lucida" ,27 , "bold"))
screen.pack()

b = Button(root,text ='c',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
b = Button(root,text ='/',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=150,y=100)
b = Button(root,text ='%',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=290,y=100)
b = Button(root,text ='',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("")).place(x=430,y=100)


b = Button(root,text ='7',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=200)
b = Button(root,text ='8',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=200)
b = Button(root,text ='9',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=290,y=200)
b = Button(root,text ='-',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=430,y=200)


b = Button(root,text ='4',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=10,y=300)
b = Button(root,text ='5',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=300)
b = Button(root,text ='6',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=290,y=300)
b = Button(root,text ='+',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=430,y=300)


b = Button(root,text ='1',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=10,y=400)
b = Button(root,text ='2',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=400)
b = Button(root,text ='3',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=290,y=400)
b = Button(root,text ='0',width=11,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=10,y=500)


b = Button(root,text ='.',width=5,height=1,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=290,y=500)
b = Button(root,text ='=',width=5,height=3,font=("arial" ,30 , "bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda:calculate()).place(x=430,y=400)

root.mainloop()