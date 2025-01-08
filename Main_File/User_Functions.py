def User_func_opts():

    import tkinter as tk
    from importlib import reload
    
    
    Command_Loop = True

    while Command_Loop:
        def log():
            Window.destroy()
            import Login_Screen as LS
            reload(LS)
            LS.Login()
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
    