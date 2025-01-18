import os
import Repair
import Main_Starter
import tkinter as tk
import Software_Activation
from importlib import reload

#Knowing The Path Of The Package
Check_Location=os.getcwd()

if 'Main_File' not in Check_Location:
    Path = Check_Location + "\\Main_File"
else:
    Path = Check_Location

try:
    File = Path.replace(r'\Main_File',r'\LICENSE')
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

try:
    with open(fr'{Path}\Data_Of_User.txt') as Data:
        Activated = eval(Data.readline())
        Accounts = eval(Data.readline())
        PinCodes = eval(Data.readline())
        Security = eval(Data.readline())
except:
    Repair.User_Data_Not_Found()


#Key Finder
def User_func(User=None):
    User_index = Accounts.index(User)
    return User_index

#just Pass
def Disable_Exit():
    '''When The Exit Button Pressed that Will Just Pass (Does Nothing)\n
    That is How I Disabled The Exit Button'''
    pass

def License():
    license = '''Copyright (c) 2026 Virati Akira Nandhan Reddy
    
Owner: Virati Akira Nandhan Reddy
Programer: Virati Akira Nandhan Reddy
Python Built Version: 3.13.0 (64-Bit)
Code Editer Used: Microsoft's Visual Studio Code
 '''
    Choice = input('Detailed Or Shortend-(D/S):')
    if Choice == "D":
        print(Detailed_Licence)
    else:
        print('\nInvalid Input! Opening Shortend Licence')
    return license

def Documentation():
    pass

#File is Locked
def Corrupted():
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
    tk.Label(War,text='If You Are Seeing This Page That You Might Had \nModified The License File Or \
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

#Heart Of The Program
def Start_Program():
    if Activated == True:
        if License_Check == True:
            reload(Main_Starter)
            Main_Starter.Start_Main()
        else:
            Corrupted()

    else:
        if License_Check == True:
            reload(Software_Activation)
            Software_Activation.Activation.Activate()
        else:
            Corrupted()

print('Hello From __init__')
print(Accounts)

print(PinCodes)
#License()
# Corrupted()

if __name__ == '__main__':
    Start_Program()