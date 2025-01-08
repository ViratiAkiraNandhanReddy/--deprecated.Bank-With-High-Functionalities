import tkinter as tk
from time import sleep 


def Buffer_At_Activation(func):
    
    def Loading():
        '''Load = tk.Tk()
        Load.title('Loading')
        # Load.resizable(False,False)
      

        Photo = tk.PhotoImage(file=fr'{Path}\Visual Data\Loading.gif',format=f'gif -index {frame}')
        tk.Label(Load,image=Photo).pack(side='top')
        sleep(0.1)
        # tk.Label.config(Load,image=Photo)
        # tk.Label.image = Photo

        Load.after(delay,Loading(frame+1,delay))
        Load.after(5000,Load.destroy)
        Load.mainloop()'''
        
        func()
        
        
    '''This Function Will Be Called When The Software is Activated'''
    
    return Loading

def Loging_Out(func):
    def logout():
        func()
    return logout

def fun():
    pass


