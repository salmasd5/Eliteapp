import tkinter as tk
import os


root = tk.Tk()
root.geometry("925x500+300+200")
root.title('Elite LOGIN')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)



bg_image = tk.PhotoImage(file="image/back.png")
bg_image = bg_image.subsample(4) 


canvas = tk.Canvas(root, width=500, height=500)
canvas.pack(fill="both", expand=True)


canvas.create_image(0, 0, image=bg_image, anchor="nw")


label = tk.Label(canvas, text="Welcome to Elite car rental", font=("Courier", 30), bg="#947b63", relief="groove")
label.place(relx=0.5, rely=0.3, anchor="center")


def open_client():
    os.system("python login.py")

client_button = tk.Button(canvas, text="Client", font=("Arial", 20), bg="#999790", width=16,command=open_client)
client_button.place(x=334,y=210)
client_button.config(highlightthickness=0, bd=3)


def open_admin():
    os.system("python login1.py")
admin_button = tk.Button(canvas, text="Admin", font=("Arial", 20), bg="#999790",width=16,command=open_admin)
admin_button.place(x=334,y=280)
admin_button.config(highlightthickness=0, bd=3)



root.mainloop()