from connection import con as connector
import hashlib
from hmac import compare_digest
class user:
    def __init__(self, username, password=None, email=None, phone=None):
        self.username = username
        self.email = email
        self.password = self._encrypt_password(password)
        self.phone = phone
    
    def _encrypt_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    def verify_password(self, password):
        return self.password == self._encrypt_password(password)
        
    def create_user(self):
        cursor = connector.cursor()
        cursor.execute("select * from user where username = (?)", (self.username,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("insert into user (username, password, email, phone) values(?,?,?,?)", (self.username, self.password, self.email, self.phone))
            connector.commit()
            print("user created")
            return True
        else:
            print("lose operation")
            return False
        connector.close()

    def edit_user(self,username):
        
        cursor = connector.cursor()
        cursor.execute("select * from user where username = ?", (username,))
        result = cursor.fetchone()
        if cursor is not None:
            cursor.execute("update user set username = ?, password = ?, email =?, phone= ? where username =?", (self.username, self.password, self.email, self.phone, username))
            connector.commit()
            print("user edited")
            return True
        else:
            print("lose operation")
            return False    
    
    def login_user(self):
        
        cursor = connector.cursor()
        cursor.execute("select password from user where username = ?", (self.username,))
        result = cursor.fetchone()
        if result is None:
            print("incorrect username or password")
            return False
        else:
            if self.password == result[0]:
                print("user connected")
                return True
            else:
                print("incorrect username or password")
                return False 
    
    
    
    
     
''' var1 = input("username")
var2 = input("new_password")
var4 = input("new_email")
var5 = int(input("new_phone"))

#var6 = input("new_username")

user1 = user(var1, var2, var4, var5)
print(user1.password)
user1.login_user() '''
#user.delete_user()'''
#user.edit_user(var1)
"""
banzet
123
tyury
jfhgj
464564
"""

