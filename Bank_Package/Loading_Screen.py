import tkinter as tk
from time import sleep 


def Buffer_At_Activation(func):
    
    def Loading():
        
        func()
        
        
    '''This Function Will Be Called When The Software is Activated'''
    
    return Loading

def Loging_Out(func):
    def logout():
        func()
    return logout

def fun():
    pass


