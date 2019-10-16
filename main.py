from tkinter import *
from tkinter import messagebox
from random import randrange
from pynput.keyboard import Key, Listener
from PIL import ImageTk

def gquit():
    if(messagebox.askquestion('Exit Hangman','Exit Hangman ?')=='yes'):
        root.destroy()
        
root=Tk()
root.title("Game:HangMan")
root.geometry("750x400+300+100")
canvas = Canvas(width=300,height=300)
canvas.pack(expand = YES, fill = BOTH)
canvas.place(x=420,y=50)

menuBar=Menu(root)
root.config(menu=menuBar)
msgMenu=Menu(menuBar, tearoff=0)  
msgMenu.add_command(label="Exit", command=gquit)  
menuBar.add_cascade(label="Action", menu=msgMenu)

image0 = ImageTk.PhotoImage(file = "begin.png")
image1 = ImageTk.PhotoImage(file = "1.png")
image2 = ImageTk.PhotoImage(file = "2.png")
image3 = ImageTk.PhotoImage(file = "3.png")
image4 = ImageTk.PhotoImage(file = "4.png")
image5 = ImageTk.PhotoImage(file = "5.png")
image6 = ImageTk.PhotoImage(file = "6.png")
image7 = ImageTk.PhotoImage(file = "7.png")
imagelist=[image0,image1,image2,image3,image4,image5,image6,image7]
#---------------------------put your code here-------------------------


life=5
#Game Title Label
L1=Label(root,text="HANGMAN")
L1.pack()
L1.place(x=130,y=15)
L1.config(font=('Comic Sans MS',25,'bold','underline'))

#Blanks
L2=Label(root,text="")
L2.pack()
L2.place(x=15,y=80)
L2.config(font=('',17,'bold'))

#Func to return a random word's index from file
def randind(a):
    try:
        return(randrange(len(a)))
    except ValueError:
        messagebox.showinfo('info','Thats all for now')
        root.destroy()
#guess_letter func to update game after each guess
def guess_letter(ch):
    global userans,qword,miss,life,imgno
    if (ch.isalpha() and (ch not in userans) and (ch not in miss)):
        if ch not in qword:
            miss.append(ch)
            life-=1
            imgno+=1
            canvas.create_image(0, 0, image = imagelist[imgno], anchor = NW)
            if(life==0):
                response=messagebox.askretrycancel('Game Over','you lose')
                if(response):
                    readygame()
                else:
                    root.destroy()
            
        while( ch in qword):
            index=qword.index(ch)
            userans[index]=ch
            qword[index]='%'
            updblank(userans)
            if('_' not in userans):
                messagebox.showinfo('Won','You Guessed all letters correctly')
                readygame()
    else:
        pass
    print("qword=",qword)
    print("userans=",userans)
    print("miss=",miss)
    print("------------")
        

#func. to update blanks
def updblank(L):
    temp=L.copy()
    if(len(L)>15):
        for i in range(15,len(L),15):
            temp.insert(i,'\n')
    ntext=""
    for i in temp:
        ntext+=i+'  '
    L2.config(text=ntext)

#Loading word list
fr=open('wordlist.txt','r')
s=fr.read()
wordlist=s.split('\n')
fr.close()

userans=list()
miss=list()
imgno=0
#function to set staring blanks
def readygame():
    global userans,qword,miss,life,imgno
    life=7
    miss=list()
    userans=list()
    imgno=0
    canvas.create_image(0, 0, image =image0, anchor = NW)
    qword=list(wordlist.pop(randind(wordlist)).upper())
    for i in qword:
        if(i.isalpha()):
            userans.append('_')
        elif(i.isspace()):
            userans.append('-')
        else:
            userans.append(i)
    print(userans)
    updblank(userans)

readygame()
#button command------------------------------
def press(a):
    print(a+' button pressed')
    
#code to handle key press-----------------------------------------------
def keypress(event):
    x = event.char
    guess_letter(x.upper())
root.bind_all('<Key>', keypress)

#-----------------------------------------------------------------------
root.resizable(width=FALSE, height=FALSE)
root.mainloop()
