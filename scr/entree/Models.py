import string as st
from connection import con as connector
import datetime as dt

class entree:
    def __init__(self, type, date, code=None):
        self.code = self.generate_unique_code()
        self.type = self.type
        self.date = dt.datetime.now()
        
    def generate_code(self):
        taile = 6
        character = "".join(random.choice(st.ascii_letters.upper()) for i in range(2))
        number = "".join(random.choice(st.digits()) for i in range(3))
        return character +"-"+ number
    
    def generate_unique_code(self):
        code  = self.generate_code()
        req = "select * from entree  where code = (?)"
        cursor.execute(req, (code,))
        result = cursor.fetchall()
        print(result)
        while result != []:
            code = self.code()
        return code    
        
    def add_entree(self):
        req = "select * from entree where code = (?)"
        cursor.execute(req, (self.code,))
        result = cursor.fetchone()
        if result is None:
            req = "insert into entree (code, type, date_operation) values (?,?,?)"
            cursor.execute(req, (self.code, self.type, self.date))
            connector.commit()
            print("entree created")
            return True
        else:
            print("lose operation")
            return False 
        
    def get_all(self):
        req = "select * from entree "
        cursor.execute(req)
        result = cursor.fetchall()
        return result     
        