from tkinter import *
from tkinter import messagebox, ttk 
import tempfile
import random
from time import strftime
from PIL import ImageTk, Image 
import os
import sqlite3



conn = sqlite3.connect('facture.db')
conn.execute('''
    CREATE TABLE IF NOT EXISTS Facture (
        num_facture INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL,
        customer_phone TEXT NOT NULL,
        customer_email TEXT NOT NULL,
        product TEXT NOT NULL,
        Couleur TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        totalNoraml INTEGER NOT NULL,
        Elite INTEGER NOT NULL,
        totalElite INTEGER NOT NULL
    )
''')

conn.commit()
conn.close()
print("table creer")



class LocationVoiture:
    def __init__(self, root):
        self.root = root
        self.root.title("ELite")
        self.root.geometry("1920x1040+0+0")

        icon = PhotoImage(file='image/load.png')
        self.root.iconphoto(True, icon)

        #NAVBAR
        navbar1 = Frame(self.root, bg="#8BD59E", height=50, width=root.winfo_width())
        navbar1.pack(side=TOP, fill=X)

        app_name1 = Label(navbar1, text="Elite", font=('Comic Sans MS', 20, 'bold'), fg='white', bg='#8BD59E')
        app_name1.pack(side=LEFT, padx=(10, 0), pady=5)

        page_name1 = Label(navbar1, text="Client Page", font=("Times", "17", "bold italic") , fg='black', bg='#8BD59E')
        page_name1.pack(side=LEFT, padx=(10, 0), pady=5, expand=True)
        page_name1.place(relx=0.5, rely=0.5, anchor=CENTER)


        nav_button1 = Menubutton(navbar1, text='☰', compound=LEFT, font=("bold", 20), fg='white', bg='#8BD59E', bd=0, activebackground='#8BD59E')
        nav_button1.pack(side=RIGHT, padx=(0, 10), pady=5)


        nav_menu1 = Menu(nav_button1, tearoff=0, bg="#8BD59E", fg="black", font=("Calibri(Body)", 15))
        nav_button1.config(menu=nav_menu1)


        def open_about():
           os.system("python about.py")

        def open_contact():
           os.system("python contact.py")

        def open_home():
           os.system("python menu.py")

        nav_menu1.add_command(label='Home', font=("Calibri(Body)", 15), command=open_home)
        nav_menu1.add_command(label='Contact', font=("Calibri(Body)", 15), command=open_contact)
        nav_menu1.add_command(label='About', font=("Calibri(Body)", 15), command=open_about)
    
        def Heure():
            Heur = strftime("%H:%M:%S")
            LabelHeure.config(text=Heur)
            LabelHeure.after(1000,Heure)


        LabelHeure = Label(navbar1, text='HH:MM:SS', font=('times new roman', 15,"bold"),bg="#8BD59E",fg="white")
        LabelHeure.place(x=1300, y=4 ,width=120,height=45)

        Heure()
 

        #Declaration client Variable
        self.c_nom = StringVar()
        self.c_phon = StringVar()

        self.n_factu = StringVar()
        z = random.randint(1000,9999)
        self.n_factu.set(z)

        self.c_email = StringVar()
        self.rech_factu = StringVar()
        self.produit = StringVar() #quelle voiture 
        self.prix = IntVar()
        self.qte = IntVar()
        self.totalnormal =  StringVar()
        self.elite = StringVar()
        self.totalelite = StringVar()
    


        


        #liste de categorie : Produit Variable 
        self.list_categorie = ["selection", "BMW" , "Mercedes" , "Audi"]
    
        #BMW Serie1
        self.souscategorieBMW = ["BMW Série 1", "BMW Série 2" , "BMW X5"]
        self.BmwSerie1 = ["Noir" , "Blanc" , "Bleu"]
        self.price_Serie1_Noir = 1500 
        self.price_Serie1_blanc = 1500 
        self.price_Serie1_bleu = 1800
        #BMW Serie2
        self.BmwSerie2 = ["Noir" , "Rouge" , "Bleu"]
        self.price_Serie2_Noir = 1500 
        self.price_Serie2_Rouge = 1800
        self.price_Serie2_bleu = 1800
        #BMW BMW X5
        self.BmwX5 = ["Noir" ,"Blanc", "Rouge" ]
        self.price_X5_Noir = 1800 
        self.price_X5_Blanc = 1800
        self.price_X5_Rouge = 2200
        #Mercedes 
        self.souscategorieMerc = ["Cla", "Classe A" , "Classe Cls"] # "Classe G"
        self.MCla = ["Noir" , "Blanc" , "Bleu"]
        self.price_MCla_Noir = 1800 
        self.price_MCla_blanc = 1500 
        self.price_MCla_bleu = 1500
        #MErc Classe A
        self.MClasseA = ["Noir" , "Rouge" , "gris"]
        self.price_MClasseA_Noir = 2200
        self.price_MClasseA_blanc = 2000
        self.price_MClasseA_gris = 2200
        #MErc Classe Cls
        self.MCCls = ["Noir" ,"Blanc", "Gris"]
        self.price_MCCls_Noir = 2300
        self.price_MCCls_Blanc = 2100
        self.price_MCCls_Gris = 2300

        #Audi A1
        self.souscategorieAudi = ["Audi A1", "Audi A7" , "Audi Q3"]
        self.Aa1 = ["Noir" , "Blanc" , "Bleu"]
        self.price_Aa1_Noir = 1500 
        self.price_Aa1_blanc = 1500 
        self.price_Aa1_bleu = 1500
        
        #Audi A7
        self.Aa7 = ["Noir" , "Rouge" , "gris"]
        self.price_Aa7_Noir = 180
        self.price_Aa7_blanc = 1800
        self.price_Aa7_gris = 1900
        # Audi Q3
        self.Aq3 = ["Noir" ,"Blanc","Gris"]
        self.price_Aq3_Noir = 2300
        self.price_Aq3_Blanc = 2100
        self.price_Aq3_Gris = 2200

             




         #Frame pour separer les clients
        Main_Frame = Frame(self.root, bd=2, relief=FLAT,bg='#F4EBD6')
        Main_Frame.place(x=0,y=55,width=1800,height=920)

        #client 
        client_frame = LabelFrame(Main_Frame, text="CLient",font=("times new roman", 15),bg='#F4EBD6')
        client_frame.place(x=10,y=5,width=450,height=150)

        #contact client 
        self.lbl_contact = Label(client_frame, text="contact",font=("times new roman",15,"bold"),bg="#F4EBD6")
        self.lbl_contact.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        
        self.txt_contact = Entry(client_frame,textvariable=self.c_phon, width=25,fg="black",border=1,bg="#F4EBD6",font=('Microsoft YaHei UI Light',11))
        self.txt_contact.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        #nom client 
        self.lbl_nomclient = Label(client_frame, text="Nom Complet",font=("times new roman",15,"bold"),bg="#F4EBD6")
        self.lbl_nomclient.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_nomclient = Entry(client_frame,textvariable=self.c_nom, width=25,fg="black",border=1,bg="#F4EBD6",font=('Microsoft YaHei UI Light',11))
        self.txt_nomclient.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        #Email client 
        self.lbl_Email = Label(client_frame, text="Email",font=("times new roman",15,"bold"),bg="#F4EBD6")
        self.lbl_Email.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        
        self.txt_Email = Entry(client_frame,textvariable=self.c_email, width=25,fg="black",border=1,bg="#F4EBD6",font=('Microsoft YaHei UI Light',11))
        self.txt_Email.grid(row=2, column=1, sticky=W, padx=5, pady=2)


######### PRODUIT 
        produit_frame = LabelFrame(Main_Frame, text="Les Voitures Disponible", font=("times new roman",15),bg="#F4EBD6")
        produit_frame.place(x=500,y=5,width=620,height=150)

        self.lbl_categorie = Label(produit_frame, text="Marque de voiture", font=("times new roman",15,"bold"),bg="#F4EBD6")
        self.lbl_categorie.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.txt_categorie = ttk.Combobox(produit_frame,values=self.list_categorie,font=('Microsoft YaHei UI Light',10),foreground="black",width=17,state="readonly")
        self.txt_categorie.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.txt_categorie.current(0)
        self.txt_categorie.bind("<<ComboboxSelected>>", self.fonctionCategorie)

        self.lbl_souscategorie = Label(produit_frame, text="Le Modele", font=("times new roman",15,"bold"),bg="#F4EBD6")
        self.lbl_souscategorie.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.txt_souscategorie = ttk.Combobox(produit_frame,values=[""],font=('Microsoft YaHei UI Light',10),foreground="black",width=17,state="readonly")
        self.txt_souscategorie.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.txt_souscategorie.current(0)
        self.txt_souscategorie.bind("<<ComboboxSelected>>", self.fonctionsousCategorie)

        self.lbl_couleure = Label(produit_frame, text="la couleure", font=("times new roman",15,"bold"),bg="#F4EBD6")
        self.lbl_couleure.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.txt_couleure = ttk.Combobox(produit_frame ,textvariable=self.produit ,font=('Microsoft YaHei UI Light',10),foreground="black",width=17,state="readonly")
        self.txt_couleure.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.txt_couleure.bind("<<ComboboxSelected>>", self.fonctionCouleure)    

        self.lbl_prix = Label(produit_frame, text="Prix", font=("times new roman",15,"bold"),bg="#F4EBD6")
        self.lbl_prix.grid(row=0, column=2, sticky=W, padx=5, pady=2)
        self.txt_prix = ttk.Combobox(produit_frame, textvariable=self.prix, font=('Microsoft YaHei UI Light',10),foreground="black",width=17,state="readonly")
        self.txt_prix.grid(row=0,column=3,sticky=W,padx=5,pady=2)
           

       #Tkk.Entry style 
        style = ttk.Style()
        style.configure('Custom.TEntry2', borderwidth=2, relief="groove" , background='#8BD59E')
        style.layout("Custom.TEntry2", [
            ("Entry.highlight", {"border": 0}),
            ("Entry.border", {"border": 0, "sticky": "nswe", "children":
                [("Entry.padding", {"sticky": "nswe", "children":
                    [("Entry.textarea", {"sticky": "nswe"})]
                 })]
            })
        ])
        self.lbl_jour = Label(produit_frame, text="Jour", font=("times new roman",15,"bold"),bg="#F4EBD6")
        self.lbl_jour.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        self.txt_jour = ttk.Entry(produit_frame, textvariable=self.qte, font=('Microsoft YaHei UI Light',10),foreground="black",width=19, style='Custom.TEntry2')
        self.txt_jour.grid(row=1,column=3,sticky=W,padx=5,pady=2)


        
        
        ## Recherche Facture
        recher_Frame = Frame(Main_Frame, bd=2 , bg="#F4EBD6")
        recher_Frame.place(x=1130, y=10, width=400, height=70)

        self.lbl_recherche = Label(recher_Frame, text="N° Facture", font=("times new roman",18,'bold'),bg='#F4EBD6')
        self.lbl_recherche.grid(row=0,column=0,sticky=W, padx=5, pady=2)

        self.txt_recherche = ttk.Entry(recher_Frame, textvariable= self.rech_factu, font=("times new roman",15,), width=10, style='Custom.TEntry2')
        self.txt_recherche.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.btn_recherche = Button(recher_Frame, text='Rechercher',command=self.rechercher ,height=1,font=("times new roman",10,),bg="#75BB99",width=9,cursor='hand2')
        self.btn_recherche.grid(row=0 , column=2)

        #Espace Facture 
        facture_label = LabelFrame(Main_Frame, text='Facture',font=("times new roman",15,"bold"), bg="#F4EBD6")
        facture_label.place(x=1130 , y=50, width=390 , height=550)
        #facture scroll
        scroll_y = Scrollbar(facture_label, orient=VERTICAL)
        self.textarea = Text(facture_label,yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"),bg='#75BB99', fg='black')
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        
        #Bas
        enbas_frame = LabelFrame(Main_Frame, text='boutton', font=("times new roman",15),bg="#F4EBD6")
        enbas_frame.place(x=0,y=600,width=1880,height=134)

        self.lbl_totalnormal = Label(enbas_frame, text="Total Brute :",font=('times new roman', 15,"bold"),bg="#F4EBD6")
        self.lbl_totalnormal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.lbl_Elite = Label(enbas_frame, text="Service Elite:",font=('times new roman', 15,"bold"),bg="#F4EBD6")
        self.lbl_Elite.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.lbl_totalElite = Label(enbas_frame, text="Total Elite:",font=('times new roman', 15,"bold"),bg="#F4EBD6")
        self.lbl_totalElite.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txt_totalnormal = ttk.Entry(enbas_frame, textvariable=self.totalnormal, font=('times new roman',15),width=20,state="readonly",style='Custom.TEntry2')
        self.txt_totalnormal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.txt_Elite = ttk.Entry(enbas_frame, textvariable=self.elite, font=('times new roman',15),width=20,state="readonly",style='Custom.TEntry2')
        self.txt_Elite.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.txt_totalElite = ttk.Entry(enbas_frame, textvariable=self.totalelite, font=('times new roman',15),width=20,state="readonly",style='Custom.TEntry2')
        self.txt_totalElite.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        


        #logo 
        frame_image = Frame(Main_Frame , bg='#F4EBD6') 
        frame_image.place(x=0 , y=170, width=1130, height=430)
        self.image = ImageTk.PhotoImage(Image.open("image/logo1.png"))
        self.lbl_image = Label(image = self.image, bg='#F4EBD6')
        lbl_image = Label(frame_image, image=self.image, bg="#F4EBD6")
        lbl_image.pack(fill=BOTH, expand=YES, )

        #CR
        my_label2 = Label(enbas_frame, text="© Elite 2023", fg='black', bg='#F4EBD6', font=('Comic Sans MS',17))
        my_label2.place(x=800,y=70)
    


        #couleur Combobox
        style = ttk.Style()
        style.theme_use('clam')

        style.map("TCombobox", fieldbackground=[("readonly", "#8BD59E")])
        style.configure("TCombobox", backfground="#8BD59E", foreground="black")


        btn_Frame = Frame(enbas_frame, bd=2, bg="#F4EBD6")
        btn_Frame.place(x=450,y=0)

        self.ajoutPanier = Button(produit_frame,command=self.ajouter, text="Ajouter Panier", height=1, font=("times new roman", 11, "bold"),bg="#8BD59E",width=15,cursor='hand2')
        self.ajoutPanier.place(x=450,y=70)

        self.generer = Button(btn_Frame,command=self.genererFacture, text="Génerer", height=1, font=("times new roman", 13, "bold"),bg="#8BD59E",width=15,cursor='hand2')
        self.generer.grid(row=2 , column=1)

        self.sauvegarde = Button(btn_Frame, text="Sauvegarder Facture",command=self.Sauvegarder, height=1, font=("times new roman", 13, "bold"),bg="#8BD59E",width=15,cursor='hand2')
        self.sauvegarde.grid(row=2 , column=2)

        self.email = Button(btn_Frame, text="Bon de reservation",command=self.imprimer, height=1, font=("times new roman", 13, "bold"),bg="#8BD59E",width=15,cursor='hand2')
        self.email.grid(row=2 , column=3)
        
        self.reini = Button(btn_Frame, text="Réinisialiser",command=self.reni, height=1, font=("times new roman", 13, "bold"),bg="#8BD59E",width=15,cursor='hand2')
        self.reini.grid(row=2 , column=4)

        self.quitte = Button(btn_Frame, text="Quitter",command=self.quitter, height=1, font=("times new roman", 13, "bold"),bg="#8BD59E",width=15,cursor='hand2')
        self.quitte.grid(row=2, column=5)


        factureS_label = Label(frame_image, text="Nos Service d'Elite",font=("times new roman",15,"bold"), bg="#8BD59E")
        factureS_label.place(x=900,y=2)
        Service_lbl = Label(frame_image, text="1-Livraison des clés\n2-Maintenance        \n3-Support 24/24     ", font=("times new roman",15),bg="#8BD59E")
        Service_lbl.place(x=900,y=35)


        self.bienvenu()
        self.l = []





      ####### Fonction buttons 

    def bienvenu(self): 
        self.textarea.delete(1.0, END)
        self.textarea.insert(END,"\t Bienvenu Chez Elite ")
        self.textarea.insert(END, f"\n\n Numéro Facture :\t\t {self.n_factu.get()}")
        self.textarea.insert(END, f"\n Nom Client:\t\t {self.c_nom.get()}")
        self.textarea.insert(END, f"\n Numéro Tel :\t\t {self.c_phon.get()}")
        self.textarea.insert(END, f"\n Email :\t {self.c_email.get()}")

        self.textarea.insert(END, "\n************************************")

        self.textarea.insert(END, f"\n Voiture \t\t\tJour\tPrix")

        self.textarea.insert(END, "\n************************************")




    def ajouter(self) : 
        self.n = self.prix.get()
        self.m = self.qte.get() * self.n
        self.l.append(self.m)
        if self.produit.get()== "" :
            messagebox.showerror("Erreur", "Selectionner une voiture")
        else : 
            self.textarea.insert(END, f"\n{self.txt_souscategorie.get()} {self.txt_couleure.get()}\t\t\t{self.qte.get()}\t{self.m}")
            self.totalnormal.set(str('%.1f'%(sum(self.l))))
            self.elite.set(str('%.1f'%200))
            self.totalelite.set(str('%.1f'%(((sum(self.l))+ 200))))



    def genererFacture (self):
        if self.produit.get()=="":
            messagebox.showerror("Erreur" , "Ajouter une voiture")
        else :
            text = self.textarea.get(10.0, (10.0+float(len(self.l))))
            self.bienvenu()
            text = self.textarea.insert(END , text)
            self.textarea.insert(END, "\n************************************") 
            self.textarea.insert(END, f"\nTotal : \t\t\t{self.totalnormal.get()}") 
            self.textarea.insert(END, f"\nElite : \t\t\t{self.elite.get()}") 
            self.textarea.insert(END, f"\nTotal Elite : \t\t\t{self.totalelite.get()}") 

        conn = sqlite3.connect('facture.db')
        conn.execute('''
            INSERT INTO Facture (num_facture, customer_name, customer_phone, customer_email, product, Couleur, quantity, totalNoraml, ELite, totalElite)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.n_factu.get(),  self.c_nom.get(), self.c_phon.get(), self.c_email.get(),self.txt_souscategorie.get() ,self.txt_couleure.get(), self.qte.get(), self.totalnormal.get(), self.elite.get(), self.totalelite.get()))

        conn.commit()
        conn.close()
        

    
 
    def Sauvegarder(self) : 
        op = messagebox.askyesno('Sauvegarde', "Voulez-vous Sauvegarder la facture?")
        if op==True : 
            self.donneFacture = self.textarea.get(1.0, END)
            f1=open("Facture/"+str(self.n_factu.get())+".txt","w")  
            f1.write(self.donneFacture)
            messagebox.showinfo("Sauvegarder", f"La facture numéro{self.n_factu.get()} a été enregistré avac succès")
            f1.close()

            # liaison database

    def imprimer(self): 
        fichier = tempfile.mktemp(".txt")
        open(fichier,"w").write(self.textarea.get("1.0",END))
        os.startfile(fichier, "print")


    def rechercher(self):
        conn = sqlite3.connect('facture.db')
        c = conn.cursor()

        c.execute("SELECT * FROM Facture WHERE num_facture = ?", (self.rech_factu.get(),))
        facture = c.fetchone()

        if facture:
            self.textarea.delete(1.0, END)
            self.textarea.insert(END,"\t Bienvenu Chez Elite\n")
            self.textarea.insert(END, f"\nNumero Facture:\t\t {facture[0]}\n")
            self.textarea.insert(END, f"Nom Client:\t\t {facture[1]}\n")
            self.textarea.insert(END, f"Numero telephone:\t\t {facture[2]}\n")
            self.textarea.insert(END, f"Email:\t {facture[3]}\n")      
            self.textarea.insert(END, "\n************************************")    
            self.textarea.insert(END, f"\n Voiture \t\tJour\tPrix")

            self.textarea.insert(END, "\n************************************")   
            self.textarea.insert(END, f"{facture[4]}\t{facture[5]}\t\t\t{facture[6]}{facture[7]}")


            self.textarea.insert(END, "\n************************************") 
            self.textarea.insert(END, f"Total:\t\t\t {facture[7]}\n")
            self.textarea.insert(END, f"Elite:\t\t\t {facture[8]}\n")
            self.textarea.insert(END, f"Total Elite:\t\t\t {facture[9]}\n")
        else:
            messagebox.showerror("Erreur", "La facture n'existe pas")

        conn.close()

    def reni(self) :
        self.textarea.delete(1.0, END)
        self.c_nom.set("")
        self.c_phon.set("")
        x=random.randint(1000,9999)
        self.n_factu.set(str(x))
        self.rech_factu.set("")
        self.produit.set("")
        self.c_email.set("")
        self.prix.set(0)
        self.qte.set(0)
        self.l=[0]
        self.totalnormal.set("")
        self.elite.set("")
        self.totalelite.set("")
        self.bienvenu()

    def quitter(self):
      root.destroy()
        
        



     ######### Fonction Categorie ############
    def fonctionCategorie(self, even="") : 
        if self.txt_categorie.get()=="BMW" :
            self.txt_souscategorie.config(values=self.souscategorieBMW)
            self.txt_souscategorie.current(0)

        if self.txt_categorie.get()=="Mercedes" :
            self.txt_souscategorie.config(values=self.souscategorieMerc)
            self.txt_souscategorie.current(0)

        if self.txt_categorie.get()=="Audi" :
            self.txt_souscategorie.config(values=self.souscategorieAudi)
            self.txt_souscategorie.current(0)


        ######## Functions :###################
    def fonctionsousCategorie (self, even=""):
            #BMW ["BMW Série 1", "BMW Série 2" , "BMW X5"]
        if self.txt_souscategorie.get()=="BMW Série 1" :
            self.txt_couleure.config(values=self.BmwSerie1)
            self.txt_couleure.current(0)

        if self.txt_souscategorie.get()=="BMW Série 2" :
            self.txt_couleure.config(values=self.BmwSerie2)
            self.txt_couleure.current(0)

        if self.txt_souscategorie.get()=="BMW X5" :
            self.txt_couleure.config(values=self.BmwX5)
            self.txt_couleure.current(0)        

             #Mercedes ["Cla", "Classe A" , "Classe Cls"]
        if self.txt_souscategorie.get()=="Cla" : 
            self.txt_couleure.config(values=self.MCla)
            self.txt_couleure.current(0)      

        if self.txt_souscategorie.get()=="Classe A" : 
            self.txt_couleure.config(values=self.MClasseA)
            self.txt_couleure.current(0) 

        if self.txt_souscategorie.get()=="Classe Cls" : 
            self.txt_couleure.config(values=self.MCCls)
            self.txt_couleure.current(0)   

            #Audi ["Audi A1", "Audi A7" , "Audi Q3"]
        if self.txt_souscategorie.get()=="Audi A1" : 
            self.txt_couleure.config(values=self.Aa1)
            self.txt_couleure.current(0)      

        if self.txt_souscategorie.get()=="Audi A7" : 
            self.txt_couleure.config(values=self.Aa7)
            self.txt_couleure.current(0) 

        if self.txt_souscategorie.get()=="Audi Q3" : 
            self.txt_couleure.config(values=self.Aq3)
            self.txt_couleure.current(0) 


##############couleur Fonction ################
    def fonctionCouleure(self,even="") : 
        if self.txt_couleure.get()=="Noir" : 
            self.txt_prix.config(values=self.price_Serie1_Noir)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Blanc" : 
            self.txt_prix.config(values=self.price_Serie1_blanc)
            self.txt_prix.current(0)   
            self.qte.set(1)
    
        if self.txt_couleure.get()=="Bleu" : 
            self.txt_prix.config(values=self.price_Serie1_bleu)
            self.txt_prix.current(0)   
            self.qte.set(1)
            
        if self.txt_couleure.get()=="Noir" : 
            self.txt_prix.config(values=self.price_Serie2_Noir)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Rouge" : 
            self.txt_prix.config(values=self.price_Serie2_Rouge)
            self.txt_prix.current(0)   
            self.qte.set(1)
    
        if self.txt_couleure.get()=="Bleu" : 
            self.txt_prix.config(values=self.price_Serie2_bleu)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Noir" : 
            self.txt_prix.config(values=self.price_X5_Noir)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Blanc" : 
            self.txt_prix.config(values=self.price_X5_Blanc)
            self.txt_prix.current(0)   
            self.qte.set(1)
    
        if self.txt_couleure.get()=="Rouge" : 
            self.txt_prix.config(values=self.price_X5_Rouge)
            self.txt_prix.current(0)   
            self.qte.set(1)


        if self.txt_couleure.get()=="Noir" : 
            self.txt_prix.config(values=self.price_MCla_Noir)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Blanc" : 
            self.txt_prix.config(values=self.price_MCla_blanc)
            self.txt_prix.current(0)   
            self.qte.set(1)
    
        if self.txt_couleure.get()=="Bleu" : 
            self.txt_prix.config(values=self.price_MCla_bleu)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Noir" : 
            self.txt_prix.config(values=self.price_MClasseA_Noir)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Rouge" : 
            self.txt_prix.config(values=self.price_MClasseA_blanc)
            self.txt_prix.current(0)   
            self.qte.set(1)
    
        if self.txt_couleure.get()=="gris" : 
            self.txt_prix.config(values=self.price_MClasseA_gris)
            self.txt_prix.current(0)   
            self.qte.set(1)  

        #
        if self.txt_couleure.get()=="Noir" : 
            self.txt_prix.config(values=self.price_MCCls_Noir)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Blanc" : 
            self.txt_prix.config(values=self.price_MCCls_Blanc)
            self.txt_prix.current(0)   
            self.qte.set(1)
    
        if self.txt_couleure.get()=="Gris" : 
            self.txt_prix.config(values=self.price_MCCls_Gris)
            self.txt_prix.current(0)   
            self.qte.set(1)           

        if self.txt_couleure.get()=="Noir" : 
            self.txt_prix.config(values=self.price_Aa1_Noir)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Blanc" : 
            self.txt_prix.config(values=self.price_Aa1_blanc)
            self.txt_prix.current(0)   
            self.qte.set(1)
    
        if self.txt_couleure.get()=="Bleu" : 
            self.txt_prix.config(values=self.price_Aa1_bleu)
            self.txt_prix.current(0)   
            self.qte.set(1)   


        if self.txt_couleure.get()=="Noir" : 
            self.txt_prix.config(values=self.price_Aa7_Noir)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Rouge" : 
            self.txt_prix.config(values=self.price_Aa7_blanc)
            self.txt_prix.current(0)   
            self.qte.set(1)
    
        if self.txt_couleure.get()=="gris" : 
            self.txt_prix.config(values=self.price_Aa7_gris)
            self.txt_prix.current(0)   
            self.qte.set(1)   

        if self.txt_couleure.get()=="Noir" : 
            self.txt_prix.config(values=self.price_Aq3_Noir)
            self.txt_prix.current(0)   
            self.qte.set(1)

        if self.txt_couleure.get()=="Blanc" : 
            self.txt_prix.config(values=self.price_Aq3_Blanc)
            self.txt_prix.current(0)   
            self.qte.set(1)
    
        if self.txt_couleure.get()=="Gris" : 
            self.txt_prix.config(values=self.price_Aq3_Gris)
            self.txt_prix.current(0)   
            self.qte.set(1)   






if __name__=="__main__":
    root=Tk()
    obj = LocationVoiture(root)
    root.mainloop()