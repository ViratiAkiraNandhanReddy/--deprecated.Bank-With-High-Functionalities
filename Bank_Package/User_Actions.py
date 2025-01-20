import tkinter as tk
from . import Login_Screen
from . import Accounts,PinCodes,Security



class User_Requirements:
    def Balance():
        pass

    def Deposit():
        pass
    
    def Withdraw():
        pass


    def User_Menu(Accounts,User_func,PinCodes,Security):
        
        Command_Loop = True

        while Command_Loop:
            def log():
                Window.destroy()
                Login_Screen.Login(Accounts,User_func,PinCodes,Security)
                nonlocal Command_Loop
                Command_Loop = False

            print(Accounts,PinCodes,Security)
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
        