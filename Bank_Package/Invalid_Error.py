from tkinter import messagebox

def Blank_Error():
    '''Error Message Screen For Blank Input'''
    messagebox.showerror(title='Blank Error',message='Input Can\'t Be Blank!')
    
def Exist_Error():
    '''Info Message For User Already Exist'''
    messagebox.showinfo(title='Exist Error',message='User Already Exists')

def Pass_Error():
    '''Error Message For Wrong Password'''
    messagebox.showerror(title='Wrong Password',message='Wrong Password Entered')

def User_Digit_Error():
    '''Error Message For Username Entry Was Only Digits'''
    messagebox.showerror(title='Username Digit Error',message='Username Can\'t Be Only Numbers')

def User_blank_Error():
    '''Error Message For Username Entry Was Only Blank'''
    messagebox.showerror(title='Username Blank Error',message='Username Can\'t Be Blank!')

def Pin_blank_Error():
    '''Error Message For Password Entry Was Only Blank'''
    messagebox.showerror(title='Password Blank Error',message='Password Can\'t Be Blank!')

def Pin_Char_Error():
    '''Error Message For Password Entry Was Against PinCode Rule (4-Digit Rule)'''
    messagebox.showerror(title='Against PinCode Rule',message='Must Contain 4 or More Characters')

def xyz():
    pass