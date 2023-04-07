from tkinter import *
import mysql.connector
from tkinter.messagebox import *
import pandas as pd
from crud import *


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="****",
    database="boutique",
    auth_plugin='mysql_native_password'
)
cursor = conn.cursor()






add_produit = ("INSERT INTO produit "
               "(nom, description, prix, quantite, id_category) "
               "VALUES (%s, %s, %s, %s, %s)")

Boutique = Crud(cursor)
class PageBoutique():

    def __init__(self, root):
        self.fenetre = root
        self.fenetre.title("Accueuil")
        self.fenetre.minsize(480,360)
        self.fenetre.config(background="white")
        self._accueil()
        
    
    def _accueil(self): #La page accueil
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack(expand=YES)
        
        titreNom = Label(self.frame, text="Afficher :",font=("Arial",20),fg="black",background="white")
        titreNom.grid(column=0,row=0)
        LivreButton = Button(self.frame, text="Livre",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageLivre)
        LivreButton.grid(column=0,row=1)
        JouetsButton = Button(self.frame, text="Jouets",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageJouet)
        JouetsButton.grid(column=1,row=1)
        ElectroButton = Button(self.frame, text="Electro-M",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageElectro)
        ElectroButton.grid(column=2,row=1)
        JeuxSoButton = Button(self.frame, text="JeuxSo",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageJeuxSo)
        JeuxSoButton.grid(column=3,row=1)
        RuptureButton = Button(self.frame, text="Rupture_Stock",font=("Arial",20),width=12, background="Blue",fg="black",command=self._pageRuptureStock)
        RuptureButton.grid(column=4,row=1)

        titreNomAjout = Label(self.frame, text="Ajouter :",font=("Arial",20),fg="black",background="white")
        titreNomAjout.grid(column=0,row=2)
        LivreButton = Button(self.frame, text="Livre",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageLivreAdd)
        LivreButton.grid(column=0,row=3)
        JouetsButton = Button(self.frame, text="Jouets",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageJouetAdd)
        JouetsButton.grid(column=1,row=3)
        ElectroButton = Button(self.frame, text="Electro-M",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageElectroAdd)
        ElectroButton.grid(column=2,row=3)
        JeuxSoButton = Button(self.frame, text="JeuxSo",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageJeuxSoAdd)
        JeuxSoButton.grid(column=3,row=3)
        
        titreNomSuppr = Label(self.frame, text="Supprimer :",font=("Arial",20),fg="black",background="white")
        titreNomSuppr.grid(column=0,row=4)
        LivreButton = Button(self.frame, text="Livre",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageLivreSupr)
        LivreButton.grid(column=0,row=5)
        JouetsButton = Button(self.frame, text="Jouets",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageJouetSupr)
        JouetsButton.grid(column=1,row=5)
        ElectroButton = Button(self.frame, text="Electro-M",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageElectroSupr)
        ElectroButton.grid(column=2,row=5)
        JeuxSoButton = Button(self.frame, text="JeuxSo",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageJeuxSoSupr)
        JeuxSoButton.grid(column=3,row=5)
        
        titreNomUpdate = Label(self.frame, text="Modifier :",font=("Arial",20),fg="black",background="white")
        titreNomUpdate.grid(column=0,row=6)
        LivreButton = Button(self.frame, text="Livre",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageLivreUpd)
        LivreButton.grid(column=0,row=7)
        JouetsButton = Button(self.frame, text="Jouets",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageJouetUpd)
        JouetsButton.grid(column=1,row=7)
        ElectroButton = Button(self.frame, text="Electro-M",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageElectroUpd)
        ElectroButton.grid(column=2,row=7)
        JeuxSoButton = Button(self.frame, text="JeuxSo",font=("Arial",20),width=8, background="Blue",fg="black",command=self._pageJeuxSoUpd)
        JeuxSoButton.grid(column=3,row=7)
        
        titreNomCSV  = Label(self.frame, text="CSV :",font=("Arial",20),fg="black",background="white")
        titreNomCSV.grid(column=0,row=8)
        
        LivreButton = Button(self.frame, text="Livre",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:self._writeCsv(1))
        LivreButton.grid(column=0,row=9)
        JouetsButton = Button(self.frame, text="Jouets",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:self._writeCsv(2))
        JouetsButton.grid(column=1,row=9)
        ElectroButton = Button(self.frame, text="Electro-M",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:self._writeCsv(3))
        ElectroButton.grid(column=2,row=9)
        JeuxSoButton = Button(self.frame, text="JeuxSo",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:self._writeCsv(4))
        JeuxSoButton.grid(column=3,row=9)
        RuptureButton = Button(self.frame, text="Rupture_Stock",font=("Arial",20),width=12, background="Blue",fg="black",command=lambda:self._writeCsvRupture())
        RuptureButton.grid(column=4,row=9)
        
    def _pageLivre(self):  #La page affichage : Livre
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(1)
        titreNom = Label(self.frame, text="Nom",font=("Arial",20),fg="black",background="white")
        titreNom.grid(column=0,row=0)
        titreDescription = Label(self.frame, text="Description",font=("Arial",20),fg="black",background="white")
        titreDescription.grid(column=1,row=0)
        titrePrix = Label(self.frame, text="Prix",font=("Arial",20),fg="black",background="white")
        titrePrix.grid(column=2,row=0)
        titreQuantite = Label(self.frame, text="Quantite",font=("Arial",20),fg="black",background="white")
        titreQuantite.grid(column=3,row=0)
        contenuNom = Label(self.frame, text='',background="white")
        contenuDescription = Label(self.frame, text='',background="white")
        contenuPrix = Label(self.frame, text='',background="white")
        contenuQuantite = Label(self.frame, text='',background="white")
        for livre in range(len(resultat)):
            contenuNom["text"] += str(resultat[livre][0]) + " / "
            contenuNom["text"] += "\n"
            contenuDescription["text"] += str(resultat[livre][1]) + " / "
            contenuDescription["text"] += "\n"
            contenuPrix["text"] += str(resultat[livre][2]) + " / "
            contenuPrix["text"] += "\n"
            contenuQuantite["text"] += str(resultat[livre][3]) + " / "
            contenuQuantite["text"] += "\n"
        contenuNom.grid(column=0,row=1)
        contenuDescription.grid(column=1,row=1)
        contenuPrix.grid(column=2,row=1)
        contenuQuantite.grid(column=3,row=1)
        QuitButton= Button(self.frame, text="Quitter",font=("Arial",20),width=8, background="Blue",fg="black",command=self._accueil)
        QuitButton.grid(column=0,row=2)
        
        
    def _pageJouet(self):   #La page affichage : Jouet
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(2)
        titreNom = Label(self.frame, text="Nom",font=("Arial",20),fg="black",background="white")
        titreNom.grid(column=0,row=0)
        titreDescription = Label(self.frame, text="Description",font=("Arial",20),fg="black",background="white")
        titreDescription.grid(column=1,row=0)
        titrePrix = Label(self.frame, text="Prix",font=("Arial",20),fg="black",background="white")
        titrePrix.grid(column=2,row=0)
        titreQuantite = Label(self.frame, text="Quantite",font=("Arial",20),fg="black",background="white")
        titreQuantite.grid(column=3,row=0)
        contenuNom = Label(self.frame, text='',background="white")
        contenuDescription = Label(self.frame, text='',background="white")
        contenuPrix = Label(self.frame, text='',background="white")
        contenuQuantite = Label(self.frame, text='',background="white")
        for livre in range(len(resultat)): #Livre = Jouet
            contenuNom["text"] += str(resultat[livre][0]) + " / "
            contenuNom["text"] += "\n"
            contenuDescription["text"] += str(resultat[livre][1]) + " / "
            contenuDescription["text"] += "\n"
            contenuPrix["text"] += str(resultat[livre][2]) + " / "
            contenuPrix["text"] += "\n"
            contenuQuantite["text"] += str(resultat[livre][3]) + " / "
            contenuQuantite["text"] += "\n"
        contenuNom.grid(column=0,row=1)
        contenuDescription.grid(column=1,row=1)
        contenuPrix.grid(column=2,row=1)
        contenuQuantite.grid(column=3,row=1)
        QuitButton= Button(self.frame, text="Quitter",font=("Arial",20),width=8, background="Blue",fg="black",command=self._accueil)
        QuitButton.grid(column=0,row=2)
        
        
    def _pageElectro(self):   #La page affichage : Electro Menager
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(3)
        titreNom = Label(self.frame, text="Nom",font=("Arial",20),fg="black",background="white")
        titreNom.grid(column=0,row=0)
        titreDescription = Label(self.frame, text="Description",font=("Arial",20),fg="black",background="white")
        titreDescription.grid(column=1,row=0)
        titrePrix = Label(self.frame, text="Prix",font=("Arial",20),fg="black",background="white")
        titrePrix.grid(column=2,row=0)
        titreQuantite = Label(self.frame, text="Quantite",font=("Arial",20),fg="black",background="white")
        titreQuantite.grid(column=3,row=0)
        contenuNom = Label(self.frame, text='',background="white")
        contenuDescription = Label(self.frame, text='',background="white")
        contenuPrix = Label(self.frame, text='',background="white")
        contenuQuantite = Label(self.frame, text='',background="white")
        for livre in range(len(resultat)): #Livre = Electro M
            contenuNom["text"] += str(resultat[livre][0]) + " / "
            contenuNom["text"] += "\n"
            contenuDescription["text"] += str(resultat[livre][1]) + " / "
            contenuDescription["text"] += "\n"
            contenuPrix["text"] += str(resultat[livre][2]) + " / "
            contenuPrix["text"] += "\n"
            contenuQuantite["text"] += str(resultat[livre][3]) + " / "
            contenuQuantite["text"] += "\n"
        contenuNom.grid(column=0,row=1)
        contenuDescription.grid(column=1,row=1)
        contenuPrix.grid(column=2,row=1)
        contenuQuantite.grid(column=3,row=1)
        QuitButton= Button(self.frame, text="Quitter",font=("Arial",20),width=8, background="Blue",fg="black",command=self._accueil)
        QuitButton.grid(column=0,row=2)
        
        
    def _pageJeuxSo(self):   #La page affichage : Jeux societe
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(4)
        titreNom = Label(self.frame, text="Nom",font=("Arial",20),fg="black",background="white")
        titreNom.grid(column=0,row=0)
        titreDescription = Label(self.frame, text="Description",font=("Arial",20),fg="black",background="white")
        titreDescription.grid(column=1,row=0)
        titrePrix = Label(self.frame, text="Prix",font=("Arial",20),fg="black",background="white")
        titrePrix.grid(column=2,row=0)
        titreQuantite = Label(self.frame, text="Quantite",font=("Arial",20),fg="black",background="white")
        titreQuantite.grid(column=3,row=0)
        contenuNom = Label(self.frame, text='',background="white")
        contenuDescription = Label(self.frame, text='',background="white")
        contenuPrix = Label(self.frame, text='',background="white")
        contenuQuantite = Label(self.frame, text='',background="white")
        for livre in range(len(resultat)): #Livre = Jeux Societe
            contenuNom["text"] += str(resultat[livre][0]) + " / "
            contenuNom["text"] += "\n"
            contenuDescription["text"] += str(resultat[livre][1]) + " / "
            contenuDescription["text"] += "\n"
            contenuPrix["text"] += str(resultat[livre][2]) + " / "
            contenuPrix["text"] += "\n"
            contenuQuantite["text"] += str(resultat[livre][3]) + " / "
            contenuQuantite["text"] += "\n"
        contenuNom.grid(column=0,row=1)
        contenuDescription.grid(column=1,row=1)
        contenuPrix.grid(column=2,row=1)
        contenuQuantite.grid(column=3,row=1)
        QuitButton= Button(self.frame, text="Quitter",font=("Arial",20),width=8, background="Blue",fg="black",command=self._accueil)
        QuitButton.grid(column=0,row=2)
        
        
    def _pageRuptureStock(self):   #La page affichage : Rupture Stock
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.readRupture()
        titreNom = Label(self.frame, text="Nom",font=("Arial",20),fg="black",background="white")
        titreNom.grid(column=0,row=0)
        titreDescription = Label(self.frame, text="Description",font=("Arial",20),fg="black",background="white")
        titreDescription.grid(column=1,row=0)
        titrePrix = Label(self.frame, text="Prix",font=("Arial",20),fg="black",background="white")
        titrePrix.grid(column=2,row=0)
        titreQuantite = Label(self.frame, text="Quantite",font=("Arial",20),fg="black",background="white")
        titreQuantite.grid(column=3,row=0)
        contenuNom = Label(self.frame, text='',background="white")
        contenuDescription = Label(self.frame, text='',background="white")
        contenuPrix = Label(self.frame, text='',background="white")
        contenuQuantite = Label(self.frame, text='',background="white")
        contenuCategorie = Label(self.frame, text='',background="white")
        for livre in range(len(resultat)): #Livre = Jeux Societe
            contenuNom["text"] += str(resultat[livre][0]) + " / "
            contenuNom["text"] += "\n"
            contenuDescription["text"] += str(resultat[livre][1]) + " / "
            contenuDescription["text"] += "\n"
            contenuPrix["text"] += str(resultat[livre][2]) + " / "
            contenuPrix["text"] += "\n"
            contenuQuantite["text"] += str(resultat[livre][3]) + " / "
            contenuQuantite["text"] += "\n"
            contenuCategorie["text"] += str(resultat[livre][4]) + " / "
            contenuCategorie["text"] += "\n"
        contenuNom.grid(column=0,row=1)
        contenuDescription.grid(column=1,row=1)
        contenuPrix.grid(column=2,row=1)
        contenuQuantite.grid(column=3,row=1)
        contenuCategorie.grid(column=4,row=1)
        QuitButton= Button(self.frame, text="Quitter",font=("Arial",20),width=8, background="Blue",fg="black",command=self._accueil)
        QuitButton.grid(column=0,row=2)
        
        
    def _pageLivreAdd(self):
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        LabelNom = Label(self.frame, text="Nom",font=("Arial",10),fg="black",background="white")
        LabelNom.grid(column=0,row=0)
        EntryNom = Entry(self.frame)
        EntryNom.grid(column=1,row=0)
        LabelDescription = Label(self.frame, text="Description",font=("Arial",10),fg="black",background="white")
        LabelDescription.grid(column=0,row=1)
        EntryDescription = Entry(self.frame)
        EntryDescription.grid(column=1,row=1)
        LabelPrix = Label(self.frame, text="Prix",font=("Arial",10),fg="black",background="white")
        LabelPrix.grid(column=0,row=2)
        EntryPrix = Entry(self.frame)
        EntryPrix.grid(column=1,row=2)
        LabelQuantite = Label(self.frame, text="Quantite",font=("Arial",10),fg="black",background="white")
        LabelQuantite.grid(column=0,row=3)
        EntryQuantite = Entry(self.frame)
        EntryQuantite.grid(column=1,row=3)
        EntryButton= Button(self.frame, text="Ajouter",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.ajout(EntryNom.get(),EntryDescription.get(),EntryPrix.get(),EntryQuantite.get(),1),self._accueil()])
        EntryButton.grid(column=0,row=4)
    def _pageJouetAdd(self):
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        LabelNom = Label(self.frame, text="Nom",font=("Arial",10),fg="black",background="white")
        LabelNom.grid(column=0,row=0)
        EntryNom = Entry(self.frame)
        EntryNom.grid(column=1,row=0)
        LabelDescription = Label(self.frame, text="Description",font=("Arial",10),fg="black",background="white")
        LabelDescription.grid(column=0,row=1)
        EntryDescription = Entry(self.frame)
        EntryDescription.grid(column=1,row=1)
        LabelPrix = Label(self.frame, text="Prix",font=("Arial",10),fg="black",background="white")
        LabelPrix.grid(column=0,row=2)
        EntryPrix = Entry(self.frame)
        EntryPrix.grid(column=1,row=2)
        LabelQuantite = Label(self.frame, text="Quantite",font=("Arial",10),fg="black",background="white")
        LabelQuantite.grid(column=0,row=3)
        EntryQuantite = Entry(self.frame)
        EntryQuantite.grid(column=1,row=3)
        EntryButton= Button(self.frame, text="Ajouter",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.ajout(EntryNom.get(),EntryDescription.get(),EntryPrix.get(),EntryQuantite.get(),2),self._accueil()])
        EntryButton.grid(column=0,row=4)
    def _pageElectroAdd(self):
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        LabelNom = Label(self.frame, text="Nom",font=("Arial",10),fg="black",background="white")
        LabelNom.grid(column=0,row=0)
        EntryNom = Entry(self.frame)
        EntryNom.grid(column=1,row=0)
        LabelDescription = Label(self.frame, text="Description",font=("Arial",10),fg="black",background="white")
        LabelDescription.grid(column=0,row=1)
        EntryDescription = Entry(self.frame)
        EntryDescription.grid(column=1,row=1)
        LabelPrix = Label(self.frame, text="Prix",font=("Arial",10),fg="black",background="white")
        LabelPrix.grid(column=0,row=2)
        EntryPrix = Entry(self.frame)
        EntryPrix.grid(column=1,row=2)
        LabelQuantite = Label(self.frame, text="Quantite",font=("Arial",10),fg="black",background="white")
        LabelQuantite.grid(column=0,row=3)
        EntryQuantite = Entry(self.frame)
        EntryQuantite.grid(column=1,row=3)
        EntryButton= Button(self.frame, text="Ajouter",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.ajout(EntryNom.get(),EntryDescription.get(),EntryPrix.get(),EntryQuantite.get(),3),self._accueil()])
        EntryButton.grid(column=0,row=4)
    def _pageJeuxSoAdd(self):
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        LabelNom = Label(self.frame, text="Nom",font=("Arial",10),fg="black",background="white")
        LabelNom.grid(column=0,row=0)
        EntryNom = Entry(self.frame)
        EntryNom.grid(column=1,row=0)
        LabelDescription = Label(self.frame, text="Description",font=("Arial",10),fg="black",background="white")
        LabelDescription.grid(column=0,row=1)
        EntryDescription = Entry(self.frame)
        EntryDescription.grid(column=1,row=1)
        LabelPrix = Label(self.frame, text="Prix",font=("Arial",10),fg="black",background="white")
        LabelPrix.grid(column=0,row=2)
        EntryPrix = Entry(self.frame)
        EntryPrix.grid(column=1,row=2)
        LabelQuantite = Label(self.frame, text="Quantite",font=("Arial",10),fg="black",background="white")
        LabelQuantite.grid(column=0,row=3)
        EntryQuantite = Entry(self.frame)
        EntryQuantite.grid(column=1,row=3)
        EntryButton= Button(self.frame, text="Ajouter",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.ajout(EntryNom.get(),EntryDescription.get(),EntryPrix.get(),EntryQuantite.get(),4),self._accueil()])
        EntryButton.grid(column=0,row=4)
    
    
    def _pageLivreSupr(self):
        for i in self.fenetre.winfo_children():
            i.destroy()
        
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(1)
        menu1 = StringVar(self.frame)
        menu1.set('Supprimer')
        deleteMenu = OptionMenu(self.frame,menu1,*resultat)
        deleteMenu.grid(column=1,row=1)
        EntryButton= Button(self.frame, text="Supprimer",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.supr(menu1.get()),self._accueil()])
        EntryButton.grid(column=0,row=4)
    
    def _pageJouetSupr(self):
        for i in self.fenetre.winfo_children():
            i.destroy()
        
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(2)
        menu1 = StringVar(self.frame)
        menu1.set('Supprimer')
        deleteMenu = OptionMenu(self.frame,menu1,*resultat)
        deleteMenu.grid(column=1,row=1)
        EntryButton= Button(self.frame, text="Supprimer",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.supr(menu1.get()),self._accueil()])
        EntryButton.grid(column=0,row=4)
    
    def _pageElectroSupr(self):
        for i in self.fenetre.winfo_children():
            i.destroy()
        
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(3)
        menu1 = StringVar(self.frame)
        menu1.set('Supprimer')
        deleteMenu = OptionMenu(self.frame,menu1,*resultat)
        deleteMenu.grid(column=1,row=1)
        EntryButton= Button(self.frame, text="Supprimer",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.supr(menu1.get()),self._accueil()])
        EntryButton.grid(column=0,row=4)
        
    def _pageJeuxSoSupr(self):
        for i in self.fenetre.winfo_children():
            i.destroy()
        
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(4)
        menu1 = StringVar(self.frame)
        menu1.set('Supprimer')
        deleteMenu = OptionMenu(self.frame,menu1,*resultat)
        deleteMenu.grid(column=1,row=1)
        EntryButton= Button(self.frame, text="Supprimer",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.supr(menu1.get()),self._accueil()])
        EntryButton.grid(column=0,row=4)  
        
    def _pageLivreUpd(self):
        global CategorieMenu,resultatIndex,menu1,menu2
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(1)
        menu1 = StringVar(self.frame)
        menu1.set('Livre')
        menu2 = StringVar(self.frame)
        menu2.set("Catégorie")
        categories = ["nom","description","prix","quantite"]
        UpdateMenu = OptionMenu(self.frame,menu1,*resultat)
        UpdateMenu.grid(column=0,row=1)
        CategorieMenu = OptionMenu(self.frame,menu2,*categories)
        CategorieMenu.grid(column=0,row=2)
        ValueEntry = Entry(self.frame)
        ValueEntry.grid(column=1,row=2)
        EntryButton= Button(self.frame, text="Modifier",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.upd(menu1.get(),menu2.get(),ValueEntry.get()),self._accueil()])
        EntryButton.grid(column=0,row=3)  
        
    def _pageJouetUpd(self):
        global CategorieMenu,resultatIndex,menu1,menu2
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(2)
        menu1 = StringVar(self.frame)
        menu1.set('Jouet')
        menu2 = StringVar(self.frame)
        menu2.set("Catégorie")
        categories = ["nom","description","prix","quantite"]
        UpdateMenu = OptionMenu(self.frame,menu1,*resultat)
        UpdateMenu.grid(column=0,row=1)
        CategorieMenu = OptionMenu(self.frame,menu2,*categories)
        CategorieMenu.grid(column=0,row=2)
        ValueEntry = Entry(self.frame)
        ValueEntry.grid(column=1,row=2)
        EntryButton= Button(self.frame, text="Modifier",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.upd(menu1.get(),menu2.get(),ValueEntry.get()),self._accueil()])
        EntryButton.grid(column=0,row=3)  

    def _pageElectroUpd(self):
        global CategorieMenu,resultatIndex,menu1,menu2
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(3)
        menu1 = StringVar(self.frame)
        menu1.set('Electro')
        menu2 = StringVar(self.frame)
        menu2.set("Catégorie")
        categories = ["nom","description","prix","quantite"]
        UpdateMenu = OptionMenu(self.frame,menu1,*resultat)
        UpdateMenu.grid(column=0,row=1)
        CategorieMenu = OptionMenu(self.frame,menu2,*categories)
        CategorieMenu.grid(column=0,row=2)
        ValueEntry = Entry(self.frame)
        ValueEntry.grid(column=1,row=2)
        EntryButton= Button(self.frame, text="Modifier",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.upd(menu1.get(),menu2.get(),ValueEntry.get()),self._accueil()])
        EntryButton.grid(column=0,row=3)  

    def _pageJeuxSoUpd(self):
        global CategorieMenu,resultatIndex,menu1,menu2
        for i in self.fenetre.winfo_children():
            i.destroy()
        self.frame = Frame(self.fenetre,background="white")
        self.frame.pack()
        resultat = Boutique.read(4)
        menu1 = StringVar(self.frame)
        menu1.set('JeuxSo')
        menu2 = StringVar(self.frame)
        menu2.set("Catégorie")
        categories = ["nom","description","prix","quantite"]
        UpdateMenu = OptionMenu(self.frame,menu1,*resultat)
        UpdateMenu.grid(column=0,row=1)
        CategorieMenu = OptionMenu(self.frame,menu2,*categories)
        CategorieMenu.grid(column=0,row=2)
        ValueEntry = Entry(self.frame)
        ValueEntry.grid(column=1,row=2)
        EntryButton= Button(self.frame, text="Modifier",font=("Arial",20),width=8, background="Blue",fg="black",command=lambda:[self.upd(menu1.get(),menu2.get(),ValueEntry.get()),self._accueil()])
        EntryButton.grid(column=0,row=3)  

    def _writeCsv(self,id):
        result = pd.read_sql_query(f"""
                                   select * from boutique.produit where id_category = {id}
                                   """,conn)
                                   
            
        dataframe = pd.DataFrame(result)
        dataframe.to_csv(r"stock.csv",index=False)
        
    def _writeCsvRupture(self):
        result = pd.read_sql_query(f"""
                                   select * from boutique.produit where quantite <= 0
                                   """,conn)
                                   
            
        dataframe = pd.DataFrame(result)
        dataframe.to_csv(r"stock.csv",index=False)
        
        
    def supr(self,entry):
        #Petite partie pour trouver l'id (d'une taille indeterminée)
        try:
            id = list(entry)[len(list(entry))-2]
            i=3
            lettre = list(entry)[len(list(entry))-i]
            while lettre.isnumeric():
                id += lettre
                i += 1
                lettre = list(entry)[len(list(entry))-i]
            id = ''.join(reversed(id))
            Boutique.delete_id(id)
            showinfo("Insertion", "L'objet a été supprimé")
        except:
            showinfo("Erreur", "Une Erreur de suppression")
            
    def upd(self,entry,category,valeur):
        #Petite partie pour trouver l'id (d'une taille indeterminée)
        try:
            id = list(entry)[len(list(entry))-2]
            i=3
            lettre = list(entry)[len(list(entry))-i]
            while lettre.isnumeric():
                id += lettre
                i += 1
                lettre = list(entry)[len(list(entry))-i]
            id = ''.join(reversed(id))
            Boutique.update(category,str(valeur),id)
            showinfo("Insertion", "L'objet a été actualisé")
        except:
            showinfo("Erreur", "Une Erreur d'actualisation")      
            
    def ajout(self,nom,description,prix,quantite,category):
        try:
            Boutique.insert((nom,description,int(prix),int(quantite),int(category)))
            showinfo("Insertion", "L'objet a été ajouté")
        except:
            showinfo("Erreur", "Une Erreur d'insertion")
fenetre = Tk()
PageBoutique(fenetre)

fenetre.mainloop()
cursor.close()
conn.close()

