from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
import base64
import urllib
import time
import datetime
import random
#from dateutil import parser
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
'''


import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *'''

root = Tk()
canvas = Canvas(root, width = 300, height = 400)
canvas.pack()
img = PhotoImage(file="money1.gif")
canvas.create_image(20,20, anchor=NW, image=img)
root.title("Budget Tracker")



width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")



USERNAME = StringVar()
PASSWORD = StringVar()
BUD_GET = IntVar()
EXP_TYPE = StringVar()
EXP_COST = IntVar()
AMT_LEFT = IntVar()
SEARCH = StringVar()



def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `expenses` (expense_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, expense_name TEXT,expense_budget TEXT, expense_cost TEXT, expense_amt TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'user' AND `password` = '4562'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('user', '4562')")
        conn.commit()


def Exit():
    result = tkMessageBox.askquestion('Budget Tracker', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('BUDGET TRACKER', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()

def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Budget Tracker/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()

def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="User Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

def Home():
    global Home
    Home = Tk()
    Home.title("Budget Tracker/Home")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="BUDGET TRACKER", font=('arial', 45))
    lbl_display.pack()
    '''MidAddNew1 = Frame(addnewform, width=600)
    MidAddNew1.pack(side=TOP, pady=50)
    lbl_qty11 = Label(MidAddNew, text="Budget:", font=('arial', 25), bd=10)
    lbl_qty11.grid(row=1, sticky=W)
    productname11 = Entry(MidAddNew, textvariable=BUD_GET, font=('arial', 25), width=15)
    productname11.grid(row=3, column=1)'''
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new budget", command=AddBudget)

    filemenu2.add_command(label="Add new expense", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Profile", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="#6666ff")

'''def start():
    global start
    name = tk.DoubleVar()
    name_w = tk.Toplevel(root)
    name_w.wm_title("Enter name")
    f1 = tk.Frame(name_w)
    f1.pack()
    L1 = tk.Label(f1, text="Please enter your name!")
    L1.grid(row=0, column=0)
    E1 = tk.Entry(f1, textvariable=name)
    E1.grid(row=1, column=0)
    N1 = tk.Button(f1, text="Next", command = Q1)
    N1.grid(row=2, column=0)'''

def AddBudget():
    global budgetform
    global productname11
    budgetform = Toplevel()
    budgetform.title("Budget Tracker/Add new Budget")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    budgetform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    budgetform.resizable(0, 0)
    BudgetForm()

def BudgetForm():
    TopAddNew1 = Frame(budgetform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew1.pack(side=TOP, pady=20)
    lbl_text1 = Label(TopAddNew1, text="Add New Budget", font=('arial', 18), width=600)
    lbl_text1.pack(fill=X)
    MidAddNew1 = Frame(budgetform, width=600)
    MidAddNew1.pack(side=TOP, pady=50)
    lbl_productname11 = Label(MidAddNew1, text="Intial Budget:", font=('arial', 25), bd=10)
    lbl_productname11.grid(row=0, sticky=W)

    productname11 = Entry(MidAddNew1, textvariable=BUD_GET, font=('arial', 25), width=15)
    productname11.grid(row=0, column=1)

    btn_add1 = Button(MidAddNew1, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=ShowAddNew)
    btn_add1.grid(row=1, columnspan=2, pady=20)

def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Budget Tracker/Add new expense")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Expense", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddNew, text="Expense Type:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    lbl_qty1 = Label(MidAddNew, text="Budget:", state="disabled", font=('arial', 25), bd=10)
    lbl_qty1.grid(row=1, sticky=W)
    lbl_qty = Label(MidAddNew, text="Expense:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=2, sticky=W)
    '''lbl_price = Label(MidAddNew, text="Amount left:", font=('arial', 25), bd=10)
    lbl_price.grid(row=3, sticky=W)'''
    productname = Entry(MidAddNew, textvariable=EXP_TYPE,font=('arial', 25), width=15)
    productname.grid(row=0, column=1)
    productname1 = Entry(MidAddNew, textvariable=BUD_GET,state="disabled",font=('arial', 25), width=15)
    productname1.grid(row=1, column=1)
    productqty = Entry(MidAddNew, textvariable=EXP_COST, font=('arial', 25), width=15)
    productqty.grid(row=2, column=1)
    '''productprice = Entry(MidAddNew, textvariable=AMT_LEFT, font=('arial', 25), width=15)
    productprice.grid(row=3, column=1)'''



    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=5, columnspan=2, pady=20)


def AddNew():
    Database()
    cursor.execute("INSERT  INTO  `expenses` (expense_name, expense_budget, expense_cost, expense_amt) VALUES(?, ?, ?, ?)", (str(EXP_TYPE.get()),int(BUD_GET.get()), int(EXP_COST.get()),(int(BUD_GET.get())-int(EXP_COST.get()))))
    '''Label(MidAddNew,text=(int(BUD_GET.get())-int(EXP_COST.get()))).grid(row=4,sticky=W)'''

    conn.commit()
    EXP_TYPE.set("")

    BUD_GET.set("")
    EXP_COST.set("")
    '''f=(int(BUD_GET.get())-int(EXP_COST.get()))'''
    AMT_LEFT.set("")


    cursor.close()
    conn.close()

def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Expenses", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ExpenseID","Expense Type", "Budget", "Expense", "Amount left"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ExpenseID', text="ExpenseID",anchor=W)

    tree.heading('Expense Type', text="Expense Type",anchor=W)
    tree.heading('Budget', text="Budget",anchor=W)
    tree.heading('Expense', text="Expense",anchor=W)
    tree.heading('Amount left', text="Amount left",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `expenses`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `expenses` WHERE `expense_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset():
    tree.delete(tree.get_children())
    DisplayData()
    SEARCH.set("")

def Delete():
    if not tree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('BUDGET TRACKER', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `expenses` WHERE `expense_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("BUDGET TRACKER/View Expense")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)

    #try:
    ViewForm()
    graph_data()
    
    graph_data2()
    
    #except Exception as e:
        #print(e)

def Logout():
    result = tkMessageBox.askquestion('BUDGET TRACKER', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()

def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()
def graph_data():

    Database()

    cursor.execute('SELECT expense_name,expense_cost FROM expenses ORDER BY expense_amt DESC ')
    data = cursor.fetchall()
    print(data)
    type1= []
    cost1 = []

    for row in data:
        type1.append(row[0])
        cost1.append(row[1])
    colors = ['gold', 'yellowgreen', 'lightcoral']
      # explode 1st slice
 
# Plot
    f1=plt.figure(1)
    plt.subplot(2,1,1)
    plt.pie(cost1, labels=type1, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    

    plt.subplot(2,2,3)
    plt.bar(type1,cost1,align='center',alpha=0.5)
    

    plt.subplot(2,2,4)
    plt.plot_date(type1,cost1,'-')

    Database()

    cursor.execute('SELECT expense_name,expense_amt FROM expenses ')
    data = cursor.fetchall()
    print(data)
    type1= []
    cost1 = []
    

    for row in data:
        type1.append(row[0])
        cost1.append(row[1])
    colors = ['gold', 'yellowgreen', 'lightcoral']
      # explode 1st slice
 
# Plot
    f1=plt.figure(2)
    plt.subplot(2,1,1)
    plt.pie(cost1, labels=type1, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    

    plt.subplot(2,2,3)
    plt.bar(type1,cost1,align='center',alpha=0.5)
    

    plt.subplot(2,2,4)
    plt.plot_date(type1,cost1,'-')
    plt.show()

    
    
    graph_data2()
def graph_data2():

    Database()

    cursor.execute('SELECT expense_name,expense_amt FROM expenses ORDER BY expense_amt DESC')
    data = cursor.fetchall()
    print(data)
    type1= []
    cost1 = []

    for row in data:
        type1.append(row[0])
        cost1.append(row[1])
    colors = ['gold', 'yellowgreen', 'lightcoral']
      # explode 1st slice
 
# Plot
    plt.pie(cost1, labels=type1, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)

    
    plt.show()
def graph_data1():
    Database()

    cursor.execute('SELECT expense_name,expense_cost FROM expenses ORDER BY expense_cost DESC')
    data = cursor.fetchall()
    print(data)
    
 
    objects = []
    performance=[]
    for row in data:
        objects.append(row[0])
        performance.append(row[1])
        
    y_pos = np.arange(len(objects))
    
     
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Expense')
    plt.title('Types')
     
    plt.show()


#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

#========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Budget Tracker", font=('arial', 45))
lbl_display.pack()

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()

