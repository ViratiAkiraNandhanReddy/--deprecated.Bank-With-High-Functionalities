#Importing Required Modules/Packages
from Bank_Package import *
from Bank_Package.Product_Activation import Software_Activation
from Bank_Package.Login import Login

if Initialization_Data.get('isActivated'):
    Activated = True 
else:
    Activated = False
    

Product_Activated = False

#Heart Of The Program
def Start_Program():
    if Activated:
        if License_Check:
            Login().Display_Login()
            print('prg started')
        else:
            Corrupted()

    else:
        if License_Check:
            global Product_Activated
            Product_Activated = Software_Activation().Activate()
        else:
            Corrupted()
Start_Program()

if Product_Activated:
    # Exit(Path,Product_Activated,User_Data)
    Activated = True
    Start_Program()
