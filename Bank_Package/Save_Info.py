# from Loading_Screen import Buffer_At_Activation,Loging_Out


# Activated = True
# @Buffer_At_Activation
def Activation_Save():
    global Activated,Act
    Activated = True
    Act = True
    print(Activated)
    Exit()

# @Loging_Out
def Exit(
    Path,Activated,Accounts,PinCodes,Security
    
    
    
    ):

    

    try:
        print('Exiting from Logout_Screen')
        with open(fr'{Path}\Data_Of_User.txt','w') as Write_Data:
            Write_Data.write(f'{str(Activated)}')
            Write_Data.write(f'\n{str(Accounts)}')
            Write_Data.write(f'\n{str(PinCodes)}')
            Write_Data.write(f'\n{str(Security)}')


    except Exception as e:
        print(e)


# Activation_Save()

