# Aidan Feess, Samuel Owen Final Project Python

import random
import math
import pickle
from tkinter import *

### Tables

colors = []
images = {}

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
    if usertype == 'member':
        user = User(name)
        pickle.dump(user, open(name,"wb"))
    elif usertype == 'admin':
        user = Admin(name)
        pickle.dump(user, open(name,"wb"))

def CreateNewUserRequest(username):
    name = str(username)
    file = open('requests.txt', 'a+')
    file.writelines(name+'\n')

def LoginUser(name):
    name = str(name)
    user = pickle.load(open(name, "rb"))
    # login stuff

#CreateNewUser(name, usertype) -- takes a username and usertype (i.e. 'aidan' and 'admin' which would be username = 'aidan' and usertype = 'admin')
#CreateNewUserRequest(username) -- takes a username and creates a request that admins can view and accept or deny
#LoginUser(name) -- takes a username and logins in as that user, giving access to whatever their usertype should see, i.e. an admin manages orders, members create them.

### GUI Functions

def switch_to_login(): ## switches to a new screen
    clear_root()
    login_screen()

def switch_to_home(): 
    clear_root()
    home_screen()

def switch_to_signup():
    clear_root()
    signup_screen()

### GUI Section

root = Tk()
root.geometry('200x150')
root.resizable(False, False)
current_objs = []

def home_screen():
    # Tkinter objects
    Title = Label(root, text="Welcome")
    Title.place(relx=0.5, rely=0.1, anchor=CENTER)

    login_button = Button(root, text='Login', padx=8.25, command=switch_to_login)
    login_button.place(x=5, y=35, anchor=W)

    signup_button = Button(root, text='Signup', padx=5, command=switch_to_signup)
    signup_button.place(x=5, y=75, anchor=W)

    quit_button = Button(root, text='Quit', command=root.destroy)
    quit_button.place(x=150,y=105, anchor=W)

    current_objs.append(signup_button)
    current_objs.append(login_button)
    current_objs.append(Title)

def login_screen():
    # Tkinter objects
    Title = Label(root, text="Login Menu")
    Title.place(relx=0.5, rely=0.1, anchor=CENTER)

    u_label = Label(root, text = 'Username:')
    u_label.place(x=0, y=25)

    u_name_box = Entry(root, border=5)
    u_name_box.place(x=65, y=25)

    back_button = Button(root, text='Back', command=switch_to_home)
    back_button.place(x=5, y=65)

    current_objs.append(u_label)
    current_objs.append(u_name_box)
    current_objs.append(Title)
    current_objs.append(back_button)
    # Function binding

    def login_user():
        username = u_name_box.get()
        print(f'Logging in as user "{username}"...')
        try:
            LoginUser(username)
        except:
            print(f"No such user as '{username}' !")

        return

    u_login = Button(root, text='Login', command=login_user)
    u_login.place(relx=0.5, y=80, anchor=CENTER)
    current_objs.append(u_login)

def signup_screen():
    # Tkinter objects
    Title = Label(root, text="Signup Menu")
    Title.place(relx=0.5, rely=0.1, anchor=CENTER)

    u_label = Label(root, text = 'Username:')
    u_label.place(x=0, y=25)

    u_name_box = Entry(root, border=5)
    u_name_box.place(x=65, y=25)

    user_types = ['Admin','Member']
    user_var = StringVar()
    user_var.set(user_types[1])

    utype = OptionMenu(root, user_var, *user_types)
    utype.place(relx=0.5, rely=.45, anchor=CENTER)

    back_button = Button(root, text='Back', command=switch_to_home)
    back_button.place(x=5, y=105)

    current_objs.append(u_label) # append the tkinter elements to the list for removal later
    current_objs.append(u_name_box)
    current_objs.append(utype)
    current_objs.append(Title)
    current_objs.append(back_button)

    # Function binding
    def get_u_name_type():
        username = u_name_box.get()
        type = user_var.get()

        if username != '' and username != ' ':
            if type.lower() == 'member' or type.lower() == 'admin':
                if type.lower() == 'member':
                    CreateNewUserRequest(username)
                    print(f"New user request created: ||{username}||")
                else:
                    CreateNewUser(username, type)
                    print(f"New administrator created: ||{username}||")
            else:
                print('Type not acceptable')
        else:
            print('Username not acceptable.')

        return

    u_signup = Button(root, text='Signup', command=get_u_name_type)
    u_signup.place(relx=0.5, rely=0.8, anchor=CENTER)
    current_objs.append(u_signup)

def clear_root():
    for item in current_objs:
        try: item.destroy() # destroy the object
        except: current_objs.remove(item) # if you can't, remove it from the list of objects.
        
home_screen()

root.mainloop()

# TODO:     1. Add a user accept screen for the admin users and a screen for orders
#               1a. Area to approve orders 
#               1b. Area to create t-shirt designs (list color, a description, and the size)
#               1c. Area to create bills
