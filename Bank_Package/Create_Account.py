'''This Module is Used For The Creation Of A New Account By Taking The Inputs From The User And Returns A List 
Of tuple Which Can Be Read By Another Module ; This Module Can Stand Alone i.e: No Dependencies

This Module Asks For The Username And Password Then Creates A Security Code 

What Does Security Code Do ? 

The Security Code is Used To Recover The Account if User Has Forgotten The Password *Should Not Share With Others
Security is a 12 Letter Unique Code Which is Made Up Of Data From Username And Password'''

#Importing The Required Modules/Packages
import PIL.Image
import customtkinter as CTk

#Icon For Better Visualization
User_Icon = PIL.Image.open(r'Bank_Package\Visual Data\User Icon.png')
Password_Icon = PIL.Image.open(r'Bank_Package\Visual Data\Key.png')

#Deny The User To Close The Window
def Disable_Exit():
    ''' This Function Will Be Called When The User Clicked The Exit Button In The Window ; Then This Function Does Nothing Because This 
    Function Has No Statements Other Than Pass ; So That Window Can't Be Closed By The User'''
    pass

#Object That Creates An New Account
class Create_Account:
    '''Class Create_Account is Used To Create An Account By Just Taking The User Inputs Then Makes A Security Code Based On The Username And 
    Password ; Security Code Will Be Of 12 Letters Unique ID Which Is Used To Recover The Account If The Password Was Forgotten Then 
    The Username And Password Will Be Stored In A Tuple Where This Tuple Will Be Appended In A List Called: self.New_Account_Details 
    
    Then This List Will Be Readed By Other Module To Store The Data In A File Or Database ; This Class Can Be Used As Stand Alone
    i.e: No Dependencies Are Required To Run This Class ; This Class Has A Method Called Creating_New_Account Which is Used To Create An Account
    And Also This Class Has A Method Called Data_Clear Which is Used To Clear All The Data Present In This Class'''

    #Initialize The Values To Start The Class
    def __init__(self,Available_Accounts:list[str],User_Security_Codes:list[str]):
        
        #Assigning A Values To Self Objects
        self.Available_Accounts = Available_Accounts
        self.User_Security_Codes = User_Security_Codes
        self.New_Account_Details:list[tuple] = []
    
    #Main Method Which is Used To Create An Account
    def Creating_New_Account(self):
        '''This Method is Used To Create An Account By Taking An Inputs From User And Appends To A List Which is Readed By The Another 
        Module This Method Also Creates A Security_Code By Using The User Inputs Which Are Taken:\n
        1.Username\n
        2.Password\n
        3.Creation Of security Code\n
        4.Redirect To Login'''

        #Contains All The Possible Errors And Getting The Values
        def Check_Assign():
            '''This Function Has All The Possible Errors While Creating An Account
            And Also Creation Of Account ; This Function Plays A Important Role In Creating An Account'''

            #Getting All The Values From The Entry
            global User_Name,User_Password
            User_Name = Username.get()
            User_Password = Password.get()
            
            #Used To Say That Account is Successfully Created
            def Create_Continue():
                '''Shows A Small Popup As Account Has Been Created Sucessfully \n
                Then Destroys After 5 Seconds ; After Destroying It Will Redirect To Login'''

                #Appending The Data in List
                self.New_Account_Details.append((User_Name,User_Password,Security_Code))

                #New Window For Information
                Create = CTk.CTk()
                Create.resizable(False,False)
                Create.title('Sucessful')
                Create.geometry('300x100')

                #Information For The User
                CTk.CTkLabel(Create,text='Account Creation Successful',font=('Roboto',18,'bold'),text_color='Lime').pack(pady=12)
                CTk.CTkLabel(Create,text='Redirecting To Login..',text_color='Orange').pack()

                #Closing All The Windows
                Create.after(5000,Create.destroy)
                Window.after(5000,Window.destroy)

                Create.mainloop()

            #Creating A Security Code
            def Security_Continue():

                #Trying To Create A Security Code
                try:
                    
                    #Destroying All the Widgets
                    Processing.destroy();Sign_Up_Label.destroy();Username_Label.destroy();User_Label_Icon.destroy()
                    Username.destroy();Password_Icon_Label.destroy();Password_Label.destroy();Register.destroy()
                    Password_Rule_Label.destroy();Password.destroy()
                    
                    #Title And Heading
                    CTk.CTkLabel(Frame,text='Security Code',font=('Roboto',25,'bold')).place(x=117,y=5)
                    Window.title('Security Code')
                    
                    #Creating security Code
                    global Security_Code
                    Security_Code = (User_Name[0:4] + User_Password[3:0:-1])
                    if Security_Code not in self.User_Security_Codes:
                        Security_Code += '@Akki'
                    else:
                         Security_Code += '#Akki'
                    
                    while len(Security_Code) < 12:
                        Security_Code += '$'
                    
                    #Information About The Security Code
                    CTk.CTkLabel(Frame,text='The Code Which Is Provided Below is A Secutity Code\nWhich is Used For The Recovery Of This New Account\nif The Password was Forgotten',font=('Roboto',14,'bold')).place(x=10,y=80)
                    CTk.CTkLabel(Frame,text=Security_Code,font=('Roboto',25,'bold'),text_color='Red').place(x=114,y=160)
                    CTk.CTkLabel(Frame,text='1.Store Or Write In A Safest Place',font=('Roboto',14,'bold')).place(x=0,y=220)
                    CTk.CTkLabel(Frame,text='2.Don\'t Share This Security Code With Others',font=('Roboto',14,'bold')).place(x=0,y=240)
                    CTk.CTkLabel(Frame,text='3.This Security Codes Will Never Changes!',font=('Roboto',14,'bold')).place(x=0,y=260)
                    CTk.CTkLabel(Frame,text='4.This Security Code is Used To Recover This Account',font=('Roboto',14,'bold')).place(x=0,y=281)

                    CTk.CTkButton(Frame,text='Create And Continue',font=('Roboto',14,'bold'),fg_color='transparent',border_width=1,corner_radius=10,command=Create_Continue,text_color='Green',hover_color='Light Grey').place(x=110,y=330)

                except:
                    pass

            #If the Username Is Not Entered But Password Is Entered 
            if (not User_Name) and User_Password:
                Username_Error = CTk.CTkLabel(Frame,text='Username is Incomplete',text_color='Orange');Username_Error.place(x=133,y=352)
                Username_Error.after(2000,Username_Error.destroy)
            
            #If The Given Username Is Already Exists In The Data Base and Password is Entered
            elif User_Name in self.Available_Accounts and User_Password:
                Username_Exists_Error = CTk.CTkLabel(Frame,text=f'The Given Username Already Exists',text_color='Orange');Username_Exists_Error.place(x=108,y=352)
                Username_Exists_Error.after(2000,Username_Exists_Error.destroy)
                
            #If The Username is Only Digits and Password is Entered
            elif User_Name.isdigit() and User_Password:
                Username_Digit_Error = CTk.CTkLabel(Frame,text='Username Can\'t Be Only Numbers/Digits',text_color='Orange');Username_Digit_Error.place(x=92,y=352)
                Username_Digit_Error.after(2000,Username_Digit_Error.destroy)
            
            #If Both Username And Password Is not Entered
            elif (not User_Name) and (not User_Password):
                Username_password_Error = CTk.CTkLabel(Frame,text='Username and Password is Incomplete',text_color='Orange');Username_password_Error.place(x=96,y=352)
                Username_password_Error.after(2000,Username_password_Error.destroy)

            #If Password Is Not Entered But Username Is Entered
            elif (not User_Password) and User_Name:
                Password_Error = CTk.CTkLabel(Frame,text='Password is Incomplete',text_color='Orange');Password_Error.place(x=133,y=352)
                Password_Error.after(2000,Password_Error.destroy)
            
            #If The Username is Entered And The Password Contains Less Than 6 Characters
            elif User_Name and ((len(User_Password)<6) and (not len(User_Password) == 0)):
                Password_Rule_Error = CTk.CTkLabel(Frame,text='Password Must Contain At least 6 Characters',text_color='Orange');Password_Rule_Error.place(x=77,y=352)
                Password_Rule_Error.after(2000,Password_Rule_Error.destroy)

            #Successfully Passed All The Criteria
            else:
                Processing = CTk.CTkLabel(Frame,text='Processing...',text_color='Orange');Processing.place(x=166,y=352)
                Processing.after(2000,Security_Continue)
                
        #Canceling The Create Account And Redirecting To Login
        def Cancel():
            '''This Function is Used To Cancel The Account Creation And Redirects To The Login Screen'''
            Window.destroy()

        #Main Window For Signing Up
        Window = CTk.CTk()
        Window.resizable(False,False)
        Window.title('Creating Account')
        Window.geometry('450x450')
        Window.protocol("WM_DELETE_WINDOW",Disable_Exit)
    
        #Frame For More Detailed
        Frame = CTk.CTkFrame(Window)
        Frame.configure(width=400,height=400)
        Frame.place(x=25,y=25)
        Sign_Up_Label = CTk.CTkLabel(Frame,text='Sign Up',font=('Roboto',25,'bold'));Sign_Up_Label.place(x=155,y=5)

        #Username Entry
        Username_Label = CTk.CTkLabel(Frame,text='Username',font=('Roboto',18,'bold'));Username_Label.place(x=50,y=85)
        User_Label_Icon = CTk.CTkLabel(Frame,text='',image=CTk.CTkImage(light_image=User_Icon,dark_image=User_Icon,size=(40,40)));User_Label_Icon.place(x=10,y=115)
        Username = CTk.CTkEntry(Frame,placeholder_text='Example: Virati Akira Nandhan Reddy',height=40,width=300,corner_radius=5,
                                font=('Roboto',16))
        Username.place(x=50,y=115)

        #Password Entry
        Password_Label = CTk.CTkLabel(Frame,text='Password',font=('Roboto',18,'bold'));Password_Label.place(x=50,y=190)
        Password_Icon_Label = CTk.CTkLabel(Frame,text='',image=CTk.CTkImage(light_image=Password_Icon,dark_image=Password_Icon,size=(40,40)));Password_Icon_Label.place(x=10,y=220)
        Password_Rule_Label = CTk.CTkLabel(Frame,text='*Must Contain At least 6 Characters',font=('Roboto',9));Password_Rule_Label.place(x=50,y=252)
        Password = CTk.CTkEntry(Frame,placeholder_text='Example: Viratiaki@Akki#2008',height=40,width=300,corner_radius=5,font=('Roboto',16))
        Password.place(x=50,y=220)

        Register = CTk.CTkButton(Frame,text='Register',width=120,border_width=1,text_color='Green',fg_color='transparent',
                                 font=('Roboto',16,'bold'),hover_color='#5E5E5E',command=Check_Assign)
        Register.place(x=142,y=310)

        CTk.CTkButton(Frame,text='Cancel',width=60,height=20,border_width=1,text_color='Grey',fg_color='transparent',font=('Roboto',12,'bold'),
                      hover_color='#5E5E5E',command=Cancel).place(x=2,y=378)
        
        #Copyright Note 
        CTk.CTkLabel(Window,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',font=('Calibri',8)).place(x=295,y=430)

        Window.mainloop()
    
    #Clear All Data
    def Data_Clear(self):
        '''Delete All The Data Present In This Class\n
        Example: User_Name , User_Password , User_Security_Code'''
        self.New_Account_Details.clear()

# Create_Account([],[]).Creating_New_Account()
#Satisfied Code Completion:66%     
'''                                                            End Of Program                                                                 '''