from tkinter import * 
from PIL import ImageTk, Image 
import os


root=Tk()
root.title('Elite LOGIN')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)


tete_label = Frame(root, bg="#8BD59E")
tete_label.place(x=0,y=00, width=1000, height=70)

my_label = Label(tete_label, text="About Us", bg='#8BD59E',fg="black", font=('Calibri(Body)', 30, 'bold'))
my_label.place(x=360,y=5)

label = Label(root, text="Bienvenue chez Elite, votre solution de location de voiture à Marrakech. Nous proposons une large gamme de voitures, un service clientèle exceptionnel et des services supplémentaires pour rendre votre voyage plus agréable. Réservez dès maintenant votre voiture de location avec CarHire et découvrez tout ce que Marrakech a à offrir.", 
              bg='#fff', font=('Calibri(Body)', 15, 'bold'),wraplength=800)
label.pack(expand=True)
label.place(x=85, y=160)

Bas_label = Frame(root, bg="#8BD59E")
Bas_label.place(x=00,y=390, width=1000, height=200)

frame_image = Frame(root , bg='white') 
frame_image.place(x=10 , y=397, width=100, height=90)
image = Image.open("image/logo.png")
new_size = (300, 300) 
img = image.resize(new_size)
photo = ImageTk.PhotoImage(img)
lbl_image = Label(frame_image, image=photo, bg="#8BD59E")
lbl_image.pack(fill=BOTH, expand=YES, )

def open_contact():
    os.system("python contact.py")
    

btn_contact = Button(root, text='Contact US', font=('times new roman',15 , 'bold'), bg='#8BD59E',fg="white",  activebackground='#8BD59E',command=open_contact)
btn_contact.place(x=750 , y=410, width=150, height=80)


root.mainloop()