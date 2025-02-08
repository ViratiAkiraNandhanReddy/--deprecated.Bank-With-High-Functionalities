#Importing Required Modules/Packages
import customtkinter as CTk  #Customized Tkinter Module
import PIL.Image  #Pillow Module To Open The Image
from random import randint  #Random Module To Generate Random Wallpaper
from datetime import datetime  #DateTime Module To Show The Date
from .Create_Account import Create_Account  #Create Account Module
from .User_Actions import User_Requirements  #User Requirements Module
from . import Detailed_Licence

#Used To Show Date
Raw_Time = datetime.now() #Shows The Current Date And Time
Date_Day = Raw_Time.strftime('%d/%b/%Y - %A') #Shows As 02/Feb/2025 - Sunday

#Background Image At Login Screen
Random_Background = randint(0,30)
Login_Background = PIL.Image.open(fr'Bank_Package\Visual Data\Login Wallpapers\{Random_Background}.jpg') #Random Wallpaper

#Required Icon For The Details
User_Icon = PIL.Image.open(r'Bank_Package\Visual Data\User Icon-Multi.png')
Password_Icon = PIL.Image.open(r'Bank_Package\Visual Data\Locked.png')
Security_Icon = PIL.Image.open(r'Bank_Package\Visual Data\Secured.png')
Developer_Icon = PIL.Image.open(r'Bank_Package\Visual Data\Chat-Bot.png')

#Deny The User To Close The Window
def Disable_Exit():
    ''' This Function Will Be Called When The User Clicked The Exit Button In The Window ; Then This Function Does Nothing Because This 
    Function Has No Statements Other Than Pass ; So That Window Can't Be Closed By The User'''
    pass

#Class For The Developer
class Developer:

    '''This Class Is Used To Show The Developer Information To The User ; Also This Class Is Used To Show The Developer's Image To The
    User ; This Class Is Used To Show The Total Balance Present In The Bank ; So The User Can Able To Know The Total Balance Present
    In The Bank ; This Class Is Used To Show The Developer's Information To The User'''

    def __init__(self,User_Balance):
        self.User_Balance = User_Balance

    def Developer_Autentication(self):
        '''This Function Is Used To Authenticate The Developer ; So The Developer Can Able To Access The Developer Information ; This
        Function Is Used To Show The Developer's Login Screen To The Developer ; So The Developer Can Able To Login To The Developer'''
        pass

    def Display_Developer(self):
        '''This Function Is Used To Display The Developer Information To The User ; So The User Can Able To View The Developer Information'''
       
        #Main Window For The Developer
        Developer_Window = CTk.CTk()
        Developer_Window.geometry('1000x500')
        Developer_Window.title('Developer')
        Developer_Window.resizable(False,False)
        Developer_Frame = CTk.CTkFrame(Developer_Window,width=980,height=480)
        Developer_Frame.place(x=10,y=10)

        #Developer's Information
        Total_Balance = CTk.CTkFrame(Developer_Frame,width=900,height=40,fg_color='Yellow',border_color='Orange',border_width=1)
        Total_Balance.place(x=5,y=5)
        CTk.CTkLabel(Total_Balance,text='Total Balance Present In The Bank',font=('Freestyle Script',26,'bold'),text_color='Purple',height=0,width=690).place(x=5,y=2)
        CTk.CTkLabel(Total_Balance,text=f'${sum(self.User_Balance)}',font=('Roboto',10,'bold'),text_color='Green',height=0).place(x=2,y=25)
        # CTk.CTkButton(Developer_Frame,text='',image=CTk.CTkImage(light_image=Developer_Icon,dark_image=Developer_Icon)).place(x=89,y=100)
        CTk.CTkButton(Developer_Frame,text='Exit',command='').place(x=200,y=300)








        Developer_Window.mainloop()
        
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
        '''This Function Is Used To Initialize The Required Variables For The License Screen ; So That We Can Able To Use The Variables'''
        self.Detailed_Licence = Detailed_Licence

    #Main Window For The License
    def Show_License(self):
        '''This Function Is Used To Show The License Information To The User In A Scrollable Format ; So The User Can Able To View The
        License Information In A Scrollable Format'''

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
    '''This Class Is Used To Show The Documentation Of The Software To The User ; Also This Class Is Used To Show The Documentation
    In A Scrollable Format ; So The User Can Able To View The Documentation In A Scrollable Format'''
    def __init__(self):
        pass

    #Documentation Of The SoftWare
    def Show_Documentation():
        pass

#Class For The Login
class Login:

    '''This Class Is Used To Show The Login Screen To The User ; Also This Class Is Used To Redirect The User To The User Actions
    If The User Name And Password Matches ; This Class Is Used To Redirect The User To The Signup Screen If The User Is Not Available
    In The DataBase ; This Class Is Used To Show The License, Developer, Documentation Options To The User ; So The User Can Able To
    View The License, Developer, Documentation ; This Class Is Used To Show The Reset Password Screen To The User ; So The User Can
    Able To Reset The Password If They Forgot The Password'''

    #Initialize The Values To Start The Class
    def __init__(self,Available_Accounts,User_PinCodes,User_Security_Codes,User_Balance):
        self.Available_Accounts:list[str] = Available_Accounts
        self.User_PinCodes:list[str] = User_PinCodes
        self.User_Security_Codes:list[str] = User_Security_Codes
        self.User_Balance:list[int|float] = User_Balance

    #Key Finder
    def User_func(self,User=None)->int:
        '''This Function Returns The Index Value Of The Account ; if The Account is Not Present Then Gives The Error'''
        User_index = self.Available_Accounts.index(User)
        return User_index

    #Shows The Login Window In The Computer Screen i.e Windows/Mac
    def Display_Login(self):
        
        '''This Function Is Used To Display The Login Screen To The User ; So The User Can Able To Login To The Account ; Also This
        Function Is Used To Show The License, Developer, Documentation Options To The User ; So The User Can Able To View The License,
        Developer, Documentation ; Also This Function Is Used To Show The Reset Password Screen To The User ; So The User Can Able To
        Reset The Password If They Forgot The Password'''

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
            Destroy_Reset_Password_Items()
            Hide_Reset_Password()
            Show_Login()
        
        #Shows The Reset Password Screen Then Hides The Login Screen in The Window
        def Show_Forgot_Password_Hide_Login():
            Destroy_Login_Items()
            Hide_Login()
            Show_Reset_Password()
        
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
            Copyright_Note.place(x=243,y=547)

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
            Copyright_Note.place_forget()
            Window.after(900,Reset_Password_Display_Items)

        #To Show The Items After The Reset Password Screen Appears
        def Reset_Password_Display_Items():
            Heading_Reset.place(x=105,y=2)
            Greet_Reset.place(x=30,y=65)
            Subheading_Reset.place(x=33,y=90)
            User_icon_Reset.place(x=140,y=140)
            Username_At_Reset_Password.place(x=30,y=204)
            Security_icon_Reset.place(x=120,y=250)
            Forgot_Security_Code_Delay.place(x=270,y=359)
            Security_Code_At_Reset.place(x=30,y=324)
            Request_Reset_Password.place(x=142,y=400)
            Cancel_Reset.place(x=2,y=538)
            Copyright_Note_Reset.place(x=247,y=541)

        #To Hide The Items Before The Reset Password Screen Disappears
        def Destroy_Reset_Password_Items():
            Heading_Reset.place_forget()
            Greet_Reset.place_forget()
            Subheading_Reset.place_forget()
            User_icon_Reset.place_forget()
            Username_At_Reset_Password.place_forget()
            Security_icon_Reset.place_forget()
            Forgot_Security_Code_Delay.place_forget()
            Security_Code_At_Reset.place_forget()
            Request_Reset_Password.place_forget()
            Cancel_Reset.place_forget()
            Copyright_Note_Reset.place_forget()
            Window.after(900,Login_Display_Items)
            pass

        #Redirecting To Signup Screen And All The Processing Is Done Here
        def Signup_Redirecting():

            #Destroying The Login Screen
            Window.destroy()

            #Going Inside The Create_Account Class
            try:

                New_Account = Create_Account(Available_Accounts=self.Available_Accounts,User_Security_Codes=self.User_Security_Codes);New_Account.Creating_New_Account()
                
                #Appending All The Data 
                for User_Name,User_Password,Security_Code in New_Account.New_Account_Details:

                    self.Available_Accounts.append(User_Name)
                    self.User_PinCodes.append(User_Password)
                    self.User_Security_Codes.append(Security_Code)
                
                #Clearing All The Data From The Class
                New_Account.Data_Clear()

                #Showing The Login Screen
                Login(self.Available_Accounts,self.User_PinCodes,self.User_Security_Codes,self.User_Balance).Display_Login()

            except:

                #if The Create_Account Module is Missing
                Login(self.Available_Accounts,self.User_PinCodes,self.User_Security_Codes,self.User_Balance).Display_Login()

        #If The Username Matches To The Password Then Redirecting To The User Actions
        def Login_Actions():
            User_Name = Username.get()
            User_Password = Password.get()

            def Redirect_To_User_Actions():

                try:
                    Security_Code = self.User_Security_Codes[self.User_func(User_Name)]
                    User_Balance = self.User_Balance[self.User_func(User_Name)]
                    Window.destroy()
                    User_Requirements(User_Name,User_Password,Security_Code,User_Balance).User_Interface()
                    Login(self.Available_Accounts,self.User_PinCodes,self.User_Security_Codes,self.User_Balance).Display_Login()
                except:
                    pass

            #If the Username Is Not Entered But Password Is Entered 
            if (not User_Name) and User_Password:
                Username_Error = CTk.CTkLabel(Frame,text='Username is Incomplete',text_color='Orange');Username_Error.place(x=133,y=442)
                Username_Error.after(2000,Username_Error.destroy)
            
            #If The Given Username Is Already Exists In The Data Base and Password is Entered
            elif (User_Name and (User_Name not in self.Available_Accounts)) and User_Password:
                Username_Not_Exists_Error = CTk.CTkLabel(Frame,text=f'The Given Username Does Not Exists',text_color='Orange');Username_Not_Exists_Error.place(x=98,y=442)
                Username_Not_Exists_Error.after(2000,Username_Not_Exists_Error.destroy)
                
            #If The Username is Only Digits and Password is Entered
            elif User_Name.isdigit() and User_Password:
                Username_Digit_Error = CTk.CTkLabel(Frame,text='Username Can\'t Be Only Numbers/Digits',text_color='Orange');Username_Digit_Error.place(x=92,y=442)
                Username_Digit_Error.after(2000,Username_Digit_Error.destroy)
            
            #If Both Username And Password Is not Entered
            elif (not User_Name) and (not User_Password):
                Username_password_Error = CTk.CTkLabel(Frame,text='Username and Password is Incomplete',text_color='Orange');Username_password_Error.place(x=96,y=442)
                Username_password_Error.after(2000,Username_password_Error.destroy)

            #If Password Is Not Entered But Username Is Entered
            elif (not User_Password) and User_Name:
                Password_Error = CTk.CTkLabel(Frame,text='Password is Incomplete',text_color='Orange');Password_Error.place(x=133,y=442)
                Password_Error.after(2000,Password_Error.destroy)
            
            #If The Username is Entered And The Password Contains Less Than 6 Characters
            elif User_Name and (User_Password != self.User_PinCodes[self.User_func(User_Name)]):
                Password_Rule_Error = CTk.CTkLabel(Frame,text='The Password is incorrect. Try Again!',text_color='Orange');Password_Rule_Error.place(x=100,y=442)
                Password_Rule_Error.after(2000,Password_Rule_Error.destroy)

            #Successfully Passed All The Criteria
            else:
                Processing = CTk.CTkLabel(Frame,text='Processing...',text_color='Orange');Processing.place(x=166,y=442)
                Processing.after(2000,Redirect_To_User_Actions)

        #Shows The License, Developer, Documentation Options
        def License_Developer_Documentation():
            '''Used To Show The License, Developer, Documentation Options To The User ; So The User Can Able To View The License,
            Developer, Documentation'''

            #Shows The License Window
            def Show_License_Window():
                Dev_Doc.destroy()
                License(Detailed_Licence).Show_License()

            #Shows The Documentation Window
            def Show_Documentation_Window():
                Dev_Doc.destroy()
                Documentation.Show_Documentation()

            #Shows The Developer Window
            def Show_Developer_Window():
                Dev_Doc.destroy()
                Developer(self.User_Balance).Display_Developer()

            #Main Window For The License, Developer, Documentation
            Dev_Doc = CTk.CTk()
            Dev_Doc.geometry('220x182')
            Dev_Doc.resizable(False,False)
            Dev_Doc.title('Bank\'s Backend Options')

            #Frame For The License, Developer, Documentation
            Dev_Doc_Frame = CTk.CTkFrame(Dev_Doc)
            Dev_Doc_Frame.configure(width=200,height=162)
            Dev_Doc_Frame.place(x=10,y=10)

            #Buttons For The License, Developer, Documentation
            CTk.CTkButton(Dev_Doc_Frame,text='Developer',font=('Roboto',16,'bold'),fg_color='Orange',hover_color='Yellow',text_color='Black',width=180,height=38,command=Show_Developer_Window).place(x=10,y=12)
            CTk.CTkButton(Dev_Doc_Frame,text='Documentation',font=('Roboto',16,'bold'),width=180,height=38,fg_color='#E63B60',hover_color='#067FD0',command=Show_Documentation_Window).place(x=10,y=62)
            CTk.CTkButton(Dev_Doc_Frame,text='License',font=('Roboto',16,'bold'),width=180,height=38,fg_color='#797EF6',hover_color='#4ADEDE',command=Show_License_Window).place(x=10,y=112)
            Dev_Doc.mainloop()

        #If The Security Code Was Forgotten
        def Forgot_Security_Code():
            Heading_Reset.place_forget();Greet_Reset.place_forget();Subheading_Reset.place_forget();User_icon_Reset.place_forget()
            Username_At_Reset_Password.place_forget();Security_icon_Reset.place_forget();Forgot_Security_Code_Delay.place_forget()
            Security_Code_At_Reset.place_forget();Request_Reset_Password.place_forget()
            
            pass

        #Requesting To Reset The Password
        def Request_Password_To_Reset():
            Username_Reset = Username_At_Reset_Password.get()
            User_Security_Code_Reset = Security_Code_At_Reset.get()

            def Security_Code_Accepted():
                pass
            
            #If the Username Is Not Entered But Password Is Entered 
            if (not Username_Reset) and User_Security_Code_Reset:
                Username_Error = CTk.CTkLabel(Frame,text='Username is Incomplete',text_color='Orange');Username_Error.place(x=133,y=442)
                Username_Error.after(2000,Username_Error.destroy)
            
            #If The Given Username Is Already Exists In The Data Base and Password is Entered
            elif Username_Reset in self.Available_Accounts and User_Security_Code_Reset:
                Username_Exists_Error = CTk.CTkLabel(Frame,text=f'The Given Username Already Exists',text_color='Orange');Username_Exists_Error.place(x=108,y=442)
                Username_Exists_Error.after(2000,Username_Exists_Error.destroy)
                
            #If The Username is Only Digits and Password is Entered
            elif Username_Reset.isdigit() and User_Security_Code_Reset:
                Username_Digit_Error = CTk.CTkLabel(Frame,text='Username Can\'t Be Only Numbers/Digits',text_color='Orange');Username_Digit_Error.place(x=92,y=442)
                Username_Digit_Error.after(2000,Username_Digit_Error.destroy)
            
            #If Both Username And Password Is not Entered
            elif (not Username_Reset) and (not User_Security_Code_Reset):
                Username_password_Error = CTk.CTkLabel(Frame,text='Username and Password is Incomplete',text_color='Orange');Username_password_Error.place(x=96,y=442)
                Username_password_Error.after(2000,Username_password_Error.destroy)

            #If Password Is Not Entered But Username Is Entered
            elif (not User_Security_Code_Reset) and Username_Reset:
                Password_Error = CTk.CTkLabel(Frame,text='Password is Incomplete',text_color='Orange');Password_Error.place(x=133,y=442)
                Password_Error.after(2000,Password_Error.destroy)
            
            #If The Username is Entered And The Password Contains Less Than 6 Characters
            elif Username_Reset and (User_Security_Code_Reset != self.User_Security_Codes[self.User_func(Username_Reset)]):
                Password_Rule_Error = CTk.CTkLabel(Frame,text='The Security Code is incorrect. Try Again!',text_color='Orange');Password_Rule_Error.place(x=87,y=442)
                Password_Rule_Error.after(2000,Password_Rule_Error.destroy)

            #Successfully Passed All The Criteria
            else:
                Processing = CTk.CTkLabel(Frame,text='Requesting...',text_color='Orange');Processing.place(x=166,y=442)
                Processing.after(2000,Security_Code_Accepted)

        #Main Window For The Login Screen
        global Window
        Window = CTk.CTk()
        Window.title('Login')
        Window.geometry('950x600')
        Window.resizable(False,False)
        Window.protocol('WM_DELETE_WINDOW',Disable_Exit)
        CTk.CTkLabel(Window,text='',image=CTk.CTkImage(light_image=Login_Background,dark_image=Login_Background,size=(950,600))).place(x=0,y=0)
        Window.after(600,Show_Login)

        #Login Screen Items
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

        Heading_Reset = CTk.CTkLabel(Frame_Reset_Password,text='Forgot Password',font=('Freestyle Script',42,'bold'),width=5)#.place(x=105,y=2)
        Greet_Reset = CTk.CTkLabel(Frame_Reset_Password,text='Get Your Account Back!',font=('Roboto',20,'bold'),text_color='#57D956')#.place(x=30,y=65)
        Subheading_Reset = CTk.CTkLabel(Frame_Reset_Password,text='Enter Required Credentials',font=('Roboto',12),height=0)#.place(x=33,y=90)
        
        User_icon_Reset = CTk.CTkLabel(Frame_Reset_Password,text='Username',font=('Roboto',24,'bold'),image=CTk.CTkImage(light_image=User_Icon,dark_image=User_Icon,size=(40,40)),compound='top')#.place(x=140,y=140)
        Username_At_Reset_Password = CTk.CTkEntry(Frame_Reset_Password,placeholder_text='Example: Virati Akira Nandhan Reddy',height=40,width=340,corner_radius=5,
                                font=('Roboto',16))#.place(x=30,y=204)
        
        Security_icon_Reset = CTk.CTkLabel(Frame_Reset_Password,text='Security Code',font=('Roboto',24,'bold'),image=CTk.CTkImage(light_image=Security_Icon,dark_image=Security_Icon,size=(45,45)),compound='top',height=0)#.place(x=120,y=250)
        Forgot_Security_Code_Delay = CTk.CTkButton(Frame_Reset_Password,text='Forgot Security Code',height=0,width=0,fg_color='transparent',hover=False,font=('Roboto',10),text_color='#218CFF',command=Forgot_Security_Code)#.place(x=270,y=359)
        Security_Code_At_Reset = CTk.CTkEntry(Frame_Reset_Password,placeholder_text='Example: Viratiaki@Akki',height=40,width=340,corner_radius=5,
                                font=('Roboto',16))#.place(x=30,y=324)
        
        Request_Reset_Password = CTk.CTkButton(Frame_Reset_Password,text='Request',width=120,border_width=1,text_color='#3264FF',
                                               fg_color='transparent',font=('Roboto',16,'bold'),hover_color='Light Blue',command=Request_Password_To_Reset)#.place(x=142,y=400)

        Cancel_Reset = CTk.CTkButton(Frame_Reset_Password,text='Cancel',fg_color='transparent',height=15,border_width=1,hover_color='#A1FB8E',width=45,command=Hide_Forgot_Password_Show_Login)#.place(x=2,y=538)
        
        #Showing The Login Screen Items
        Window.after(1500,Login_Display_Items)

        #Copyright Note And The Way To Enter The Developer Options/License Information
        Copyright_Note = CTk.CTkButton(Frame,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',font=('Calibri',8),command=License_Developer_Documentation,hover=False,width=0,
                      height=0,fg_color='transparent',text_color='#218CFF')#.place(x=243,y=547)
        Copyright_Note_Reset = CTk.CTkLabel(Frame_Reset_Password,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',font=('Calibri',8))#.place(x=247,y=540)
        
        Window.mainloop()

# Login(['Developer','Aki'],['4321','1000'],['eve321','Ki000'],[0,10000]).Display_Login()