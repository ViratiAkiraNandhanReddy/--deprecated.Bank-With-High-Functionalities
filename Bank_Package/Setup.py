import json
import socket
import subprocess, platform
import datetime, time
from PIL import Image
import customtkinter as CTk
from tkinter import messagebox

SETUPDATA = {

    "isActivated": False,
    "Manager Name": None,
    "Manager Password": None,
    "Manager Security Code": None,
    "Downloaded On": None,
    "Path Of User Data": None,
    "Back Up Of User Data Path": None,
    "License Check": None,
    "Recently Used On": None,
    "Data Base Type": None

}

PRODUCTKEYS = [ # 10 Product Keys 

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

APPPASSWORDWEBSITE = 'https://myaccount.google.com/apppasswords'
GITHUBREPOWEBSITE = 'https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities'

ERRORLOGS = open(r'D:\GitHub\Bank-With-High-Functionalities\Log Files\ErrorLogs.txt','a') 

WelcomeImage = Image.open(r'Bank_Package\Visual Data\WelcomeImageAtSetup.jpg')

with open(r'D:\GitHub\Bank-With-High-Functionalities\TERMS OF SERVICE.txt') as FILE:

    TERMSANDCONDITIONS: str = FILE.read()

# To Open The Browser
def OpenBrowserForSpecifiedUrl(url: str) -> None: # Works For Windows, Mac, Linux

    '''
    ## Purpose
    The `OpenBrowserForSpecifiedUrl` function is designed to open a specified URL in the default web browser. It supports Windows, Mac, and Linux operating systems.

    ## Parameters
    - `url` (str): The URL to be opened in the browser.

    ## Return Type
    - `None`: This function does not return any value.

    ## Exception Handling
    The function includes exception handling to log errors and provide a fallback message if the URL cannot be opened. Errors are logged in the `ErrorLogs.txt` file.

    ## Example Usage
    ```python
    # Example usage of OpenBrowserForSpecifiedUrl
    OpenBrowserForSpecifiedUrl("https://www.example.com")
    ```

    ## Notes
    - Ensure that the system has a default browser configured.
    - The function uses platform-specific commands to open the browser.
    - The `subprocess.run` method is used to execute the command in the shell.
    '''
    
    try:

        if platform.system() == 'Windows':
            subprocess.run(f"Start {url}", shell = True)

        elif platform.system() == 'Mac':
            subprocess.run(f"open {url}", shell = True)

        elif platform.system() == 'Linux':
            subprocess.run(f"xdg-open {url}", shell = True)

    except Exception as e: # Logging and fallback

        ERRORLOGS.write(f'\n[ERROR]: [Setup.py][{datetime.datetime.now().strftime('%d/%b/%Y @ %I:%M:%S %p')}] - Failed To Open {url} ; ErrorType: [ {e} ]')
    
    
class SetUp:

    def __init__(self) -> None:
        pass


    def SetupWindows(self) -> None:

        def GoTo_TermsAndConditionsFrame() -> None: # WelcomeFrame -> TermsAndConditionsFrame -- 1
            WelcomeFrame.place_forget()
            Window.geometry('800x600')
            TermsAndConditionsFrame.place(x = 5, y = 5)

        def GoBackTo_WelcomeFrame() -> None: # WelcomeFrame <- TermsAndConditionsFrame -- 2
            TermsAndConditionsFrame.place_forget()
            Window.geometry('800x400')
            WelcomeFrame.place(x = 5, y = 5)

        def GoTo_SoftwareActivationFrame() -> None: # TermsAndConditionsFrame -> SoftwareActivationFrame -- 3
            TermsAndConditionsFrame.place_forget()
            Window.geometry('800x400')
            SoftwareActivationFrame.place(x = 5, y = 5)

        def GoBackTo_TermsAndConditionsFrame() -> None: # TermsAndConditionsFrame <- SoftwareActivationFrame -- 4
            SoftwareActivationFrame.place_forget()
            Window.geometry('800x600')
            TermsAndConditionsFrame.place(x = 5, y = 5)

        def GoTo_ManagerModeSetupFrame() -> None: # SoftwareActivationFrame -> ManagerModeSetupFrame -- 5
            SoftwareActivationFrame.place_forget()
            ManagerModeSetupFrame.place(x = 5, y = 5)

        def GoBackTo_SoftwareActivationFrame() -> None: # SoftwareActivationFrame <- ManagerModeSetupFrame -- 6
            ManagerModeSetupFrame.place_forget()
            SoftwareActivationFrame.place(x = 5, y = 5)











        global Window
        Window = CTk.CTk()
        Window.title('Setup')
        Window.geometry('800x400')
        Window.resizable(False,False)
        Window.protocol('WM_DELETE_WINDOW', lambda: Window.destroy() if messagebox.askyesno(title = 'Exit Setup', message = 'Setup Is Not Complete. If You Exit Now, The Program Will Not Be Installed.\n\nYou May Run Setup Again At Another Time To Complete The Installation.\n\nExit Setup?') else None)

        # Welcome

        WelcomeFrame = CTk.CTkFrame(Window,790,390) ; WelcomeFrame.place(x=5,y=5)
        CTk.CTkLabel(WelcomeFrame,text='',image=CTk.CTkImage(light_image=WelcomeImage,dark_image=WelcomeImage,size=(790,358))).place(x=0,y=0)
        CTk.CTkButton(WelcomeFrame,text='Let\'s Get Started!',corner_radius=4,fg_color='transparent',border_color='grey',border_width=1,hover_color='grey',command=GoTo_TermsAndConditionsFrame).place(x=648,y=360)
        
        # Terms & Conditions

        def isTermsAndConditionsAccepted() -> None:

            if ACCEPTED.get():
                ContinueToActivation.configure(fg_color = '#4CAF50', state = 'normal')
            else:
                ContinueToActivation.configure(fg_color = '#B0B0B0', state = 'disabled')

        ACCEPTED = CTk.BooleanVar()
        TermsAndConditionsFrame = CTk.CTkFrame(Window,790,590) 
        TermsAndConditionsScrollableFrame = CTk.CTkScrollableFrame(TermsAndConditionsFrame,764,530) ; TermsAndConditionsScrollableFrame.place(x=2,y=2)
        
        TermsAndConditionsTextFrame = CTk.CTkFrame(TermsAndConditionsScrollableFrame,764,4600) ; TermsAndConditionsTextFrame.grid(row = 0, column = 0)
        CTk.CTkLabel(TermsAndConditionsTextFrame, text="TERMS OF SERVICE", font=("Arial", 22,'bold'),width=764).place(x=0,y=10)
        CTk.CTkLabel(TermsAndConditionsTextFrame, text='Copyright (c) 2026 Virati Akira Nandhan Reddy', font=("Roboto", 22,'bold'),width=764).place(x=0,y=50)
        CTk.CTkLabel(TermsAndConditionsTextFrame, text=f"{TERMSANDCONDITIONS[18:]}", font=("Roboto", 14), width=764, justify='left').place(x=5, y=90)

        CTk.CTkCheckBox(TermsAndConditionsFrame,text = 'I Agree To The License Terms & Conditions', variable = ACCEPTED, offvalue = False, onvalue = True, command = isTermsAndConditionsAccepted ,border_width = 1,
                        checkbox_height = 18, checkbox_width = 18, hover_color = '#45A049', fg_color = '#4CAF50').place(x=7,y=557)
        CTk.CTkButton(TermsAndConditionsFrame, text = 'Back', corner_radius=4, fg_color='transparent', border_color='grey', hover_color='grey', border_width=1, width=100 ,command=GoBackTo_WelcomeFrame).place(x=556, y=553)
        ContinueToActivation = CTk.CTkButton(TermsAndConditionsFrame, text = 'Accept & Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black',hover_color='#45A049',
                                             state='disabled', width=120 ,command = GoTo_SoftwareActivationFrame) ; ContinueToActivation.place(x=663, y=553)
        
        # Software Activation

        def isProductkeyMatching() -> None:

            if ProductKeyToBeVerified.get() in PRODUCTKEYS:

                ACTIVATEBUTTON.configure(fg_color = '#A9C5E8', state = 'disabled', text_color_disabled = 'Black')
                ProductKeyToBeVerified.configure(state = 'disabled')
                Status.configure(text = 'STATUS : ACTIVATED', text_color = 'lime')
                ContinueToManagerMode.configure(fg_color = '#4CAF50', state = 'normal')
                SETUPDATA['isActivated'] = True


            else: # Error Message 

                ProductKeyError = CTk.CTkLabel(SoftwareActivationFrame, text = 'The Product Key That You Entered Didn\'t Work. Check The Product Key &\nTry Again, Or Enter A Different One.',
                                               text_color = 'Orange') ; ProductKeyError.place(x = 20, y = 245)
                ProductKeyError.after(8000,ProductKeyError.destroy)

        SoftwareActivationFrame = CTk.CTkFrame(Window,790,390)
        CTk.CTkLabel(SoftwareActivationFrame, text = 'Enter a Product Key', font=('Arial', 28), text_color='#378F9C', justify = 'left').place(x=20,y=17)
        CTk.CTkLabel(SoftwareActivationFrame, text = 'Product Keys Will Be Available On Our Official GitHub Page. Please Visit The Repository To Access The Keys & Stay Updated.\nWe Recommend ' \
        'Checking The Repository Regularly For New Updates, Instructions, Or Important Notices Regarding This Software.\n\nWe Truly Appreciate Your Patience & Support As We Work To Provide The Best ' \
        'Experience Possible. Thank You For Being With Us.',
                      font=('Roboto', 13), justify = 'left').place(x=20,y=67)
        CTk.CTkLabel(SoftwareActivationFrame, text = 'Product Key', font = ('Roboto', 16), justify = 'left').place(x = 20, y = 170)
        ProductKeyToBeVerified = CTk.CTkEntry(SoftwareActivationFrame, placeholder_text = 'XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX', font=('Consolas', 14), width = 407) ; ProductKeyToBeVerified.place(x = 20, y = 201)
        CTk.CTkButton(SoftwareActivationFrame, text = '> Visit The GitHub Repository By Clicking Here <', fg_color='transparent', hover = False, text_color = 'Cyan',command = lambda: OpenBrowserForSpecifiedUrl(GITHUBREPOWEBSITE)).place(x = 20, y = 350)
        
        Status = CTk.CTkLabel(SoftwareActivationFrame, text = 'STATUS : NOT ACTIVATED', text_color = 'Red' ,font = ('Roboto', 18, 'bold')) ; Status.place(x = 505 , y = 240 )
        ACTIVATEBUTTON = CTk.CTkButton(SoftwareActivationFrame, text = 'ACTIVATE', text_color = 'Black', corner_radius=4, width=100, fg_color = '#007ACC', hover_color = '#3399FF', command = isProductkeyMatching) ; ACTIVATEBUTTON.place(x = 156, y = 290)
        CTk.CTkButton(SoftwareActivationFrame, text = 'Back', corner_radius=4, fg_color='transparent', border_color='grey', hover_color='grey', border_width=1, width=100 ,command = GoBackTo_TermsAndConditionsFrame).place(x = 580, y = 357)
        ContinueToManagerMode = CTk.CTkButton(SoftwareActivationFrame, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black',hover_color='#45A049',
                      state = 'disabled', width = 100, command = GoTo_ManagerModeSetupFrame) ; ContinueToManagerMode.place(x = 685, y = 357)
        
        # Manager Mode Setup

        ManagerModeSetupFrame = CTk.CTkFrame(Window,790,390)



        CTk.CTkButton(ManagerModeSetupFrame, text = 'Back', corner_radius = 4, fg_color = 'transparent', border_color='grey', hover_color='grey', border_width=1, width=100 ,command = GoBackTo_SoftwareActivationFrame).place(x = 580, y = 357)
        ContinueToGmailSetup = CTk.CTkButton(ManagerModeSetupFrame, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black',hover_color='#45A049',
                      state = 'disabled', width = 100, command = GoTo_ManagerModeSetupFrame) ; ContinueToGmailSetup.place(x = 685, y = 357)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        Window.mainloop()



SetUp().SetupWindows()
