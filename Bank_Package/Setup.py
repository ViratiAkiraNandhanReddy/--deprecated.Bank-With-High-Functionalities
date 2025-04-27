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

APPPASSWORDWEBSITE = 'www.google.com'
GITHUBREPOWEBSITE = ''

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

    def ManagerModeSetup(self) -> None:

        global ManagerModeSetupFrame
        ManagerModeSetupFrame = CTk.CTkFrame(Window,790,390) ; ManagerModeSetupFrame.place(x=5,y=5)
        
        
        CTk.CTkButton(ManagerModeSetupFrame,text='Next',corner_radius=4,fg_color='transparent',border_color='grey',hover_color='grey',border_width=1).place(x=660,y=360)

    def SetupWindows(self) -> None:

        def GoTo_TermsAndConditionsFrame() -> None: # WelcomeFrame -> TermsAndConditionsFrame -- 1
            WelcomeFrame.place_forget()
            Window.geometry('800x600')
            TermsAndConditionsFrame.place(x=5,y=5)

        def GoBackTo_WelcomeFrame() -> None: # WelcomeFrame <- TermsAndConditionsFrame -- 2
            TermsAndConditionsFrame.place_forget()
            Window.geometry('800x400')
            WelcomeFrame.place(x=5, y=5)

        def GoTo_SoftwareActivationFrame() -> None: # TermsAndConditionsFrame -> SoftwareActivationFrame -- 3
            TermsAndConditionsFrame.place_forget()
            Window.geometry('800x400')
            SoftwareActivationFrame.place(x=5,y=5)

        def GoBackTo_TermsAndConditionsFrame() -> None: # TermsAndConditionsFrame <- SoftwareActivationFrame -- 4
            SoftwareActivationFrame.place_forget()
            Window.geometry('800x600')
            TermsAndConditionsFrame.place(x=5,y=5)












        global Window
        Window = CTk.CTk()
        Window.title('Setup')
        Window.geometry('800x400')
        Window.resizable(False,False)
        Window.protocol('WM_DELETE_WINDOW', lambda: Window.destroy() if messagebox.askyesno(title = 'Exit Setup', message = 'Setup Is Not Complete. If You Exit Now, The Program Will Not Be Installed.\n\nYou May Run Setup Again At Another Time To Complete The Installation.\n\nExit Setup?') else None)

        WelcomeFrame = CTk.CTkFrame(Window,790,390) ; WelcomeFrame.place(x=5,y=5)
        CTk.CTkLabel(WelcomeFrame,text='',image=CTk.CTkImage(light_image=WelcomeImage,dark_image=WelcomeImage,size=(790,358))).place(x=0,y=0)
        CTk.CTkButton(WelcomeFrame,text='Let\'s Get Started!',corner_radius=4,fg_color='transparent',border_color='grey',border_width=1,hover_color='grey',command=GoTo_TermsAndConditionsFrame).place(x=648,y=360)
        

        def isTermsAndConditionsAccepted() -> None:

            if ACCEPTED.get():
                ContinueToActivation.configure(fg_color = '#4CAF50', state = 'normal')
            else:
                ContinueToActivation.configure(fg_color = '#B0B0B0', state = 'disabled')

        ACCEPTED = CTk.BooleanVar()
        TermsAndConditionsFrame = CTk.CTkFrame(Window,790,590) 
        TermsAndConditionsScrollableFrame = CTk.CTkScrollableFrame(TermsAndConditionsFrame,764,530) ; TermsAndConditionsScrollableFrame.place(x=2,y=2)
        
        TermsAndConditionsTextFrame = CTk.CTkFrame(TermsAndConditionsScrollableFrame,764,4900) ; TermsAndConditionsTextFrame.grid(row = 0, column = 0)
        CTk.CTkLabel(TermsAndConditionsTextFrame, text="TERMS OF SERVICE", font=("Arial", 22,'bold'),width=764).place(x=0,y=10)
        CTk.CTkLabel(TermsAndConditionsTextFrame, text='Copyright (c) 2026 Virati Akira Nandhan Reddy', font=("Roboto", 22,'bold'),width=764).place(x=0,y=50)
        CTk.CTkLabel(TermsAndConditionsTextFrame, text=f"{TERMSANDCONDITIONS[18:]}", font=("Roboto", 14), width=764, justify='left').place(x=5, y=90)
        
        CTk.CTkCheckBox(TermsAndConditionsFrame,text = 'I Agree To The License Terms & Conditions', variable = ACCEPTED, offvalue = False, onvalue = True, command = isTermsAndConditionsAccepted ,border_width = 1,
                        checkbox_height = 18, checkbox_width = 18, hover_color = '#45A049', fg_color = '#4CAF50').place(x=7,y=557)
        CTk.CTkButton(TermsAndConditionsFrame, text = 'Back', corner_radius=4, fg_color='transparent', border_color='grey', hover_color='grey', border_width=1, width=100 ,command=GoBackTo_WelcomeFrame).place(x=556, y=553)
        ContinueToActivation = CTk.CTkButton(TermsAndConditionsFrame, text = 'Accept & Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black',hover_color='#45A049',
                                             state='disabled', width=120 ,command = GoTo_SoftwareActivationFrame) ; ContinueToActivation.place(x=663, y=553)
        
        
        SoftwareActivationFrame = CTk.CTkFrame(Window,790,390)
        CTk.CTkLabel(SoftwareActivationFrame, text = 'Enter a Product Key', font=('Arial', 28), text_color='#378F9C', justify = 'left').place(x=20,y=17)
        CTk.CTkLabel(SoftwareActivationFrame, text = 'Product Keys Will Be Available On Our Official GitHub Page. Please Visit The Repository To Access The Keys And Stay Updated.\n\nWe Recommend ' \
        'Checking The Repository Regularly For New Updates, Instructions,\nOr Important Notices Regarding This Software.\n\nWe Truly Appreciate Your Patience & Support As We Work To Provide The Best ' \
        'Experience Passible.\nThank You For Being With Us. ',
                      font=('Roboto', 14), justify = 'left').place(x=20,y=67)
        CTk.CTkButton(SoftwareActivationFrame, text = 'Back', corner_radius=4, fg_color='transparent', border_color='grey', hover_color='grey', border_width=1, width=100 ,command = GoBackTo_TermsAndConditionsFrame).place(x=558, y=355)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        Window.mainloop()

OpenBrowserForSpecifiedUrl(APPPASSWORDWEBSITE)

SetUp().SetupWindows()
