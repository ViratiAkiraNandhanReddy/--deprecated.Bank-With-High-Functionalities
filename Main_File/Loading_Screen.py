
def Buffer_At_Activation(func):
    def Loading():
        print('Loading')
        func()
        pass
    '''This Function Will Be Called When The Software is Activated'''
    return Loading

def Loging_Out(func):
    def logout():
        func()
    return logout

    
