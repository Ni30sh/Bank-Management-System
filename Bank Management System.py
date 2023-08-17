from tkinter import *
from tkinter import Toplevel, messagebox
import time
import mysql.connector
import random

def open_account():
    def submit_data():
        global conn, cur
        account_val = ACCOUNT.get()
        name_val = NAME.get()
        aadhar_val = AADHAR.get()
        dob_val = DOB.get()
        address_val = ADDRESS.get()
        contact_val = CONTACT.get()
        email_val = EMAIL.get()
        openingbalance_val = OPNINGBLANCE.get()
        date = time.strftime("%d-%m-%Y")

        strn = "USE bank_manegement"
        cur.execute(strn)

        strn = "SELECT * FROM ACCOUNTS WHERE account = %s"
        cur.execute(strn, (account_val,))
        existing_data = cur.fetchall()
        if existing_data :
            messagebox.showinfo("Notification", "Account Already Exist. !")
        else:
            values1 = (
             account_val, name_val, aadhar_val, dob_val, address_val, contact_val, email_val, openingbalance_val, date)
            strn = "INSERT INTO ACCOUNTS VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(strn, values1)
            values2 = (aadhar_val, openingbalance_val)
            strn1 = "INSERT INTO AMOUNT VALUES (%s, %s)"
            cur.execute(strn1, (values2))
            conn.commit()
            message = messagebox.askyesnocancel("Notification", "ACCOUNT OPEN SUCCESSFULLY... WANT TO CLEAR THE FORM")
            if message == True:
                ACCOUNT.set("")
                NAME.set("")
                AADHAR.set("")
                DOB.set("")
                ADDRESS.set("")
                CONTACT.set("")
                EMAIL.set("")
                OPNINGBLANCE.set("")

    root = Toplevel()
    root.grab_set()
    root.geometry("450x450+800+130")  # W X H
    root.title("Admission Shell")
    # root.iconbitmap()
    root.resizable(False, False)
    root.config(bg="white")
    #####################################____________________________________

    suggest_label = Label(root, text="To Open New Account ", bg="white",
                          font=("Time in romana", 14, "bold"))
    suggest_label.place(x=16, y=10)
    id_label = Label(root, text="ACCOUNT  :", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"))
    id_label.place(x=17, y=60)
    name_label = Label(root, text="NAME :", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"))
    name_label.place(x=17, y=95)
    aadhar_label = Label(root, text="AADHAR :", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"))
    aadhar_label.place(x=17, y=130)
    mobile_label = Label(root, text="DOB :", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"))
    mobile_label.place(x=17, y=165)
    address_label = Label(root, text="ADDRESS :", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"))
    address_label.place(x=17, y=200)
    dob_label = Label(root, text="CONTACT :", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"))
    dob_label.place(x=17, y=235)
    email_label = Label(root, text="EMAIL :", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"))
    email_label.place(x=17, y=270)
    gender_label = Label(root, text="OPENING BAL. :", bg="white", font=("Microsoft YaHei UI Light", 12, "bold"))
    gender_label.place(x=17, y=305)
    # _______________________________________________________________________________________________________________

    ACCOUNT = StringVar()
    NAME = StringVar()
    AADHAR = StringVar()
    DOB = StringVar()
    ADDRESS = StringVar()
    CONTACT = StringVar()
    EMAIL = StringVar()
    OPNINGBLANCE = StringVar()
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    id_entry = Entry(root, textvariable=ACCOUNT, width=21, fg="blue", bd=0,
                     font=("Microsoft YaHei UI Light", 13, "bold"))
    id_entry.place(x=200, y=60)
    Frame(root, width=210, height=2, bg="black").place(x=200, y=83)

    name_entry = Entry(root, textvariable=NAME, width=21, fg="blue", bd=0,
                       font=("Microsoft YaHei UI Light", 13, "bold"))
    name_entry.place(x=200, y=95)
    Frame(root, width=210, height=2, bg="black").place(x=200, y=118)

    aadhar_entry = Entry(root, textvariable=AADHAR, width=21, fg="blue", bd=0,
                         font=("Microsoft YaHei UI Light", 13, "bold"))
    aadhar_entry.place(x=200, y=130)
    Frame(root, width=210, height=2, bg="black").place(x=200, y=153)

    mobile_entry = Entry(root, textvariable=DOB, width=21, fg="blue", bd=0,
                         font=("Microsoft YaHei UI Light", 13, "bold"))
    mobile_entry.place(x=200, y=165)

    Frame(root, width=210, height=2, bg="black").place(x=200, y=188)

    address_entry = Entry(root, textvariable=ADDRESS, width=21, fg="blue", bd=0,
                          font=("Microsoft YaHei UI Light", 13, "bold"))
    address_entry.place(x=200, y=200)
    #
    Frame(root, width=210, height=2, bg="black").place(x=200, y=223)
    #

    dob_entry = Entry(root, textvariable=CONTACT, width=21, fg="blue", bd=0,
                      font=("Microsoft YaHei UI Light", 13, "bold"))
    dob_entry.place(x=200, y=235)

    Frame(root, width=210, height=2, bg="black").place(x=200, y=258)

    email_entry = Entry(root, textvariable=EMAIL, width=21, fg="blue", bg="white", bd=0,
                        font=("Microsoft YaHei UI Light", 13, "bold"))
    email_entry.place(x=200, y=270)

    Frame(root, width=210, height=2, bg="black").place(x=200, y=293)

    password_entry = Entry(root, textvariable=OPNINGBLANCE, width=21, fg="blue", bg="white", bd=0,
                           font=("Microsoft YaHei UI Light", 13, "bold"))
    password_entry.place(x=200, y=305)
    Frame(root, width=210, height=2, bg="black").place(x=200, y=328)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    submit_btn = Button(root, text="SUBMIT", font=("time in romana", 12, "bold"), activeforeground="white",
                        activebackground="blue", bg="#00bfff", command=submit_data, fg="white")
    submit_btn.place(x=120, y=384, width=200, height=40)

    root.mainloop()


#
def WITHDRAWAL_money():
    entry_aadhar = StringVar()
    entry_amount = StringVar()

    def withdraw_amount():
        global conn, cur
        aadhar_no = entry_aadhar.get()
        amount = entry_amount.get()

        strn = "USE bank_manegement"
        cur.execute(strn)

        strn = "SELECT balance FROM amount WHERE aadhar = %s"
        cur.execute(strn, (aadhar_no,))
        results = cur.fetchall()

        if results:
            account_balance = results[0][0]

            if int(amount) <= account_balance:
                # Withdrawal successful
                updated_balance = account_balance - int(amount)
                sql = "UPDATE amount SET balance = %s  where aadhar = %s"
                data = (updated_balance, aadhar_no)
                cur.execute(sql, data)
                conn.commit()
                messagebox.showinfo("Success", f"Withdrawal successful! Account balance: {updated_balance}")
            else:
                messagebox.showerror("Insufficient Balance", "Withdrawal amount exceeds account balance.")
        else:
            messagebox.showerror("Invalid Aadhar No", "No account with this Aadhar number.")

    # Create Tkinter window

    root3 = Toplevel()
    root3.geometry('310x270+600+200')
    root3.resizable(False, False)
    root3.title("Withdrawal Window")

    aadhar_label = Label(root3, text="Withdrawal By Aadhar and Amount", font=("chiller", 10, "bold"))
    aadhar_label.place(x=10, y=8)

    aadhar_label = Label(root3, text="AADHAR :", font=("chiller", 10, "bold"))
    aadhar_label.place(x=20, y=40)

    aadhar_entry = Entry(root3, textvariable=entry_aadhar, bd=0, font=("chiller", 13, "bold"))
    aadhar_entry.place(x=20, y=70, width=215, height=25)
    Frame(root3, width=215, height=2, bg="black").place(x=20, y=93)

    amount_label = Label(root3, text="AMOUNT : ", font=("chiller", 10, "bold"))
    amount_label.place(x=20, y=108)

    amount_entry = Entry(root3, textvariable=entry_amount, bd=0, font=("chiller", 13, "bold"))
    amount_entry.place(x=20, y=135, width=215, height=25)
    Frame(root3, width=215, height=2, bg="black").place(x=20, y=158)

    submit_btm = Button(root3, text="SUBMIT", command=withdraw_amount, font=("chiller", 12, "bold"),
                        bg="dark blue", activeforeground="black",
                        activebackground="white", fg="white")
    submit_btm.place(x=100, y=190, width=100)

    root3.mainloop()


def deposit_money():
    entry_aadhar = StringVar()
    entry_amount = StringVar()

    def deposit_amount():
        global conn, cur
        aadhar_no = entry_aadhar.get()
        amount = entry_amount.get()

        strn = "USE bank_manegement"
        cur.execute(strn)

        strn = "SELECT balance FROM amount WHERE aadhar = %s"
        cur.execute(strn, (aadhar_no,))
        results = cur.fetchall()

        if results:
            account_balance = results[0][0]
            updated_balance = account_balance + int(amount)
            sql = "UPDATE amount SET balance = %s  where aadhar = %s"
            data = (updated_balance, aadhar_no)
            cur.execute(sql, data)
            conn.commit()
            messagebox.showinfo("Deposit Window",
                                f"Deposit successful! Account balance: {updated_balance} of Aadhar Number : {aadhar_no}")
        else:
            messagebox.showerror("Invalid Aadhar No", "No Account with this Aadhar number.")

    # Create Tkinter window

    root4 = Toplevel()
    root4.geometry('310x270+600+200')
    root4.resizable(False, False)
    root4.title("Deposit Window")

    aadhar_label = Label(root4, text="Deposit with Aadhar and Amount", font=("chiller", 10, "bold"))
    aadhar_label.place(x=10, y=8)

    aadhar_label = Label(root4, text="AADHAR :", font=("chiller", 10, "bold"))
    aadhar_label.place(x=20, y=40)

    aadhar_entry = Entry(root4, textvariable=entry_aadhar, bd=0, font=("chiller", 13, "bold"))
    aadhar_entry.place(x=20, y=70, width=215, height=25)
    Frame(root4, width=215, height=2, bg="black").place(x=20, y=93)

    amount_label = Label(root4, text="AMOUNT : ", font=("chiller", 10, "bold"))
    amount_label.place(x=20, y=108)

    amount_entry = Entry(root4, textvariable=entry_amount, bd=0, font=("chiller", 13, "bold"))
    amount_entry.place(x=20, y=135, width=215, height=25)
    Frame(root4, width=215, height=2, bg="black").place(x=20, y=158)

    submit_btm = Button(root4, text="SUBMIT", command=deposit_amount, font=("chiller", 12, "bold"),
                        bg="dark blue", activeforeground="black",activebackground="white", fg="white")
    submit_btm.place(x=100, y=190, width=100)
    root4.mainloop()


def show_balance():
    entry_aadhar = StringVar()
    def show_balance():
        global conn, cur

        strn = "USE bank_manegement"
        cur.execute(strn)

        aadhar_no = entry_aadhar.get()
        strn = "SELECT balance FROM amount WHERE aadhar = %s"
        cur.execute(strn, (aadhar_no,))
        result = cur.fetchall()

        if result:
            balance = result[0]
            messagebox.showinfo("Bank Balance", f"The Balance of Aadhar {aadhar_no} is {balance}")
        else:
            messagebox.showinfo("Bank Balance", "No Open Account of this Aadhar Number")

    root1 = Toplevel()
    root1.geometry('390x200+900+300')
    root1.resizable(False, False)
    root1.title("Balance Window")

    sugest_label = Label(root1, text="To Know Your Bank Balance Enter Aadhar Number", font=("chiller", 10, "bold"))
    sugest_label.pack(ipadx=10, ipady=5, )
    aadhar_label = Label(root1, text="Aadhar Number :", font=("chiller", 10, "bold"))
    aadhar_label.pack(ipady=15)
    # #####################################################################################

    aadhar_entry = Entry(root1, textvariable=entry_aadhar, bd=0, font=("chiller", 10, "bold"))
    aadhar_entry.place(y=80, x=110, height=30, width=180)
    Frame(root1, width=180, height=2, bg="black").place(x=110, y=109)
    submit_button = Button(root1, text="SUBMIT", command=show_balance, bg="blue", activeforeground="black",
                           activebackground="white", fg="white")
    submit_button.place(x=160, y=130, height=30, width=90)  #

    root1.mainloop()


#####################################################################################################################
def connect_database():
    def connect_server_btm():
        global cur, conn
        host = host_val.get()
        user = user_val.get()
        password = password_val.get()
        try:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password, )
            cur = conn.cursor()  # Create a cursor object
        except:
            messagebox.showerror("Notification", "DATA IS INCORRECT PLEASE TRY AGAIN")
            return
        try:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password, )
            cur = conn.cursor()
            strn = "CREATE DATABASE bank_manegement"
            cur.execute(strn)
            strn = "USE bank_manegement"
            cur.execute(strn)
            strn = """CREATE TABLE ACCOUNTS (
                 Account VARCHAR(255),
                     NAME VARCHAR(255),
                              AADHAR BIGINT,
                           DOB VARCHAR(255),
              ADDRESS VARCHAR(255),
               `CONTACT NO` VARCHAR(255),
                          EMAIL VARCHAR(255),
                                            OPENINGBALANCE VARCHAR(255),
                           `DATE` VARCHAR(255)) """

            cur.execute(strn)
            strn = """CREATE TABLE AMOUNT (
                           AADHAR BIGINT,
                           BALANCE BIGINT)"""
            cur.execute(strn)
            conn.close()
            messagebox.showinfo("Notification", "DATABASE CREATED. ! NOW YOU ARE IN DATABASE")
        except:
            strin = "USE bank_manegement"
            cur.execute(strin)
            messagebox.showinfo("Notification", "NOW YOU ARE CONNECTED TO THE DATABASE")
        try:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password)
            cur = conn.cursor()
            label.config(text="C", font=('chiller', 13, 'italic bold'), bg="green")

        except mysql.connector.connect:
            label.config(text="D", font=('chiller', 13, 'italic bold'), bg="red")

        root.destroy()

    def press1(event):
        if host_entry.get() == 'Enter Host Name':
            host_entry.delete(0, END)

    def press2(event):
        if user_entry.get() == 'Enter User Name':
            user_entry.delete(0, END)

    def press3(event):
        if password_entry.get() == 'Enter Password':
            password_entry.delete(0, END)

    root = Toplevel()
    root.geometry('380x300+800+200')
    root.title("Connection Window")

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    host_val = StringVar()
    user_val = StringVar()
    password_val = StringVar()

    host_entry = Entry(root, textvariable=host_val, bd=0, font=("Microsoft YaHei UI Light", 13, "bold"))
    host_entry.place(x=47, y=40, height=30, width=280)
    Frame(root, width=280, height=2, bg="black").place(x=47, y=68)
    host_entry.insert(0, 'Enter Host Name')
    host_entry.bind('<FocusIn>', press1)

    user_entry = Entry(root, textvariable=user_val, bd=0, font=("Microsoft YaHei UI Light", 13, "bold"))
    user_entry.place(x=47, y=90, height=30, width=280)
    Frame(root, width=280, height=2, bg="black").place(x=47, y=120)
    user_entry.insert(0, 'Enter User Name')
    user_entry.bind('<FocusIn>', press2)

    password_entry = Entry(root, textvariable=password_val, bd=0, font=("Microsoft YaHei UI Light", 13, "bold"))
    password_entry.place(x=47, y=140, height=30, width=280)
    Frame(root, width=280, height=2, bg="black").place(x=47, y=167)
    password_entry.insert(0, 'Enter Password')
    password_entry.bind('<FocusIn>', press3)

    submit_button = Button(root, text="SUBMIT", command=connect_server_btm, bg="dark blue", activeforeground="black",
                           activebackground="white", fg="white")
    submit_button.place(x=120, y=230, height=34, width=140)

    root.mainloop()


#################################################################################### indecater calling function

colors = ["red", "green", "blue", "yellow", "pink", "red2"]


def titlebar_color():
    fg = random.choice(colors)
    title.config(fg=fg)
    title.after(150, titlebar_color)


def titlebar():
    global count, text
    if count >= len(x):
        count = 0
        text = ""
        title.config(text=text)
    else:
        text = text + x[count]
        title.config(text=text)
        count += 1
    title.after(250, titlebar)


############################################################################### CALLING CLOCK

def timer():
    time_module = time.strftime("%r")
    date_module = time.strftime("%d-%m-%Y")
    clock.config(text=time_module + "\n" + date_module)
    clock.after(300, timer)


####################################################################################### OVER ALL FRAME

qwe = Tk()
qwe.title("Banking Management System")
qwe.geometry("900x600+250+40")  # w x h
qwe.resizable(False, False)
qwe.configure(bg="black")

#############################################################################################  yellowframe

firstframe = Frame(qwe, bg="white")
firstframe.place(x=0, y=130, height=550, width=900)
firstframe1 = Frame(qwe, bg="pink")
firstframe1.place(x=50, y=165, height=400, width=790)

#############################################################################################  IMAGE BUTTON
im = PhotoImage(file=r"openaccoun12t.png")
im1 = PhotoImage(file=r"get-money_88981.png")
im2 = PhotoImage(file=r"""6338900hgfx.png""")
im3 = PhotoImage(file=r"""wallet.png""")
im4 = PhotoImage(file="""wallwsr.png""")

######################################################################################################### BUTTONS

open_btn = Button(firstframe1, font=("Microsoft", 12, "bold"), borderwidth=3, activeforeground="blue",
                  activebackground="white", image=im, command=open_account, relief="flat")
open_btn.place(x=150, y=50, height=130, width=150)
open_btn.place1 = Label(firstframe1, text="OPEN ACCOUNT")
open_btn.place1.place(x=160, y=160, height=15, width=130)

DePosite_btn = Button(firstframe1, font=("Microsoft", 12, "bold"), borderwidth=3, relief="flat",
                      activeforeground="blue",
                      activebackground="white", image=im1, command=deposit_money)
DePosite_btn.place(x=150, y=230, height=130, width=150)
open_btn.place1 = Label(firstframe1, text="DEPOSIT MONEY")
open_btn.place1.place(x=160, y=335, height=17, width=135)

WDL_btn = Button(firstframe1, font=("Microsoft", 12, "bold"), borderwidth=3, relief="flat", activeforeground="blue",
                 activebackground="white", image=im2, command=WITHDRAWAL_money)
WDL_btn.place(x=480, y=50, height=130, width=150)
open_btn.place1 = Label(firstframe1, text="WITHDRAWAL MONEY", anchor="center")
open_btn.place1.place(x=488, y=160, height=15, width=135)

SB_btn = Button(firstframe1, font=("Microsoft", 12, "bold"), borderwidth=3, activeforeground="blue", relief="flat",
                activebackground="white", image=im3, command=show_balance)
SB_btn.place(x=480, y=230, height=130, width=150)
open_btn.place1 = Label(firstframe1, text="SHOW BALANCE")
open_btn.place1.place(x=486, y=335, height=15, width=130)

############################################################################################ indicater

x = "WELCOME TO BANK MANAGEMENT SYSTEM"
count = 0
text = ''
title = Label(qwe, text=x, font=('chiller', 17, ' bold'), fg="white", bg="black")
title.place(x=100, y=45, width=700)
titlebar()
titlebar_color()
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
image_bank = Label(qwe, bg="black", image=im4, )
image_bank.place(x=10, y=10, height=100, width=150)
############################################################################################### CLOCK

clock = Label(qwe, font=('Microsoft YaHei', 9, 'bold'), fg="white", bg="black")
clock.place(x=777, y=0)
timer()

database_button = Button(qwe, text=" DATABASE ", font=('chiller', 13, 'italic bold'),activeforeground="black",activebackground="red", command=connect_database)
database_button.place(x=745, y=96)
label = Label(qwe, text="D", font=('chiller', 13, 'italic bold'), bg="red", fg="white")
label.place(x=863, y=96, height=33, width=36)
qwe.mainloop()