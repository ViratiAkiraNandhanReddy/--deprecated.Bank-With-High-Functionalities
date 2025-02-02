#Importing Required Modules/Packages
import customtkinter as CTk
import PIL.Image
from random import randint
from datetime import datetime
from .Create_Account import Create_Account
from .User_Actions import User_Requirements
from . import Detailed_Licence

#Used To Show Date
Raw_Time = datetime.now()
Date_Day = Raw_Time.strftime('%d/%b/%Y - %A') #Shows As 02/Feb/2025 - Sunday

#Background Image At Login Screen
Random_Background = randint(0,30)
Login_Background = PIL.Image.open(fr'Bank_Package\Visual Data\Login Wallpapers\{Random_Background}.jpg')

#Required Icon For The Details
User_Icon = PIL.Image.open(r'Bank_Package\Visual Data\User Icon-Multi.png')
Password_Icon = PIL.Image.open(r'Bank_Package\Visual Data\Locked.png')

#Deny The User To Close The Window
def Disable_Exit():
    ''' This Function Will Be Called When The User Clicked The Exit Button In The Window ; Then This Function Does Nothing Because This 
    Function Has No Statements Other Than Pass ; So That Window Can't Be Closed'''
    pass

#Class For The Developer
class Developer:
    def __init__(self):
        pass

    def Developer():
        
        Developer_Window = CTk.CTk()
        Developer_Window.geometry('250x150')
        Developer_Window.title('Developer')
        Developer_Window.resizable(False,False)
        Developer_Window.mainloop()
        pass

#Class For The License
class License:

    '''This Class Is Used To Show The License Information To The User In A Scrollable Format ; Also This Class Shows The Detailed
    Overview Of The License ; And We Can Able To View The License Repeatedly Over Time , The Source Of License Is Provided By The
    __init__ Hence This Class Is Depended On That File , That Mean Without That Module This Class is Useless And In This Class The 
    License Data Will Be (As it is) In The LICENSE File Except The Restricted Zone, Because It is Useless To Show To The User As We
    Know That They Don't Understand The Text In It\n
    Content Included in This Window:\n
    1.Owner Name\n
    2.License\n
    3.Some Conditions\n
    4.Owner Contacts
    '''

    def __init__(self,Detailed_Licence):
        self.Detailed_Licence = Detailed_Licence

    #Main Window For The License
    def Show_License(self):

        #License's Main Window
        License_Window = CTk.CTk()
        License_Window.geometry('640x470')
        License_Window.resizable(False,False)
        License_Window.title('License')

        #Frame And The Text
        License_Frame = CTk.CTkScrollableFrame(License_Window,height=400,width=600,label_text='License And Conditions',
                                               label_font=('Roboto',24));License_Frame.place(x=10,y=10)
        CTk.CTkLabel(License_Frame,text=self.Detailed_Licence[:4427],font=('Roboto',14)).pack()
        License_Window.mainloop()

#Class For The Documentation
class Documentation:
    def __init__(self):
        pass

    #Documentation Of The SoftWare
    def Show_Documentation():
        pass

#Class For The Login
class Login:
    def __init__(self,Available_Accounts,User_PinCodes,User_Security_Codes,User_Balance):
        self.Available_Accounts:list = Available_Accounts
        self.User_PinCodes:list = User_PinCodes
        self.User_Security_Codes:list = User_Security_Codes
        self.User_Balance:list = User_Balance

    def Display_Login(self):

        global x_login,x_reset
        x_login = 960
        x_reset = -410
        print(self.Available_Accounts)
        print(self.User_PinCodes)
        print(self.User_Security_Codes)

        #Shows The Login Screen in The Window
        def Show_Login():
            '''Used To Show The Login Screen To The User ; So The Login Screen Will Be Showed'''
            global x_login
            x_login -= 10
            if x_login >= 530:
                Frame.place(x=x_login,y=20)
                Window.after(10,Show_Login)
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
        
        #Shows The Reset Password Screen in The Window
        def Show_Reset_Password():
            '''Used To Show The Reset Password Screen To The User ; So The Reset Password Screen Will Be Showed'''
            global x_reset
            x_reset += 10
            if x_reset <= 20:
                Frame_Reset_Password.place(x=x_reset,y=20)
                Window.after(10,Show_Reset_Password)
            if x_reset >= 20:
                return 
        
        #Hides The Reset Password Screen in The Window
        def Hide_Reset_Password():
            '''Used To Move The Reset Password Screen Away From The Screen ; So The Login Screen Will Be Hidden'''
            global x_reset
            x_reset -= 10
            if x_reset >= -410:
                Frame_Reset_Password.place(x=x_reset,y=20)
                Window.after(10,Hide_Reset_Password)
            if x_login < -410:
                return
        
        #Hides The Reset Password Screen Then Shows The Login Screen in The Window
        def Hide_Forgot_Password_Show_Login():
            # Login_Display_Items()
            Window.after(1200,Login_Display_Items)
            Hide_Reset_Password()
            Show_Login()
        
        #Shows The Reset Password Screen Then Hides The Login Screen in The Window
        def Show_Forgot_Password_Hide_Login():
            Destroy_Login_Items()
            Hide_Login()
            

            Show_Reset_Password()

            # Window.after(4000,Hide_Reset_Password)
            # Window.after(2000,Show_Login)
            pass
        
        #To Show The Items After The Login Screen Appears
        def Login_Display_Items():
            Date.place(x=301,y=0)
            Heading.place(x=175,y=2)
            Greet.place(x=30,y=65)
            Subheading.place(x=33,y=100)
            User_icon_Delay.place(x=140,y=140)
            Username.place(x=30,y=204)
            Password_icon_Delay.place(x=140,y=260)
            Forgot_Password_Delay.place(x=288,y=359)
            Password.place(x=30,y=324)
            Login_Button_Delay.place(x=142,y=400)
            Sign_Up_Delay.place(x=2,y=538)

        #To Hide The Items Before The Login Screen Disappears
        def Destroy_Login_Items():
            Date.place_forget()
            Heading.place_forget()
            Greet.place_forget()
            Subheading.place_forget()
            User_icon_Delay.place_forget()
            Username.place_forget()
            Password_icon_Delay.place_forget()
            Forgot_Password_Delay.place_forget()
            Password.place_forget()
            Login_Button_Delay.place_forget()
            Sign_Up_Delay.place_forget()
            Window.after(1200,Reset_Password_Display_Items)

        #To Show The Items After The Reset Password Screen Appears
        def Reset_Password_Display_Items():
            Heading_Reset.place(x=105,y=2)
            Greet_Reset.place(x=30,y=65)
            Cancel_Reset.place(x=2,y=538)

        #To Hide The Items Before The Reset Password Screen Disappears
        def Destroy_Reset_Password_Items():
            pass

        #Redirecting To Signup Screen And All The Processing Is Done Here
        def Signup_Redirecting():
            Window.destroy()
            try:
                New_Account = Create_Account(Available_Accounts=self.Available_Accounts,User_Security_Codes=self.User_Security_Codes);New_Account.Creating_New_Account()
                for User_Name,User_Password,Security_Code in New_Account.New_Account_Details:
                    self.Available_Accounts.append(User_Name)
                    self.User_PinCodes.append(User_Password)
                    self.User_Security_Codes.append(Security_Code)
                Login(self.Available_Accounts,self.User_PinCodes,self.User_Security_Codes,self.User_Balance).Display_Login()
            except:
                pass

        #If The Username Matches To The Password Then Redirecting To The User Actions
        def Login_Actions():
            User_Name = Username.get()
            User_Password = Password.get()
            Security_Code = self.User_Security_Codes[self.Available_Accounts.index(User_Name)]
            User_Balance = self.User_Balance[self.Available_Accounts.index(User_Name)]
            Window.destroy()
            User_Requirements(User_Name,User_Password,Security_Code,User_Balance).User_Interface()
            Login(self.Available_Accounts,self.User_PinCodes,self.User_Security_Codes,self.User_Balance).Display_Login()

        def License_Developer_Documentation():

            def Show_License_Window():
                Dev_Doc.destroy()
                License(Detailed_Licence).Show_License()

            Dev_Doc = CTk.CTk()
            Dev_Doc.geometry('300x252')
            Dev_Doc.resizable(False,False)
            Dev_Doc.title('Great To See You Here')

            Dev_Doc_Frame = CTk.CTkFrame(Dev_Doc)
            Dev_Doc_Frame.configure(width=280,height=232)
            Dev_Doc_Frame.place(x=10,y=10)

            CTk.CTkButton(Dev_Doc_Frame,text='Developer',font=('Roboto',20,'bold'),fg_color='Orange',hover_color='Yellow',text_color='Black',width=240,height=48).place(x=20,y=22)
            CTk.CTkButton(Dev_Doc_Frame,text='Documentation',font=('Roboto',20,'bold'),width=240,height=48,fg_color='#E63B60',hover_color='#067FD0').place(x=20,y=92)
            CTk.CTkButton(Dev_Doc_Frame,text='License',font=('Roboto',20,'bold'),width=240,height=48,fg_color='#797EF6',hover_color='#4ADEDE',command=Show_License_Window).place(x=20,y=162)
            Dev_Doc.mainloop()


        #Main Window
        Window = CTk.CTk()
        Window.title('Login')
        Window.geometry('950x600')
        Window.resizable(False,False)
        Window.protocol('WM_DELETE_WINDOW',Disable_Exit)
        CTk.CTkLabel(Window,text='',image=CTk.CTkImage(light_image=Login_Background,dark_image=Login_Background,size=(950,600))).place(x=0,y=0)
        Window.after(600,Show_Login)
        # Window.after(10000,Hide_Login)

        #Login Screen
        Frame = CTk.CTkFrame(Window,corner_radius=0)
        Frame.configure(width=400,height=560)
        Frame.place(x=x_login,y=20)
        Date = CTk.CTkLabel(Frame,text=Date_Day,text_color='Orange',height=10,font=('Roboto',9))#.place(x=311,y=0)
        Heading = CTk.CTkLabel(Frame,text='Login',font=('Freestyle Script',42,'bold'),width=5)#.place(x=175,y=2)
        Greet = CTk.CTkLabel(Frame,text='Welcome Back!',font=('Roboto',30,'bold'),text_color='#57D956')#.place(x=30,y=65)
        Subheading = CTk.CTkLabel(Frame,text='Sign in to Your Account',height=0,font=('Roboto',12))#.place(x=33,y=100)
        
        #Username Entry
        User_icon_Delay = CTk.CTkLabel(Frame,text='Username',font=('Roboto',24,'bold'),image=CTk.CTkImage(light_image=User_Icon,dark_image=User_Icon,size=(40,40)),compound='top')#.place(x=140,y=140)
        Username = CTk.CTkEntry(Frame,placeholder_text='Example: Virati Akira Nandhan Reddy',height=40,width=340,corner_radius=5,
                                font=('Roboto',16))#;Username.place(x=30,y=204)
        
        #Password Entry And Reset Password
        Password_icon_Delay = CTk.CTkLabel(Frame,text='Password',font=('Roboto',24,'bold'),image=CTk.CTkImage(light_image=Password_Icon,dark_image=Password_Icon,size=(40,40)),compound='top')#.place(x=140,y=260)
        Forgot_Password_Delay = CTk.CTkButton(Frame,text='Forgot Password',height=0,width=0,fg_color='transparent',hover=False,font=('Roboto',10),text_color='#218CFF',command=Show_Forgot_Password_Hide_Login)#.place(x=288,y=359)
        Password = CTk.CTkEntry(Frame,placeholder_text='Example: Viratiaki@Akki#2008',height=40,width=340,corner_radius=5,
                                font=('Roboto',16))#;Password.place(x=30,y=324)
        
        #Login Button And SignUp Button
        Login_Button_Delay = CTk.CTkButton(Frame,text='Login',width=120,border_width=1,text_color='Green',fg_color='transparent',font=('Roboto',16,'bold'),
                      command=Login_Actions)#.place(x=142,y=400)
        Sign_Up_Delay = CTk.CTkButton(Frame,text='Sign Up',width=50,height=15,border_width=1,text_color='Lime',fg_color='transparent',font=('Roboto',12,'bold'),
                                      command=Signup_Redirecting,corner_radius=10)#.place(x=2,y=538)
        
        


        #Reset Password Screen
        Frame_Reset_Password = CTk.CTkFrame(Window,corner_radius=0)
        Frame_Reset_Password.configure(width=400,height=560)
        Frame_Reset_Password.place(x=x_reset,y=20)
        Heading_Reset = CTk.CTkLabel(Frame_Reset_Password,text='Forgot Password',font=('Freestyle Script',42,'bold'),width=5,text_color='Lime')#.place(x=105,y=2)
        Greet_Reset = CTk.CTkLabel(Frame_Reset_Password,text='Sad To See You Here!',font=('Freestyle Script',28),width=5,text_color='Red')#.place(x=30,y=65)
        Cancel_Reset = CTk.CTkButton(Frame_Reset_Password,text='Cancel',fg_color='transparent',height=15,border_width=1,hover_color='#A1FB8E',width=45,command=Hide_Forgot_Password_Show_Login)#.place(x=2,y=538)

        
        Window.after(1200,Login_Display_Items)
        
        
        









        #Copyright Note And The Way To Enter The Developer Options/License Information
        CTk.CTkButton(Frame,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',font=('Calibri',8),command=License_Developer_Documentation,hover=False,width=0,
                      height=0,fg_color='transparent',text_color='#218CFF').place(x=243,y=547)
        CTk.CTkLabel(Frame_Reset_Password,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',font=('Calibri',8)).place(x=247,y=540)
        
        Window.mainloop()

# Login(['Developer','Aki'],['4321','1000'],['eve321','Ki000'],[None,10000]).Display_Login()































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