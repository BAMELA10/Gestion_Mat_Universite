
import sting as st 
import tkinter as tk
from connection import con as connector
from connection import cursor

class Cout:
    def __init__(self,operation,montant,id_article, code=None):
        self.code = self.generate_unique_code()
        self.operation = operation
        self.montant = montant
        self.id_article = id_article
        
    def generate_code(self):
        taile = 6
        character = "".join(random.choice(st.ascii_letters.upper()) for i in range(2))
        number = "".join(random.choice(st.digits()) for i in range(3))
        return character +"-"+ number
    
    def generate_unique_code(self):
        code  = self.generate_code()
        req = "select * from cout  where code = (?)"
        cursor.execute(req, (code,))
        result = cursor.fetchall()
        print(result)
        while result != []:
            code = self.code()
        return code    
    
    def add_cout(self):
        req = "select * from cout where code = (?)"
        cursor.execute(req, (self.code,))
        result = cursor.fetchone()
        if result is None:
            req = "insert into cout (code, operation, montant, id_article) values (?,?,?,?,?)"
            cursor.execute(req, (self.code, self.operation, self.montant, self.id_article,))
            connector.commit()
            print("cout created")
            return True
        else:
            print("lose operation")
            return False 
        
        
    def get_all(self):
        req = "select * from cout "
        cursor.execute(req)
        result = cursor.fetchall()
        return result  
    