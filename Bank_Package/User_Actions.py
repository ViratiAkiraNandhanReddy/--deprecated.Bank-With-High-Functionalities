import customtkinter as CTk
from . import Accounts,PinCodes,Security,User_func
print(Accounts,PinCodes,Security)

class User_Requirements:




    def Balance()->str:
        Balance_Window = CTk.CTk()
        Balance_Window._set_appearance_mode('dark')
        Balance_Window.geometry()
        Balance_Window.title('Balance Available')
        Balance_Window.resizable(False,False)
        CTk.CTkLabel(Balance_Window,text=f'Balance Available:${''}',fg_color='Lime').pack()
        


        Balance_Window.mainloop()

    def Deposit():
        pass
    
    def Withdraw():
        pass

    def Menu(Accounts,User_func,PinCodes,Security,User_index):

        from . import Login_Screen
        
        
        Command_Loop = True

        while Command_Loop:
            def log():
                Window.destroy()
                Login_Screen.Login(Accounts,User_func,PinCodes,Security)
                nonlocal Command_Loop
                Command_Loop = False


            Window = CTk.CTk()
            Window.geometry('300x500')
            Window.title('User Functions')
            B = CTk.CTkButton(Window,text='Balance',fg_color='Green')
            B.place(x=130,y=10)
            D = CTk.CTkButton(Window,text='Deposit',fg_color='Blue')
            D.place(x=90,y=50)
            W = CTk.CTkButton(Window,text='Withdrawal',fg_color='Red')
            W.place(x=150,y=50)
            C = CTk.CTkButton(Window,text='Log Out',command=log,fg_color='Purple')
            C.place(x=130,y=400)
            Window.mainloop()

# User_Requirements.Balance()#.Menu([],1,[],[])