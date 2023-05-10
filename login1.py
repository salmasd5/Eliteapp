from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import ast
import os




root=Tk()
root.title('Elite LOGIN')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

#Signin Function : 
def signin():
    username=user.get()
    Password=code.get()
    
    if username=='Elite123' and Password =='Emsi2023' :
        os.system("python admin.py")
        

    elif username!='Elite123' and Password!='Emsi2023' :
        messagebox.showerror('Invalid','Invalid Username and Password')

    elif Password!='Emsi2023' :
        messagebox.showerror('Invalid','Invalid Password')

    elif username!='Elite123'  :
        messagebox.showerror('Invalid','Invalid Username')
        


# Navbar
navbar = Frame(root, bg="#DAAB3A", height=50, width=root.winfo_width())
navbar.pack(side=TOP, fill=X)

app_name = Label(navbar, text="Elite", font=('Comic Sans MS', 20, 'bold'), fg='white', bg='#DAAB3A')
app_name.pack(side=LEFT, padx=(10, 0), pady=5)

page_name = Label(navbar, text="Admin Page", font=("Times", "17", "bold italic") , fg='black', bg='#DAAB3A')
page_name.pack(side=LEFT, padx=(10, 0), pady=5, expand=True)
page_name.place(relx=0.5, rely=0.5, anchor=CENTER)


nav_button = Menubutton(navbar, text='☰', compound=LEFT, font=("bold", 20), fg='white', bg='#DAAB3A', bd=0, activebackground='#DAAB3A')
nav_button.pack(side=RIGHT, padx=(0, 10), pady=5)


nav_menu = Menu(nav_button, tearoff=0, bg="#DAAB3A", fg="black", font=("Calibri(Body)", 15))
nav_button.config(menu=nav_menu)


def open_contact():
    os.system("python conatact.py")

def open_About():
    os.system("python about.py")

def open_menu():
    os.system("python admin.py")


nav_menu.add_command(label='Home', font=("Calibri(Body)", 15), command=open_menu)
nav_menu.add_command(label='Contact', font=("Calibri(Body)", 15), command=open_contact)
nav_menu.add_command(label='About', font=("Calibri(Body)", 15), command=open_About)

#Image 
pil_image = Image.open('image/login1.png')

width = 400
height = 400
pil_image = pil_image.resize((width, height), Image.ANTIALIAS)
img = ImageTk.PhotoImage(pil_image)
label = Label(root, image=img, bg='white')
label.place(x=50, y=60)


#CopyRight
my_label2 = Label(root, text="© Elite 2023", fg='black', bg='white', font=('Comic Sans MS',11))
my_label2.place(x=390,y=470)



#Frame Signin
My_frame=Frame(root,width=350,height=350,bg="white")
My_frame.place(x=510,y=140)


heading=Label(My_frame,text='Sign in',fg='#DAAB3A',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#UserName
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,'UserName')  
 
user = Entry(My_frame,width=25,fg="black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'UserName')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)

Frame(My_frame,width=295,height=2,bg='black').place(x=25,y=107)

user_icone=PhotoImage(file="image/username.png").subsample(2)
user_icone_button = Label(root, image=user_icone, bg='white', bd=0, highlightbackground='white')
user_icone_button.place(x=500, y=223)


#Mot De Pass 
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,'Password') 
code = Entry(My_frame,width=25,fg="black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>',on_leave)

Frame(My_frame,width=295,height=2,bg='black').place(x=25,y=177)

#Hide and Show MDP
button_mode=True

def hide():
    global button_mode

    if button_mode:
        eyeButton.configure(image=closeeye,activebackground="white")
        code.config(show="*")
        button_mode=False

    else:
        eyeButton.config(image=openeye,activebackground='white')
        code.config(show="")
        button_mode=True


openeye=PhotoImage(file="image/eye.png").subsample(2, 2)
closeeye=PhotoImage(file="image/hidden.png").subsample(2, 2)

eyeButton = Button(My_frame, image=openeye,bg='white', bd=0, highlightbackground='white',command=hide)
eyeButton.place(x=300, y=155)

#Password icone
password_icone=PhotoImage(file="image/password.png").subsample(2)
password_icone_button = Label(root, image=password_icone, bg='white', bd=0, highlightbackground='white')
password_icone_button.place(x=500, y=294)



#Button
Button(My_frame,width=39,pady=7,text='Sign In',bg='#DAAB3A',fg='white',border=0,command=signin).place(x=35,y=204)


root.mainloop() 