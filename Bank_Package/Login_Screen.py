import customtkinter as CTk
import PIL.Image
from random import randint
from datetime import datetime

Raw_Time = datetime.now()
Date_Day = Raw_Time.strftime('%d/%b/%Y - %A')

Random_Background = randint(0,30)
Login_Background = PIL.Image.open(fr'Bank_Package\Visual Data\Login Wallpapers\{Random_Background}.jpg')

User_Icon = PIL.Image.open(r'Bank_Package\Visual Data\User Icon-Multi.png')
Password_Icon = PIL.Image.open(r'Bank_Package\Visual Data\Locked.png')

        

#Deny The User To Close The Window
def Disable_Exit():
    ''' This Function Will Be Called When The User Clicked The Exit Button In The Window ; Then This Function Does Nothing Because This 
    Function Has No Statements Other Than Pass ; So That Window Can't Be Closed'''
    pass

class Login:
    def __init__(self):
        pass

    def Display_Login():

        global x_login
        x_login = 960
        
        #Shows The Login Screen in The Window
        def Show_Login():
            '''Used To Show The Login Screen To The User ; So The Login Screen Will Be Showed'''
            global x_login
            x_login -= 10
            if x_login >= 530:
                Frame.place(x=x_login,y=20)
                Window.after(1,Show_Login)
            if x_login < 530:
                return 

        #Hides The Login Screen in The Window
        def Hide_Login():
            '''Used To Move The Login Screen Away From The Screen ; So The Login Screen Will Be Hidden'''
            global x_login
            x_login += 10
            if x_login <= 960:
                Frame.place(x=x_login,y=20)
                Window.after(10,Hide_Login)
            if x_login > 960:
                return
        
        def Forgot_Password():
            Hide_Login()
            pass





        Window = CTk.CTk()
        Window.title('Login')
        Window.geometry('950x600')
        # Window.resizable(False,False)
        Window.protocol('WM_DELETE_WINDOW',Disable_Exit)
        CTk.CTkLabel(Window,text='',image=CTk.CTkImage(light_image=Login_Background,dark_image=Login_Background,size=(950,600))).place(x=0,y=0)
        Window.after(2000,Show_Login)
        # Window.after(10000,Hide_Login)

        Frame = CTk.CTkFrame(Window,corner_radius=0)
        Frame.configure(width=400,height=560)
        Frame.place(x=x_login,y=20)
        CTk.CTkLabel(Frame,text=Date_Day,text_color='Orange',height=10,font=('Roboto',9)).place(x=311,y=0)
        CTk.CTkLabel(Frame,text='Login',font=('Freestyle Script',42,'bold'),width=5).place(x=175,y=2)
        CTk.CTkLabel(Frame,text='Welcome Back!',font=('Roboto',30,'bold'),text_color='#57D956').place(x=30,y=65)
        CTk.CTkLabel(Frame,text='Sign in to Your Account',height=0,font=('Roboto',12)).place(x=33,y=100)
        CTk.CTkLabel(Frame,text='Username',font=('Roboto',24,'bold'),image=CTk.CTkImage(light_image=User_Icon,dark_image=User_Icon,size=(40,40)),compound='top').place(x=140,y=140)
        Username = CTk.CTkEntry(Frame,placeholder_text='Example: Virati Akira Nandhan Reddy',height=40,width=340,corner_radius=5,
                                font=('Roboto',16));Username.place(x=30,y=204)
        
        CTk.CTkLabel(Frame,text='Password',font=('Roboto',24,'bold'),image=CTk.CTkImage(light_image=Password_Icon,dark_image=Password_Icon,size=(40,40)),compound='top').place(x=140,y=260)
        CTk.CTkButton(Frame,text='Forgot Password',height=0,width=0,fg_color='transparent',hover=False,font=('Roboto',10),text_color='Light Blue',command=Forgot_Password).place(x=288,y=359)
        Password = CTk.CTkEntry(Frame,placeholder_text='Example: Viratiaki@Akki#2008',height=40,width=340,corner_radius=5,
                                font=('Roboto',16));Password.place(x=30,y=324)
        
        
        CTk.CTkButton(Frame,text='Login',width=120,border_width=1,text_color='Green',fg_color='transparent',font=('Roboto',16,'bold'),
                      command='').place(x=142,y=400)
        
        









        #Copyright Note 
        CTk.CTkLabel(Frame,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',font=('Calibri',8)).place(x=247,y=540)
        Window.mainloop()

Login.Display_Login()































# def Login(Available_Accounts,PinCodes,Security)->str:

#     def User_func(User=None)->int:
#         User_index = Available_Accounts.index(User)
#         return User_index

#     def Disable_Exit():
#         pass

#     import tkinter as tk
#     # from . import Create_Account as CA
#     # from . import Invalid_Error
#     # from __init__ import Accounts,User_func,PinCodes,Disable_Exit
#     # from .User_Actions import User_Requirements

#     command_Login = True

#     while command_Login:

#         #Redirecting to Create_Account Module
#         def Create():
#             Window.destroy()
#             # CA.Create_Account(Available_Accounts,PinCodes,Security,User_func)
#             nonlocal command_Login 
#             command_Login = False

#         #Getting All The Values
#         def Values():
#             global UserName,PinCode
#             UserName = User.get()    
#             PinCode = Pin.get()
#             Window.destroy()


#         #Creating The Main Login screen
#         Window = tk.Tk()
#         Window.geometry('350x250')
#         Window.title('Login')
#         Window.configure(background='#C3C3C3')
#         Window.resizable(False,False)

#         # tk.Label(Window,text='Login',font=('Roboto 18 bold'),fg='Black').pack()

#         UserIcon = tk.PhotoImage(file=r'Bank_Package\Visual Data\1177568.png')
#         tk.Label(Window,image=UserIcon,bg='#C3C3C3').grid(row=2,column=2)

#         tk.Label(Window,text='PinCode').grid(row=4,column=2)
#         User = tk.Entry(Window,bg='#A1A1A1',fg='Dark Green',relief='solid',border=1)
#         Pin = tk.Entry(Window,fg='Red',bg='#A1A1A1',relief='solid',border=1)
#         Pin.place(x=72,y=99,relwidth=0.7,relheight=0.1)
#         User.place(x=72,y=70,relwidth=0.7,relheight=0.1)
#         New_Acc = tk.Button(Window,text='Sign Up',command=Create,fg='Dark Red').place(x=15,y=210)
#         Continue = tk.Button(Window,text='Continue',command=Values,fg='Green').grid(row=6,column=3)
#         Window.protocol("WM_DELETE_WINDOW",Disable_Exit)
#         Window.mainloop()


#         #Using The Info Of Users
#         try:
#             print(UserName)
#             print(PinCode)
#             if UserName in Available_Accounts:
#                 if PinCodes[User_func(UserName)] == PinCode:
#                     User_Requirements.User_Menu(Available_Accounts,PinCodes,Security,User_func)
#                 elif PinCodes[User_func(UserName)] != PinCode:
#                     Invalid_Error.Pass_Error()

#             elif UserName == '':
#                 Invalid_Error.User_blank_Error()

#             elif PinCode == '':
#                 Invalid_Error.Pin_blank_Error()

#             else:
#                 try:                    

#                     #If Yes Goes to The Module
#                     def Yes():
#                         if Yes_Bt.configure():
#                             Verify.destroy()
#                             CA.Create_Account([],[],[],[],[],[],[]).Creating_New_Account()#.New_Account(Available_Accounts,User_func,PinCodes,Security)
#                             nonlocal command_Login
#                             command_Login = False

#                     #If No Loop Runs Again
#                     def No():
#                         Verify.destroy()
                        
#                     Verify = tk.Tk()
#                     Verify.title('Account Not Available')
#                     Verify.geometry('300x180')
#                     Verify.resizable(False,False)
#                     Verify.protocol("WM_DELETE_WINDOW",Disable_Exit)
#                     tk.Label(Verify,text='Oops! Account Not Available In The DataBase',fg='Red').pack()
#                     tk.Label(Verify,text='Do You Want To Create An Account',fg='Blue').pack(pady=20)
#                     Yes_Bt = tk.Button(Verify,text='Create An Account',fg='Green',command=Yes)
#                     Yes_Bt.pack()
#                     No_Bt = tk.Button(Verify,text='No Thanks!',fg='Red',command=No)
#                     No_Bt.pack(pady=20)
#                     Verify.mainloop()

#                 except:
#                     pass
#         except:
#             Window.mainloop()