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
    File = Path.removesuffix(r'\Main_File') + r'\LICENSE' 
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
        Activated:bool = eval(Data.readline())
        Accounts:list[str] = eval(Data.readline())
        PinCodes:list[str] = eval(Data.readline())
        Security:list[str] = eval(Data.readline())
except:
    Repair.User_Data_Not_Found()

def User_func(User=None)->int:
    User_index = Accounts.index(User)
    return User_index

def Disable_Exit():
    '''When The Exit Button Pressed that Will Just Pass (Does Nothing)\n
    That is How I Disabled The Exit Button'''
    pass

def License()->str:
    license = '''Copyright (c) 2026 Virati Akira Nandhan Reddy
    
Owner: Virati Akira Nandhan Reddy
Programer: Virati Akira Nandhan Reddy
Python Built Version: 3.13.0 (64-Bit)
Code Editer Used: Microsoft's Visual Studio Code
 '''
    Choice = input('Detailed Or Shortend-(D/S):')
    match Choice:
        case 'D'|'d':
            print(Detailed_Licence)
            pass
        case 'S'|'s':
            pass
            
        case _:
            print('\nInvalid Input! Opening Shortend Licence')
    return license

def Documentation()->str:
    pass

def Corrupted():
    War = tk.Tk()
    War.title('Locked')
    War.resizable(False,False)
    War.geometry('350x400')
    tk.Label(text='File Locked By The Owner :(',font=('40'),fg='red').pack()

    War.mainloop() 

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
            Software_Activation.Activate()
        else:
            Corrupted()

print('Hello From __init__')
print(PinCodes)
#License()
# Corrupted()

if __name__ == '__main__':
    Start_Program()