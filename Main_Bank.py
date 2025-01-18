from Bank_Package import *


#Heart Of The Program
def Start_Program():
    if Activated == True:
        if License_Check == True:
            # reload(Main_Starter)
            # Main_Starter.Start_Main()
            print('prg started')
        else:
            Corrupted()

    else:
        if License_Check == True:
            # reload(Activation)
            # Software_Activation.Activate()
            print('prg act')
        else:
            Corrupted()
Start_Program()
