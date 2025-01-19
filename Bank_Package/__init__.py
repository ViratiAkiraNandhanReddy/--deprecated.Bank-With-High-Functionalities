''' Copyright (c) 2026 Virati Akira Nandhan Reddy

            **Owner Details**
Owner/Author: Virati Akira Nandhan Reddy
GitHub: ViratiAkiraNandhanReddy
Instagram: Viratiaki53
Gmail: Viratiaki29@gmail.com
Nationality: Indian/American 

At Sarting Of This Project My Age Was 16 (Class 11)

            **Program Details**
Python Built Version: 3.13.0 (64-Bit)
Code Editor: Microsoft's Visual Studio Code
License: MIT License 

Sarted On: 13-Dec-2024 @ 6:21 PM

Ended On: 

            **Package Details**
Contains All The Programs And Other Data To Run The Main Program 
E.g:Login_Screen,Data_Of_User And Many More

This Is A Required Package To Run The Bank-With-High-Functionalities

            **Achievements**
My First Package Based Biggest Project


'''


#Importing The Required Modules/Packages
import os
import tkinter as tk
from time import sleep

#Knowing The Path Of The Package
Check_Location=os.getcwd()

#Creating A Global Path
if 'Bank_Package' not in Check_Location:
    Path = Check_Location + "\\Bank_Package"
else:
    Path = Check_Location

#Security Check
try:
    File = Path.removesuffix(r'\Bank_Package') + r'\LICENSE' 
    with open(File) as File_check:
        Licence_Data_Check = File_check.read()

    #To View The License
    Detailed_Licence = Licence_Data_Check

    if 'Virati Akira Nandhan Reddy' in Licence_Data_Check and \
        'Akki@Google#Ai&Software_Engineer@Google//$10T|2030%Successful!"Owner"2008+^AKKI~Copyright.(c)<2026>Virati-Akira*Nandhan:Reddy'\
        in Licence_Data_Check:
        License_Check = True
    else:
        License_Check = False
except FileNotFoundError:
    License_Check = False

#Grabing Data From Data_Of_User.txt File
try:
    with open(fr'{Path}\Data_Of_User.txt') as Data:
        Activated:bool = eval(Data.readline())
        Accounts:list[str] = eval(Data.readline())
        PinCodes:list[str] = eval(Data.readline())
        Security:list[str] = eval(Data.readline())

    Repair = 'Not Required'
except:
    Repair = 'Required'
    print('Error While Reading Data')

#Key Finder
def User_func(User=None)->int:
    User_index = Accounts.index(User)
    return User_index

#To View The Licence(Summarised/Detailed)
def License()->None:
    #Summarised Version of License
    license = '''Copyright (c) 2026 Virati Akira Nandhan Reddy
    
Programmer/Owner: Virati Akira Nandhan Reddy
Python Built Version: 3.13.0 (64-Bit)
Code Editer Used: Microsoft's Visual Studio Code
License: MIT License

 '''
    
    Choice = input('Detailed Or Summarised - (D/S):')
    match Choice:
        case 'D'|'d':
            print(Detailed_Licence)

        case 'S'|'s':
            print(license)
            
        case _:
            print('\nInvalid Input! Opening Summarised Licence')
            print('\nLoading...\n')
            sleep(8)
            print(license)
    
#Documentation Of The SoftWare
def Documentation()->str:
    pass

#File is Locked
def Corrupted()->None:
    '''This Function Will Show A Tab That File Is Locked And Some Basic Information'''

    #Setting Up The Tab
    War = tk.Tk()
    War.title('Software Locked')
    War.resizable(False,False)
    War.geometry('400x400')
    War.config(bg='#FFBDBD')

    #Information
    tk.Label(War,text='File Locked By The Owner :(',font=('Roboto 22'),fg='red',bg='#FFBDBD').pack()
    tk.Label(War,text=' Summary',fg='Blue',font=('Roboto 14'),bg='#FFBDBD').pack(anchor='nw',pady=7)
    tk.Label(War,text='If You Are Seeing This Page Then You Might Had \nModified The License File Or \
You Might Modified The \nRestricted Zone in License File',bg='#FFBDBD',font=('Roboto 12')).pack()
    
    #What Next
    tk.Label(War,text='You Are Restricted To Use This Software!',fg='#8D00FF',bg='#FFBDBD',font=('Roboto 14')).pack(pady=18)
    tk.Label(War,text='What You Can Do Now?',bg='#FFBDBD',font=('Roboto 14'),fg='#194A00').pack(anchor='nw',pady=15)
    tk.Label(War,text='1.Contact The Owner Through GitHub/Mail\nOr',bg='#FFBDBD',font=('Roboto 12')).pack(anchor='nw')
    tk.Label(War,text='2.Reinstall The Software From GitHub',bg='#FFBDBD',font=('Roboto 12')).pack(anchor='nw')
    
    #Copyright Note
    tk.Label(War,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',fg='Black',bg='#FFBDBD',font=('Calibri 8')).place(x=178,y=380)
    
    #Data Will Be Saved
    tk.Label(War,text='The User Data Will be Saved Safely!',fg='Green',bg='#FFBDBD',font=('Roboto 17')).pack(pady=10)

    War.mainloop() 



print('Hello From __init__')
print(PinCodes)
# License()
# Corrupted()

#Satisfied Code Completion: 65%
'''                                                         End Of Program                                                                    '''
