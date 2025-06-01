#Importing Required Modules/Packages
import datetime
from Bank_Package import *
import Bank_Package.utils as utils
from Bank_Package.Login import Login

GITHUBREPOWEBSITE = 'https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities'

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

def Product_Activation() -> None:

    def isProductkeyMatching() -> None:
        
        if ProductKeyToBeVerified.get() in PRODUCTKEYS:

            ACTIVATEBUTTON.configure(fg_color = '#A9C5E8', state = 'disabled', text_color_disabled = 'Black')
            ProductKeyToBeVerified.configure(state = 'disabled')
            Status.configure(text = 'STATUS : ACTIVATED', text_color = 'lime')
            Continue.configure(fg_color = '#4CAF50', state = 'normal')
            Initialization_Data['isActivated'] = True

    Window = CTk.CTk()
    Window.title('Product Activation')
    Window.geometry('800x400')
    Window.resizable(False, False)
    Window.protocol('WM_DELETE_WINDOW', lambda: Window.destroy() if Initialization_Data.get('isActivated') else exit())
    CTk.CTkLabel(Window, text = 'Enter a Product Key', font=('Arial', 28), text_color='#378F9C', justify = 'left').place(x=20,y=17)
    CTk.CTkLabel(Window, text = 'Product Keys Will Be Available On Our Official GitHub Page. Please Visit The Repository To Access The Keys & Stay Updated.\nWe Recommend ' \
    'Checking The Repository Regularly For New Updates, Instructions, Or Important Notices Regarding This Software.\n\nWe Truly Appreciate Your Patience & Support As We Work To Provide The Best ' \
    'Experience Possible. Thank You For Being With Us.',
                    font=('Roboto', 13), justify = 'left').place(x=20,y=67)
    CTk.CTkLabel(Window, text = 'Product Key', font = ('Roboto', 16), justify = 'left').place(x = 20, y = 170)
    ProductKeyToBeVerified = CTk.CTkEntry(Window, placeholder_text = 'XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX', font=('Consolas', 14), width = 407) ; ProductKeyToBeVerified.place(x = 20, y = 201)
    CTk.CTkButton(Window, text = '> Visit The GitHub Repository By Clicking Here <', fg_color='transparent', hover = False, text_color = '#21968B',command = lambda: utils.OpenBrowserForSpecifiedUrl(GITHUBREPOWEBSITE)).place(x = 5, y = 357)
    
    Status = CTk.CTkLabel(Window, text = 'STATUS : NOT ACTIVATED', text_color = 'Red' ,font = ('Roboto', 18, 'bold')) ; Status.place(x = 505 , y = 240 )
    ACTIVATEBUTTON = CTk.CTkButton(Window, text = 'ACTIVATE', text_color = 'Black', corner_radius=4, width=100, fg_color = '#007ACC', hover_color = '#3399FF', command = isProductkeyMatching) ; ACTIVATEBUTTON.place(x = 156, y = 290)
    CTk.CTkButton(Window, text = 'Cancel', corner_radius = 4, fg_color = '#7BC47F', text_color = 'Black', hover_color = '#6BBF59', width = 100, command = lambda: [Window.destroy(), exit()]).place(x = 580, y = 357)
    Continue = CTk.CTkButton(Window, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black', hover_color='#45A049',
                    state = 'disabled', width = 100, command = Window.destroy) ; Continue.place(x = 685, y = 357)
    

    Window.mainloop()

if not Initialization_Data.get('isActivated', False):
    Product_Activation()

if not License_Check:
    Corrupted()
    exit()

print('prg started')
Initialization_Data["Recently Used On"] = datetime.datetime.now().strftime('%d-%b-%Y -- %A @ %I:%M:%S %p')
Login().Display_Login()

