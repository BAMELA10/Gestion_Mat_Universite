import string as st
from connection import con as connector, cursor

class Article:
    def __init__(self,name,stock,id_categorie, id_fournisseur, code=None):
        self.code = self.generate_unique_code()
        self.name = name
        self.stock = stock
        self.id_categorie = id_categorie
        self.id_fournisseur = id_fournisseur
        
    def generate_code(self):
        taile = 6
        character = "".join(random.choice(st.ascii_letters.upper()) for i in range(2))
        number = "".join(random.choice(st.digits()) for i in range(3))
        return character +"-"+ number
    
    def generate_unique_code(self):
        code  = self.generate_code()
        req = "select * from article  where code = (?)"
        cursor.execute(req, (code,))
        result = cursor.fetchall()
        print(result)
        while result != []:
            code = self.code()
        return code    
        
            
    def add_article(self):
        req = "select * from article where code = (?)"
        cursor.execute(req, (self.code,))
        result = cursor.fetchone()
        if result is None:
            req = "insert into article (code, Nom, stock, categorie, fournisseur) values (?,?,?,?,?)"
            cursor.execute(req, (self.code, self.name, self.stock, self.id_categorie, self.id_fournisseur))
            connector.commit()
            print("article created")
            return True
        else:
            print("lose operation")
            return False 
        
    def edit_article(self, name):
        connector.ping()
        cursor = connector.cursor()
        req = "select * from article where intitulé = ?"
        cursor.execute(req, (name,))
        result = cursor.fetchone()
        if result is not None:
            req = "update article set Nom = ?, stock = ?, categorie = ?, fournisseur = ?  where Nom = ?"
            cursor.execute(req, (self.name, self.stock, self.id_categorie, self.id_fournisseur,))
            connector.commit()
            print("article edited")
            return True
        else:
            print("lose operation")
            return False    
    
    def get_all(self):
        req = "select * from article "
        cursor.execute(req)
        result = cursor.fetchall()
        return result    
    