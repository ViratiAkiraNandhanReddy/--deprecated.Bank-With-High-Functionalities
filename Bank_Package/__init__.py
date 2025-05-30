''' 
# Copyright (c) 2024 - 2026 Virati Akira Nandhan Reddy


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
 ```python
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
##### 3. I Wrote My First 1000 lines Program For a Module `Setup.py` \\[ 13-May-2025 @ 2:12 PM\\]
##### 4. I Wrote My First 2000 lines Program For a Module `Setup.py` \\[ 19-May-2025 @ 1:59 PM\\]
##### 5. I Wrote My First 3000 lines Program For a Module `Setup.py` \\[ 30-May-2025 @ 2:08 AM\\]




'''


import os
import json
import tkinter as tk
import customtkinter as CTk
from . import Repair_Product

__Version__ = '0.0.1 - Beta'
__Author__ = 'Virati Akira Nandhan Reddy'
__License__ = 'MIT License ( Restructured )'
__Python_Version__ = '3.13.0 (64-Bit)'
__Code_Editer__ = "Microsoft's Visual Studio Code"

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
        Detailed_Licence = File_check.read()

    if 'Virati Akira Nandhan Reddy' in Detailed_Licence and \
        'Akki@Google#Ai&Software_Engineer@Google//$10T|2030%Successful!"Owner"2008+^AKKI~Copyright.(c)<2026>Virati-Akira*Nandhan:Reddy'\
        in Detailed_Licence:
        License_Check = True
    else:
        License_Check = False
except FileNotFoundError:
    License_Check = False

try:

    with open(fr'{Path}\DATABASE\JSON\ADMINISTRATIVE FILES\Initialization.json','r') as load:
        Initialization_Data: dict = json.load(load)

except FileNotFoundError:

    pass

except json.JSONDecodeError:

    pass

try:

    with open(fr'{Path}\DATABASE\JSON\ADMINISTRATIVE FILES\json.database.connector.json','r') as Bridge:
        BridgeData: dict = json.load(Bridge)

except FileNotFoundError:

    pass

except json.JSONDecodeError:

    pass

def AccessUserData(Username: str) -> dict:

    try:
        
        with open(fr'{Path}\DATABASE\JSON\USERDATA\{Username}.json','r') as json_Data:
            User_Data = json.load(json_Data)

        #Returns The The Data To The Module
        return User_Data

    except FileNotFoundError:

        return {'FileNotFoundError': True , 'JSONDecodeError': False} 

    except json.JSONDecodeError:

        return {'JSONDecodeError': True , 'FileNotFoundError': False}   

#File is Locked
def Corrupted() -> None:
    '''This Function Will Show A Tab That File Is Locked And Some Basic Information'''

    #Setting Up The Tab
    Window = CTk.CTk()
    Window.title('Unauthorised Modification')
    Window.resizable(False, False)
    Window.geometry('400x400')

    #Information
    CTk.CTkLabel(Window, text = 'Unauthorised Modification Detected :(', font = ('Segoe UI', 16)).place(x = 10, y = 10)
    CTk.CTkLabel(Window, text = ' Summary',fg='Blue',font = ('Segoe UI', 12),bg='#FFBDBD').pack(anchor='nw',pady=7)
    CTk.CTkLabel(Window, text = 'If You Are Seeing This Page Then You Might Had \nModified The License File Or \
You Might Modified The \nRestricted Zone in License File',bg='#FFBDBD',font=('Roboto', 12)).pack()
    
    #What Next
    CTk.CTkLabel(Window, text = 'You Are Restricted To Use This Software!',fg='#8D00FF',bg='#FFBDBD',font = ('Segoe UI', 12)).pack(pady=18)
    CTk.CTkLabel(Window, text = 'What You Can Do Now?',bg='#FFBDBD',font = ('Segoe UI', 12),fg='#194A00').pack(anchor='nw',pady=15)
    CTk.CTkLabel(Window, text = '1.Contact The Owner Through GitHub/Mail\nOr',bg='#FFBDBD',font=('Roboto', 12)).pack(anchor='nw')
    CTk.CTkLabel(Window, text = '2.Reinstall The Software From GitHub',bg='#FFBDBD',font=('Roboto', 12)).pack(anchor='nw')
    
    #Copyright Note
    CTk.CTkLabel(Window, text = 'Copyright (c) 2026 Virati Akira Nandhan Reddy',fg='Black',bg='#FFBDBD',font=('Calibri', 8)).place(x=178,y=380)
    
    #Data Will Be Saved
    CTk.CTkLabel(Window, text = 'The User Data Will be Saved Safely!',fg='Green',bg='#FFBDBD',font=('Roboto', 17)).pack(pady=10)

    Window.mainloop() 


print('Hello From __init__')

#Satisfied Code Completion: 65%
'''                                                         End Of Program                                                                    '''
