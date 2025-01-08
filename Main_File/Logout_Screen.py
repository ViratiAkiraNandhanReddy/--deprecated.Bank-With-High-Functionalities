from Loading_Screen import Buffer_At_Activation,Loging_Out
import __init__ as init

# Activated = True
Path =init.Path
@Buffer_At_Activation
def Activation_Save():
    global Activated,Act
    Activated = True
    Act = True
    print(Activated)
    Exit()

@Loging_Out
def Exit():

    try:
        Act_Sav = Act
    except NameError:
        Act_Sav = False

    try:
        print('Exiting from Logout_Screen')
        with open(fr'{init.Path}\Data_Of_User.txt','w') as Write_Data:
            Write_Data.write(f'{str(Activated if Act_Sav == True else init.Activated)}')
            Write_Data.write(f'\n{str(init.Accounts)}')
            Write_Data.write(f'\n{str(init.PinCodes)}')
            Write_Data.write(f'\n{str(init.Security)}')


    except Exception as e:
        print(e)


# Activation_Save()