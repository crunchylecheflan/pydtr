import mysql.connector
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from conn import db
from dtr_time import *

# DATABASE
db = db

class sourceCode():
    #GLOBAL VARIABLES USED
    global userPin         
    global userPinRegs                             
    global stringPinRegs
    global userPinPass
    global stringPinPass
    global stringPin
    global entryName
    global status 

    entryName = ""
    userPin =[]
    userPinRegs =[]
    userPinPass =[]
    stringPin = ""
    stringPinPass = ""
    stringPinRegs = ""
    status = ""
    # BACK BUTTON


    #---------------------------------------------------#
    #                    ENTRY PART                     #
    #---------------------------------------------------#
    # FOR LOGIN PIN
    def pin_Input(self,login):
        pinInput = Entry(login, width=8,font=( "Times New Roman",30),fg="#CDC2AE",bg="#354259")
        pinInput.pack(side="left", anchor="nw", padx=50, pady=20)
        pinInput.config(highlightbackground = "red", highlightcolor= "red")
        return pinInput
    # FOR LOGIN PASS
    def pin_Input_Pass(self,passw):
        pinInput = Entry(passw, width=8,font=( "Times New Roman",30),fg="#354259",bg="#CDC2AE")
        pinInput.pack(side="left", anchor="nw", padx=50, pady=20)
        pinInput.config(highlightbackground = "red", highlightcolor= "red")
        return pinInput
    # FOR REGISTRATION
    def pin_Input_Regs(self,regs):
        pinInput = Entry(regs, width=8,font=( "Times New Roman",30),fg="#354259",bg="#CDC2AE")
        pinInput.pack(side="left", anchor="nw", padx=50, pady=20)
        pinInput.config(highlightbackground = "red", highlightcolor= "red")
        return pinInput
    # FOR REGISTRATION REGISTER
    def name_Input_Regs(self,regs):
        pinInput = Entry(regs, width=25,font=( "Times New Roman",20),fg="#354259",bg="#CDC2AE")
        pinInput.place(x=300,y=20)
        pinInput.config(highlightbackground = "red", highlightcolor= "red")
        return pinInput
    #FUNCTIONS FOR BUTTONS ( ON CLICK )
    # -- get ID -- #
    def getPin(self,pin,entry):
        global userPin
        userPin += pin
        entry.delete(0, END)
        entry.insert(0, userPin)
        print(userPin)
    # -- clear TEXT AREA -- #
    def clearPin(self,entry):
        global userPin
        userPin.clear()
        entry.delete(0, END)
        entry.insert(0, userPin)
    # -- backSpace ( <- )  -- #
    def bckSpace(self,entry):
        global userPin
        userPin.pop()
        entry.delete(0, END)
        entry.insert(0, userPin)
    # -- get ID -- # -- REGISTER -- #
    def getPinRegs(self,pin,entry):
        global userPinRegs
        userPinRegs += pin
        entry.delete(0, END)
        entry.insert(0, userPinRegs)
        print(userPinRegs)
    # -- clear TEXT AREA -- # -- REGISTER -- #
    def clearPinRegs(self,entry):
        global userPinRegs
        userPinRegs.clear()
        entry.delete(0, END)
        entry.insert(0, userPinRegs)
    # -- backSpace ( <- )  -- # -- REGISTER -- #
    def bckSpaceRegs(self,entry):
        global userPinRegs
        userPinRegs.pop()
        entry.delete(0, END)
        entry.insert(0, userPinRegs)
    def getPinPass(self,pin,entry):
        global userPinPass
        userPinPass += pin
        entry.delete(0, END)
        entry.insert(0, userPinPass)
        print(userPinPass)
    # -- clear TEXT AREA -- # -- REGISTER -- #
    def clearPinPass(self,entry):
        global userPinPass
        userPinPass.clear()
        entry.delete(0, END)
        entry.insert(0, userPinPass)
    # -- backSpace ( <- )  -- # -- REGISTER -- #
    def bckSpacePass(self,entry):
        global userPinPass
        userPinPass.pop()
        entry.delete(0, END)
        entry.insert(0, userPinPass)
    # -- navigate to other tab -- #
    def gotoLogs(self,entry,logs,login,passw,notebook):
        global status
        global userPin
        global stringPin

        # REPLACING THE WHITE SPACES
        stringPin =  entry.get().replace(" ", "")
        pinConfig = len(stringPin)

        # SQL VALIDATION
        mycursor = db.cursor()
        sql = ("SELECT * FROM `employid` WHERE EMPID=%s")
        eyed = (stringPin,)
        mycursor.execute(sql,eyed)
        myresult = mycursor.fetchall()
        db.commit()
        # PIN VALIDATIONS
        # IF PIN IS MORE THAN 3 OR THREE == ERROR
        # IF PIN IS LESS THAN O == ERROR
        # IF PIN IS LESS THAN 3 == ERROR
        if(pinConfig > 3):
            messagebox.showerror("ALERT MESSAGE", "PIN must be less than 3 digits!")
        elif(pinConfig <= 0):
            messagebox.showerror("ALERT MESSAGE", "You must enter your PIN first!")
        elif(pinConfig < 3):
            messagebox.showerror("ALERT MESSAGE", "PIN must contain at least 3 digits!")
        else:        
            if(len(myresult)<=0):
                messagebox.showerror("ALERT MESSAGE", "UNKOWN PIN DETECTED!")
            else:
                # CORRECT PIN / SUCCESS PIN INSERT
                userPin.clear()
                entry.delete(0, END)
                entry.insert(0, userPin)

                notebook.add(passw,text="Password")
                notebook.add(login,text="Login")
                notebook.hide(0)
                notebook.hide(1)
                #CALLING THE TABLE
                sc.table(logs,stringPin)
    # -- navigate to other tab -- #
    def gotoLogsPass(self,entry,logs,notebook):
        global status
        global userPin
        global stringPin
        global stringPinPass
        print(stringPin)
        # REPLACING THE WHITE SPACES
        passw =  entry.get().replace(" ", "")
        # SQL VALIDATION
        mycursor = db.cursor()
        sql = ("SELECT * FROM `employid` WHERE EMPID=%s AND EMPPASS=%s")
        eyed = (stringPin,passw,)
        mycursor.execute(sql,eyed)
        myresult = mycursor.fetchall()
        db.commit()
        # PIN VALIDATIONS
        # IF PIN IS MORE THAN 3 OR THREE == ERROR
        # IF PIN IS LESS THAN O == ERROR
        # IF PIN IS LESS THAN 3 == ERROR     
        if(len(myresult)<=0):
            messagebox.showerror("ALERT MESSAGE", "PASSWORD INCORRECT, TRY IT AGAIN!")
        else:
            # CORRECT PIN / SUCCESS PIN INSERT
            userPinPass.clear()
            entry.delete(0, END)
            entry.insert(0, userPinPass)
            notebook.add(logs,text="Logs")
            notebook.hide(0)
            notebook.hide(2)
            #CALLING THE TABLE
            sc.table(logs,stringPin)
    def registration(self,entry,regs,login,notebook,regsName):
        global status
        global userPinRegs
        global stringPinRegs
        global entryName

        entryName = regsName.get()
        # REPLACING THE WHITE SPACES
        stringPinRegs =  entry.get().replace(" ", "")
        pinConfig = len(stringPinRegs)
        print(entryName,stringPinRegs)

        # SQL VALIDATION
        mycursor = db.cursor()
        sql = ("SELECT * FROM `employid` WHERE EMPID=%s")
        eyed = (stringPinRegs,)
        mycursor.execute(sql,eyed)
        myresult = mycursor.fetchall()
        db.commit()
        # PIN VALIDATIONS
        # IF PIN IS MORE THAN 3 OR THREE == ERROR
        # IF PIN IS LESS THAN O == ERROR
        # IF PIN IS LESS THAN 3 == ERROR
        if(pinConfig > 3):
            messagebox.showerror("ALERT MESSAGE", "PIN must be less than 3 digits!")
        elif(pinConfig <= 0):
            messagebox.showerror("ALERT MESSAGE", "You must enter your PIN first!")
        elif(pinConfig < 3):
            messagebox.showerror("ALERT MESSAGE", "PIN must contain at least 3 digits!")
        else:        
            if(len(myresult)>0):
                messagebox.showerror("ALERT MESSAGE", "YOU ALREADY REGISTERED!")
            else:
                regs_VAL = messagebox.askyesno("REGISTRATION MESSAGE", "REGISTRATION CONFIRMATION")
                # CORRECT PIN / SUCCESS PIN INSERT
                if(regs_VAL==1):
                    mycursor = db.cursor()
                    mycursor.execute("INSERT INTO employid (EMPID, EMPNAME) VALUES (%s,%s)", (stringPinRegs,entryName))
                    db.commit()
                    userPinRegs.clear()
                    entry.delete(0, END)
                    entry.insert(0, userPinRegs)
                    regsName.delete(0, END)
                    regsName.insert(0, userPinRegs)

                    notebook.add(login,text="Login")
                    notebook.add(regs,text="Register")
                    notebook.hide(1)
                    messagebox.showinfo("REGISTRATION SUCCESFUL","REGISTERED NAME AND ID ARE SUCCESFULLY ENTERED!")
                
    #---------------------------------------------------#
    #                   TREE VIEW CODES                 #
    #---------------------------------------------------#
    def table(self,logs,pin):
    #SQL VALIDATIONS
        mycursor = db.cursor()
        sql = ("SELECT * FROM `time_logs` WHERE EMPID=%s")
        eyed = (pin,)
        mycursor.execute(sql,eyed)

        # TABLE COLUMN -- no idea what for
        my_game = ttk.Treeview(logs,height=15)
        my_game['columns'] = ('ID', 'NAME', 'IN', 'STATUS', 'DATE','OUT')
        my_game.column("#0", width=0,  stretch=NO)
        my_game.column("ID",anchor=CENTER, width=40)
        my_game.column("NAME",anchor=CENTER,width=160)
        my_game.column("IN",anchor=CENTER,width=80)
        my_game.column("STATUS",anchor=CENTER,width=60)
        my_game.column("DATE",anchor=CENTER,width=80)
        my_game.column("OUT",anchor=CENTER,width=70)
        
        # TABLE HEADING  -- obviously the header of the table
        my_game.heading("#0",text="",anchor=CENTER)
        my_game.heading("ID",text="ID",anchor=CENTER)
        my_game.heading("NAME",text="NAME",anchor=CENTER)
        my_game.heading("IN",text="IN",anchor=CENTER)
        my_game.heading("STATUS",text="STATUS",anchor=CENTER)
        my_game.heading("DATE",text="DATE",anchor=CENTER)
        my_game.heading("OUT",text="OUT",anchor=CENTER)
        
        # getting all the info
        col = mycursor.fetchall()  

        # print all the information that fetched
        for x in col:
            my_game.insert(parent='',index='end',values=('{0}'.format(x[0]),'{0}'.format(x[1]),'{0}'.format(x[2]),'{0}'.format(x[3]),'{0}'.format(x[4]),'{0}'.format(x[5])))
        db.commit()
        my_game.place(x=170,y=10)
        db.commit()

    # NUM PAD BUTTONS #
    def num_pad(self,login,pinEnt):
        btn = Button(login, text="7", width=4, height=2, command=lambda:sc.getPin("7",pinEnt)).place(x=70,y=100)
        btn = Button(login, text="8", width=4, height=2, command=lambda:sc.getPin("8",pinEnt)).place(x=110,y=100)
        btn = Button(login, text="9", width=4, height=2, command=lambda:sc.getPin("9",pinEnt)).place(x=150,y=100)
        btn = Button(login, text="4", width=4, height=2, command=lambda:sc.getPin("4",pinEnt)).place(x=70,y=150)
        btn = Button(login, text="5", width=4, height=2, command=lambda:sc.getPin("5",pinEnt)).place(x=110,y=150)
        btn = Button(login, text="6", width=4, height=2, command=lambda:sc.getPin("6",pinEnt)).place(x=150,y=150)
        btn = Button(login, text="1", width=4, height=2, command=lambda:sc.getPin("1",pinEnt)).place(x=70,y=200)
        btn = Button(login, text="2", width=4, height=2, command=lambda:sc.getPin("2",pinEnt)).place(x=110,y=200)
        btn = Button(login, text="3", width=4, height=2, command=lambda:sc.getPin("3",pinEnt)).place(x=150,y=200)
        btn = Button(login, text="0", width=4, height=2, command=lambda:sc.getPin("0",pinEnt)).place(x=110,y=250)
    def num_pad_regs(self,regs,pinEnt):
        btn = Button(regs, text="7", width=4, height=2, command=lambda:sc.getPinRegs("7",pinEnt)).place(x=70,y=100)
        btn = Button(regs, text="8", width=4, height=2, command=lambda:sc.getPinRegs("8",pinEnt)).place(x=110,y=100)
        btn = Button(regs, text="9", width=4, height=2, command=lambda:sc.getPinRegs("9",pinEnt)).place(x=150,y=100)
        btn = Button(regs, text="4", width=4, height=2, command=lambda:sc.getPinRegs("4",pinEnt)).place(x=70,y=150)
        btn = Button(regs, text="5", width=4, height=2, command=lambda:sc.getPinRegs("5",pinEnt)).place(x=110,y=150)
        btn = Button(regs, text="6", width=4, height=2, command=lambda:sc.getPinRegs("6",pinEnt)).place(x=150,y=150)
        btn = Button(regs, text="1", width=4, height=2, command=lambda:sc.getPinRegs("1",pinEnt)).place(x=70,y=200)
        btn = Button(regs, text="2", width=4, height=2, command=lambda:sc.getPinRegs("2",pinEnt)).place(x=110,y=200)
        btn = Button(regs, text="3", width=4, height=2, command=lambda:sc.getPinRegs("3",pinEnt)).place(x=150,y=200)
        btn = Button(regs, text="0", width=4, height=2, command=lambda:sc.getPinRegs("0",pinEnt)).place(x=110,y=250)
    def num_pad_pass(self,passw,pinEnt):
        btn = Button(passw, text="7", width=4, height=2, command=lambda:sc.getPinPass("7",pinEnt)).place(x=70,y=100)
        btn = Button(passw, text="8", width=4, height=2, command=lambda:sc.getPinPass("8",pinEnt)).place(x=110,y=100)
        btn = Button(passw, text="9", width=4, height=2, command=lambda:sc.getPinPass("9",pinEnt)).place(x=150,y=100)
        btn = Button(passw, text="4", width=4, height=2, command=lambda:sc.getPinPass("4",pinEnt)).place(x=70,y=150)
        btn = Button(passw, text="5", width=4, height=2, command=lambda:sc.getPinPass("5",pinEnt)).place(x=110,y=150)
        btn = Button(passw, text="6", width=4, height=2, command=lambda:sc.getPinPass("6",pinEnt)).place(x=150,y=150)
        btn = Button(passw, text="1", width=4, height=2, command=lambda:sc.getPinPass("1",pinEnt)).place(x=70,y=200)
        btn = Button(passw, text="2", width=4, height=2, command=lambda:sc.getPinPass("2",pinEnt)).place(x=110,y=200)
        btn = Button(passw, text="3", width=4, height=2, command=lambda:sc.getPinPass("3",pinEnt)).place(x=150,y=200)
        btn = Button(passw, text="0", width=4, height=2, command=lambda:sc.getPinPass("0",pinEnt)).place(x=110,y=250)
    # -- FUNCTION BUTTON FOR TIME IN -- #  
    def time_in(self,logs):

        # CALLING A VALUE FROM THE FUNCTION FROM DIFFERENT PYTHON FILE
        current_time = timeNow()# GETTING TIME RIGHT NOW FROM DTR_TIME.PY
        date = dateNow()# GETTING DATE TODAY FROM DTR_TIME.PY

        # T MEANS THE TIME BASIS OF CONSIDERATION AS LATE
        t = datetime.time(8, 15, 00) # FORMAT ( HOUR/S, MINUTE/S, SECONDS )
        t1 = t.strftime("%H:%M:%S") # FIXNG THE TIME FORMAT

        # IF YOU ARE NOT LATE
        if(t1 > current_time):
            status = ""
        # YOURE PRETTY LATE
        elif(t1 <= current_time):
            status = "Late"
        print(status)
        # SQL VALIDATIONS
        mycursor = db.cursor()
        sql = ("SELECT * FROM tstamp_table INNER JOIN employid on employid.EMPID = tstamp_table.EMPCODE WHERE tstamp_table.EMPCODE=%s AND tstamp_table.DATE=%s")
        eyed = (stringPin,date,)
        mycursor.execute(sql,eyed)
        myresult = mycursor.fetchall()
        db.commit()

        # GETTING THE LENGTH FROM THE SQL RESULT   
        x = len(myresult)

        # IF THE RESULT FROM THE SQL IS ZERO OR '0' == SUCCESS
        if(x==0):
            mycursor = db.cursor()
            mycursor.execute("INSERT INTO tstamp_table (EMPCODE, TIMESTAMP,STATUS,DATE) VALUES (%s,%s,%s,%s)", (stringPin,current_time,status,date))
            mycursor.execute("INSERT INTO time_out (out_EMPCODE,out_DATE) VALUES(%s,%s)", (stringPin,date))
            sc.table(logs,stringPin)
            db.commit()
        else:
            messagebox.showinfo("ALERT MESSAGE","YOU ALREADY TIMED IN!") #IF THE RESULT IS ALREADY POPULATED THROWS A MESSAGE
    # -- FUNCTION BUTTON FOR TIME OUT -- #  
    def time_out(self,logs):

        #CALLING A VALUE FROM THE FUNCTION FROM DIFFERENT PYTHON FILE
        current_time = timeNow() # GETTING TIME RIGHT NOW
        date = dateNow() # GETTING DATE TODAY

        # SQL VALIDATIONS
        mycursor = db.cursor()
        sql = ("SELECT time_out.out_TIME, tstamp_table.DATE FROM time_out INNER JOIN employid on employid.EMPID=time_out.out_EMPCODE INNER JOIN tstamp_table on tstamp_table.DATE = time_out.out_DATE AND tstamp_table.EMPCODE = time_out.out_EMPCODE WHERE time_out.out_EMPCODE=%s AND tstamp_table.DATE=%s AND time_out.out_TIME=''")
        eyed = (stringPin,date,)
        mycursor.execute(sql,eyed)
        myresult = mycursor.fetchall()
        db.commit()
        
        # GETTING THE LENGTH FROM THE SQL RESULT
        x = len(myresult)

        out_VAL = messagebox.askyesno('TIME OUT', 'Are you sure you want to time out?')
        if(out_VAL == 1):
            # IF THE RESULT FROM THE SQL IS ZERO OR '0' == SUCCESS
            if(x==1):
                #SQL VALIDATIONS
                mycursor = db.cursor()
                sql = ("UPDATE time_out SET out_TIME=%s WHERE out_EMPCODE=%s AND out_DATE=%s")
                eyed = (current_time,stringPin,date,)
                mycursor.execute(sql,eyed)
                sc.table(logs,stringPin)
                db.commit()
            else: 
                messagebox.showinfo("ALERT MESSAGE","YOU ALREADY TIMED OUT!") #IF THE RESULT IS ALREADY POPULATED THROWS A MESSAGE

sc = sourceCode()
