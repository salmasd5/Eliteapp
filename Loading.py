from tkinter import *
from tkinter import ttk
import os

root = Tk()
image= PhotoImage(file="image/load.png")

height = 430 
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(True)

root.config(background='#57a1f8')

welcome_label = Label(text="Elite APP",bg='#57a1f8',font=('Trebuchet Ms', 30 , 'bold'),fg='#FFFFFF')
welcome_label.place(x=180, y=25)

bg_label = Label(root,image=image,bg='#57a1f8')
bg_label.place(x=130 , y=100)


progress_label = Label(root, text="loading...",font=('Trebuchet Ms', 13 , 'bold'),fg='#FFFFFF',bg='#57a1f8')
progress_label.place(x=190 , y=330)

progress = ttk.Style()
progress.theme_use('clam')
progress.configure('red.Horizontal.TProgressbar',background='#108cff')

progress = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate', style='red.Horizontal.TProgressbar')
progress.place(x=60 , y=370)
 

def top():
    root.withdraw()
    os.system('python menu.py')
    root.destroy()

i = 0 

def load() :
    global i 
    if i <= 10 : 
        txt = 'Loading... ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(600, load)
        progress['value'] = 10*i
        i += 1
    else:
        top()

load()


root.resizable(False,False)
root.mainloop()