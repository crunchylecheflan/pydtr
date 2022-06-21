from tkinter import*
from tkinter import ttk
from time import *
import pandas as pd
from datetime import date, datetime
import mysql.connector
from mysql.connector import Error
import datetime
from c_center import center
import tkinter.font as font
from conn import db
from dtr_time import *
from source import *
#---------------------------------------------------#
#                MYSQL CONNENCTION CODE             #
#---------------------------------------------------#
db = db
t = sourceCode()
#---------------------------------------------------#
#                ROOT AND NOTEBOOK PACK             #
#---------------------------------------------------#
root = Tk()
notebook = ttk.Notebook(root)
notebook.pack()
#---------------------------------------------------#
#               FRAMES / TABS SETTINGS              #
#---------------------------------------------------#
login = Frame(notebook, bg="#354259")
logs = Frame(notebook,  bg="#354259")
regs = Frame(notebook,  bg="#354259")
passw = Frame(notebook,  bg="#354259")
notebook.pack(expand=True,fill="both",padx=10,pady=10)
#---------------------------------------------------#
#                   ROOT SETTINGS                   #
#---------------------------------------------------#
center(root)
root.title("Daily Time Recorder")
root.resizable(0,0)
root.geometry("700x400")
root.configure(bg="#354259")
#---------------------------------------------------#
#                   MAIN AREA CODES                 #
#---------------------------------------------------#
notebook.add(login,text="Login")    
notebook.add(regs,text="Register")   
ttk.Style().configure("TNotebook", background="#354259")   #configure "tabs" background color

dtrTitle = Label(login,text="Time Login", font=("Times New Roman",40),bg="#354259", fg="#CDC2AE")
dtrTitle.pack(side="right", anchor="ne", padx=50, pady=10)


dtrTitle = Label(regs,text="Registration", font=("Times New Roman",40),bg="#354259", fg="#CDC2AE")
dtrTitle.pack(side="right", anchor="w", padx=50, pady=10)

empName = Label(regs,text="Employee Name", font=("Times New Roman",20),bg="#354259", fg="#CDC2AE")
empName.place(x=385,y=70)
# CALLING TIME IN FUNCTION BUTTON () #
def time_in():
    t.time_in(logs)
# CALLING TIME OUT FUNCTION BUTTON () #    
def time_out():
    t.time_out(logs)
def regsName():
    regsName = t.name_Input_Regs(regs)
    return regsName
regs_Name = regsName()

def bckBtn():
    notebook.add(login,text="Login")
    notebook.add(regs,text="Register")
    notebook.hide(3)

#---------------------------------------------------#
#                   TREE VIEW CODES                 #
#---------------------------------------------------#

def export():
    t.export()
    

def table():
    test = t.table(logs,stringPin)
    export(test)

#---------------------------------------------------#
#                   TIME AREA CODES                 #
#---------------------------------------------------#
def update():
    timeStr = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeStr)
    timeLabel.after(1000,update)

timeLabel = Label(login, font=("Times New Roman",40), fg="#CDC2AE",bg="#354259")
timeLabel.place(x=350,y=140)


# -- Time Called
update()
#---------------------------------------------------#
#                    ENTRY PART                     #
#---------------------------------------------------#
def pinInput(): 
    pil =  t.pin_Input(login)
    return pil
pinEnt = pinInput()

def pinInputRegs():
    pil =  t.pin_Input_Regs(regs)
    return pil
pinRegs = pinInputRegs()
def pinInputPass():
    pil =  t.pin_Input_Pass(passw)
    return pil
pinPass = pinInputPass()
#---------------------------------------------------#
#                    NUMPAD PART                    #
#---------------------------------------------------#
def numPad():
    t.num_pad(login,pinEnt)
numPad()

def numPadRegs():
    t.num_pad_regs(regs,pinRegs)
numPadRegs()

def numPadPass():
    t.num_pad_pass(passw,pinPass)
numPadPass()
#---------------------------------------------------#---------#
#                    BUTTONS PART                   #  LOGIN  #   
#---------------------------------------------------#---------#
# FUNCTIONS
def clearPin():
    t.clearPin(pinEnt)
def bckSpace():
    t.bckSpace(pinEnt)
def gotoLogs():
    t.gotoLogs(pinEnt,logs,login,passw,notebook)    

clrbtn = Button(login, text="Clear",width=4, height=2, command=lambda:clearPin())
clrbtn.place(x=70,y=250)
btn = Button(login, text="<-",  width=4, height=2, command=lambda:bckSpace())
btn.place(x=150,y=250)
loginBtn = Button(login, text="Enter",  width=4, height=2, command=lambda:gotoLogs())
loginBtn.place(x=110,y=300)
#---------------------------------------------------#---------#
#                    BUTTONS PART                   #  PASSW  #   
#---------------------------------------------------#---------#
# FUNCTIONS
def clearPinPass():
    t.clearPinPass(pinPass)
def bckSpacePass():
    t.bckSpacePass(pinPass)
def gotoLogsPass():
    t.gotoLogsPass(pinPass,logs,notebook)
clrbtn = Button(passw, text="Clear",width=4, height=2, command=lambda:clearPinPass())
clrbtn.place(x=70,y=250)
btn = Button(passw, text="<-",  width=4, height=2, command=lambda:bckSpacePass())
btn.place(x=150,y=250)
passBtn = Button(passw, text="Enter",  width=4, height=2, command=lambda:gotoLogsPass())
passBtn.place(x=110,y=300)
#---------------------------------------------------#---------#
#                    BUTTONS PART                   #  REGIS  #   
#---------------------------------------------------#---------#
# FUNCTIONS
def clearPinRegs():
    t.clearPinRegs(pinRegs)
def bckSpaceRegs():
    t.bckSpaceRegs(pinRegs)
def register():
    t.registration(pinRegs,regs,login,notebook,regs_Name)
clrbtn = Button(regs, text="Clear",width=4, height=2, command=lambda:clearPinRegs())
clrbtn.place(x=70,y=250)
btn = Button(regs, text="<-",  width=4, height=2, command=lambda:bckSpaceRegs())
btn.place(x=150,y=250)

regBtn = Button(regs, text="Enter",  width=4, height=2, command=lambda:register())
regBtn.place(x=110,y=300)
#---------------------------------------------------#---------#
#                    BUTTONS PART                   #  LOGS   #   
#---------------------------------------------------#---------#
fs5 = font.Font(size=5)
fs15 = font.Font(size=15)
clrbtn = Button(logs,
                text="TIME IN", 
                bg="#1E5128", fg="#CDC2AE",
                activebackground='#1E5128',
                width=10,
                command=lambda:time_in())
clrbtn['font'] = fs15
clrbtn.place(x=30,y=30)

bt = Button(logs,
            text="TIME OUT",
            bg="#B33030",
            fg="#A1B57D",
            activebackground='#B33030',
            width=10,
            command=lambda:time_out())
bt['font'] = fs15
bt.place(x=30,y=100)
bt = Button(logs,
            text="LOG OUT",
            bg="#B33030",
            fg="#A1B57D",
            activebackground='#B33030',
            width=10,
            command=lambda:bckBtn())
bt['font'] = fs15
bt.place(x=30,y=260)
bt = Button(logs,
            text="EXPORT",
            bg="#1E5128",
            fg="#A1B57D",
            activebackground='#B33030',
            width=10,
            command=lambda:export())
bt['font'] = fs15
bt.place(x=30,y=210)
#---------------------------------------------------#
#                   ROOT END PART                   #
#---------------------------------------------------#
root.mainloop()
