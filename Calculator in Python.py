import tkinter
from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.configure(bg="skyblue")
ans=""
def show(val):
    global ans
    ans+=val
    label_result.config(text=ans)
def clear():
    global ans
    ans=""
    label_result.config(text=ans)
def calculate():
    global ans
    answer=""
    if ans!="":
        try:
            answer=eval(ans)
        except:
            answer='please enter vallied sequence'
            ans=''
    label_result.config(text=answer)
    label1.config(text='u got it ')
label_result=Label(root,width=25,height=2,text="",font=("arial",40))
label_result.pack()
label1=Label(root,text="u got the ans",width=10,height=1,font=("arial",20))
Button(root,text='C',width=5,height=1,font=("arial",30,'bold'),command=lambda:clear()).place(x=10,y=120)
Button(root,text='/',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("/")).place(x=150,y=120)
Button(root,text='%',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("%")).place(x=290,y=120)
Button(root,text='*',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("*")).place(x=430,y=120)
#
Button(root,text='7',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("7")).place(x=10,y=220)
Button(root,text='8',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("8")).place(x=150,y=220)
Button(root,text='9',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("9")).place(x=290,y=220)
Button(root,text='-',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("-")).place(x=430,y=220)
####
Button(root,text='4',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("4")).place(x=10,y=320)
Button(root,text='5',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("5")).place(x=150,y=320)
Button(root,text='6',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("6")).place(x=290,y=320)
Button(root,text='+',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("+")).place(x=430,y=320)
#####
Button(root,text='1',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("1")).place(x=10,y=420)
Button(root,text='2',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("2")).place(x=150,y=420)
Button(root,text='3',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("3")).place(x=290,y=420)
Button(root,text='0',width=5,height=1,font=("arial",30,'bold'),command=lambda:show("0")).place(x=430,y=420)
###
Button(root,text='.',width=5,height=1,font=("arial",30,'bold'),command=lambda:show(".")).place(x=10,y=500)
Button(root,text='=',width=5,height=1,font=("arial",30,'bold'),command=lambda:calculate()).place(x=150,y=500)

root.mainloop()
