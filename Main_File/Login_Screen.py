def Login()->str:

    import tkinter as tk
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