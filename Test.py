import tkinter as tk
import Invalid_Error
from __init__ import Accounts,PinCodes,User_func

Command = True 

while Command:
    def New_Account():

        def Stop():
            Window_NA.destroy()
            Login()

        def Values():
            global Acc
            Acc=New.get()
            Window_NA.destroy()
        
        Window_NA = tk.Tk()
        Window_NA.title('New Account')
        Window_NA.geometry('350x120')
        tk.Label(Window_NA,text='Creating An New Account',fg='Red').grid(column=2)
        tk.Label(Window_NA,text='New Username').grid(row=2,pady=20)
        New = tk.Entry(Window_NA)
        New.grid(row=2,column=2,ipadx=30)
        Continue = tk.Button(text='Continue',fg='Green',command=Values).grid(row=3,column=2)
        Cancel = tk.Button(text='Cancel',fg='Red',command=Stop).grid(row=3,column=3)

        Window_NA.mainloop()

        try:
            if Acc == '':
                Invalid_Error.Blank_Error()
            elif Acc in Accounts:
                Invalid_Error.Exist_Error()
            elif Acc.isdigit()==True:
                Invalid_Error.Digit_Error()
            else:
                Accounts.append(Acc)
                def Values_Pin():
                    global Pin_New
                    Pin_New = New_P.get()
                    if len(Pin_New) < 4:
                        Win = tk.Toplevel(Window)
                        Invalid_Error.Pin_Char_Error()
                        Win.mainloop()
                Window = tk.Tk()
                Window.title('PinCode')
                tk.Label(Window,text='** Must Contain 4 or More Characters **').grid(row=0,column=1)
                tk.Label(Window,text='New PinCode').grid(row=1,column=0)
                New_P = tk.Entry(Window)
                New_P.grid(row=1,column=1)
                Continue_Pin = tk.Button(Window,text='Continue',fg='Green',command=Values_Pin).grid(row=2,column=1)
                Window.mainloop()

        except:
            pass


    def User_Functions():

        def log():
            Window.destroy()
            global UserName,PinCode
            UserName = None
            PinCode = None
            Login()
            

        Window = tk.Tk()
        Window.geometry('300x500')
        B = tk.Button(Window,text='Balance',fg='Green')
        B.place(x=130,y=10)
        D = tk.Button(Window,text='Deposit',fg='Blue')
        D.place(x=90,y=50)
        W = tk.Button(Window,text='Withdrawal',fg='Red')
        W.place(x=150,y=50)
        C = tk.Button(Window,text='Log Out',command=log,fg='Purple')
        C.place(x=130,y=400)
        Window.mainloop()


    def Login():

        #Getting All The Values
        def Values():
            global UserName,PinCode
            UserName = User.get()
            PinCode = Pin.get()
            Window.destroy()
            
                
        def Create():
            Window.destroy()
            New_Account()

        #Creating The Main Login screen
        Window = tk.Tk()
        Window.geometry('250x150')
        Window.title('Login')
        tk.Label(Window,text='Username').grid(row=2,column=2)
        tk.Label(Window,text='PinCode').grid(row=4,column=2)
        User = tk.Entry(Window)
        Pin = tk.Entry(Window,fg='Red')
        Pin.grid(row=4,column=3,pady=20)
        User.grid(row=2,column=3,padx=20)
        New_Acc = tk.Button(Window,text='Sign Up',command=Create,fg='Dark Red').place(x=15,y=110)
        Continue = tk.Button(Window,text='Continue',command=Values,fg='Green').grid(row=6,column=3)

        Window.mainloop()

        #Using The Info Of Users
        try:
            print(UserName)
            print(PinCode)
            if UserName in Accounts:
                if PinCodes[User_func(UserName)] == PinCode:
                    User_Functions()
                elif PinCode.startswith('',0) and PinCode.endswith('',0):
                    Invalid_Error.Pin_blank_Error()
                

            elif UserName == None or '':
                Invalid_Error.User_blank_Error()
            elif UserName == '':
                Invalid_Error.User_blank_Error()
            elif PinCode == None or '':
                Invalid_Error.Pin_blank_Error()
            elif PinCode == '':
                Invalid_Error.Pin_blank_Error()
            else:
                try:

                    #If Yes Goes to The Module
                    def Yes():
                        if Yes_Bt.configure():
                            Verify.destroy()
                            New_Account()

                    #If No Loop Runs Again
                    def No():
                        Verify.destroy()
                        
                    Verify = tk.Tk()
                    Verify.title('Account Not Available')
                    Verify.geometry('300x180')
                    tk.Label(Verify,text='Oops! Account Not Available In The DataBase',fg='Red').pack()
                    tk.Label(Verify,text='Do You Want To Create An Account',fg='Blue').pack(pady=20)
                    Yes_Bt = tk.Button(Verify,text='Create An Account',fg='Green',command=Yes)
                    Yes_Bt.pack()
                    No_Bt = tk.Button(Verify,text='No Thanks!',fg='Red',command=No)
                    No_Bt.pack(pady=20)
            
                    Verify.mainloop()
                except:
                    pass
        except:
            Window.mainloop()

    Login()