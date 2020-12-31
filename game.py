import tkinter
from tkinter import*
import random
from tkinter import messagebox

          ## Words

answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]
  ##use randrange function

num =  random.randrange(0, len(words), 1)
         ## reset buttom functionality
def reset():
    global words,answers,num
    num=random.randrange(0,len(words),1)
    lbl.config(text=words[num])
    e.delete(0,END)
## function made
def default():
    global words,answers,num
    lbl.config(text=words[num])

                ### check button functionallity

def check():
    global words,answers,num
    var=e.get()
    if var==answers[num]:
        messagebox.showinfo("Success","This is correct answer")
        reset()
    else:
        messagebox.showerror("Error","This is wrong answer")
        e.delete(0,END)

               



root=tkinter.Tk()
root.geometry("350x400+400+300")
root.title("jumbbled")
root.configure(background="#000000")

                        ##### Label
lbl=Label(root,text="you here",font=("Verdana",18),bg="#000000",fg="#ffffff")
lbl.pack(pady=30)

## Entry box
ans=StringVar()   ## to get data from entry
e=Entry(root,font=("Verdana",20),textvariable=ans)
e.pack()

    ##Buttons
bt=Button(root,text="Check",font=("Comic sans ms",16),width=16,bg="#4C4B4B",fg="#45CE30",relief=GROOVE,command=check)
bt.pack(pady=30)

btreset=Button(root,text="Reset",font=("Comic sans ms",16),width=16,bg="#4C4B4B",fg="#FF362E",relief=GROOVE,command=reset)
btreset.pack()

##call function

default()
root.mainloop()

