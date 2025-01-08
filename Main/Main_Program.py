import tkinter as tk
from Logout_Screen import Activation_Save




def Activate ():

    Product_keys = [

    '2030-GITH-UBGC-AKKI-DIST-FIRS-TPRJ-INDI-AUSA-2026',
    '2030-AKKI-FIRS-TPRJ-HAPP-YGIT-DIST-USAI-NDIA-2026',
    '2030-DEV0-FIRS-TPRJ-INDI-AUSA-AKKI-AT18-0022-2026',
    '2030-GITH-UBAT-AKKI-USAI-NDIA-FIRS-TPRJ-2008-2026',
    '2030-AKKI-ATUS-AGOO-GLEA-ISSE-100M-USAI-NDIA-2026',
    '2030-USAI-NDIA-GOOG-LEAI-WITH-AKKI-WITH-$10T-2026',
    '2030-ALLR-IGHT-SREC-IVED-WITH-AKKI-INDI-AUSA-2026',
    '2030-USAI-NDIA-2008-VSCO-DEPY-THON-AIAT-AKKI-2026',
    'USAI-NDIA-VIRA-TIAK-IRAN-ANDH-ANRE-DDY1-2008-2030',
    'LAST-PROD-UCTK-EYAT-AKKI-PROG-RAM1-USAI-NDIA-2030'
    
    ]

    Terms_Conditions = '''

jlsyfjydysFDyFDkySTduyas


'''

    #New Window For Product Key
    def Product_Key()->None:

        #Getting The Key
        def Key():
            if Entery_Key.get() in Product_keys:
                Window_Activate.destroy()
                Activation_Save()

            else:
                Invalid = tk.Label(Window_Activate,text='Invalid Product Key',fg='Yellow',bg='#4F55A8').place(x=200,y=200)
        
        #Removeing Text in Example
        def Temp(Key=None)->None:
            Entery_Key.delete(0,'end')
            Entery_Key.config(fg='White')
        
        #Initial Setup Of Window
        Window.destroy()
        Window_Activate = tk.Tk()
        Window_Activate.title('Product Key')
        Window_Activate.geometry('640x320')
        Window_Activate.resizable(False,False)
        Window_Activate.configure(background='#4F55A8')
        
        #Instructions For The User
        tk.Label(Window_Activate,text='Enter a Product Key',bg='#4F55A8',fg='White',font=('Calibri 22'),justify='left',height=2).place(x=10,y=0)
        tk.Label(Window_Activate,text='The Product Keys For This Software Will Be Provided By The Owner, Also Provided In The \nWebsite That You Downloaded From (GitHub)',bg='#4F55A8',font=('Calibri 13')).place(x=10,y=80)
        tk.Label(Window_Activate,text='Product Key',bg='#4F55A8',font=('Calibri 14'),fg='White').place(x=10,y=140)
        
        #Product Key Entry
        Entery_Key = tk.Entry(Window_Activate,font=('Consolas',12),border=2,bg='#2F3263',relief='ridge',highlightbackground='White')
        Entery_Key.insert(0,string='XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX')
        Entery_Key.config(fg='#82829C')
        Entery_Key.place(x=10,y=168,relwidth=0.75,relheight=0.09)
        Entery_Key.bind('<FocusIn>',Temp)
        
        #Spepping Up
        tk.Button(Window_Activate,text='Authenticate',fg='White',command=Key,bg='#1E2040',activebackground='grey').place(x=485,y=250)
        tk.Button(Window_Activate,text='Cancel',fg='White',command=Window_Activate.destroy,bg='#1E2040',activebackground='grey').place(x=580,y=250)
        
        #Copyright Note 
        tk.Label(Window_Activate,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',fg='White',bg='#4F55A8',font=('Calibri 8')).place(x=418,y=300)
        Window_Activate.mainloop()
    
    def Accepted():
        if OK.get() == True:
            Next.config(state='normal')
        elif OK.get() == False:
            Next.config(state='disabled')



    print("hello I'M software Activation")
    Window = tk.Tk()
    Window.title('Activation Window')
    Window.geometry('750x500')
    Window.config(background='Light Blue')
    Window.resizable(False,False)
    OK = tk.BooleanVar()



    
    Terms = tk.Frame(Window,background='White',height=380,width=700)
    Terms.place(x=25,y=25)
    tk.Label(Terms,text=Terms_Conditions,bg='White').place(x=10,y=20)
    



    Check = tk.Checkbutton(Window,text='Accept All Terms And Conditions',underline=0,variable=OK,onvalue=True,\
                           offvalue=False,command=Accepted,bg='Light Blue',activebackground='Light Blue').place(x=25,y=410)
    Next = tk.Button(Window,text='Next',state='disabled',command=Product_Key,font=(10),activebackground='#316E7A',bg='#68ABC9',relief='ridge')
    tk.Button(Window,text='Cancel',fg='Red',command=Window.destroy,font=(10),activebackground='#316E7A',bg='#68ABC9',relief='ridge').place(x=662,y=435)
    Next.place(x=580,y=435,width=60)

    #Copyright Note 
    tk.Label(Window,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',\
             fg='Black',bg='Light Blue',font=('Calibri 8')).place(x=528,y=480)
    



    Window.mainloop()
    

        
    
def User_func_opts():
    from importlib import reload
    
    Command_Loop = True

    while Command_Loop:
        def log():
            Window.destroy()
            Login()
            nonlocal Command_Loop
            Command_Loop = False


        Window = tk.Tk()
        Window.geometry('300x500')
        Window.title('User Functions')
        B = tk.Button(Window,text='Balance',fg='Green')
        B.place(x=130,y=10)
        D = tk.Button(Window,text='Deposit',fg='Blue')
        D.place(x=90,y=50)
        W = tk.Button(Window,text='Withdrawal',fg='Red')
        W.place(x=150,y=50)
        C = tk.Button(Window,text='Log Out',command=log,fg='Purple')
        C.place(x=130,y=400)
        Window.mainloop()
    



def New_Account():
    import Invalid_Error
    from __init__ import Accounts,PinCodes,Security
    import Login_Screen as LS


    Command_New_Acc = True

    while Command_New_Acc:
        def Stop():
            Window_NA.destroy() 
            Login()
            nonlocal Command_New_Acc
            Command_New_Acc = False
                        

            
        def Values():
            global Acc
            Acc=New.get()
            Window_NA.destroy()

        Window_NA = tk.Tk()
        Window_NA.title('New Account')
        Window_NA.geometry('350x120')
        Window_NA.resizable(False,False)
        tk.Label(Window_NA,text='Creating An New Account',fg='Red').grid(column=2)
        tk.Label(Window_NA,text='New Username').grid(row=2,pady=20)
        New = tk.Entry(Window_NA)
        New.grid(row=2,column=2,ipadx=30)
        Continue = tk.Button(text='Continue',fg='Green',command=Values).grid(row=3,column=2)
        Cancel = tk.Button(text='Cancel',fg='Red',command=Stop).grid(row=3,column=3)

        Window_NA.mainloop()

        try:
            if Acc == '':
                Invalid_Error.User_blank_Error()
            elif Acc in Accounts:
                Invalid_Error.Exist_Error()
            elif Acc.isdigit()==True:
                Invalid_Error.User_Digit_Error()
            else:
                
                def Values_Pin():
                    global Pin_New
                    Pin_New = New_P.get()
                    if len(Pin_New) < 4:  
                        Invalid_Error.Pin_Char_Error()
                    else:
                        Window.destroy()
                        def Values_Login():
                            Window_sec.destroy()
                            Accounts.append(Acc)
                            PinCodes.append(Pin_New)    
                            Login()
                            nonlocal Command_New_Acc
                            Command_New_Acc = False
                            global Security_Code
                            Security_Code = None
                        Window_sec = tk.Tk()
                        tk.Label(Window_sec,text='In Case You Forget PinCode Use This Security Code',fg='Red',pady=10).pack()
                        Security_Code=Acc[0:4] + Pin_New[1:5]
                        if Security_Code not in Security:
                            Security.append(Security_Code)
                        else:
                            Security.append(Acc[0:4] + Pin_New[1:4] + '#')
                        tk.Label(Window_sec,text=Security_Code,fg='Dark Blue',pady=10,font=(40)).pack()
                        tk.Button(Window_sec,text='Continue',fg='Green',command=Values_Login).pack()
                        Window_sec.mainloop()

                Window = tk.Tk()
                Window.title('PinCode')
                Window.resizable(False,False)
                tk.Label(Window,text='** Must Contain 4 or More Characters **').grid(row=0,column=1)
                tk.Label(Window,text='New PinCode').grid(row=1,column=0)
                New_P = tk.Entry(Window)
                New_P.grid(row=1,column=1)
                Continue_Pin = tk.Button(Window,text='Continue',fg='Green',command=Values_Pin).grid(row=2,column=1)
                Window.mainloop()
        except:
            pass




def Login()->str:

    from importlib import reload
    import Create_Account as CA
    import Invalid_Error
    from __init__ import Accounts,User_func,PinCodes,Disable_Exit
    from User_Functions import User_func_opts

    command_Login = True

    while command_Login:

        #Redirecting to Create_Account Module
        def Create():
            Window.destroy()
            reload(CA)
            CA.New_Account()
            nonlocal command_Login 
            command_Login = False

        #Getting All The Values
        def Values():
            global UserName,PinCode
            UserName = User.get()    
            PinCode = Pin.get()
            Window.destroy()


        #Creating The Main Login screen
        Window = tk.Tk()
        Window.geometry('250x150')
        Window.title('Login')
        Window.resizable(False,False)
        tk.Label(Window,text='Username').grid(row=2,column=2)
        tk.Label(Window,text='PinCode').grid(row=4,column=2)
        User = tk.Entry(Window)
        Pin = tk.Entry(Window,fg='Red')
        Pin.grid(row=4,column=3,pady=20)
        User.grid(row=2,column=3,padx=20)
        New_Acc = tk.Button(Window,text='Sign Up',command=Create,fg='Dark Red').place(x=15,y=110)
        Continue = tk.Button(Window,text='Continue',command=Values,fg='Green').grid(row=6,column=3)
        Window.protocol("WM_DELETE_WINDOW",Disable_Exit)
        Window.mainloop()


        #Using The Info Of Users
        try:
            print(UserName)
            print(PinCode)
            if UserName in Accounts:
                if PinCodes[User_func(UserName)] == PinCode:
                    User_func_opts()
                elif PinCodes[User_func(UserName)] != PinCode:
                    Invalid_Error.Pass_Error()

            elif UserName == '':
                Invalid_Error.User_blank_Error()

            elif PinCode == '':
                Invalid_Error.Pin_blank_Error()

            else:
                try:                    

                    #If Yes Goes to The Module
                    def Yes():
                        if Yes_Bt.configure():
                            Verify.destroy()
                            CA.New_Account()
                            nonlocal command_Login
                            command_Login = False

                    #If No Loop Runs Again
                    def No():
                        Verify.destroy()
                        
                    Verify = tk.Tk()
                    Verify.title('Account Not Available')
                    Verify.geometry('300x180')
                    Verify.resizable(False,False)
                    Verify.protocol("WM_DELETE_WINDOW",Disable_Exit)
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