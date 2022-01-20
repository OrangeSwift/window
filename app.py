#SDG
#20/01/2022

from tkinter import *

root=Tk()
root.title('Login')
root.geometery('500x500')


connection = sqlite3.connect('priv')
#use this to write to DB
cursor=connection.cursor()
#Create Table
cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
                (username TEXT, password TEXT)''')
   
# Commit these changes to the DB
connection.commit()
# Close my connection
connection.close()

class winLog1:
  def __init__(self, username, password, frame, button, smallFrame):
    
    self.username = username
    self.password = password
    self.frame = frame
    self.button = button
    self.smallFrame = smallFrame
    
    
    
    
    
    
    root.mainloop()
    
    # import sqlite3

  
  
               
               
               
               
               
               
  
