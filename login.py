from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import ast
import subprocess
import sqlite3
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

        # connect to the users database
    conn = sqlite3.connect('users.db')

    # query the database for the provided username and password
    cursor = conn.execute(f"SELECT username, password FROM users WHERE username='{username}' AND password='{Password}'")
    result = cursor.fetchone()

    # close the database connection
    conn.close()

    # check if the query returned a result
    if result:
        # destroy the root window
        root.destroy()

        # launch the index.py file
        subprocess.call(["python", "index.py"])

    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

       
#liason sign up -signin 
def sign_up_command():
    window=Toplevel(root)
    window.title("Elite SIGN UP")
    window.geometry('925x500+300+200')
    window.config(bg='#fff')
    window.resizable(False,False)

#Sign Up Function 

    conn = sqlite3.connect('users.db')

    def sign_up():
        username=user.get()
        password=code.get()
        confirmP=confirm_code.get()

        if password == confirmP:
            try:
                # create the users table if it doesn't exist
                conn.execute('''CREATE TABLE IF NOT EXISTS users
                                 (username TEXT PRIMARY KEY,
                                  password TEXT);''')
            # insert the user information into the users table
                conn.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
                conn.commit()

                messagebox.showinfo('sign_up', 'Successfully Signed Up')
                window.destroy()

            except Exception as e:
                print(e)
                messagebox.showerror('Error', 'Failed to Sign Up')

        else:
            messagebox.showerror('Error', 'Passwords do not match')




#sign destroy
    def sign(): 
        window.destroy()
#navbar
    navbar1 = Frame(window, bg="#57a1f8", height=50, width=root.winfo_width())
    navbar1.pack(side=TOP, fill=X)

    app_name1 = Label(navbar1, text="Elite", font=('Comic Sans MS', 20, 'bold'), fg='white', bg='#57a1f8')
    app_name1.pack(side=LEFT, padx=(10, 0), pady=5)

    page_name1 = Label(navbar1, text="Client Page", font=("Times", "17", "bold italic") , fg='black', bg='#57a1f8')
    page_name1.pack(side=LEFT, padx=(10, 0), pady=5, expand=True)
    page_name1.place(relx=0.5, rely=0.5, anchor=CENTER)


    nav_button1 = Menubutton(navbar1, text='☰', compound=LEFT, font=("bold", 20), fg='white', bg='#57a1f8', bd=0, activebackground='#57a1f8')
    nav_button1.pack(side=RIGHT, padx=(0, 10), pady=5)


    nav_menu1 = Menu(nav_button1, tearoff=0, bg="#57a1f8", fg="black", font=("Calibri(Body)", 15))
    nav_button1.config(menu=nav_menu1)

    def open_About1():
      os.system("python about.py")

    def open_contact1():
      os.system("python contact.py")

    def open_home1():
      os.system("python menu.py")


    nav_menu1.add_command(label='Home', font=("Calibri(Body)", 15), command=open_home1)
    nav_menu1.add_command(label='Contact', font=("Calibri(Body)", 15), command=open_contact1)
    nav_menu1.add_command(label='About', font=("Calibri(Body)", 15), command=open_About1)
    


#image
    img = PhotoImage(file='image/sign_up.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=120)


#signUp frame
    My_frame=Frame(window,width=350,height=390,bg="white")
    My_frame.place(x=480,y=80)

    heading=Label(My_frame,text="Sign Up",fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)

#UserName
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        if user.get() =='' :
            user.insert(0,'UserName') 

    user = Entry(My_frame,width=25,fg="black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(My_frame,width=295,height=2,bg='black').place(x=25,y=107)

#Password
    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        if code.get() =='' :
            code.insert(0,'Password') 

    code = Entry(My_frame,width=25,fg="black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Username')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>',on_leave)

    Frame(My_frame,width=295,height=2,bg='black').place(x=25,y=177)

#confirmation PSWD
    def on_enter(e):
        confirm_code.delete(0,'end')

    def on_leave(e):
        if confirm_code.get() =='' :
            confirm_code.insert(0,'Password Confirmation ') 

    confirm_code = Entry(My_frame,width=25,fg="black",border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0,'Password Confirmation')
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>',on_leave)

    Frame(My_frame,width=295,height=2,bg='black').place(x=25,y=247)

    my_label3 = Label(window, text="© CarHire 2023", fg='black', bg='white', font=('Comic Sans MS',11))
    my_label3.place(x=400,y=470)



#Button 
    Button(My_frame,width=39,pady=7,text="Sign Up",bg='#57a1f8',fg='white',border=0,command=sign_up).place(x=35,y=280)
    label1 =Label(My_frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=90,y=340)

    signin=Button(My_frame,width=6,text='Sign In',border=0,bg='white',cursor='hand2',fg="#57a1f8",command=sign)
    signin.place(x=200,y=340)




    window.mainloop()



##################################################

# Navbar
navbar = Frame(root, bg="#57a1f8", height=50, width=root.winfo_width())
navbar.pack(side=TOP, fill=X)

app_name = Label(navbar, text="Elite", font=('Comic Sans MS', 20, 'bold'), fg='white', bg='#57a1f8')
app_name.pack(side=LEFT, padx=(10, 0), pady=5)

page_name = Label(navbar, text="Client Page", font=("Times", "17", "bold italic") , fg='black', bg='#57a1f8')
page_name.pack(side=LEFT, padx=(10, 0), pady=5, expand=True)
page_name.place(relx=0.5, rely=0.5, anchor=CENTER)


nav_button = Menubutton(navbar, text='☰', compound=LEFT, font=("bold", 20), fg='white', bg='#57a1f8', bd=0, activebackground='#57a1f8')
nav_button.pack(side=RIGHT, padx=(0, 10), pady=5)


nav_menu = Menu(nav_button, tearoff=0, bg="#57a1f8", fg="black", font=("Calibri(Body)", 15))
nav_button.config(menu=nav_menu)


def open_About2():
    os.system("python about.py")

def open_contact2():
    os.system("python contact.py")

def open_home2():
    os.system("python menu.py")

nav_menu.add_command(label='Home', font=("Calibri(Body)", 15), command=open_home2)
nav_menu.add_command(label='Contact', font=("Calibri(Body)", 15), command=open_contact2)
nav_menu.add_command(label='About', font=("Calibri(Body)", 15), command=open_About2)

#Image 
img = PhotoImage(file='image/login.png')
Label(root,image=img,bg='white').place(x=50,y=100)


#CopyRight
my_label2 = Label(root, text="© Elite 2023", fg='black', bg='white', font=('Comic Sans MS',11))
my_label2.place(x=400,y=470)


#Frame Signin
My_frame=Frame(root,width=350,height=350,bg="white")
My_frame.place(x=500,y=120)


heading=Label(My_frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
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


#Button
Button(My_frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
my_label=Label(My_frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
my_label.place(x=75,y=270)

sign_up= Button(My_frame,width=6,text='Sign Up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign_up_command)
sign_up.place(x=215,y=270)




root.mainloop() 