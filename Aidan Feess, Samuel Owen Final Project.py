# Aidan Feess, Samuel Owen Final Project Python

import random
import math
import pickle
from tkinter import *
from unicodedata import name

### Tables

colors = []
images = {}
users = []

### Classes Section

class Admin():
    def __init__(self, username):
        self.priv = 'admin'
        self.username = username

    def give_name(self, name):
        self.username = name

    def get_name(self):
        return self.username

class User():
    def __init__(self, username):
        self.priv = 'admin'
        self.username = username

    def give_name(self, name):
        self.username = name

    def get_name(self):
        return self.username

### Misc Functions Section

def CreateNewUser(name, usertype):
    name = str(name)
    if usertype == 'm':
        user = User(name)
        pickle.dump(user, open(name,"wb"))
    elif usertype == 'a':
        user = Admin(name)
        pickle.dump(user, open(name,"wb"))

def ViewUser(name):
    name = str(name)
    user = pickle.load(open(name, "rb"))
    print(user.username)

#CreateNewUser(u_name, u_type) -- takes a username and type (i.e. 'aidan' and 'admin' which would be u_name = 'aidan' and u_type = 'a')
#ViewUser(u_name2) -- takes a username and outputs information relating to that user

### GUI Section

root = Tk()
root.geometry('400x400')

Title = Label(root, text="Aidan and Sam T-Shirts Login Menu")
Title.place(x=100,y=0)

#u_label = Label(root, text = 'Username')

#u_name_box = Entry(root, border=5)


#utype_label = Label(root, text = 'User Type')

#u_type_box = Entry(root, border=5)


###### Functions for recieving and interpreting the values given by text boxes
#def get_u_name(name):
#    username = u_name_box.get()
#    
#    return
#def get_u_type(u_type):
#    u_type = u_name_box.get()
#    
#    return

#u_name_box.bind('<Return>', get_u_name)
#u_type_box.bind('<Return>', get_u_type)

root.mainloop()