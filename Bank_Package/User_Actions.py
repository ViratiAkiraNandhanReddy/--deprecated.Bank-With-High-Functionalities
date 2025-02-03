import customtkinter as CTk
from datetime import datetime

#Deny The User To Close The Window
def Disable_Exit():
    ''' This Function Will Be Called When The User Clicked The Exit Button In The Window ; Then This Function Does Nothing Because This 
    Function Has No Statements Other Than Pass ; So That Window Can't Be Closed'''
    pass

#The Present/Current Time As Available In Your Computer
Raw_Time = datetime.now()
Date_Day = Raw_Time.strftime('%d/%b/%Y - %A')
Time_Greetings = int(Raw_Time.strftime('%H'))

if Time_Greetings >= 0 and Time_Greetings < 12:
    Greetings = 'Good Morning'

elif Time_Greetings >= 12 and Time_Greetings < 16:
    Greetings = 'Good Afternoon'

elif Time_Greetings >= 16 and Time_Greetings < 20:
    Greetings = 'Good Evening'

else:
    Greetings = 'Good Night'


class Loan:
    def __init__(self):
        pass

    def Show_interest_Calculator():
        pass
    #Calculates the loan interest
    def Interest(Amount:int|float)->float:
        if Amount <= 10E6 and Amount > 9E6:
            return 1.29
        elif Amount <= 9E6 and Amount > 8E6:
            return 1.99
        elif Amount <= 8E6 and Amount > 7E6:
            return 2.29
        elif Amount <= 7E6 and Amount > 6E6:
            return 2.84
        elif Amount <= 6E6 and Amount > 5E6:
            return 3.14
        elif Amount <= 5E6 and Amount > 4E6:
            return 3.99
        elif Amount <= 4E6 and Amount > 3E6:
            return 4.25
        elif Amount <= 3E6 and Amount > 2E6:
            return 4.85
        elif Amount <= 2E6 and Amount > 1E6:
            return 5.19
        elif Amount <= 1E6 and Amount > 5E5:
            return 5.88
        else:
            return 7.49
        

class User_Requirements:
    def __init__(self,User_Name:str,User_Password:str,Security_Code:str,User_Balance:float):
        self.User_Name = User_Name
        self.User_Password = User_Password
        self.Security_Code = Security_Code
        self.User_Balance = User_Balance

    def Deposit():
        pass

    def Withdraw():
        pass

    def User_Interface(self):

        #Creation Of Window And Settings Also Showing The Date
        Window = CTk.CTk()
        Window.title('User Interface')
        Window.resizable(False,False)
        Window.geometry('1200x600')
        Window.protocol('WM_DELETE_WINDOW',Disable_Exit)
        CTk.CTkLabel(Window,text=Date_Day,text_color='Orange',height=10).place(x=1050,y=2)
        CTk.CTkLabel(Window,text=f'Security Code: {self.Security_Code}',text_color='Orange',height=10).place(x=20,y=2)
        
        
        #Main Frame Contained In The Window
        Frame = CTk.CTkFrame(Window)
        Frame.configure(width=1160,height=560)
        Frame.place(x=20,y=20)
        
        #User Greetings And Logout
        CTk.CTkLabel(Frame,text=f'{Greetings}, {self.User_Name}',font=('Freestyle Script',40,'bold'),text_color='#378F9C').place(x=10,y=2)
        CTk.CTkButton(Frame,text='Logout',font=('Freestyle Script',30),fg_color='transparent',hover=False,width=40,height=14,text_color='Red',command=Window.destroy).place(x=1100,y=1)
        CTk.CTkLabel(Frame,text='-'*1160,text_color='Grey',font=('Roboto',2),height=0).place(x=0,y=48)

        #Balance Frame That Shows The User Bank Balance Which is Contained in The Main Frame
        Balance_Frame = CTk.CTkFrame(Frame,fg_color='#9E1076')
        Balance_Frame.configure(width=200,height=50)
        Balance_Frame.place(x=10,y=60)
        CTk.CTkLabel(Balance_Frame,text='Your Bank Balance:',font=('Roboto',16),height=14).place(x=5,y=3)
        Balance = CTk.CTkLabel(Balance_Frame,text=f'${self.User_Balance:.2f}',text_color='Lime').place(x=5,y=20)

        CTk.CTkButton(Frame,text='Deposit').place(x=1010,y=484)
        CTk.CTkButton(Frame,text='Withdraw').place(x=1010,y=522)








        


        


        #Copyright Note 
        CTk.CTkLabel(Window,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',font=('Calibri',8)).place(x=1046,y=580)

        Window.mainloop()

User_Requirements('Virati Akira Nandhan Reddy','','Virati181@Akki',1234567986548).User_Interface()


