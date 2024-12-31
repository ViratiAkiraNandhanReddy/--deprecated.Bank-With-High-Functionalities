import tkinter as tk

Product_keys = [

    '2030-GITH-UBGC-AKKI-DIST-FIRS-TPRJ-INDI-AUSA-2026',
    '2030-AKKI-FIRS-TPRJ-HAPP-YGIT-DIST-USAI-NDIA-2026',
    '2030-DEV0-FIRS-TPRJ-INDI-AUSA-AKKI-AT18-0022-2026',
    '2030-GITH-UBAT-AKKI-USAI-NDIA-FIRS-TPRJ-2008-2026',
    '2030-AKKI-ATUS-AGOO-GLEA-ISSE-100M-USAI-NDIA-2026',
    '2030-USAI-NDIA-GOOG-LEAI-WITH-AKKI-WITH-$10T-2026',
    '2030-ALLR-IGHT-SREC-IVED-WITH-AKKI-INDI-AUSA-2026',
    '2030-USAI-NDIA-2008-VSCO-DEPY-THON-AIAT-AKKI-2026',
    'USAI-NDIA-VIRA-TIAK-IRAN-ANDH-ANRE-DDY1-2008-2030',
    'LAST-PROD-UCTK-EYAT-AKKI-PROG-RAM1-USAI-NDIA-2030'

]

Terms_Conditions = '''

jlsyfjydysFDyFDkySTduyas


'''
def Activate ():

    #New Window For Product Key
    def Product_Key()->None:

        #Getting The Key
        def Key():
            if Entery_Key.get() in Product_keys:
                Window_Activate.destroy()
                pass
            else:
                Invalid = tk.Label(Window_Activate,text='Invalid Product Key',fg='Yellow',bg='#4F55A8').place(x=200,y=200)
        
        #Removeing Text in Example
        def Temp(Key=None)->None:
            Entery_Key.delete(0,'end')
            Entery_Key.config(fg='White')
        
        #Initial Setup Of Window
        Window.destroy()
        Window_Activate = tk.Tk()
        Window_Activate.title('Product Key')
        Window_Activate.geometry('640x320')
        Window_Activate.resizable(False,False)
        Window_Activate.configure(background='#4F55A8')
        
        #Instructions For The User
        tk.Label(Window_Activate,text='Enter a Product Key',bg='#4F55A8',fg='White',font=('Calibri 22'),justify='left',height=2).place(x=10,y=0)
        tk.Label(Window_Activate,text='The Product Keys For This Software Will Be Provided By The Owner, Also Provided In The \nWebsite That You Downloaded From (GitHub)',bg='#4F55A8',font=('Calibri 13')).place(x=10,y=80)
        tk.Label(Window_Activate,text='Product Key',bg='#4F55A8',font=('Calibri 14'),fg='White').place(x=10,y=140)
        
        #Product Key Entry
        Entery_Key = tk.Entry(Window_Activate,font=('Consolas',12),border=2,bg='#2F3263',relief='ridge',highlightbackground='White')
        Entery_Key.insert(0,string='XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX')
        Entery_Key.config(fg='#82829C')
        Entery_Key.place(x=10,y=168,relwidth=0.75,relheight=0.09)
        Entery_Key.bind('<FocusIn>',Temp)
        
        #Spepping Up
        tk.Button(Window_Activate,text='Authenticate',fg='White',command=Key,bg='#1E2040',activebackground='grey').place(x=485,y=250)
        tk.Button(Window_Activate,text='Cancel',fg='White',command=Window_Activate.destroy,bg='#1E2040',activebackground='grey').place(x=580,y=250)
        
        #Copyright Note 
        tk.Label(Window_Activate,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',fg='White',bg='#4F55A8',font=('Calibri 8')).place(x=418,y=300)
        Window_Activate.mainloop()
    
    def Accepted():
        if OK.get() == True:
            Next.config(state='normal')
        elif OK.get() == False:
            Next.config(state='disabled')



    print("hello I'M software Activation")
    Window = tk.Tk()
    Window.title('Activation Window')
    Window.geometry('750x500')
    Window.config(background='Light Blue')
    Window.resizable(False,False)
    OK = tk.BooleanVar()



    
    Terms = tk.Frame(Window,background='White',height=380,width=700)
    Terms.place(x=25,y=25)
    tk.Label(Terms,text=Terms_Conditions,bg='White').place(x=10,y=20)
    



    Check = tk.Checkbutton(Window,text='Accept All Terms And Conditions',underline=0,variable=OK,onvalue=True,\
                           offvalue=False,command=Accepted,bg='Light Blue',activebackground='Light Blue').place(x=25,y=410)
    Next = tk.Button(Window,text='Next',state='disabled',command=Product_Key,font=(10),activebackground='#316E7A',bg='#68ABC9',relief='ridge')
    tk.Button(Window,text='Cancel',fg='Red',command=Window.destroy,font=(10),activebackground='#316E7A',bg='#68ABC9',relief='ridge').place(x=662,y=435)
    Next.place(x=580,y=435,width=60)

    #Copyright Note 
    tk.Label(Window,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',\
             fg='Black',bg='Light Blue',font=('Calibri 8')).place(x=528,y=480)
    



    Window.mainloop()
    


    
        
    
    