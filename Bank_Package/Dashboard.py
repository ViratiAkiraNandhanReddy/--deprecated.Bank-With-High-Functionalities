import customtkinter as CTk
from datetime import datetime
from PIL import Image


# User_Icon = Image.open(r'Bank_Package\Visual Data\User Icon.png')
darkModeIcon = Image.open(r'Bank_Package\Visual Data\dark.png')
lightModeIcon = Image.open(r'Bank_Package\Visual Data\light.png')
dateIcon = Image.open(r'Bank_Package\Visual Data\Date.png')
AuthenticationIcon = Image.open(r'Bank_Package\Visual Data\Two Factor Authentication.png')
Danger_Zone_Icon = Image.open(r'Bank_Package\Visual Data\Danger Zone.png')
# securityCodeIcon = Image.open(r'Bank_Package\Visual Data\securityCode.png')
# depositIcon = Image.open(r'Bank_Package\Visual Data\deposit.png')
# withdrawIcon = Image.open(r'Bank_Package\Visual Data\withdraw.png')
# settingsIcon = Image.open(r'Bank_Package\Visual Data\settings.png')
# logoutIcon = Image.open(r'Bank_Package\Visual Data\logout.png')
# balanceIcon = Image.open(r'Bank_Package\Visual Data\balance.png')
# interestIcon = Image.open(r'Bank_Package\Visual Data\interest.png')
# loanIcon = Image.open(r'Bank_Package\Visual Data\loan.png')
# loanInterestIcon = Image.open(r'Bank_Package\Visual Data\loanInterest.png')
# loanCalculatorIcon = Image.open(r'Bank_Package\Visual Data\loanCalculator.png')


#The Present/Current Time As Available In Your Computer
Raw_Time = datetime.now()
Date_Day = Raw_Time.strftime('%d/%b/%Y - %a')
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

    def Show_interest_Calculator(self):
        pass
    #Calculates the loan interest
    def Interest(self,Amount:int|float)->float:
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

    Universal_Profile_Icon_0 = Image.open(r'Bank_Package\Visual Data\User Icons\Universal_Profile_Icon_0.png')
    Universal_Profile_Icon_1 = Image.open(r'Bank_Package\Visual Data\User Icons\Universal_Profile_Icon_1.png')
    Universal_Profile_Icon_2 = Image.open(r'Bank_Package\Visual Data\User Icons\Universal_Profile_Icon_2.png')
    Universal_Profile_Icon_3 = Image.open(r'Bank_Package\Visual Data\User Icons\Universal_Profile_Icon_3.png')

    Boys_Profile_Icon_0 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_0.png')
    Boys_Profile_Icon_1 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_1.png')
    Boys_Profile_Icon_2 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_2.png')
    Boys_Profile_Icon_3 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_3.png')
    Boys_Profile_Icon_4 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_4.png')
    Boys_Profile_Icon_5 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_5.png')
    Boys_Profile_Icon_6 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_6.png')
    Boys_Profile_Icon_7 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_7.png')
    Boys_Profile_Icon_8 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_8.png')
    Boys_Profile_Icon_9 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_9.png')
    Boys_Profile_Icon_10 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_10.png')
    Boys_Profile_Icon_11 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_11.png')
    Boys_Profile_Icon_12 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_12.png')
    Boys_Profile_Icon_13 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_13.png')
    Boys_Profile_Icon_14 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_14.png')
    Boys_Profile_Icon_15 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_15.png')
    Boys_Profile_Icon_16 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_16.png')
    Boys_Profile_Icon_17 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_17.png')
    Boys_Profile_Icon_18 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_18.png')
    Boys_Profile_Icon_19 = Image.open(r'Bank_Package\Visual Data\User Icons\Boys_Profile_Icon_19.png')

    Girls_Profile_Icon_0 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_0.png')
    Girls_Profile_Icon_1 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_1.png')
    Girls_Profile_Icon_2 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_2.png')
    Girls_Profile_Icon_3 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_3.png')
    Girls_Profile_Icon_4 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_4.png')
    Girls_Profile_Icon_5 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_5.png')
    Girls_Profile_Icon_6 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_6.png')
    Girls_Profile_Icon_7 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_7.png')
    Girls_Profile_Icon_8 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_8.png')
    Girls_Profile_Icon_9 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_9.png')
    Girls_Profile_Icon_10 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_10.png')
    Girls_Profile_Icon_11 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_11.png')
    Girls_Profile_Icon_12 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_12.png')
    Girls_Profile_Icon_13 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_13.png')
    Girls_Profile_Icon_14 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_14.png')
    Girls_Profile_Icon_15 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_15.png')
    Girls_Profile_Icon_16 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_16.png')
    Girls_Profile_Icon_17 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_17.png')
    Girls_Profile_Icon_18 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_18.png')
    Girls_Profile_Icon_19 = Image.open(r'Bank_Package\Visual Data\User Icons\Girls_Profile_Icon_19.png')

    Kids_Profile_Icon_0 = Image.open(r'Bank_Package\Visual Data\User Icons\Kids_Profile_Icon_0.png')
    Kids_Profile_Icon_1 = Image.open(r'Bank_Package\Visual Data\User Icons\Kids_Profile_Icon_1.png')
    Kids_Profile_Icon_2 = Image.open(r'Bank_Package\Visual Data\User Icons\Kids_Profile_Icon_2.png')
    Kids_Profile_Icon_3 = Image.open(r'Bank_Package\Visual Data\User Icons\Kids_Profile_Icon_3.png')

    def __init__(self,UserData: dict):
        self.UserData = UserData
        self.ProfileIcon: str = 'self.' + UserData.get('ProfileIcon','Universal_Profile_Icon_0')
        self.Value = True
        self.Date = False
    

    def Deposit(self):
        Deposit = CTk.CTkFrame(Frame,width=200,height=100);Deposit.place(x=1000,y=200)
        val = CTk.CTkInputDialog(text='Enter Amount',title='Deposit')

    def Withdraw(self):
        pass
    
    def Settings(self):


        def changeProfilePicture():

            currentProfileIcon.configure(state = 'disabled')

            def readProfileIcon(Icon:str):

                self.ProfileIcon = Icon
                User_Info.configure(image = CTk.CTkImage(light_image=eval(self.ProfileIcon),dark_image=eval(self.ProfileIcon),size=(40,40)))
                currentProfileIcon.configure(image = CTk.CTkImage(light_image=eval(self.ProfileIcon),dark_image=eval(self.ProfileIcon),size=(35,35)))
                ProfileIconFrame.place_forget()
                currentProfileIcon.configure(state = 'normal')

            ProfileIconFrame = CTk.CTkScrollableFrame(Settings_Frame,width=232,height=230);ProfileIconFrame.place(x=895,y=248)


            #Universal Profile Icons
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Universal_Profile_Icon_0,dark_image=self.Universal_Profile_Icon_0,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Universal_Profile_Icon_0')).grid(column=0,row=0)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Universal_Profile_Icon_1,dark_image=self.Universal_Profile_Icon_1,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Universal_Profile_Icon_1')).grid(column=1,row=0,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Universal_Profile_Icon_2,dark_image=self.Universal_Profile_Icon_2,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Universal_Profile_Icon_2')).grid(column=2,row=0)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Universal_Profile_Icon_3,dark_image=self.Universal_Profile_Icon_3,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Universal_Profile_Icon_3')).grid(column=3,row=0,padx=5)

            #Boys Profile Icons
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_0,dark_image=self.Boys_Profile_Icon_0,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_0')).grid(column=0,row=1,pady=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_1,dark_image=self.Boys_Profile_Icon_1,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_1')).grid(column=1,row=1,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_2,dark_image=self.Boys_Profile_Icon_2,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_2')).grid(column=2,row=1)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_3,dark_image=self.Boys_Profile_Icon_3,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_3')).grid(column=3,row=1,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_4,dark_image=self.Boys_Profile_Icon_4,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_4')).grid(column=0,row=2)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_5,dark_image=self.Boys_Profile_Icon_5,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_5')).grid(column=1,row=2,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_6,dark_image=self.Boys_Profile_Icon_6,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_6')).grid(column=2,row=2)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_7,dark_image=self.Boys_Profile_Icon_7,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_7')).grid(column=3,row=2,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_8,dark_image=self.Boys_Profile_Icon_8,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_8')).grid(column=0,row=3,pady=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_9,dark_image=self.Boys_Profile_Icon_9,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_9')).grid(column=1,row=3,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_10,dark_image=self.Boys_Profile_Icon_10,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_10')).grid(column=2,row=3)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_11,dark_image=self.Boys_Profile_Icon_11,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_11')).grid(column=3,row=3,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_12,dark_image=self.Boys_Profile_Icon_12,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_12')).grid(column=0,row=4)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_13,dark_image=self.Boys_Profile_Icon_13,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_13')).grid(column=1,row=4,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_14,dark_image=self.Boys_Profile_Icon_14,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_14')).grid(column=2,row=4)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_15,dark_image=self.Boys_Profile_Icon_15,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_15')).grid(column=3,row=4,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_16,dark_image=self.Boys_Profile_Icon_16,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_16')).grid(column=0,row=5,pady=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_17,dark_image=self.Boys_Profile_Icon_17,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_17')).grid(column=1,row=5,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_18,dark_image=self.Boys_Profile_Icon_18,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_18')).grid(column=2,row=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Boys_Profile_Icon_19,dark_image=self.Boys_Profile_Icon_19,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Boys_Profile_Icon_19')).grid(column=3,row=5,padx=5)

            #Girls Profile Icons
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_0,dark_image=self.Girls_Profile_Icon_0,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_0')).grid(column=0,row=6)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_1,dark_image=self.Girls_Profile_Icon_1,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_1')).grid(column=1,row=6,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_2,dark_image=self.Girls_Profile_Icon_2,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_2')).grid(column=2,row=6)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_3,dark_image=self.Girls_Profile_Icon_3,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_3')).grid(column=3,row=6,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_4,dark_image=self.Girls_Profile_Icon_4,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_4')).grid(column=0,row=7,pady=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_5,dark_image=self.Girls_Profile_Icon_5,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_5')).grid(column=1,row=7,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_6,dark_image=self.Girls_Profile_Icon_6,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_6')).grid(column=2,row=7)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_7,dark_image=self.Girls_Profile_Icon_7,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_7')).grid(column=3,row=7,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_8,dark_image=self.Girls_Profile_Icon_8,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_8')).grid(column=0,row=8)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_9,dark_image=self.Girls_Profile_Icon_9,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_9')).grid(column=1,row=8,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_10,dark_image=self.Girls_Profile_Icon_10,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_10')).grid(column=2,row=8)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_11,dark_image=self.Girls_Profile_Icon_11,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_11')).grid(column=3,row=8,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_12,dark_image=self.Girls_Profile_Icon_12,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_12')).grid(column=0,row=9,pady=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_13,dark_image=self.Girls_Profile_Icon_13,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_13')).grid(column=1,row=9,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_14,dark_image=self.Girls_Profile_Icon_14,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_14')).grid(column=2,row=9)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_15,dark_image=self.Girls_Profile_Icon_15,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_15')).grid(column=3,row=9,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_16,dark_image=self.Girls_Profile_Icon_16,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_16')).grid(column=0,row=10)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_17,dark_image=self.Girls_Profile_Icon_17,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_17')).grid(column=1,row=10,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_18,dark_image=self.Girls_Profile_Icon_18,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_18')).grid(column=2,row=10)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Girls_Profile_Icon_19,dark_image=self.Girls_Profile_Icon_19,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Girls_Profile_Icon_19')).grid(column=3,row=10,padx=5)

            #Kids Profile Icons
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Kids_Profile_Icon_0,dark_image=self.Kids_Profile_Icon_0,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Kids_Profile_Icon_0')).grid(column=0,row=11,pady=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Kids_Profile_Icon_1,dark_image=self.Kids_Profile_Icon_1,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Kids_Profile_Icon_1')).grid(column=1,row=11,padx=5)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Kids_Profile_Icon_2,dark_image=self.Kids_Profile_Icon_2,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Kids_Profile_Icon_2')).grid(column=2,row=11)
            CTk.CTkButton(ProfileIconFrame,text='',fg_color='transparent',hover_color='Grey',image=CTk.CTkImage(light_image=self.Kids_Profile_Icon_3,dark_image=self.Kids_Profile_Icon_3,size=(46,46)),height=0,width=0,command=lambda:readProfileIcon('self.Kids_Profile_Icon_3')).grid(column=3,row=11,padx=5)



        #Hides/Shows The Date 
        def HideDate():
            
            #Change The Value Of The Data Base - json
            self.UserData['Hide Date'] = HideDateSwitch.get()

            #True - Hide Date
            if self.UserData.get('Hide Date'):
                Date_Label.place_forget()

            #False - Show Date
            elif not self.UserData.get('Hide Date'):
                Date_Label.place(x=1070,y=2)





            


        def com():
            op = Appearance_Mode_Switch.get()
            self.Value = op
            print(self.Value)
            
            if not op:
                print('Light Mode')
                # CTk.set_appearance_mode('light')
            elif op:
                print('Dark Mode')
                # CTk.set_appearance_mode('dark')
                # Window.set

            

        #Original Frame
        Settings_Frame = CTk.CTkFrame(Frame,width=1160,height=560)
        Settings_Frame.place(x=0,y=0)
        CTk.CTkButton(Settings_Frame,text='❌',fg_color='transparent',height=0,width=0,hover_color='Red',font=('Roboto',16),
                      command=Settings_Frame.place_forget).place(x=1128,y=4)


        #Appearance Mode Frame
        Appearance_Mode = CTk.CTkFrame(Settings_Frame,width=134,height=50);Appearance_Mode.place(x=10,y=500)
        _Mode = CTk.BooleanVar(Appearance_Mode,True if self.UserData.get('Appearance Mode') == 'dark' else False)
        CTk.CTkLabel(Appearance_Mode,text='',image=CTk.CTkImage(light_image=lightModeIcon,dark_image=lightModeIcon,size=(40,40))).place(x=5,y=5)
        CTk.CTkLabel(Appearance_Mode,text='',image=CTk.CTkImage(light_image=darkModeIcon,dark_image=darkModeIcon,size=(40,40))).place(x=89,y=5)
        Appearance_Mode_Switch = CTk.CTkSwitch(Appearance_Mode,text='',width=0,height=0,switch_height=16,switch_width=34,progress_color='transparent',
                                               variable=_Mode,onvalue=True,offvalue=False,command=com);Appearance_Mode_Switch.place(x=50,y=17)


        #Hide Date Frame
        Hide_Date = CTk.CTkFrame(Settings_Frame,width=210,height=50);Hide_Date.place(x=10,y=10)
        _Date = CTk.BooleanVar(Hide_Date,bool(self.UserData.get('Hide Date')))

        CTk.CTkLabel(Hide_Date,text='   Hide Date',font=('Freestyle Script',26,'bold'),image=CTk.CTkImage(light_image=dateIcon,dark_image=dateIcon,size=(40,40)),compound='left').place(x=5,y=5)
        HideDateSwitch = CTk.CTkSwitch(Hide_Date,text='',width=0,height=0,switch_height=16,switch_width=34,command=HideDate,variable=_Date);HideDateSwitch.place(x=159,y=17)


        #Change Profile Icon Frame 
        profileIcon = CTk.CTkFrame(Settings_Frame,width=255,height=50);profileIcon.place(x=895,y=500)
        CTk.CTkLabel(profileIcon,text='Current Profile Picture :',height=40,font=('Freestyle Script',26,'bold')).place(x=5,y=5)
        currentProfileIcon = CTk.CTkButton(profileIcon,text='',height=0,width=0,hover_color='Grey',fg_color='transparent',
                      image=CTk.CTkImage(light_image=eval(self.ProfileIcon),dark_image=eval(self.ProfileIcon),size=(35,35)),compound='right',
                      command=changeProfilePicture);currentProfileIcon.place(x=208,y=4)
        

        
        greetColor = CTk.CTkFrame(Settings_Frame,width=255,height=50);greetColor.place(x=895,y=188)
        CTk.CTkLabel(greetColor,text='change greet color').place(x=0,y=0)
        currentGreetColor = CTk.CTkButton(greetColor,text='',hover=False,fg_color='#378F9C',height=40,width=40).place(x=209,y=5)




        Security_2FA = CTk.CTkFrame(Settings_Frame,width=310,height=50);Security_2FA.place(x=154,y=500)
        CTk.CTkLabel(Security_2FA,text='  Two Factor Authentication',height=0,width=0,font=('Roboto',14,'bold'),image=CTk.CTkImage(light_image=AuthenticationIcon,dark_image=AuthenticationIcon,size=(40,40)),compound='left').place(x=5,y=5)
        CTk.CTkSwitch(Security_2FA,text='',width=0,height=0,switch_height=16,switch_width=34,progress_color='Green',fg_color='Red').place(x=259,y=17)


        notfy = CTk.CTkScrollableFrame(Settings_Frame,width=300,height=190,label_text='     Notification Type                        Email         Push',label_anchor='w');notfy.place(x=10,y=238)
        # CTk.CTkLabel(notfy,text='notification email push').pack()

        Sec = CTk.CTkFrame(notfy,width=300,height=50,border_width=1);Sec.pack(padx = 10,pady = 10)
        CTk.CTkLabel(Sec,text='aldfgjfgjla').place(x=10,y=10)
        CTk.CTkSwitch(Sec,text='',width=0,height=0,switch_height=16,switch_width=34).place(x=238,y=17)

        Sec1 = CTk.CTkFrame(notfy,width=300,height=50,border_width=1);Sec1.pack(padx = 10)
        CTk.CTkSwitch(Sec1,text='',width=0,height=0,switch_height=16,switch_width=34).place(x=238,y=17)


        Sec2 = CTk.CTkFrame(notfy,width=300,height=50,border_width=1);Sec2.pack(padx = 10,pady = 10)
        CTk.CTkSwitch(Sec2,text='',width=0,height=0,switch_height=16,switch_width=34).place(x=238,y=17)


        Sec3 = CTk.CTkFrame(notfy,width=300,height=50,border_width=1);Sec3.pack(padx = 10)
        CTk.CTkSwitch(Sec3,text='',width=0,height=0,switch_height=16,switch_width=34).place(x=238,y=17)


        Sec4 = CTk.CTkFrame(notfy,width=300,height=50,border_width=1);Sec4.pack(padx = 10,pady = 10)
        CTk.CTkSwitch(Sec4,text='',width=0,height=0,switch_height=16,switch_width=34).place(x=238,y=17)


        Sec5 = CTk.CTkFrame(notfy,width=300,height=50,border_width=1);Sec5.pack(padx = 10)
        CTk.CTkSwitch(Sec5,text='',width=0,height=0,switch_height=16,switch_width=34).place(x=238,y=17)


        Sec6 = CTk.CTkFrame(notfy,width=300,height=50,border_width=1);Sec6.pack(padx = 10,pady = 10)
        CTk.CTkSwitch(Sec6,text='',width=0,height=0,switch_height=16,switch_width=34).place(x=238,y=17)


        contactus = CTk.CTkFrame(Settings_Frame,width=411,height=50);contactus.place(x=474,y=500)
        CTk.CTkLabel(contactus,text='Contact us  Mail  Feedback  issue  suggestion ').place(x=10,y=10)


        Danger_Zone = CTk.CTkFrame(Settings_Frame,width=200,height=50);Danger_Zone.place(x=685,y=440)
        # CTk.CTkLabel(Danger_Zone,text='danger Zone : del acc , wipe all the data and money(donetes to Bank),etc').place(x=10,y=10)
        Dan = CTk.CTkButton(Danger_Zone,text='Danger Zone   >',font=('Roboto',16,'bold'),hover_color='Grey',image=CTk.CTkImage(light_image=Danger_Zone_Icon,dark_image=Danger_Zone_Icon,size=(40,40)),
                            height=46,width=196,fg_color='transparent',compound='left',text_color='Black' if self.UserData.get('Appearance Mode') == 'light' else 'White').place(x=2,y=2)
        # CTk.CTkButton(Danger_Zone,text='›',font=('Roboto',35),height=0,width=15,fg_color='transparent').place(x=180,y=1)












        #Copyright Note 
        CTk.CTkLabel(Settings_Frame,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',font=('Calibri',8),height=0).place(x=1004,y=550)




    def User_Interface(self):

        #Creation Of Window And Settings Also Showing The Date
        global Window,Frame,User_Info,Date_Label
        Window = CTk.CTk()
        Window.title('User Interface')
        Window.resizable(False,False)
        Window.geometry('1200x600')
        Window.protocol('WM_DELETE_WINDOW',lambda: None)
        CTk.set_appearance_mode(str(self.UserData.get('Appearance Mode')))

        if not self.UserData.get('Hide Date'):
            Date_Label = CTk.CTkLabel(Window,text=Date_Day,text_color='Orange',height=10);Date_Label.place(x=1070,y=2)
        # CTk.CTkLabel(Window,text=f'Security Code: {self.Security_Code}',text_color='Orange',height=10).place(x=20,y=2)
        
        
        #Main Frame Contained In The Window
        Frame = CTk.CTkFrame(Window)
        Frame.configure(width=1160,height=560)
        Frame.place(x=20,y=20)
        
        #User Greetings And Logout
        CTk.CTkLabel(Frame,text=f'{Greetings}, {self.UserData.get('User Name')}',font=('Freestyle Script',40,'bold'),text_color='#378F9C').place(x=10,y=2)
        # CTk.CTkButton(Frame,text='Logout',font=('Freestyle Script',30),fg_color='transparent',hover=False,width=40,height=14,text_color='Red',command=Window.destroy).place(x=1100,y=1)
        CTk.CTkLabel(Frame,text='-'*1160,text_color='Grey',font=('Roboto',2),height=0).place(x=0,y=48)

        #Balance Frame That Shows The User Bank Balance Which is Contained in The Main Frame
        Balance_Frame = CTk.CTkFrame(Frame,fg_color='#9E1076')
        Balance_Frame.configure(width=200,height=50)
        Balance_Frame.place(x=10,y=60)
        CTk.CTkLabel(Balance_Frame,text='Your Bank Balance:',font=('Roboto',16),height=14).place(x=5,y=3)
        Balance = CTk.CTkLabel(Balance_Frame,text=f'${self.UserData.get('Balance'):.2f}',text_color='Lime').place(x=5,y=20)
        User_Info = CTk.CTkButton(Frame,text='',image=CTk.CTkImage(light_image=eval(self.ProfileIcon),dark_image=eval(self.ProfileIcon),size=(40,40)),
                                  height=0,width=0,fg_color='transparent',hover=False,command=self.Settings);User_Info.place(x=1112,y=0)


        

        CTk.CTkButton(Frame,text='Deposit',command=self.Deposit).place(x=1010,y=484)
        CTk.CTkButton(Frame,text='Withdraw',command=self.Withdraw).place(x=1010,y=522)








        


        


        

        Window.mainloop()

# User_Requirements(UserData={'Hide Date':False,'Appearance Mode':'dark','Balance':62472572,'User Name':'Virati Akira Nandhan Reddy'}).User_Interface()



