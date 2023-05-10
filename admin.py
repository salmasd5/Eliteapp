from pickle import APPEND
from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter
from time import strftime
import os



sqlite3.connect("Caar.db")
print("database created")
c=sqlite3.connect("Caar.db")
curses=c.cursor() 
curses.execute("CREATE TABLE IF NOT EXISTS Voiture(IMMATRICULATION VARCHAR(20),MARQUE  VARCHAR(20), MODELE VARCHAR(20),CLASSE VARCHAR(20),SERIE VARCHAR(20),COULEUR VARCHAR(20) ,TYPE_CARBURANT VARCHAR(20), NOMBRE_DE_PLACES INTEGER , TRANSMISSION VARCHAR(20), PRIX_LOCATION REAL, DISPONIBILITE VARCHAR(20))")
c.commit()
c.close()
print("table est cree avec succes")


class Voiture:
    def __init__(self, main):
        self.main = main
        self.T_Frame= Frame(self.main, height=50, width=1200, background="#2eb4d9", bd=2)
        self.T_Frame.pack()
        self.Title=Label(self.T_Frame, text ="ELITE:gestion des voitures",foreground="white", font="arial 20 bold", width=1800, bg="#2eb4d9")
        self.Title.pack()

        self.Frame_1=Frame(self.main, height=780, width=400, bd=2, relief=GROOVE, bg="#2eb4d9")
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)


        Label(self.Frame_1, text=" Cars details:",  background="#2eb4d9", font="arial 12 bold").place(x=40, y=20)
        
        self.Im=Label(self.Frame_1, text="Im:", background="#2eb4d9", font="arial 11 bold")
        self.Im.place(x=10,y=50)
        self.Im_Entry=Entry(self.Frame_1, width=40)
        self.Im_Entry.place(x=150, y=50)

        self.Marque=Label(self.Frame_1, text="Marque:", background="#2eb4d9", font="arial 11 bold")
        self.Marque.place(x=10,y=90)
        self.Marque_Entry=Entry(self.Frame_1, width=40)
        self.Marque_Entry.place(x=150, y=90)

        self.Modele=Label(self.Frame_1, text="Modele:", background="#2eb4d9", font="arial 11 bold")
        self.Modele.place(x=10,y=130)
        self.Modele_Entry=Entry(self.Frame_1, width=40)
        self.Modele_Entry.place(x=150, y=130)

        self.Classe=Label(self.Frame_1, text="Classe :", background="#2eb4d9", font="arial 11 bold")
        self.Classe.place(x=10,y=170)
        self.Classe_Entry=Entry(self.Frame_1, width=40)
        self.Classe_Entry.place(x=150, y=170)

        self.Couleur=Label(self.Frame_1, text="Couleur :", background="#2eb4d9", font="arial 11 bold")
        self.Couleur.place(x=10,y=210)
        self.Couleur_Entry=Entry(self.Frame_1, width=40)
        self.Couleur_Entry.place(x=150, y=210)

        self.Serie=Label(self.Frame_1, text="Serie :", background="#2eb4d9", font="arial 11 bold")
        self.Serie.place(x=10,y=250)
        self.Serie_Entry=Entry(self.Frame_1, width=40)
        self.Serie_Entry.place(x=150, y=250)

        self.Typecarb=Label(self.Frame_1, text="Type de carburant:", background="#2eb4d9", font="arial 11 bold")
        self.Typecarb.place(x=10,y=290)
        self.Typecarb_Entry=Entry(self.Frame_1, width=40)
        self.Typecarb_Entry.place(x=150, y=290)

        

        self.Nbplaces=Label(self.Frame_1, text="nombre de places :", background="#2eb4d9", font="arial 11 bold")
        self.Nbplaces.place(x=10,y=330)
        self.Nbplaces_Entry=Entry(self.Frame_1, width=40)
        self.Nbplaces_Entry.place(x=150, y=330)
        
        self.Transmission=Label(self.Frame_1, text="Transmission :", background="#2eb4d9", font="arial 11 bold")
        self.Transmission.place(x=10,y=370)
        self.Transmission_Entry=Entry(self.Frame_1, width=40)
        self.Transmission_Entry.place(x=150, y=370)

        self.Prixloc=Label(self.Frame_1, text="Prix de location :", background="#2eb4d9", font="arial 11 bold")
        self.Prixloc.place(x=10,y=410)
        self.Prixloc_Entry=Entry(self.Frame_1, width=40)
        self.Prixloc_Entry.place(x=150, y=410)

        self.Disponibilite=Label(self.Frame_1, text="Disponibilite :", background="#2eb4d9", font="arial 11 bold")
        self.Disponibilite.place(x=10,y=450)
        self.Disponibilite_Entry=Entry(self.Frame_1, width=40)
        self.Disponibilite_Entry.place(x=150, y=450)

        

        


        

# =========BUTTONS====================
        self.Button_Frame=Frame(self.Frame_1, height=750, width=250, relief=GROOVE, bd=2, background="black")
        self.Button_Frame.place(x=80, y=490)

        self.Add=Button(self.Button_Frame, text="Add", width=25, font="arial 11 bold", command=self.Add)
        self.Add.pack()
        
        self.Delete=Button(self.Button_Frame, text="Delete", width=25, font="arial 11 bold", command=self.Delete)
        self.Delete.pack()
        
        self.Update=Button(self.Button_Frame, text="Update", width=25, font="arial 11 bold", command=self.Update)
        self.Update.pack()
        
        self.Clear=Button(self.Button_Frame, text="Clear", width=25, font="arial 11 bold", command=self.Clear)
        self.Clear.pack()
        
        

        
        self.Frame_2=Frame(self.main, height=1080, width=1000, bd=2, relief=GROOVE, bg="#00BFFF")
        self.Frame_2.pack(side=RIGHT)

        
    

        
        

        self.tree=ttk.Treeview(self.Frame_2, columns=("c1", "c2", "c3", "c4","c5" , "c6","c7","c8", "c9", "c10", "c11"), show='headings', height=25)
        

        

        self.tree.column("#1", anchor=CENTER, width=50)
        self.tree.heading("#1", text="IMMATRICULATION")
        
        self.tree.column("#2", anchor=CENTER, width=80)
        self.tree.heading("#2", text="Marque")
        
        self.tree.column("#3", anchor=CENTER, width=80)
        self.tree.heading("#3", text="Modele")
        
        self.tree.column("#4", anchor=CENTER, width=80)
        self.tree.heading("#4", text="Classe")
        
        self.tree.column("#5", anchor=CENTER, width=105)
        self.tree.heading("#5", text="Couleur")
        
        self.tree.column("#6", anchor=CENTER , width=80 )
        self.tree.heading("#6", text="Serie")

        self.tree.column("#7", anchor=CENTER , width=80)
        self.tree.heading("#7", text="Type de carburant")

        self.tree.column("#8", anchor=CENTER , width=50)
        self.tree.heading("#8", text="Nbr places")

        self.tree.column("#9", anchor=CENTER ,width=80)
        self.tree.heading("#9", text="Transmission")

        self.tree.column("#10", anchor=CENTER, width=50)
        self.tree.heading("#10", text="Prix de location")

        self.tree.column("#11", anchor=CENTER )
        self.tree.heading("#11", text="Disponibilte")

        

      

        
        

        
    

        
        # Affiche le widget Treeview dans la fenêtre Tkinter
        self.tree.pack()
        c=sqlite3.connect("Caar.db")
        curses=c.cursor()
        curses.execute("SELECT * FROM Voiture")

        # Fetch all the rows
        rows = curses.fetchall()

        # Loop over the rows and insert them into the treeview
        for row in rows:
            self.tree.insert("", "end", values=row)

        # Close the cursor and the connection
        curses.close()
        c.close()

    def Add(self):
        im= self.Im_Entry.get()
        marque = self.Marque_Entry.get()
        modele = self.Modele_Entry.get()
        classe = self.Classe_Entry.get()
        couleur = self.Couleur_Entry.get()
        serie = self.Serie_Entry.get()
        typecarb = self.Typecarb_Entry.get()
        nbplaces = self.Nbplaces_Entry.get()
        transmission = self.Transmission_Entry.get()
        prixloc = self.Prixloc_Entry.get()
        disponibilite = self.Disponibilite_Entry.get()

        c=sqlite3.connect("Caar.db")
        curses=c.cursor()
        curses.execute("INSERT INTO  Voiture(IMMATRICULATION, MARQUE, MODELE, CLASSE, COULEUR ,SERIE , TYPE_CARBURANT , NOMBRE_DE_PLACES, TRANSMISSION , PRIX_LOCATION , DISPONIBILITE) VALUES(?,?,?,?,?,?,?,?,?,?,?)", (im,marque ,modele, classe , couleur, serie, typecarb , nbplaces,transmission, prixloc,  disponibilite))
        self.tree.insert("", index=0, values=(im, marque, modele, classe, couleur,serie,typecarb,nbplaces,transmission,prixloc,disponibilite))
        c.commit()
        c.close()
        print("value inserted")
    
    def Delete(self):
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]

        c = sqlite3.connect("Caar.db")
        cursor = c.cursor()

    # Use a parameterized query to delete the selected row
        cursor.execute("DELETE FROM Voiture WHERE IMMATRICULATION=?", (selected_item,))

        print("value deleted")
        c.commit()
        c.close()

        self.tree.delete(item)



    def Update(self):
        im = self.Im_Entry.get()
        marque = self.Marque_Entry.get()
        modele = self.Modele_Entry.get()
        classe = self.Classe_Entry.get()
        couleur = self.Couleur_Entry.get()
        serie = self.Serie_Entry.get()
        typecarb = self.Typecarb_Entry.get()
        nbplaces = self.Nbplaces_Entry.get()
        transmission = self.Transmission_Entry.get()
        prixloc = self.Prixloc_Entry.get()
        disponibilite = self.Disponibilite_Entry.get()
    
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            self.tree.item(item, values=(im, marque, modele,classe,couleur, serie, typecarb,nbplaces,transmission,prixloc,disponibilite))
            selected_item=self.tree.item(item)['values'][0]
            c=sqlite3.connect("Caar.db")
            cursor=c.cursor()
            cursor.execute("UPDATE Voiture SET IMMATRICULATION=?, MARQUE=?, MODELE=?, CLASSE=?, SERIE=?, TYPE_CARBURANT=?, NOMBRE_DE_PLACES=?,TRANSMISSION=?, PRIX_LOCATION=?, DISPONIBILITE=?  WHERE IMMATRICULATION=?", (selected_item ,marque, modele, classe, serie, typecarb,nbplaces , transmission, prixloc,disponibilite, selected_item))
            c.commit()
            c.close()
            print("Values updated")

        

    
    def Clear(self):
        self.Im_Entry.delete(0,END)
        self.Marque_Entry.delete(0,END)
        self.Modele_Entry.delete(0,END)
        self.Classe_Entry.delete(0,END)
        self.Couleur_Entry.delete(0,END)
        self.Serie_Entry.delete(0,END)
        self.Typecarb_Entry.delete(0,END)
        self.Nbplaces_Entry.delete(0,END)
        self.Transmission_Entry.delete(0,END)
        self.Prixloc_Entry.delete(0,END)
        self.Disponibilite_Entry.delete(0,END)
        
    



main =Tk()
main.title("gestion de voiture")
main.resizable(False,False)
main.geometry("1300x700")
Voiture(main)
main.mainloop()


