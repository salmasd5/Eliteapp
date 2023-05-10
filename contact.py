from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import ast
import os




root=Tk()
root.title('Elite LOGIN')
root.geometry('925x500+300+200')
root.configure(bg='#8BD59E')
root.resizable(False,False)



navbar = Frame(root, bg="#8BD59E", height=50, width=root.winfo_width())
navbar.pack(side=TOP, fill=X)

app_name = Label(navbar, text="Elite", font=('Comic Sans MS', 20, 'bold'), fg='white', bg='#8BD59E')
app_name.pack(side=LEFT, padx=(10, 0), pady=5)

page_name = Label(navbar, text="Our Contact", font=("Times", "17", "bold italic") , fg='black', bg='#8BD59E')
page_name.pack(side=LEFT, padx=(10, 0), pady=5, expand=True)
page_name.place(relx=0.5, rely=0.5, anchor=CENTER)


nav_button = Menubutton(navbar, text='☰', compound=LEFT, font=("bold", 20), fg='white', bg='#8BD59E', bd=0, activebackground='#8BD59E')
nav_button.pack(side=RIGHT, padx=(0, 10), pady=5)


nav_menu = Menu(nav_button, tearoff=0, bg="#8BD59E", fg="black", font=("Calibri(Body)", 15))
nav_button.config(menu=nav_menu)


def open_about():
    os.system("python about.py")

def open_home():
    os.system("python menu.py")


nav_menu.add_command(label='Home', font=("Calibri(Body)", 15), command=open_home)
nav_menu.add_command(label='Contact', font=("Calibri(Body)", 15))
nav_menu.entryconfigure(1, foreground='red') 
nav_menu.add_command(label='About', font=("Calibri(Body)", 15), command=open_about)




###########

zakaria_frame=Frame(root,width=312,height=500,bg="#F4EBD6")
zakaria_frame.place(x=0,y=50)

Z_name = Label(zakaria_frame, text="ZKARIA ZINAOUI", fg='black', bg='#F4EBD6', font=('Verdana',16, "bold"))
Z_name.place(x=50,y=20)

zak_frame=Frame(zakaria_frame,width=130,height=130)
zak_frame.place(x=120,y=75)


image = Image.open("image/admin1.png")


new_size = (90, 90) 
image = image.resize(new_size)

photo = ImageTk.PhotoImage(image)

label_image = Label(zak_frame, image=photo)
label_image.pack()

zakaria_insta_label = Label(zakaria_frame, text="@Zakaria.Zinaoui",font=('Calibri(Body)', 20, 'bold'), bg="#F4EBD6")
zakaria_insta_label.place(x=70,y=213)

insta_icone=PhotoImage(file="image/insta.png")
insta_icone_button = Label(zakaria_frame, image=insta_icone, bg='white', bd=0, highlightbackground='#F4EBD6')
insta_icone_button.place(x=17, y=210)


zakaria_linkendin_label = Label(zakaria_frame, text="/Zakaria Zinaoui",font=('Calibri(Body)', 20, 'bold'), bg="#F4EBD6")
zakaria_linkendin_label.place(x=72,y=290)

linkedin_icone=PhotoImage(file="image/linkedin.png")
linkedin_icone_button = Label(zakaria_frame, image=linkedin_icone, bg='white', bd=0, highlightbackground='#F4EBD6')
linkedin_icone_button.place(x=17, y=283)






###################################""
salma_frame=Frame(root,width=312,height=500,bg="#F4EBD6")
salma_frame.place(x=315,y=50)
S_name = Label(salma_frame, text="Salma Daigham", fg='black', bg='#F4EBD6', font=('Verdana',18, "bold"))
S_name.place(x=50,y=20)

s_frame=Frame(salma_frame,width=130,height=130)
s_frame.place(x=120,y=65)

image1 = Image.open("image/admin.png")

new_size1 = (95, 95) 
image1 = image1.resize(new_size1)

photo1 = ImageTk.PhotoImage(image1)

label_image1 = Label(s_frame, image=photo1)
label_image1.pack()

salma_insta_label = Label(salma_frame, text="@Salma Daigham",font=('Calibri(Body)', 20, 'bold'), bg="#F4EBD6")
salma_insta_label.place(x=70,y=213)

insta1_icone=PhotoImage(file="image/insta.png")
insta1_icone_button = Label(salma_frame, image=insta_icone, bg='white', bd=0, highlightbackground='#F4EBD6')
insta1_icone_button.place(x=17, y=210)


salma_linkendin_label = Label(salma_frame, text="/Salma Daigham",font=('Calibri(Body)', 20, 'bold'), bg="#F4EBD6")
salma_linkendin_label.place(x=72,y=290)

linkedin1_icone=PhotoImage(file="image/linkedin.png")
linkedin1_icone_button = Label(salma_frame, image=linkedin_icone, bg='white', bd=0, highlightbackground='#F4EBD6')
linkedin1_icone_button.place(x=17, y=283)

#####################


imane_frame=Frame(root,width=315,height=500,bg="#F4EBD6")
imane_frame.place(x=630,y=50)
I_name = Label(imane_frame, text="Iman tahiri ", fg='black', bg='#F4EBD6', font=('Verdana',18, "bold"))
I_name.place(x=50,y=20)

i_frame=Frame(imane_frame,width=130,height=130)
i_frame.place(x=120,y=65)

image3 = Image.open("image/admin.png")

new_size3 = (95, 95) 
image3 = image3.resize(new_size3)

photo3 = ImageTk.PhotoImage(image3)

label_image3 = Label(i_frame, image=photo3)
label_image3.pack()

imane_insta_label = Label(imane_frame, text="@Imane Tahiri",font=('Calibri(Body)', 20, 'bold'), bg="#F4EBD6")
imane_insta_label.place(x=70,y=213)

insta2_icone=PhotoImage(file="image/insta.png")
insta2_icone_button = Label(imane_frame, image=insta_icone, bg='white', bd=0, highlightbackground='#F4EBD6')
insta2_icone_button.place(x=17, y=210)


imane_linkendin_label = Label(imane_frame, text="/Imane Tahiri",font=('Calibri(Body)', 20, 'bold'), bg="#F4EBD6")
imane_linkendin_label.place(x=72,y=290)

linkedin2_icone=PhotoImage(file="image/linkedin.png")
linkedin2_icone_button = Label(imane_frame, image=linkedin_icone, bg='white', bd=0, highlightbackground='#F4EBD6')
linkedin2_icone_button.place(x=17, y=283)




root.mainloop() 