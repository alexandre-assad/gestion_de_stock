import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Monkeyking300!",
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
        conn.commit()
    def read(self,id):
        self.cursor.execute(f"SELECT produit.nom,produit.description,produit.prix,produit.quantite,categorie.nom,produit.id FROM produit INNER JOIN categorie ON produit.id_category = categorie.id WHERE produit.id_category = {id}")
        resultat = self.cursor.fetchall()
        return resultat
    
    def readRupture(self):
        self.cursor.execute(f"SELECT produit.nom,produit.description,produit.prix,produit.quantite,categorie.nom FROM produit INNER JOIN categorie ON produit.id_category = categorie.id WHERE produit.quantite <= 0")
        resultat = self.cursor.fetchall()
        return resultat
    
    def delete_id(self,id):
        self.cursor.execute(f"DELETE FROM produit WHERE id = {id}")
        conn.commit()
    def update(self,categorie,newValue,id):
        self.cursor.execute(f"UPDATE produit SET produit.{categorie} = {newValue} WHERE id = {id}")
        conn.commit()
