''' 
# Copyright (c) 2026 Virati Akira Nandhan Reddy


<!-- Owner Details -->


---
## <ins>*Owner Details*</ins>
#### Owner/Author: *Virati Akira Nandhan Reddy*
#### GitHub: [ViratiAkiraNandhanReddy](https://github.com/ViratiAkiraNandhanReddy)
#### Gmail: Viratiaki29@gmail.com 
#### LinkedIn: [virati-akira-nandhan-reddy](https://linkedin.com/in/virati-akira-nandhan-reddy/)
#### X(Twitter): [Viratiaki53](https://x.com/Viratiaki53)
#### Instagram: [Viratiaki53](https://instagram.com/viratiaki53/)
Nationality: Indian/American 

##### <ins>***At Sarting Of This Project My Age Was 16 (Class 11)***</ins>


<!-- Program Details -->


---
## <ins>*Program Details*</ins>
##### Python Built Version: 3.13.0 (64-Bit)
##### Code Editor: Microsoft's Visual Studio Code
##### License: MIT License (Open Source With Some Restrictions)


*Sarted On:* <ins>**13-Dec-2024 @ 6:21 PM**</ins>

*Ended On:* 


<!-- Syntax -->


---
## <ins>*Syntax*</ins>
 ```
 import Bank_Package
 or 
 from Bank_Package import <Required Modules>
 ```


<!-- Package Details -->


---
## <ins>*Package Details*</ins>
Contains All The Programs And Other Data To Run The Main Program 
E.g:Login_Screen,Data_Of_User And Many More

This Is A Required Package To Run The Bank-With-High-Functionalities


<!-- Purpose -->


---
## <ins>*Purpose*</ins>
The Purpose Of This Package Is To Provide A High Functional Bank Program To The Users With The Help Of Python


<!-- Modules -->


---
## <ins>*Modules*</ins>
#### 1. Login_Screen
#### 2. Create_Account
#### 3. Product_Activation


<!-- Dependencies -->


---
## <ins>*Dependencies*</ins>
### 1. `customtkinter`
### 2. `time`
### 3. `os`
### 4. `PIL`
### 5. `json`
### 6. `tkinter`



<!-- Note -->


---
## <ins>*Note*</ins>
### This Package is Used For The Main Program To Run
### This Package <ins>*Can't Be Used To Create A New Program*</ins> i.e, It Can't Be Used As A Library



<!-- Achievements -->


---
## <ins>*Achievements*</ins>
##### 1. My First Package Based Biggest Project
##### 2. I Learnt How To Send Gmail To The People From The Python





'''


#Importing The Required Modules/Packages
import os
import tkinter as tk
from time import sleep
from . import Repair_Product
import customtkinter as CTk
import PIL
import json

__Version__ = '0.0.1 - Beta'
__Author__ = 'Virati Akira Nandhan Reddy'
__License__ = 'MIT License ( Restructured )'
__Python_Version__ = '3.13.0 (64-Bit)'
__Code_Editer__ = 'Microsoft\'s Visual Studio Code'

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
'''try:
    with open(fr'{Path}Data_Of_User.txt') as Data:
        Is_Product_Activated:bool = eval(Data.readline())

        #User Details
        Available_Accounts:list[str] = eval(Data.readline())
        User_PinCodes:list[str] = eval(Data.readline())
        User_Security_Codes:list[str] = eval(Data.readline())
        User_Balance:list[str] = eval(Data.readline())

        #Details Of Loan Lenders
        Loan_Available_For_User:list[float|int] = eval(Data.readline())
        Loan_Taken_Per_User:list[float|int] = eval(Data.readline())
        Loan_Interest_Amount_Per_User:list[float|int] = eval(Data.readline())
        Rate_Of_Interest_Per_User:list[float] = eval(Data.readline())
except:
    Repair_Product.User_Data_Lost()
    print('Error While Reading User Data')'''

try:

    with open(fr'{Path}\Bank Initialization.json','r') as load:
        Initialization_Data: dict = json.load(load)

except FileNotFoundError:

    pass

except json.JSONDecodeError:

    pass

try:

    with open(fr'{Path}\User Data Bridge.json','r') as Bridge:
        BridgeData: dict = json.load(Bridge)

except FileNotFoundError:

    pass

except json.JSONDecodeError:

    pass

def AccessUserData(Username: str) -> dict:

    try:
        
        with open(fr'{Path}\User Data\{Username}.json','r') as json_Data:
            User_Data = json.load(json_Data)

        #Returns The The Data To The Module
        return User_Data

    except FileNotFoundError:

        return {'FileNotFoundError': True , 'JSONDecodeError': False} 

    except json.JSONDecodeError:

        return {'JSONDecodeError': True , 'FileNotFoundError': False}
    

'''#Key Finder
def User_func(User=None)->int:
    ''This Function Returns The Index Value Of The Account ; if The Account is Not Present Then Gives The Error''
    User_index = Available_Accounts.index(User)
    return User_index'''


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
# print(User_PinCodes)
# License()
# Corrupted()

#Satisfied Code Completion: 65%
'''                                                         End Of Program                                                                    '''
