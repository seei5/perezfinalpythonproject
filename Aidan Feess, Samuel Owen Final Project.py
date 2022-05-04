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

u_name = input('Input username: ')
u_type = input('Input user type (m/a): ')

CreateNewUser(u_name, u_type)

u_name2 = input('Input username: ')
ViewUser(u_name2)

### GUI Section

root = Tk()

Title = Label(root, text="Aidan and Sam T-Shirts Login Menu")
Title.pack(side=TOP)

u_label = Label(root, text = 'Username')
u_label.pack(side=LEFT)
u_name_box = Entry(root, border=5)
u_name_box.pack(side=RIGHT)

###### Functions for recieving and interpreting the values given by text boxes
def get_u_name(name):
    username = u_name_box.get()
    #for name in 
    return

u_name_box.bind('<Return>', get_u_name)

root.mainloop()