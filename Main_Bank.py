from Bank_Package import *
# from Bank_Package.Start_Bank import Bank_Started
from Bank_Package.Product_Activation import Software_Activation
from Bank_Package.Save_Info import Exit
from Bank_Package.Login_Screen import Login
from Bank_Package.Create_Account import New_Account
from Bank_Package import Invalid_Error
from Bank_Package.User_Actions import User_Requirements

# from 


#Heart Of The Program
def Start_Program():
    if Activated == True:
        if License_Check == True:
            Login(Accounts,User_func,PinCodes,Security)
            print('prg started')
        else:
            Corrupted()

    else:
        if License_Check == True:
            global Product_Activated
            Product_Activated = Software_Activation.Activate()
        else:
            Corrupted()
Start_Program()

if Product_Activated == True:
    Exit(Path,Product_Activated,Accounts,PinCodes,Security)
    Activated = True
    Start_Program()
