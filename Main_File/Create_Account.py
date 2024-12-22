def New_Account():
    import tkinter as tk
    import Invalid_Error
    from __init__ import Accounts,PinCodes,Security
    import Login_Screen as LS
    from importlib import reload
    def Stop():
        Window_NA.destroy()
        reload(LS)
        LS.Login()
                

        
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
                Invalid_Error.User_blank_Error()
            elif Acc in Accounts:
                Invalid_Error.Exist_Error()
            elif Acc.isdigit()==True:
                Invalid_Error.Digit_Error()
            else:
                
                def Values_Pin():
                    global Pin_New
                    Pin_New = New_P.get()
                    if len(Pin_New) < 4:  
                        Invalid_Error.Pin_Char_Error()
                    else:
                        Window.destroy()
                        def Values():
                            Window_sec.destroy()
                            Accounts.append(Acc)
                            PinCodes.append(Pin_New) 
                            reload(LS)   
                            LS.Login()
                            
                            Security_Code = None
                        Window_sec = tk.Tk()
                        tk.Label(Window_sec,text='In Case You Forget PinCode Use This Security Code',fg='Red',pady=10).pack()
                        Security_Code=Acc[0:4] + Pin_New[1:5]
                        if Security_Code not in Security:
                            Security.append(Security_Code)
                        tk.Label(Window_sec,text=Security_Code,fg='Dark Blue',pady=10,font=(40)).pack()
                        tk.Button(Window_sec,text='Continue',fg='Green',command=Values).pack()
                        Window_sec.mainloop()

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