import json
import io, os
import requests
import subprocess
import zipfile as Zip
import customtkinter as CTk

_LocalAppDataDirectory_ = str(os.environ.get('LOCALAPPDATA')) + r'\Bank-With-High-Functionalities'

class installer:

    def Download_And_Install(self) -> None:
        Window = CTk.CTk()















        Window.mainloop()

try:

    with open(fr'{_LocalAppDataDirectory_}\Bank_Package\DATABASE\JSON\ADMINISTRATIVE FILES\Initialization.json', 'r') as CONDITION:
        
        if json.load(CONDITION)["Manager Name"] == None:
            
            # Redirects To Setup
            subprocess.run(fr'{_LocalAppDataDirectory_}\Bank_Package\Setup.exe')
        
        else:
            
            # Redirects To Uninstall
            subprocess.run(fr'{_LocalAppDataDirectory_}\Bank_Package\Uninstall.exe')
except:

    # Runs `installer` Class
    installer().Download_And_Install()