# Aidan Feess, Samuel Owen Final Project Python

import random
import math
import pickle
from tkinter import *
import os

## Create neccessary files

def createnewfile(filename):
    try:
        with open(f'{filename}.txt', 'r') as file:
            file.read()
            file.close()
    except:
        with open(f'{filename}.txt', 'w+') as file:
            file.write('a')
            file.truncate(0)
            file.close()

createnewfile('colors')
createnewfile('designs')
createnewfile('requests')
createnewfile('ordervar')

with open('ordervar.txt','r') as file:
    text = file.read()
    if text == '' or text == ' ':
        file.close()
        with open('ordervar.txt', 'w') as file:
            file.write('0')
            file.close()

### Classes Section

# prices: hat = $1.75, shirt = $3.25

class Admin(): ## admin class
    def __init__(self, username):
        self.priv = 'admin'
        self.username = username

    def give_name(self, name):
        self.username = name
        SaveNewInfoToUser(self, self.username)

    def get_type(self):
        return self.priv

    def get_name(self):
        return self.username

class User(): ## member class
    def __init__(self, username, designs = []):
        self.priv = 'member'
        self.username = username
        self.designs = designs # list of lists (a design is a list that holds color and design)
        self.orders = []

    def give_name(self, name):
        self.username = name
        SaveNewInfoToUser(self, self.username)

    def give_new_design(self, design):
        self.designs.append(design)
        SaveNewInfoToUser(self, self.username)

    def give_new_order(self, order):
        self.orders.append(order)
        SaveNewInfoToUser(self, self.username)

    def remove_order(self, order):
        self.orders.remove(order)
        SaveNewInfoToUser(self, self.username)

    def get_designs(self):
        return self.designs

    def get_orders(self):
        return self.orders

    def get_type(self):
        return self.priv

    def get_name(self):
        return self.username

### Misc Functions Section

def ChangeOrderVar(amt):
    with open('ordervar.txt', 'r') as file:
        ordervar = file.read()
        ordervar = int(ordervar)+amt
        ordervar = str(ordervar)
        file.close()
    with open('ordervar.txt', 'w') as file:
        file.truncate(0)
        file.writelines(ordervar)
        file.close()

def GetOrderVar():
    with open('ordervar.txt', 'r') as file:
        ordervar = int(file.read())
        file.close()
        return ordervar

def CreateNewUser(name, usertype):
    name = str(name)
    usertype=usertype.lower()
    if usertype == 'member':
        user = User(name)
        pickle.dump(user, open(name,"wb"))
    elif usertype == 'admin':
        user = Admin(name)
        pickle.dump(user, open(name,"wb"))

def SaveNewInfoToUser(user, username):
    pickle.dump(user, open(username, 'wb'))

def CreateNewUserRequest(username):
    name = str(username)
    file = open('requests.txt', 'a+')
    file.writelines(name+'\n')

def CreateOrderRequest(user, owner, tshirts=0, hats=0, price=0, shirt_types=None, hat_types=None):
    ordervar = GetOrderVar()
    owner = 'Orderer: '+owner
    tshirts = "Shirts: "+str(tshirts)
    hats = 'Hats: '+str(hats)
    price = 'Price: $'+str(price)
    if shirt_types == None: shirt_types = 'None'
    else:
        shirt_types = str(shirt_types)
        shirt_types = shirt_types.strip(")")
        shirt_types = shirt_types.strip('(')
    if hat_types == None: hat_types = 'None'
    else: hat_types = str(hat_types)
    elementlist = [owner, tshirts, hats, price, shirt_types, hat_types, 'Status: Pending']
    createnewfile(f'order{ordervar}')
    with open(f'order{ordervar}.txt', 'w') as file:
        for element in elementlist:
            if element == 'None':
                pass
            else:
                file.writelines(element+'\n')
    user.give_new_order(f'order{ordervar}')
    ChangeOrderVar(1)

def LoginUser(name):
    name = str(name)
    user = pickle.load(open(name, "rb"))
    switch_to_logged_in(user.get_type(), user)

def get_user(username):
    user = pickle.load(open(username, "rb"))
    return user

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

def switch_to_logged_in(utype, user):
    clear_root()
    logged_in_screen(utype, user)

### GUI Section

root = Tk()
root.geometry('200x150')
root.resizable(False, False)
current_objs = []

def appendtolist(objs):
    for obj in objs:
        current_objs.append(obj)

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

    appendtolist([signup_button, login_button, Title])

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
    # Function binding

    def login_user():
        username = u_name_box.get()
        print(f'Logging in as user "{username}"...')
        LoginUser(username)
        try:
            LoginUser(username)
        except:
            print(f"No such user as '{username}' !")

        return

    u_login = Button(root, text='Login', command=login_user)
    u_login.place(relx=0.5, y=80, anchor=CENTER)

    appendtolist([u_login, u_label, u_name_box, Title, back_button])

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

    appendtolist([u_label, u_name_box, utype, Title, back_button,u_signup])

def logged_in_screen(utype, user):
    utype = utype.upper()
    Title = Label(root, text=f"LOGGED IN AS {utype}")
    Title.place(relx=0.5, rely=0.1, anchor=CENTER)
    appendtolist([Title])

    def reset_screen(): # allows for multiple things to be viewed over time
        for item in current_objs:
            if item != Title:
                try: item.destroy() 
                except: current_objs.remove(item) 

    if utype == 'ADMIN':
        def default():
            reset_screen()

            view_types = ['View Requests', 'View Orders', 'Create Designs'] # User requests, orders, create designs, create bills
            view_var = StringVar()
            view_var.set(view_types[0])
            
            new_view = OptionMenu(root, view_var, *view_types)
            new_view.place(relx=0.5, rely=.45, anchor=CENTER)

            def view_new():
                new_screen = view_var.get()
                reset_screen()
                if new_screen == 'View Requests':
                    show_user_requests()
                elif new_screen == 'Create Designs':
                    show_create_designs()
                elif new_screen == 'View Orders':
                    show_order_requests()

            change_scrn = Button(root, text='View', command=view_new)
            change_scrn.place(relx=0.5, rely=0.8, anchor=CENTER)

            logout = Button(root, text='Logout', command=switch_to_login)
            logout.place(x=150,y=130, anchor=W)

            appendtolist([logout, new_view, change_scrn])
        default()
    elif utype == 'MEMBER':
        def default():
            reset_screen()

            view_types = ['Create Custom Design', 'Order Items', 'View Orders'] # Create T-Shirt or hat, Order T-Shirt or hat, View Orders
            view_var = StringVar()
            view_var.set(view_types[1])
            
            new_view = OptionMenu(root, view_var, *view_types)
            new_view.place(relx=0.5, rely=.45, anchor=CENTER)

            def view_new():
                new_screen = view_var.get()
                reset_screen()
                if new_screen == 'Create Custom Design':
                    show_tshirt_creator()
                elif new_screen == 'Order Items':
                    show_create_orders()
                elif new_screen == 'View Orders':
                    show_view_orders()

            change_scrn = Button(root, text='View', command=view_new)
            change_scrn.place(relx=0.5, rely=0.8, anchor=CENTER)

            logout = Button(root, text='Logout', command=switch_to_login)
            logout.place(x=150,y=130, anchor=W)

            appendtolist([logout, new_view, change_scrn])
        default()

    def show_user_requests():
        u_list_text = Label(root, text=f"User Requests:")
        u_list_text.place(relx=0.1, rely=0.2, anchor=W)

        back = Button(root, text='Back', command=default)
        back.place(x=150,y=80, anchor=W)

        file = open('requests.txt', 'r')
        user_list = Listbox(root, height=5, selectmode=SINGLE)
        for line in file:
            user_list.insert(END, str(line))
        user_list.place(anchor=W, y=80)
        file.close()

        def cmd_accept():
            selected = user_list.curselection()
            name = user_list.get(selected)
            namel = list(name) # replace and strip functions not working, had to make custom one
            for letter in range(len(namel)): #namel = namelist
                if letter == len(namel) or letter == len(namel)-1:
                    namel.remove(namel[letter])
            name = ''
            for letter in namel:
                name = name + letter
            try:
                CreateNewUser(name, 'member')
                user_list.delete(selected)
                selected = selected[0]
                with open('requests.txt', 'r') as file:
                    lines = file.readlines()
                    file.close()
                del lines[selected]
                with open('requests.txt', 'w+') as file:
                    for line in lines:
                        file.write(line)
                    file.close()
            except:
                print('ERR: Could not create user.')
            
        def cmd_deny():
            selected = user_list.curselection()
            name = user_list.get(selected)
            namel = list(name) # replace and strip functions not working, had to make custom one
            for letter in range(len(namel)): #namel = namelist
                if letter == len(namel) or letter == len(namel)-1:
                    namel.remove(namel[letter])
            name = ''
            for letter in namel:
                name = name + letter
            try:
                user_list.delete(selected)
                selected = selected[0]
                with open('requests.txt', 'r') as file:
                    lines = file.readlines()
                    file.close()
                del lines[selected]
                with open('requests.txt', 'w+') as file:
                    for line in lines:
                        file.write(line)
                    file.close()
            except:
                print('ERR: Could not deny user.')

        accept = Button(root, text='Accept', command=cmd_accept)
        accept.place(x=5,y=135, anchor=W)

        deny = Button(root, text='Deny', command=cmd_deny)
        deny.place(x=60,y=135, anchor=W)

        appendtolist([user_list, u_list_text, accept, deny, back])

    def show_create_designs():
        back = Button(root, text='Back', command=default)
        back.place(x=150,y=80, anchor=W)

        def make_new_CLORDS():  # CLORDS means Color or Design
            choicetype = choice_var.get()
            if choicetype == 'New color':
                with open('colors.txt', 'a+') as file:
                    file.writelines(CLORDS_entry.get()+'\n')
                    file.close()
            elif choicetype == 'New design':
                with open('designs.txt', 'a+') as file:
                    file.writelines(CLORDS_entry.get()+'\n')
                    file.close()

        choices = ['New color','New design']
        choice_var = StringVar()
        choice_var.set(choices[0])
        new_CLORDS = OptionMenu(root, choice_var, *choices)
        new_CLORDS.place(relx=.5, rely=.3, anchor=CENTER)

        CLORDS_entry = Entry(root)
        CLORDS_entry.place(anchor=CENTER, relx=.5, rely=.5)

        CLORDS_button = Button(root, text='Submit', command=make_new_CLORDS)
        CLORDS_button.place(anchor=CENTER, relx=.5, rely=.7)
        appendtolist([new_CLORDS,CLORDS_entry,CLORDS_button,back])

    def show_tshirt_creator():
        back = Button(root, text='Back', command=default)
        back.place(x=150,y=80, anchor=W)

        ## COLORS
        c_label = Label(root, text = 'Choose color.')
        c_label.place(relx=.025, rely=.2, anchor=W)

        colors_list = []
        with open('colors.txt', 'r') as file:
            for line in file:
                colors_list.append(line)
        color_var = StringVar()
        color_var.set(colors_list[0])

        tshirtcolor = OptionMenu(root, color_var, *colors_list)
        tshirtcolor.place(relx=0.025, rely=.4, anchor=W)

        ## DESIGNS
        d_label = Label(root, text = 'Choose design.')
        d_label.place(relx=.4, rely=.2, anchor=W)

        designs_list = []
        with open('designs.txt', 'r') as file:
            for line in file:
                designs_list.append(line)
        design_var = StringVar()
        design_var.set(designs_list[0])

        tshirtdesign = OptionMenu(root, design_var, *designs_list)
        tshirtdesign.place(relx=0.4, rely=.4, anchor=W)

        def createdesign():
            color=color_var.get()
            color = str(color)
            color = color.strip('\n')
            picture=design_var.get()
            picture = str(picture)
            picture = picture.strip('\n')
            user.give_new_design([color, picture])

        create_design_button = Button(root, text='Create design', command=createdesign)
        create_design_button.place(anchor=CENTER, relx=.5, rely=.8)
        
        appendtolist([back, tshirtcolor, tshirtdesign, d_label, c_label, create_design_button])

    def show_create_orders():
        def placeorder():
            owner = user.get_name()
            if 'T-Shirt' in ordervar.get(): # tshirt or hat identifier
                tshirts = orderamt.get()
                hats = 0
                price = 3.25*int(tshirts)
                shirttype = orderdesignsvar.get(), ordervar.get()[-1]
                hattype = None
            else:
                hats = orderamt.get()
                tshirts = 0
                price = 1.75*int(hats)
                hattype = orderdesignsvar.get()
                shirttype = None
            
            CreateOrderRequest(user, owner, tshirts, hats, price, shirt_types=shirttype, hat_types=hattype)

        back = Button(root, text='Back', command=default)
        back.place(x=150,y=130, anchor=W)
        ordermenu_label = Label(root, text='Order Type:')
        ordermenu_label.place(anchor=CENTER, rely=.25, relx=.25)

        ordertypes = ['T-Shirt S', 'T-Shirt M', 'T-Shirt L', 'Hat']
        ordervar = StringVar()
        ordervar.set(ordertypes[0])

        ordermenu = OptionMenu(root, ordervar, *ordertypes)
        ordermenu.place(anchor=CENTER, rely=.45, relx=.25)

        try: orderdesigns = user.get_designs()
        except: orderdesigns = ['White, Plain']
        
        orderdesignsvar = StringVar()
        try: orderdesignsvar.set(orderdesigns[0])
        except: orderdesigns = ['White, Plain']; orderdesignsvar.set(orderdesigns[0])

        orderdesignsmenu = OptionMenu(root, orderdesignsvar, *orderdesigns)
        orderdesignsmenu.place(anchor=CENTER, rely=.65, relx=.25)

        orderamt_label = Label(root, text='Order Amount:')
        orderamt_label.place(anchor=CENTER, rely=.25, relx=.75)

        orderamt = Entry(root)
        orderamt.place(anchor=CENTER, rely=.45, relx=.75)

        orderbut = Button(root, text="Place order", command = placeorder)
        orderbut.place(anchor=CENTER, y=130, relx=.5)

        appendtolist([back, ordermenu_label, orderamt_label, ordermenu, orderbut, orderamt, orderdesignsmenu])

    def show_view_orders():
        back = Button(root, text='Back', command=default)
        back.place(x=150,y=130, anchor=W)

        view_selector_label = Label(root, text='Your orders:')
        view_selector_label.place(anchor=W, x=5, rely=.2)

        def view_info():
            filename = selection_var.get()
            with open(f'{filename}.txt', 'r') as file:
                box.delete('1.0', END)
                for line in file:
                    box.insert(END, line)
                file.close()

        try: 
            selections = user.get_orders()
            selection_var = StringVar()
            selection_var.set(selections[0])

            selections_menu = OptionMenu(root, selection_var, *selections)
            selections_menu.place(anchor=W, x=5, rely=.4)

            view_button = Button(root, text="View Contents", command=view_info)
            view_button.place(anchor=E, relx=.95, rely=.4)

            appendtolist([selections_menu, view_button])

            box = Text(root, height = 4, width=15)
            box.place(anchor=W, x=5, rely=.75)
        except:
            box = Text(root, height = 5, width=15)
            box.insert(END, "No orders yet, come back when you've ordered something!")
            box.place(anchor=W, x=5, rely=.6)

        appendtolist([view_selector_label, box, back])

    def show_order_requests():
        back = Button(root, text='Back', command=default)
        back.place(x=150,y=130, anchor=W)

        view_selector_label = Label(root, text='Orders:')
        view_selector_label.place(anchor=W, x=5, rely=.2)

        def view_info():
            filename = selection_var.get()
            with open(f'{filename}', 'r') as file:
                box.delete('1.0', END)
                for line in file:
                    box.insert(END, line)
                file.close()

        def view_info_wVar(boxitem):
            filename = selection_var.get()
            with open(f'{filename}', 'r') as file:
                boxitem.delete('1.0', END)
                for line in file:
                    boxitem.insert(END, line)
                file.close()

        def accept_order():
            box1 = Text(root, height=3, width=9)
            box1.place(anchor=CENTER, relx=.25, rely=.425)
            box2 = Text(root, height=3, width=9)
            box2.place(anchor=CENTER, relx=.75, rely=.425)
            back = Button(root, text='Back', command=default)
            back.place(x=150,y=130, anchor=W)
            view_info_wVar(box1)
            labelbox1 = Label(root, text='Info')
            labelbox1.place(anchor=CENTER, relx=.25, rely=.2)
            labelbox2 = Label(root, text='Make bill')
            labelbox2.place(anchor=CENTER, relx=.75, rely=.2)

            order = selection_var.get()
            def modify_order():
                with open(order, 'w') as file:
                    file.truncate(0)
                    text=box2.get("1.0",END)
                    file.write(text)
                    file.close()
            confirm_button = Button(root, text="Confirm", command=modify_order)
            confirm_button.place(anchor=W, x=5, rely=.75)
            reset_screen()
            appendtolist([box1, box2, back, labelbox1, labelbox2, confirm_button])

        def deny_order():
            order = selection_var.get()
            with open(order, 'r') as file:
                for line in file:
                    if 'Orderer' in line:
                        username = line[9:-1]
                file.close()
            user=get_user(username)
            order = order.strip('.txt')
            user.remove_order(order)
            os.remove(f'{order}.txt')
            ChangeOrderVar(-1)
            selections.remove(f'{order}.txt')
            box.delete('1.0', END)

        def check_accepted(order):
            with open(order, 'r') as file:
                for line in file:
                    if 'accepted' in line.lower():
                        return False
                return True

        try: 
            selections = []
            files = os.listdir('.')
            for file in files:
                if '.txt' in file:
                    if 'order' in file:
                        if file != 'ordervar.txt':
                            if check_accepted(file):
                                selections.append(file)
            selection_var = StringVar()
            selection_var.set(selections[0])

            selections_menu = OptionMenu(root, selection_var, *selections)
            selections_menu.place(anchor=W, x=5, rely=.4)

            view_button = Button(root, text="View", command=view_info)
            view_button.place(anchor=W, relx=.5, rely=.4)

            accept_button = Button(root, text="Accept", command=accept_order)
            accept_button.place(anchor=W, x=150,y=55)

            deny_button = Button(root, text="Deny", command=deny_order)
            deny_button.place(anchor=W, x=150,y=80)

            appendtolist([selections_menu, accept_button, view_button, deny_button])

            box = Text(root, height = 4, width=15)
            box.place(anchor=W, x=5, rely=.75)
        except:
            box = Text(root, height = 5, width=15)
            box.insert(END, "No orders yet.")
            box.place(anchor=W, x=5, rely=.6)

        appendtolist([view_selector_label, box, back])

def clear_root():
    for item in current_objs:
        try: item.destroy() # destroy the object
        except: current_objs.remove(item) # if you can't, remove it from the list of objects.
        
home_screen()

root.mainloop()