from tkinter import *
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*****",
    database="boutique",
    auth_plugin='mysql_native_password'
)
cursor = conn.cursor()






add_produit = ("INSERT INTO produit "
               "(nom, description, prix, quantite, id_category) "
               "VALUES (%s, %s, %s, %s, %s)")
class Crud:
    
    def __init__(self,cursor):
        self.cursor = cursor
        

    def insert(self,newValue):
        self.cursor.execute(add_produit, newValue)
        self.cursor.commit()
    def read(self,id):
        self.cursor.execute(f"SELECT produit.nom,produit.description,produit.prix,produit.quantite,categorie.nom FROM produit INNER JOIN categorie ON produit.id_category = categorie.id WHERE produit.id_category = {id}")
        resultat = self.cursor.fetchall()
        return resultat
    
    def readRupture(self):
        self.cursor.execute(f"SELECT produit.nom,produit.description,produit.prix,produit.quantite,categorie.nom FROM produit INNER JOIN categorie ON produit.id_category = categorie.id WHERE produit.quantite <= 0")
        resultat = self.cursor.fetchall()
        return resultat
    
    def delete_id(self,id):
        self.cursor.execute(f"DELETE FROM produit WHERE id = {id}")
        
    def update(self,categorie,newValue,id):
        self.cursor.execute(f"UPDATE produit SET produit.{categorie} = {newValue} WHERE id = {id}")


Boutique = Crud(cursor)
class PageBoutique():

    def __init__(self, root):
        self.fenetre = root
        self.fenetre.title("Accueuil")
        self.fenetre.minsize(480,360)
        self.fenetre.config(background="white")
        self._accueil()
        
    
    def _accueil(self):
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
        
    def _pageLivre(self): 
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
    def _pageJouet(self): 
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
    def _pageElectro(self): 
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
        
        
    def _pageJeuxSo(self): 
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
    def _pageRuptureStock(self): 
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
fenetre = Tk()
PageBoutique(fenetre)

fenetre.mainloop()
cursor.close()
conn.close()

