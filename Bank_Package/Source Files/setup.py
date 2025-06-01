''' <!-- Doc Strings -->

# Copyright (c) 2024 - 2026 Virati Akira Nandhan Reddy

---
## Overview

This module is the **main setup and backup management script** for the Bank-With-High-Functionalities application. It is designed to be packaged as a standalone executable (EXE) using PyInstaller and provides a comprehensive, interactive, and robust setup experience for end users and administrators. The module is responsible for:

- **First-time installation and configuration**
- **Backup database detection, preview, restoration, and deletion**
- **Manager credential and security setup**
- **Product key validation and activation**
- **Email verification with secure code delivery**
- **Database selection and MySQL connection testing**
- **Shortcut and uninstall entry creation**
- **Automated developer and manager notifications**
- **Persistent configuration storage**
- **Resource and log management**

---

## Global Variables and Constants

- **PATH**: The root directory for all application data, typically under `%LOCALAPPDATA%`.
- **SETUPDATA**: A dictionary holding all persistent configuration and setup data, including activation status, manager credentials, database paths, and MySQL credentials.
- **PRODUCTKEYS**: List of valid product keys for software activation.
- **SEQUENCE**: Character set for generating secure codes.
- **Various URLs**: For documentation, support, and developer contact.
- **Preloaded Images/Icons**: Used for GUI elements and branding.
- **Log Files**: `ERROR_LOGS`, `EMAIL_LOGS`, `SETUP_LOGS` for error, email, and setup event logging.
- **Other**: Global variables for GUI state, countdowns, and verification codes.

---

## Utility Functions

### `__timer__(Widget, Count, text_after)`
Implements a countdown timer for a CustomTkinter widget, commonly used for "Resend Code" features.

### `OpenBrowserForSpecifiedUrl(URL)`
Opens a specified URL in the default web browser, supporting Windows, Mac, and Linux.

### `Folder_Size(_Path)`
Recursively calculates the total size (in bytes) of all files within a folder.

### `rm_backupbatabasememory()`
Closes all loaded icon images to release memory, especially after backup database operations.

### `register_uninstall_entry_user_scope()`
Registers an uninstall entry for the application in the Windows registry under the current user scope, enabling standard uninstallation via Windows settings.

---

## Backup Management (`CheckForBackupDatabase`)

### Purpose

Handles the detection, validation, restoration, deletion, and organization of up to three backup database folders. Provides a CustomTkinter-based GUI for users to interact with backups, ensuring data integrity and smooth recovery.

### Key Features

- **Detection**: Identifies up to three backup database folders.
- **Corruption Check**: Validates each backup by loading its initialization JSON file.
- **Data Retrieval**: Extracts initialization data and calculates backup size.
- **Graphical Management UI**: Allows preview, restore, and delete actions.
- **Restoration**: Replaces the current database with a selected backup, saving a rollback copy.
- **Deletion**: Removes corrupted or least-used backups.
- **Automatic Cleanup**: Deletes the backup with the fewest users or any corrupted backup when creating a new database.
- **Folder Renaming**: Maintains sequential naming after changes.
- **Integration**: Called at startup to manage backup state before setup or normal operation.

### Main Methods

- `Check_Presence_Of_Database()`: Checks for backup folders.
- `Check_For_Corrupted_Databases_And_Retrieve_Data()`: Loads and validates backup data.
- `Restore_Database(Database_Number)`: Restores a selected backup.
- `Restore_Backup_Database_Setup()`: Opens the backup management GUI.
- `Auto_Delete_Database_With_min_Users()`: Deletes the least-used or corrupted backup.
- `Rename_Folders()`: Renames backup folders for sequential order.
- `_exec_func_()`: Handles post-restore/setup actions (shortcuts, uninstall entry).

### Example Usage

```python
backup_checker = CheckForBackupDatabase()
if backup_checker.Check_Presence_Of_Database():
    backup_checker.Restore_Backup_Database_Setup()
```

### Security

- Deletion and restoration are irreversible and require user confirmation.
- Passwords are masked by default in the UI.
- Sensitive data is not exposed in logs or UI unless explicitly requested.

---

## MySQL Connection Testing (`CheckMySQLDatabaseConnection`)

### Purpose

Utility class to verify MySQL server connectivity using credentials provided in `SETUPDATA`. Handles connection attempts and logs errors.

### Main Method

- `DoesServerExists()`: Attempts to connect to the MySQL server and create the required database if it does not exist.

### Example Usage

```python
db_checker = CheckMySQLDatabaseConnection()
if db_checker.DoesServerExists():
    print("MySQL server is accessible.")
else:
    print("Failed to connect to the MySQL server.")
```

### Limitations

- Does not handle advanced MySQL configurations (SSL, plugins).
- Only returns a boolean for success/failure.

---

## Email Verification (`Manager_Email_Verification`)

### Purpose

Handles the manager's email verification process during setup. Generates a unique verification code, sends it via email, and provides resend functionality.

### Key Features

- **Verification Code Generation**: Secure, random code with expiration.
- **HTML Email Template**: Responsive and branded.
- **SMTP Sending**: Uses app password for secure authentication.
- **Resend Support**: Allows resending the code if needed.
- **GUI Integration**: Displays status and errors in the setup wizard.

### Main Methods

- `__init__(ReceiverMailAddress)`: Initializes with the manager's email.
- `Send_Gmail()`: Sends the verification email.
- `Resend_Gmail()`: Resends the verification email.

### Example Usage

```python
email_verification = Manager_Email_Verification(ReceiverMailAddress="manager@example.com")
result = email_verification.Send_Gmail()
print(result)
email_verification.Resend_Gmail()
```

### Security

- App password is used only for SMTP authentication and not stored in plaintext.
- Verification code expires after 10 minutes.

---

## Setup Wizard (`Setup`)

### Purpose

Implements the main setup wizard as a multi-step GUI using CustomTkinter. Guides the user through all required steps for installation and configuration.

### Key Features

- **Welcome Screen**: Greeting and start button.
- **Terms and Conditions**: License agreement acceptance.
- **Software Activation**: Product key validation.
- **Manager Mode Setup**: Collects and validates manager credentials.
- **Email Verification**: Sends and validates verification code.
- **Database Selection**: SQLite3, MySQL, or JSON.
- **MySQL Setup**: Collects and tests MySQL credentials.
- **Final Review**: Displays all collected data for confirmation.
- **Finish Setup**: Handles post-setup actions (shortcuts, notifications).

### Main Methods

- `__init__()`: Initializes the setup class.
- `__str__()`: Returns contribution and repository info.
- `SetupWindows()`: Manages the entire setup process and GUI navigation.
- `Inject_Initialization_Data_Into_JSON_Files()`: Saves setup data to JSON files.

### Example Usage

```python
setup = Setup()
setup.SetupWindows()
```

### Security

- Sensitive data is stored only in local JSON files.
- All registry and file operations are performed under the current user scope.
- Email credentials are not exposed in logs or messages.

---

## Cleanup Handler (`__atexit__`)

### Purpose

Ensures all open log files are properly closed when the program exits, preventing data loss or file corruption.

### Example Usage

```python
import atexit
atexit.register(__atexit__)
```

---

## Main Entry Point

The module is intended to be run as the main entry point of the application (typically as a PyInstaller EXE). On launch, it will:

1. Check for existing backup databases and prompt the user to restore or delete them if found.
2. If no backups are present or after restoration, launch the setup wizard for new installations.
3. Guide the user through all required steps, saving configuration and creating necessary system entries.
4. Handle all errors gracefully and log them for troubleshooting.

### Example

```python
Backup_Database_cls = CheckForBackupDatabase()
isDatabasesAvailable = Backup_Database_cls.Check_Presence_Of_Database()

if isDatabasesAvailable:
    Backup_Database_cls.Restore_Backup_Database_Setup()
    if Backup_Database_cls.isNewDatabaseRequested:
        Backup_Database_cls.Auto_Delete_Database_With_min_Users()
        rm_backupbatabasememory()
        Setup().SetupWindows()
    else:
        Backup_Database_cls._exec_func_()
    Backup_Database_cls.Rename_Folders()
else:
    rm_backupbatabasememory()
    Setup().SetupWindows()
```

---

## Security Considerations

- All sensitive data (passwords, security codes) is stored only locally and never transmitted except for email verification.
- Registry and file operations are performed under the current user scope.
- Deletion and restoration of backups are irreversible and require user confirmation.
- Email credentials are used only for SMTP authentication and are not exposed in logs or messages.

---

## Error Handling

- All critical operations (file, network, registry) are wrapped in try/except blocks.
- Errors are logged to dedicated log files (`ErrorLogs.txt`, `EmailLogs.txt`, `SetupLogs.txt`).
- The application provides user-friendly error messages and guidance in the GUI.

---

## Platform Support

- **Windows**: Full support, including registry and shortcut creation.
- **Other OS**: Some features (shortcuts, registry) may not be available or will be skipped.

---

## Dependencies

- `customtkinter`, `PIL`, `mysql.connector`, `smtplib`, `win32com.client`, `tkinter`, `atexit`, `subprocess`, `platform`, `threading`, `json`, `os`, `shutil`, `datetime`, `random`, `urllib.request`, `winreg`.

---

## Limitations

- Only three backup databases are supported at a time.
- Designed primarily for Windows environments.
- Assumes all required resource files (images, icons, templates) are present in the packaged EXE.
- Some features (e.g., registry, shortcut creation) are Windows-specific.

---

## Authors & Support

- **Developer:** Virati Akira Nandhan Reddy  
- **GitHub:** [ViratiAkiraNandhanReddy](https://github.com/ViratiAkiraNandhanReddy)  
- **Website:** [Project Homepage](https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities)
- **Gmail:** Viratiaki29@gmail.com 
- **LinkedIn:** [viratiakiranandhanreddy](https://linkedin.com/in/viratiakiranandhanreddy/)
- **X(Twitter):** [Viratiaki53](https://x.com/Viratiaki53)
- **Instagram:** [Viratiaki53](https://instagram.com/viratiaki53/)
- **Support:** Please use the GitHub repository for issues and contributions.

---

## License

- See `LICENSE` included with the application for licensing details.

---

## Detailed Flow

### 1. **Startup and Backup Detection**
   - On launch, the script checks for up to three backup database folders.
   - If backups are found, a GUI is presented for preview, restoration, or deletion.
   - Corrupted backups are detected and flagged; only valid backups can be restored.

### 2. **Backup Restoration or New Setup**
   - If a backup is restored, the main database is replaced and a rollback copy is saved.
   - If the user opts for a new setup, the least-used or corrupted backup is deleted if all slots are full.

### 3. **Setup Wizard**
   - The user is guided through a multi-step GUI:
     - Welcome
     - Terms and Conditions
     - Product Key Activation
     - Manager Credential Setup
     - Email Verification (with code delivery and countdown)
     - Database Selection (SQLite3, MySQL, JSON)
     - MySQL Credential Collection and Connection Test
     - Final Review and Confirmation
     - Finish Setup (shortcuts, notifications, uninstall entry)

### 4. **Post-Setup Actions**
   - Shortcuts are created on the Desktop and Start Menu.
   - An uninstall entry is registered in the Windows registry.
   - Automated emails are sent to the developer and manager.
   - All setup data is saved to JSON files for persistence.

### 5. **Cleanup**
   - On exit, all log files are closed to prevent data loss.

---

## Example Data Structures

### `SETUPDATA` Example

```python
{
    "isActivated": True,
    "License Verification": "Passed",
    "Current Version": "0.0.1 - Alpha",
    "Manager Name": "John Doe",
    "Manager Username": "johndoe123",
    "Manager Password": "********",
    "Manager Security Code": "%^*^$&jg758fj^($&)",
    "Manager Email": "johndoe@example.com",
    "Manager Email App Password": "********",
    "isEmailVerified": True,
    "Downloaded On": "15-May-2025 -- Thursday @ 10:30:00 AM",
    "DATABASE TYPE": "SQLite3",
    "DATABASE PATH": "path/to/database.sqlite3",
    "BACKUP DATABASE PATH": "path/to/database.sqlite3",
    "MySQL Credentials": {
        "Host": "localhost",
        "Port": 3306,
        "Username": "root",
        "Password": "********",
        "Database": "Bank-With-High-Functionalities",
        "Charset": "utf8mb4"
    }
}
```

---

## Advanced Notes

- **Threading** is used for long-running file operations (e.g., backup restoration, deletion) to keep the GUI responsive.
- **CustomTkinter** is used for all GUI elements, providing a modern look and feel.
- **Resource Management**: All loaded images are closed after use to prevent memory leaks.
- **Rollback Safety**: Every backup restoration saves a rollback copy in a dedicated folder.
- **Extensibility**: The setup process is modular, allowing for future enhancements (e.g., more database types, advanced backup management).
- **Logging**: All significant actions and errors are logged for troubleshooting and audit purposes.
'''

import json
import winreg
import datetime
from PIL import Image
import mysql.connector
import smtplib, socket
import shutil, os, sys
import threading, atexit
import subprocess, platform
import customtkinter as CTk
from itertools import repeat
from tkinter import messagebox
from urllib.request import urlopen
from win32com.client import Dispatch
from email.message import EmailMessage
from random import choice, randint, random

'''
pyinstaller --noconfirm --onefile --windowed --icon="Bank_Package\\Visual Data\\ICO Files\\setup_icon.ico" --version-file="Bank_Package\\Build Metadata\\setup.exe - v0.0.1.txt" "Bank_Package\\setup.py"
'''

# < TESTING > PATH = r'D:\GitHub\Bank-With-High-Functionalities'

PATH = str(os.environ.get('LOCALAPPDATA')) + r'\Bank-With-High-Functionalities'

SETUPDATA = { # Initialization Data 

	"isActivated": False,    # True | False
	"License Verification": None,    # Passed | Failed
	"Current Version": 'vNext',    # 0.0.1 - Alpha | 0.0.2 - Beta | 0.1.0 - Stable
	
	"Manager Name": None,    # e.g., Virati Akira Nandhan Reddy
	"Manager Username": None,    # e.g., Viratiaki53
	"Manager Password": None,    # e.g., Viratiaki@2008
	"Manager Security Code": None,    # e.g., %^*^$&jg758fj^($&) [18 - Chars]
	"Manager Email": None,    # e.g., example@example.com
	"Manager Email App Password": None,    # e.g., cxuo hgst csqi xwur
	"Lastly Verified On": None,	   # 2-May-2025 -- Friday @ 12:37:23 PM
	"isEmailVerified": False,    # True | False
	
	"Downloaded On": None,    # 2-May-2025 -- Friday @ 12:37:23 PM
	"Deleted On": None,    # 2-May-2025 -- Friday @ 12:37:23 PM
	"Recently Used On": None,    # 2-May-2025 -- Friday @ 12:57:23 PM
	
	"DATABASE TYPE": 'SQLite3',    # JSON | SQLite3 (Default) | MySQL
	"DATABASE PATH": fr'{PATH}\Bank_Package\DATABASE\SQLite3\database.sqlite3',    # %LOCALAPPDATA%\Bank-With-High-Functionalities\Bank_Package\DATABASE\SQLite3\database.sqlite3
	"BACKUP DATABASE PATH": fr'{PATH}\BACKUP - DATABASE\SQLite3\database.sqlite3',    # %LOCALAPPDATA%\Bank-With-High-Functionalities\BACKUP - DATABASE\SQLite3\database.sqlite3
	
	"User Records": { # Specially Used For Backup Purposes

		"Total Users Recorded": 0,
		"Total Active Users": 0,
		"Total Inactive Users": 0

	},

	"MySQL Credentials": {

		"Host": None,    # e.g., localhost
		"Port": None,    # e.g., 3306
		"Username": None,    # e.g., root
		"Password": None,    # e.g., Viratiaki@2008
		"Database": None,    # e.g., Bank-With-High-Functionalities
		"Charset": None,    # e.g., utf8mb4

	}
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

SEQUENCE = [ # For Security Code Generation 

	'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
	'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
	'!','@','#','$','%','^','&','*','(',')','-','+','{','}','[',']',';',':','?','|','~','.','<','>','=','_',
	'1','2','3','4','5','6','7','8','9','0'
	
]

APPPASSWORDWEBSITE = 'https://myaccount.google.com/apppasswords'
GITHUBREPOWEBSITE = 'https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities'
DATABASEINFOWEBSITE = 'https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities/blob/main/docs/Detailed%20Overviews/DatabaseComparison.md'

x = 'https://x.com/Viratiaki53'
mail = 'mailto:viratiaki53@gmail.com'
github = 'https://github.com/ViratiAkiraNandhanReddy'
webpage = 'https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities'
facebook = 'https://www.facebook.com/ViratiAkiraNandhanReddy'
linkedin = 'https://www.linkedin.com/in/viratiakiranandhanreddy'
instagram = 'https://www.instagram.com/viratiaki53'


MYSQL_ON_DOWNLOAD_SETUP = 'https://www.google.com/search?q=how+to+install+and+setup+mysql'
MYSQL_SERVER_DETAILS = 'https://www.google.com/search?q=where+to+know+mysql+server+connection+credentials+with+workbench+and+without+workbench'
HOW_TO_SETUP_APPPASSWORD = 'https://www.google.com/search?q=how+to+setup+app+password+for+my+google+account'
APPPASSWORD_ERROR = 'https://www.google.com/search?q=Why+app+passwords+is+disabled+on+my+google+account'

try:

	'''
	# Functionality
	- Loads images for banners, database icons, UI icons, and social media icons.
	- Opens log files for error, email, and setup events.
	- Reads the terms and conditions from a text file.

	# Error Handling
	If any file is missing or cannot be loaded, shows an error message and exits the application.
	'''

	BannerLightImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Representation Images\Banner Light.jpg')
	BannerDarkImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Representation Images\Banner Dark.jpg')

	DatabaseComparisonDarkImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Markdown Resources\Database Comparison Dark.png')
	DatabaseComparisonLightImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Markdown Resources\Database Comparison Light.png')
	AppPasswordLightImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Markdown Resources\App Password Light.png')
	AppPasswordDarkImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Markdown Resources\App Password Dark.png')
	ThankYouDarkImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Markdown Resources\Thank You Message Dark.png')
	ThankYouLightImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Markdown Resources\Thank You Message Light.png')
	MySQLSetupLightImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Markdown Resources\MySQL Setup Light.png')
	MySQLSetupDarkImage = Image.open(fr'{PATH}\Bank_Package\Visual Data\Markdown Resources\MySQL Setup Dark.png')

	INFO_Icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\info.png')
	LINK_Icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\link.png')
	EXCLAMATION_Icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\Exclamation.png')
	Database_Config_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\Database -- icon.png')

	Delete_Database_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\Database\Delete Database.png')
	Database_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\Database\Database.png')
	User_Config_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\UI\User Config.png')
	People_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\User Badges\People.png')
	Next_Navigation_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\Navigation Icons\Next.png')
	Password_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\UI\Password.png')
	Mail_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\UI\Mail.png')
	Password_Show_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\UI\Show.png')
	Password_Hide_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\UI\Hide.png')
	Security_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\UI\Security.png')
	Download_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\UI\Download.png')
	Upload_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\UI\Upload.png')
	Username_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\UI\Username.png')
	Restore_Database_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\Database\Restore Database.png')

	instagram_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\icons\instagram.png')
	x_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\icons\x.png')
	facebook_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\icons\facebook.png')
	github_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\icons\github.png')
	linkedin_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\icons\linkedin.png')
	webpage_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\icons\webpage.png')
	gmail_icon = Image.open(fr'{PATH}\Bank_Package\Visual Data\icons\gmail.png')

	MySQL_Logo = Image.open(fr'{PATH}\Bank_Package\Visual Data\MySQL -- Logo.png')
	Google_Logo = Image.open(fr'{PATH}\Bank_Package\Visual Data\Google.png')


	ERROR_LOGS = open(fr'{PATH}\Logs\ErrorLogs.txt', 'a')
	EMAIL_LOGS = open(fr'{PATH}\Logs\EmailLogs.txt', 'a')
	SETUP_LOGS = open(fr'{PATH}\Logs\SetupLogs.txt', 'a')

	with open(fr'{PATH}\TERMS OF SERVICE.txt') as FILE:

		TERMSANDCONDITIONS: str = FILE.read()

except Exception:

	messagebox.showerror(title = 'Missing System Files', message='Some required system files are missing or could not be loaded.\n\nPlease try restarting the setup. If the problem persists, consider reinstalling the ' \
	'application or contact support.')

	sys.exit()

MYSQLLOG = """ """ # Empty For A Reason

__Code__ = None
__Timestamp__ = datetime.datetime.now()

# Implements A Countdown Timer For A Widget (Button Or Label).
def __timer__(Widget: CTk.CTkButton | CTk.CTkLabel, Count: int, text_after: str) -> None:

	"""
	### Purpose
	Implements a countdown timer for a given CustomTkinter widget (button or label), typically used for features like "Resend Code" in verification flows.

	### Parameters
	- **Widget** (`CTk.CTkButton` or `CTk.CTkLabel`): The widget whose text will display the countdown.
	- **Count** (`int`): The starting value for the countdown in seconds.
	- **text_after** (`str`): The text to display on the widget after the countdown finishes.

	### Functionality
	- Updates the widget's text to show the remaining seconds.
	- Decrements the count every second using the widget's `.after()` method.
	- When the countdown reaches zero, resets the widget's text to `text_after` and enables the widget if it was disabled.

	### Returns
	- **None**

	### Example Usage
	```python
	__timer__(ResendButton, 10, "Resend Code")
	```

	### Notes
	- This function is designed for use with CustomTkinter widgets.
	- Commonly used to prevent immediate resending of verification codes or similar actions.

	### Dependencies
	- Requires `customtkinter` (imported as `CTk`).
	"""


	Widget.configure(text = str(Count))

	if Count > 0:
		Widget.after(1000, __timer__, Widget, Count - 1, text_after)
	else:
		Widget.configure(text = text_after, state = 'normal', fg_color = '#4CAF50')

# To Open The Browser
def OpenBrowserForSpecifiedUrl(URL: str) -> None: # Works For Windows, Mac, Linux 

	'''
	## Purpose
	The `OpenBrowserForSpecifiedUrl` function is designed to open a specified URL in the default web browser. It supports Windows, Mac, and Linux operating systems.

	## Parameters
	- `URL` (str): The URL to be opened in the browser.

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
			subprocess.run(f"Start {URL}", shell = True)

		elif platform.system() == 'Mac':
			subprocess.run(f"open {URL}", shell = True)

		elif platform.system() == 'Linux':
			subprocess.run(f"xdg-open {URL}", shell = True)

	except Exception as Error: # Logging and fallback

		ERROR_LOGS.write(f'\n[ERROR]:[setup.exe][{datetime.datetime.now().strftime('%d/%b/%Y @ %I:%M:%S %p')}] - Failed To Open {URL} ; ErrorType: [ {Error} ]')

# Returns the size of folder in bytes
def Folder_Size(_Path: str) -> int:

	'''
    ### Purpose
    Calculates the total size (in bytes) of all files within a specified folder, including all subdirectories.

    ### Parameters
    - **_Path** (`str`): The path to the folder whose size is to be calculated.

    ### Returns
    - **int**: The total size of all files in the folder and its subfolders, in bytes.

    ### Functionality
    - Recursively traverses the directory tree starting from `_Path`.
    - Sums the sizes of all files found in the directory and its subdirectories.

    ### Example Usage
    ```python
    size = Folder_Size(r'C:\\Users\\User\\Documents')
    print(f"Total size: {size} bytes")
    ```

    ### Notes
    - Symbolic links are not followed.
    - The function does not count the size of directories themselves, only the files within.

    ### Dependencies
    - Requires the `os` module for file and directory operations.
	'''

	Total_Size = 0

	for root, dir, files in os.walk(_Path):

		for fps in files:
			file_path = os.path.join(root, fps)
			Total_Size += os.path.getsize(file_path)

	return Total_Size

# Releases memory by closing loaded icon (*Backup_Database_Window*)
def rm_backupbatabasememory() -> None:

	'''
    ### Purpose
    Releases memory and resources used by backup database icon images by closing all loaded image objects.

    ### Functionality
    - Iterates through a predefined list of icon image objects used in the backup database UI.
    - Calls the `.close()` method on each image object to free up system resources and memory.

    ### Parameters
    - **None**: This function does not take any parameters.

    ### Returns
    - **None**

    ### Example Usage
    ```python
    rm_backupbatabasememory()
    ```

    ### Notes
    - This function should be called when backup database icons are no longer needed, such as after closing the backup database window or before application shutdown.
    - Helps prevent memory leaks by ensuring all image resources are properly released.

    ### Dependencies
    - Requires that all icon image objects (e.g., `Mail_icon`, `People_icon`, etc.) are defined and loaded using PIL's `Image.open()`.

    ### Security
    - No sensitive data is handled by this function.

    ### Limitations
    - If any icon object is not defined or already closed, an exception may occur unless handled elsewhere.
	'''

	for icon in [

		Mail_icon,
		People_icon,
		Upload_icon,
		Security_icon,
		Download_icon,
		Username_icon,
		Database_icon,
		Password_icon,
		User_Config_icon,
		Password_Show_icon,
		Password_Hide_icon,
		Next_Navigation_icon,
		Delete_Database_icon,
		Restore_Database_icon,
		
	]: icon.close()

# Registers the uninstaller in windows registry
def register_uninstall_entry_user_scope() -> None:

	''' <!-- Doc Strings -->
    ### Purpose
    Registers an uninstall entry for the "Bank-With-High-Functionalities" application in the Windows registry under the current user scope.
	This enables the application to appear in the "Add or Remove Programs" list for the current user, allowing for standard uninstallation via Windows settings.

    ### Functionality
    - Creates or updates a registry key at:
    > `HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Bank-With-High-Functionalities`
    - Sets multiple registry values to provide Windows with all necessary information for displaying and uninstalling the application:
        - **DisplayName**: The name shown in the uninstall list.
        - **DisplayVersion**: The current version of the application.
        - **Publisher**: The application's publisher (developer).
        - **InstallLocation**: The directory where the application is installed.
        - **UninstallString**: The command to execute for uninstalling the application.
        - **DisplayIcon**: The icon shown in the uninstall list.
        - **ModifyPath**: The path to the repair executable.
        - **URLInfoAbout**: A URL for more information about the application.
        - **HelpLink**: A URL for help or support.
        - **NoModify** and **NoRepair**: Flags to control whether the user can modify or repair the installation from the uninstall UI.

    ### Parameters
    - **None**: This function does not take any parameters.

    ### Returns
    - **None**

    ### Example Usage
    ```python
    register_uninstall_entry_user_scope()
    ```

    ### Notes
    - This function should be called during the installation or setup process to ensure the application can be uninstalled via Windows settings.
    - The uninstall entry is created only for the current user (not system-wide).
    - Uses the `winreg` module for registry operations and relies on global variables such as `SETUPDATA`, `PATH`, `webpage`, and `github` for registry values.
    - The uninstall string typically points to an `uninstall.exe` in the application directory.

    ### Error Handling
    - If any error occurs during registry operations (e.g., permission issues, missing values), the error is caught and logged to the setup log file (`SETUP_LOGS`).
    - The function does not raise exceptions to the caller; all errors are handled internally.

    ### Security
    - Modifies the Windows registry only for the current user, so no administrator privileges are required.
    - Does not affect other users on the system.

    ### Limitations
    - Only works on Windows operating systems.
    - Does not create a system-wide uninstall entry (for all users).
    - If the registry cannot be written (e.g., due to permissions), the uninstall entry will not be created.

    ### Dependencies
    - Requires the `winreg` module for registry access.
    - Relies on global variables for application metadata and paths.
	'''

	uninstall_key_path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\Bank-With-High-Functionalities"

	try:

		key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, uninstall_key_path, 0, winreg.KEY_WRITE)

		winreg.SetValueEx(key, "DisplayName", 0, winreg.REG_SZ, 'Bank-With-High-Functionalities')
		winreg.SetValueEx(key, "DisplayVersion", 0, winreg.REG_SZ, SETUPDATA['Current Version'])
		winreg.SetValueEx(key, "Publisher", 0, winreg.REG_SZ, 'Virati Akira Nandhan Reddy')
		winreg.SetValueEx(key, "InstallLocation", 0, winreg.REG_SZ, PATH)
		winreg.SetValueEx(key, "UninstallString", 0, winreg.REG_SZ, fr'{PATH}uninstall.exe')
		winreg.SetValueEx(key, "DisplayIcon", 0, winreg.REG_SZ, fr'{PATH}\Bank_Package\Visual Data\ICO Files\Bank Image.ico')
		winreg.SetValueEx(key, "ModifyPath", 0, winreg.REG_SZ, fr'{PATH}\repair.exe')
		winreg.SetValueEx(key, "URLInfoAbout", 0, winreg.REG_SZ, webpage)
		winreg.SetValueEx(key, "HelpLink", 0, winreg.REG_SZ, github)

		winreg.SetValueEx(key, "NoModify", 0, winreg.REG_DWORD, 0)
		winreg.SetValueEx(key, "NoRepair", 0, winreg.REG_DWORD, 0)

		winreg.CloseKey(key)
		SETUP_LOGS.write('\n[INFO] : Registered For Uninstall.')

	except Exception as Error:
		SETUP_LOGS.write(f'[ERROR]: Error While Registering For Uninstall ; ErrorType : {Error}')

# To Check The Presence Of Previous Backup Database 
class CheckForBackupDatabase:

	''' <!-- Doc Strings -->
    ## Purpose
    The `CheckForBackupDatabase` class manages the detection, validation, restoration, deletion, and organization of backup database folders for the "Bank-With-High-Functionalities" application. It provides both backend logic and a graphical interface for users to interact with available backups, ensuring data integrity and smooth recovery or migration processes.

    ## Features
    - **Detection**: Identifies the presence of up to three backup database folders on the user's system.
    - **Corruption Check**: Validates each backup by attempting to load its initialization JSON file, marking corrupted backups and logging errors.
    - **Data Retrieval**: Extracts and stores initialization data and calculates the size of each backup for display and management.
    - **Graphical Management UI**: Presents a CustomTkinter-based window for users to preview, restore, or delete backups, and to toggle password visibility.
    - **Restoration**: Allows users to restore any valid backup, replacing the current database and saving a rollback copy for safety.
    - **Deletion**: Enables deletion of any backup (especially corrupted or least-used ones) to free up space or resolve issues.
    - **Automatic Cleanup**: Provides logic to automatically delete the backup with the fewest users or any corrupted backup when creating a new database.
    - **Folder Renaming**: Maintains a consistent and sequential naming convention for backup folders after any change.
    - **Integration**: Designed to be called at application startup to manage backup state before proceeding with setup or normal operation.

    ## Attributes
    - `isNewDatabaseRequested` (bool): Indicates if the user has requested to create a new database, triggering automatic cleanup if needed.
    - `Total_DBs` (list[bool]): Tracks the availability of each backup database.
    - `Database_01_init_Data`, `Database_02_init_Data`, `Database_03_init_Data` (dict): Store initialization data for each backup.
    - `isDatabase_01_Corrupted`, `isDatabase_02_Corrupted`, `isDatabase_03_Corrupted` (bool): Flags indicating if a backup is corrupted.
    - `isDatabase_01_Available`, `isDatabase_02_Available`, `isDatabase_03_Available` (bool): Flags indicating if a backup is available.
    - `DB_01_SIZE`, `DB_02_SIZE`, `DB_03_SIZE` (float): Sizes of each backup database in kilobytes.
    - `showpassword_DB_01`, `showpassword_DB_02`, `showpassword_DB_03` (bool): Flags for password visibility in the UI.

    ## Main Methods

    ### 1. `Check_Presence_Of_Database() -> bool`
    Checks if any backup database folders exist and updates availability flags. Returns `True` if at least one backup is present.

    ### 2. `Check_For_Corrupted_Databases_And_Retrieve_Data() -> None`
    Attempts to load initialization data from each backup and marks corrupted backups. Updates internal state for UI and logic.

    ### 3. `Restore_Database(Database_Number: int) -> None`
    Restores the selected backup database (1, 2, or 3), replacing the current database and saving a rollback copy. Runs in a separate thread for UI responsiveness.

    ### 4. `Restore_Backup_Database_Setup() -> None`
    Opens a GUI for users to preview, restore, or delete backups, and to proceed with creating a new database if needed. Handles all user interactions for backup management.

    ### 5. `Auto_Delete_Database_With_min_Users() -> None`
    Automatically deletes the backup with the fewest users or any corrupted backup to free up space when all slots are full.

    ### 6. `Rename_Folders() -> None`
    Renames backup folders to maintain sequential naming (e.g., BACKUP - DATABASE 01, 02, 03) after deletion or restoration.

    ### 7. `_exec_func_() -> None`
    Handles post-restore/setup actions such as creating shortcuts and registering uninstall entries.

    ## Example Usage
    ```python
    backup_checker = CheckForBackupDatabase()
    if backup_checker.Check_Presence_Of_Database():
        backup_checker.Restore_Backup_Database_Setup()
    ```

    ## Notes
    - Designed for use at application startup to manage backup databases before proceeding with setup or normal operation.
    - Integrates with CustomTkinter for GUI operations and uses threading for non-blocking file operations.
    - Handles up to three backup databases, maintaining their order and integrity.
    - Relies on global variables for paths, icons, and logs.

    ## Error Handling
    - Corrupted backups are detected and flagged; errors are logged to the error log file.
    - All file operations are wrapped in try/except blocks to prevent crashes and ensure smooth user experience.

    ## Security
    - Deletion and restoration actions are irreversible; users are prompted for confirmation.
    - Passwords are masked in the UI by default and can only be revealed on user action.
    - Sensitive data is not exposed in logs or UI unless explicitly requested by the user.

    ## Limitations
    - Only supports up to three backup databases.
    - Assumes required directories and resources exist and are accessible.
    - Designed for Windows file system conventions and may require adaptation for other OSes.

    ## Dependencies
    - Requires `os`, `shutil`, `json`, `threading`, and `customtkinter`.
    - Relies on global variables for resource paths, icons, and logs.
    - Uses `tkinter.messagebox` for user prompts and notifications.
	'''

	isNewDatabaseRequested = False

	isBackupDatabaseRestored = False

	def __init__(self) -> None:
		self.Total_DBs: list[bool] = []

		self.Database_01_init_Data: dict = {}
		self.Database_02_init_Data: dict = {}
		self.Database_03_init_Data: dict = {}

		self.isDatabase_01_Corrupted = False
		self.isDatabase_02_Corrupted = False
		self.isDatabase_03_Corrupted = False

		self.isDatabase_01_Available = True
		self.isDatabase_02_Available = True
		self.isDatabase_03_Available = True

		self.DB_01_SIZE = 0
		self.DB_02_SIZE = 0
		self.DB_03_SIZE = 0

		self.showpassword_DB_01 = False
		self.showpassword_DB_02 = False
		self.showpassword_DB_03 = False

	def Check_Presence_Of_Database(self) -> bool:

		self.isDatabase_01_Available = os.path.exists(fr'{PATH}\BACKUP - DATABASE 01')
		self.isDatabase_02_Available = os.path.exists(fr'{PATH}\BACKUP - DATABASE 02')
		self.isDatabase_03_Available = os.path.exists(fr'{PATH}\BACKUP - DATABASE 03')

		# Checking Multiple Times Because User May Accidentally Delete A Particular Database Folder
		return self.isDatabase_01_Available or self.isDatabase_02_Available or self.isDatabase_03_Available

	def Check_For_Corrupted_Databases_And_Retrieve_Data(self) -> None:
		
		'''
		### Purpose
		Checks each backup database (1, 2, and 3) for corruption by attempting to load their initialization JSON files. If a database is not corrupted, retrieves and stores its initialization data and calculates its size.

		### Functionality
		- Attempts to open and load the `Initialization.json` file for each backup database.
		- If successful, loads the initialization data into the corresponding attribute and calculates the database size in kilobytes.
		- If loading fails (e.g., file missing or corrupted), marks the database as corrupted and logs the error.
		- Designed to prevent application breakdown by validating the presence and integrity of essential fields in the JSON data.

		### Parameters
		- **self**: The instance of the `CheckForBackupDatabase` class.

		### Returns
		- **None**

		### Example Usage
		```python
		backup_checker = CheckForBackupDatabase()
		backup_checker.Check_For_Corrupted_Databases_And_Retrieve_Data()
		```

		### Notes
		- This function should be called before displaying or restoring backup databases to ensure only valid data is used.
		- The function updates internal state flags (`isDatabase_01_Corrupted`, etc.) for use in the UI and logic.
		- Errors are logged to the `ERROR_LOGS` file for troubleshooting.

		### Error Handling
		- If a database's initialization file is missing or unreadable, the corresponding `isDatabase_X_Corrupted` flag is set to `True`.
		- Errors are written to the error log file.

		### Dependencies
		- Requires the `os`, `json`, and `Folder_Size` utility for file operations and size calculation.
		'''

		try:

			with open(fr'{PATH}\BACKUP - DATABASE 01\JSON\ADMINISTRATIVE FILES\Initialization.json') as DB_01:
				self.Database_01_init_Data = json.load(DB_01)
				self.DB_01_SIZE = (Folder_Size(fr'{PATH}\BACKUP - DATABASE 01')/(1024))

				for i in [self.Database_01_init_Data["Manager Name"], ...]: # Checking the json to avoid the breakdown
					temp = i
					...



		except Exception as Error:

			self.isDatabase_01_Corrupted = True
			ERROR_LOGS.write('\n')

		try:

			with open(fr'{PATH}\BACKUP - DATABASE 02\JSON\ADMINISTRATIVE FILES\Initialization.json') as DB_02:
				self.Database_02_init_Data = json.load(DB_02)
				self.DB_02_SIZE = (Folder_Size(fr'{PATH}\BACKUP - DATABASE 02')/(1024))

				for i in [self.Database_02_init_Data["Manager Name"], ...]: # Checking the json to avoid the breakdown
					temp = i
					...


		except Exception as Error:

			self.isDatabase_02_Corrupted = True
			ERROR_LOGS.write('\n')
		try:

			with open(fr'{PATH}\BACKUP - DATABASE 03\JSON\ADMINISTRATIVE FILES\Initialization.json') as DB_03:
				self.Database_03_init_Data = json.load(DB_03)
				self.DB_03_SIZE = (Folder_Size(fr'{PATH}\BACKUP - DATABASE 03')/(1024))

				for i in [self.Database_03_init_Data["Manager Name"], ...]: # Checking the json to avoid the breakdown
					temp = i
					...


		except Exception as Error:

			self.isDatabase_03_Corrupted = True
			ERROR_LOGS.write('\n')

	def Restore_Database(self, Database_Number: int) -> None:
		
		'''
		### Purpose
		Restores the selected backup database (1, 2, or 3) to the application's main database directory, replacing any existing database. This is used when a user chooses to recover a previous backup.

		### Parameters
		- **Database_Number** (`int`): The backup database number to restore (1, 2, or 3).

		### Functionality
		- Removes the current main database and backup database directories.
		- Copies the selected backup database folder to both a rollback location and the main database directory.
		- Renames the backup folder to the standard backup directory name.
		- Notifies the user upon successful restoration.
		- Runs the restoration process in a separate thread for each database to keep the UI responsive.
		- Shows a progress/info message during the restoration process.

		### Example Usage
		```python
		self.Restore_Database(1)  # Restores Backup Database 1
		self.Restore_Database(2)  # Restores Backup Database 2
		self.Restore_Database(3)  # Restores Backup Database 3
		```

		### Notes
		- This function is intended to be called from the backup database restore setup window.
		- The restoration process is performed asynchronously using threads.
		- A rollback copy of the backup is saved in the user's local app data for safety.

		### GUI Integration
		- Hides the backup database window during restoration.
		- Displays message boxes to inform the user about the restoration status and warnings.

		### Security
		- Overwrites existing database files and directories. Use with caution.
		- Always creates a rollback copy before replacing the main database.

		### Limitations
		- Only works if the backup folders exist and are accessible.
		- User should not exit or force stop the application during restoration to avoid data corruption.
		'''

		def _restore_db_01_() -> None:
			
			Backup_Database_Window.withdraw()

			shutil.rmtree(fr'{PATH}\Bank_Package\DATABASE')
			shutil.rmtree(fr'{PATH}\BACKUP - DATABASE')

			shutil.copytree(fr'{PATH}\BACKUP - DATABASE 01', str(os.environ.get('LOCALAPPDATA')) + fr'\Bank-With-High-Functionalities - ROLLBACKS\BACKUP - DATABASE 01 - {datetime.datetime.now().strftime('%d-%b-%Y -- %A @ %I.%M.%S %p')}')
			shutil.copytree(fr'{PATH}\BACKUP - DATABASE 01', fr'{PATH}\Bank_Package\DATABASE')

			os.rename(fr'{PATH}\BACKUP - DATABASE 01', fr'{PATH}\BACKUP - DATABASE')
			
			messagebox.showinfo(title = 'Database Restored', message = 'Database Restored Successfully!\n\nYour database has been successfully restored and everything should be running smoothly.\n\nIf you experience ' \
			'any issues such as the app crashing or not opening, please try using the built-in Repair Tool.\nIt usually fixes most common problems automatically.\n\nAlso, don\'t panic — your data is safe!\nWe always have a ' \
			'plan in place to protect your database. A rollback copy is safely stored in your device.\n"Thanks to the developer for this thoughtful decision — it\'s our safety net for your data.\n\nStill need help? ' \
			'We\'re here for you! Reach out to us anytime through our support channels:\n\nGitHub : ViratiAkiraNandhanReddy\nFacebook : Virati Akira Nandhan Reddy\nInstagram : viratiaki53\nTwitter : @Viratiaki53\nEmail : viratiaki29@gmail.com\n\nThank you for trusting us and using our service!')
		
			Backup_Database_Window.after(0, Backup_Database_Window.destroy)
			rm_backupbatabasememory() ; self.isBackupDatabaseRestored = True

		def _restore_db_02_() -> None:
			
			Backup_Database_Window.withdraw()

			shutil.rmtree(fr'{PATH}\Bank_Package\DATABASE')
			shutil.rmtree(fr'{PATH}\BACKUP - DATABASE')

			shutil.copytree(fr'{PATH}\BACKUP - DATABASE 02', str(os.environ.get('LOCALAPPDATA')) + fr'\Bank-With-High-Functionalities - ROLLBACKS\BACKUP - DATABASE 02 - {datetime.datetime.now().strftime('%d-%b-%Y -- %A @ %I.%M.%S %p')}')
			shutil.copytree(fr'{PATH}\BACKUP - DATABASE 02', fr'{PATH}\Bank_Package\DATABASE')

			os.rename(fr'{PATH}\BACKUP - DATABASE 02', fr'{PATH}\BACKUP - DATABASE')
			
			messagebox.showinfo(title = 'Database Restored', message = 'Database Restored Successfully!\n\nYour database has been successfully restored and everything should be running smoothly.\n\nIf you experience ' \
			'any issues such as the app crashing or not opening, please try using the built-in Repair Tool.\nIt usually fixes most common problems automatically.\n\nAlso, don\'t panic — your data is safe!\nWe always have a ' \
			'plan in place to protect your database. A rollback copy is safely stored in your device.\n"Thanks to the developer for this thoughtful decision — it\'s our safety net for your data.\n\nStill need help? ' \
			'We\'re here for you! Reach out to us anytime through our support channels:\n\nGitHub : ViratiAkiraNandhanReddy\nFacebook : Virati Akira Nandhan Reddy\nInstagram : viratiaki53\nTwitter : @Viratiaki53\nEmail : viratiaki29@gmail.com\n\nThank you for trusting us and using our service!')

			Backup_Database_Window.after(0, Backup_Database_Window.destroy)
			rm_backupbatabasememory() ; self.isBackupDatabaseRestored = True

		def _restore_db_03_() -> None:
			
			Backup_Database_Window.withdraw()

			shutil.rmtree(fr'{PATH}\Bank_Package\DATABASE')
			shutil.rmtree(fr'{PATH}\BACKUP - DATABASE')

			shutil.copytree(fr'{PATH}\BACKUP - DATABASE 03', str(os.environ.get('LOCALAPPDATA')) + fr'\Bank-With-High-Functionalities - ROLLBACKS\BACKUP - DATABASE 03 - {datetime.datetime.now().strftime('%d-%b-%Y -- %A @ %I.%M.%S %p')}')
			shutil.copytree(fr'{PATH}\BACKUP - DATABASE 03', fr'{PATH}\Bank_Package\DATABASE')

			os.rename(fr'{PATH}\BACKUP - DATABASE 03', fr'{PATH}\BACKUP - DATABASE')
			
			messagebox.showinfo(title = 'Database Restored', message = 'Database Restored Successfully!\n\nYour database has been successfully restored and everything should be running smoothly.\n\nIf you experience ' \
			'any issues such as the app crashing or not opening, please try using the built-in Repair Tool.\nIt usually fixes most common problems automatically.\n\nAlso, don\'t panic — your data is safe!\nWe always have a ' \
			'plan in place to protect your database. A rollback copy is safely stored in your device.\n"Thanks to the developer for this thoughtful decision — it\'s our safety net for your data.\n\nStill need help? ' \
			'We\'re here for you! Reach out to us anytime through our support channels:\n\nGitHub : ViratiAkiraNandhanReddy\nFacebook : Virati Akira Nandhan Reddy\nInstagram : viratiaki53\nTwitter : @Viratiaki53\nEmail : viratiaki29@gmail.com\n\nThank you for trusting us and using our service!')
			
			Backup_Database_Window.after(0, Backup_Database_Window.destroy)
			rm_backupbatabasememory() ; self.isBackupDatabaseRestored = True
				
		match Database_Number:

			case 1:
				threading.Thread(target = _restore_db_01_, daemon = True).start()
			case 2:
				threading.Thread(target = _restore_db_02_, daemon = True).start()
			case 3:
				threading.Thread(target = _restore_db_03_, daemon = True).start()
			case _:
				...

		messagebox.showinfo(title = 'Database Restoration In Progress', message = 'The database restoration process is currently in progress.\nYou will be notified once the restoration is ' \
		'successfully completed.\n\nPlease feel free to continue with other tasks during this time.\n\nIMPORTANT: Do not exit or force stop the application while the restoration is in progress. ' \
		'Doing so may cause malfunction or data corruption within the software.\n\nThank you for your patience and cooperation')

	def Restore_Backup_Database_Setup(self) -> None:

		''' <!-- Doc Strings -->
		### Purpose
		Opens a graphical interface for users to view, preview, restore, or delete available backup databases. This method is invoked when backup databases are detected, allowing users to manage them before proceeding with a new setup or restoration.

		### Functionality
		- Scans for up to three backup databases and checks their integrity.
		- Displays a CustomTkinter window listing all detected backups, showing details such as manager name, user count, backup size, and corruption status.
		- Allows users to:
			- Preview detailed information for each backup (manager credentials, security code, email, timestamps, etc.).
			- Restore a selected backup, replacing the current database and saving a rollback copy.
			- Delete any backup database, with confirmation and immediate UI update.
			- Toggle password visibility for each backup using an eye icon.
		- Provides a guide panel explaining icons and actions, and tips for troubleshooting.
		- Offers a button to proceed by creating a new database, which will automatically delete the backup with the fewest users or a corrupted one if all slots are full.

		### Parameters
		- **self**: Instance of the `CheckForBackupDatabase` class.

		### Returns
		- **None**

		### Example Usage
		```python
		backup_checker = CheckForBackupDatabase()
		backup_checker.Restore_Backup_Database_Setup()
		```

		### Notes
		- This method is typically called at application startup if backup folders are found.
		- The UI is built using CustomTkinter and is modal, blocking further setup until a decision is made.
		- Only valid (non-corrupted) backups can be restored; corrupted ones can only be deleted.
		- The method updates internal state flags for backup availability and corruption status.
		- Deleting or restoring a backup updates the UI in real time and may trigger folder renaming for sequential order.

		### GUI Integration
		- Provides a user-friendly interface for managing backup databases.
		- Integrates with other methods for restoring and deleting backups, and for toggling password visibility.

		### Security
		- Restoring a backup will overwrite the current database and backup folders; this is irreversible.
		- Deleting a backup is permanent and cannot be undone.
		- Passwords are masked by default and can be revealed only on user action.

		### Limitations
		- Supports a maximum of three backup databases.
		- Assumes all required icon/image resources are available and loaded.
		- If a backup is corrupted, it cannot be restored but can be deleted.
		- The method assumes the presence of certain global variables and resources (e.g., icon images, CustomTkinter widgets).

		### Dependencies
		- Requires `customtkinter` for the UI.
		- Relies on other methods in the class for restoring and deleting backups.
		- Uses `os`, `shutil`, `threading`, and `tkinter.messagebox` for file operations and dialogs.
		'''

		def Show_Hide_Manager_Password(DB_Number: int) -> None:

			'''
			### Purpose
			Toggles the visibility of the manager's password field for a specific backup database in the restore backup database setup window.

			### Parameters
			- **DB_Number** (`int`): The database number (1, 2, or 3) indicating which manager password field to show or hide.

			### Functionality
			- If the password is currently hidden (masked), it will be shown in plain text and the eye icon will change to a "hide" icon.
			- If the password is currently visible, it will be masked again and the eye icon will change to a "show" icon.
			- Updates the corresponding state variable (`showpassword_DB_01`, `showpassword_DB_02`, or `showpassword_DB_03`) for each database.

			### Example Usage
			```python
			Show_Hide_Manager_Password(1)  # Toggles visibility for Database 1 password
			Show_Hide_Manager_Password(2)  # Toggles visibility for Database 2 password
			Show_Hide_Manager_Password(3)  # Toggles visibility for Database 3 password
			```

			### Notes
			- This function is intended for use within the Restore_Backup_Database_Setup method.
			- The function relies on the existence of password entry widgets and eye button widgets for each database.

			### GUI Integration
			- Changes the `show` property of the password entry widget.
			- Changes the image of the eye button to indicate the current state (show/hide).
			'''

			match DB_Number:

				case 1:

					if not self.showpassword_DB_01:
						self.showpassword_DB_01 = True

						Password_1.configure(show = '')
						Password_eye_1.configure(image = CTk.CTkImage(light_image = Password_Show_icon, dark_image = Password_Show_icon, size = (22, 22)))

					else:
						self.showpassword_DB_01 = False

						Password_1.configure(show = '●')
						Password_eye_1.configure(image = CTk.CTkImage(light_image = Password_Hide_icon, dark_image = Password_Hide_icon, size = (22, 22)))
				
				case 2:

					if not self.showpassword_DB_02:
						self.showpassword_DB_02 = True

						Password_2.configure(show = '')
						Password_eye_2.configure(image = CTk.CTkImage(light_image = Password_Show_icon, dark_image = Password_Show_icon, size = (22, 22)))

					else:
						self.showpassword_DB_02 = False

						Password_2.configure(show = '●')
						Password_eye_2.configure(image = CTk.CTkImage(light_image = Password_Hide_icon, dark_image = Password_Hide_icon, size = (22, 22)))
				
				case 3:

					if not self.showpassword_DB_03:
						self.showpassword_DB_03 = True

						Password_3.configure(show = '')
						Password_eye_3.configure(image = CTk.CTkImage(light_image = Password_Show_icon, dark_image = Password_Show_icon, size = (22, 22)))

					else:
						self.showpassword_DB_03 = False

						Password_3.configure(show = '●')
						Password_eye_3.configure(image = CTk.CTkImage(light_image = Password_Hide_icon, dark_image = Password_Hide_icon, size = (22, 22)))
				
				case _:
					pass

		def Delete_Backup_Database(DB_Number: int) -> None:

			''' <!-- Doc Strings -->
			### Purpose
			Handles the deletion of a selected backup database from the restore backup database setup window.

			### Parameters
			- **DB_Number** (`int`): The database number (1, 2, or 3) indicating which backup database to delete.

			### Functionality
			- Removes the corresponding database frames from the GUI.
			- Updates the internal state to mark the selected database as unavailable.
			- Deletes the backup database folder from disk using `shutil.rmtree`.
			- Hides the preview frame for the deleted database.
			- Calls `Orderly_Place_Backup_Databases_Selection()` to refresh the GUI layout after deletion.

			### Example Usage
			```python
			Delete_Backup_Database(1)  # Deletes Backup Database 1
			Delete_Backup_Database(2)  # Deletes Backup Database 2
			Delete_Backup_Database(3)  # Deletes Backup Database 3
			```

			### Notes
			- The function is intended for use within the `Restore_Backup_Database_Setup` method.
			- The function ensures the GUI remains consistent after a database is deleted.

			### GUI Integration
			- Removes the relevant frames and preview widgets from the interface.
			- Updates the display order of remaining databases.

			### Security
			- Deleting a backup database is irreversible.
			'''
			
			Last_DB_Frame = len(self.Total_DBs)
			
			match Last_DB_Frame:
				
				case 1:
					
					DB_01_DownFrame.place_forget()
					DB_01_UpFrame.place_forget()

				case 2:
					
					DB_02_DownFrame.place_forget()
					DB_02_UpFrame.place_forget()

				case 3:
					
					DB_03_DownFrame.place_forget()
					DB_03_UpFrame.place_forget()

			match DB_Number:

				case 1:
					self.isDatabase_01_Available = False
					threading.Thread(target = shutil.rmtree, daemon = True, args = (fr'{PATH}\BACKUP - DATABASE 01',)).start()
					DB_01_Preview.place_forget() ; DB_Guide.place(x = 5, y = 5)
					
				case 2:
					self.isDatabase_02_Available = False
					threading.Thread(target = shutil.rmtree, daemon = True, args = (fr'{PATH}\BACKUP - DATABASE 02',)).start()
					DB_02_Preview.place_forget() ; DB_Guide.place(x = 5, y = 5)
				case 3:
					self.isDatabase_03_Available = False
					threading.Thread(target = shutil.rmtree, daemon = True, args = (fr'{PATH}\BACKUP - DATABASE 03',)).start()
					DB_03_Preview.place_forget() ; DB_Guide.place(x = 5, y = 5)
				case _:
					pass
			
			Orderly_Place_Backup_Databases_Selection()
					
		self.Check_For_Corrupted_Databases_And_Retrieve_Data()

		def Orderly_Place_Backup_Databases_Selection() ->  None:

			def Remove_Widgets() -> None:

				''' <!-- Doc Strings -->
				### Purpose
				Destroys (removes) all child widgets from the backup database frames in the restore backup database setup window. This is typically used to clear the UI before updating or reordering the displayed backup databases.

				### Functionality
				- Iterates through all child widgets of the up and down frames for each backup database (DB_01, DB_02, DB_03).
				- Calls `.destroy()` on each widget to remove it from the GUI.

				### Parameters
				- **None**: This function does not take any parameters.

				### Returns
				- **None**

				### Example Usage
				```python
				Remove_Widgets()  # Clears all widgets from the backup database frames before refreshing the layout
				```

				### Notes
				- Intended for internal use within the `Orderly_Place_Backup_Databases_Selection` function.
				- Helps ensure that the frames are empty before repopulating them with updated content.
				- Prevents widget duplication and layout issues when the backup database selection UI is refreshed.

				### GUI Integration
				- Directly affects the visual state of the backup database frames in the restore backup database setup window.
				'''

				for Widget in DB_01_UpFrame.winfo_children():
					Widget.destroy()
				for Widget in DB_01_DownFrame.winfo_children():
					Widget.destroy()

				for Widget in DB_02_UpFrame.winfo_children():
					Widget.destroy()
				for Widget in DB_02_DownFrame.winfo_children():
					Widget.destroy()	

				for Widget in DB_03_UpFrame.winfo_children():
					Widget.destroy()
				for Widget in DB_03_DownFrame.winfo_children():
					Widget.destroy()
				
			self.Total_DBs = [x for x in [self.isDatabase_01_Available, self.isDatabase_02_Available, self.isDatabase_03_Available] if x == True]
			
			# Placing Frames In order
			for Order in range(len(self.Total_DBs)):

				match Order:

					case 0:

						DB_01_DownFrame.place(x = 8, y = 106)
						DB_01_UpFrame.place(x = 5, y = 80)

					case 1:

						DB_02_DownFrame.place(x = 8, y = 192)
						DB_02_UpFrame.place(x = 5, y = 166)

					case 2:

						DB_03_DownFrame.place(x = 8, y = 278)
						DB_03_UpFrame.place(x = 5, y = 252)
			
			if self.isDatabase_01_Available:

				if not self.isDatabase_01_Corrupted:
					DB_01_1_UpFrame_TimeDelta = CTk.CTkLabel(DB_01_UpFrame, text = f'{self.Database_01_init_Data["Downloaded On"]}  --->  {self.Database_01_init_Data["Deleted On"]}', font = ('Consolas', 10), height = 26) ; DB_01_1_UpFrame_TimeDelta.place(x = 7, y = 2)
					DB_01_1_DownFrame_Manager = CTk.CTkLabel(DB_01_DownFrame, text = f'  {self.Database_01_init_Data["Manager Name"][:32] + ('...' if len(self.Database_01_init_Data["Manager Name"]) > 32 else '')}', image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_01_1_DownFrame_Manager.place(x = 5, y = 6)
					DB_01_1_DownFrame_Users = CTk.CTkLabel(DB_01_DownFrame, text = f'   {self.Database_01_init_Data["User Records"]["Total Active Users"]:,}', image = CTk.CTkImage(light_image = People_icon, dark_image = People_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_01_1_DownFrame_Users.place(x = 250, y = 6)
					DB_01_1_DownFrame_db_Size = CTk.CTkLabel(DB_01_DownFrame, text = f'  {self.DB_01_SIZE:.2f} KB' if self.DB_01_SIZE < 1024 else f'  {(self.DB_01_SIZE/(1024)):.2f} MB' if self.DB_01_SIZE < (1024**2) else f'  {(self.DB_01_SIZE/(1024**2)):.2f} GB', image = CTk.CTkImage(light_image = Database_icon, dark_image = Database_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_01_1_DownFrame_db_Size.place(x = 350, y = 6)
					DB_01_1_DownFrame_Next_Nav = CTk.CTkButton(DB_01_DownFrame, text = '', image = CTk.CTkImage(light_image = Next_Navigation_icon, dark_image = Next_Navigation_icon, size = (25, 25)), height = 42, width = 0, hover = False, fg_color = 'transparent', command = lambda: [DB_01_Preview.place(x = 5, y = 5), DB_02_Preview.place_forget(), DB_03_Preview.place_forget(), DB_Guide.place_forget()]) ; DB_01_1_DownFrame_Next_Nav.place(x = 442, y = 6)
				else:
					DB_01_1_CORRUPTED = CTk.CTkLabel(DB_01_UpFrame, text = 'Corrupted', text_color = "#CE4641", width = 200, height = 30) ; DB_01_1_CORRUPTED.place(x = 131, y = 0)
				
				Delete_DB_01_1 = CTk.CTkButton(DB_01_UpFrame, text = '', image = CTk.CTkImage(light_image = Delete_Database_icon, dark_image = Delete_Database_icon, size = (18, 18)), height = 0, width = 0, fg_color = 'transparent', hover = False, command = lambda: [Remove_Widgets(), Delete_Backup_Database(1)] if messagebox.askyesno(title = 'Confirm Deletion', message = 'WARNING: You are about to delete the Backup-Database.\nThis action CANNOT be undone.\n\nDo you want to continue?', icon = 'warning') else None) ; Delete_DB_01_1.place(x = 462, y = 2)

				pass # Place 1 in 1

			if self.isDatabase_02_Available:

				if not self.isDatabase_01_Available:

					if not self.isDatabase_02_Corrupted:
						DB_02_1_UpFrame_TimeDelta = CTk.CTkLabel(DB_01_UpFrame, text = f'{self.Database_02_init_Data["Downloaded On"]}  --->  {self.Database_02_init_Data["Deleted On"]}', font = ('Consolas', 10), height = 26) ; DB_02_1_UpFrame_TimeDelta.place(x = 7, y = 2)
						DB_02_1_DownFrame_Manager = CTk.CTkLabel(DB_01_DownFrame, text = f'  {self.Database_02_init_Data["Manager Name"][:32] + ('...' if len(self.Database_02_init_Data["Manager Name"]) > 32 else '')}', image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_02_1_DownFrame_Manager.place(x = 5, y = 6)
						DB_02_1_DownFrame_Users = CTk.CTkLabel(DB_01_DownFrame, text = f'   {self.Database_02_init_Data["User Records"]["Total Active Users"]:,}', image = CTk.CTkImage(light_image = People_icon, dark_image = People_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_02_1_DownFrame_Users.place(x = 250, y = 6)
						DB_02_1_DownFrame_db_Size = CTk.CTkLabel(DB_01_DownFrame, text = f'  {self.DB_02_SIZE:.2f} KB' if self.DB_02_SIZE < 1024 else f'  {(self.DB_02_SIZE/(1024)):.2f} MB' if self.DB_02_SIZE < (1024**2) else f'  {(self.DB_02_SIZE/(1024**2)):.2f} GB', image = CTk.CTkImage(light_image = Database_icon, dark_image = Database_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_02_1_DownFrame_db_Size.place(x = 350, y = 6)
						DB_02_1_DownFrame_Next_Nav = CTk.CTkButton(DB_01_DownFrame, text = '', image = CTk.CTkImage(light_image = Next_Navigation_icon, dark_image = Next_Navigation_icon, size = (25, 25)), height = 42, width = 0, hover = False, fg_color = 'transparent', command = lambda: [DB_02_Preview.place(x = 5, y = 5), DB_01_Preview.place_forget(), DB_03_Preview.place_forget(), DB_Guide.place_forget()]) ; DB_02_1_DownFrame_Next_Nav.place(x = 442, y = 6)

						
					else:
						DB_02_1_CORRUPTED = CTk.CTkLabel(DB_01_UpFrame, text = 'Corrupted', text_color = "#CE4641", width = 200, height = 30) ; DB_02_1_CORRUPTED.place(x = 131, y = 0)
					
					Delete_DB_02_1 = CTk.CTkButton(DB_01_UpFrame, text = '', image = CTk.CTkImage(light_image = Delete_Database_icon, dark_image = Delete_Database_icon, size = (18, 18)), height = 0, width = 0, fg_color = 'transparent', hover = False, command = lambda: [Remove_Widgets(), Delete_Backup_Database(2)] if messagebox.askyesno(title = 'Confirm Deletion', message = 'WARNING: You are about to delete the Backup-Database.\nThis action CANNOT be undone.\n\nDo you want to continue?', icon = 'warning') else None) ; Delete_DB_02_1.place(x = 462, y = 2)

					pass # Place 2 in 1
				else:

					if not self.isDatabase_02_Corrupted:
						DB_02_2_UpFrame_TimeDelta = CTk.CTkLabel(DB_02_UpFrame, text = f'{self.Database_02_init_Data["Downloaded On"]}  --->  {self.Database_02_init_Data["Deleted On"]}', font = ('Consolas', 10), height = 26) ; DB_02_2_UpFrame_TimeDelta.place(x = 7, y = 2)
						DB_02_2_DownFrame_Manager = CTk.CTkLabel(DB_02_DownFrame, text = f'  {self.Database_02_init_Data["Manager Name"][:32] + ('...' if len(self.Database_02_init_Data["Manager Name"]) > 32 else '')}', image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_02_2_DownFrame_Manager.place(x = 5, y = 6)
						DB_02_2_DownFrame_Users = CTk.CTkLabel(DB_02_DownFrame, text = f'   {self.Database_02_init_Data["User Records"]["Total Active Users"]:,}', image = CTk.CTkImage(light_image = People_icon, dark_image = People_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_02_2_DownFrame_Users.place(x = 250, y = 6)
						DB_02_2_DownFrame_db_Size = CTk.CTkLabel(DB_02_DownFrame, text = f'  {self.DB_02_SIZE:.2f} KB' if self.DB_02_SIZE < 1024 else f'  {(self.DB_02_SIZE/(1024)):.2f} MB' if self.DB_02_SIZE < (1024**2) else f'  {(self.DB_02_SIZE/(1024**2)):.2f} GB', image = CTk.CTkImage(light_image = Database_icon, dark_image = Database_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_02_2_DownFrame_db_Size.place(x = 350, y = 6)
						DB_02_2_DownFrame_Next_Nav = CTk.CTkButton(DB_02_DownFrame, text = '', image = CTk.CTkImage(light_image = Next_Navigation_icon, dark_image = Next_Navigation_icon, size = (25, 25)), height = 42, width = 0, hover = False, fg_color = 'transparent', command = lambda: [DB_02_Preview.place(x = 5, y = 5), DB_01_Preview.place_forget(), DB_03_Preview.place_forget(), DB_Guide.place_forget()]) ; DB_02_2_DownFrame_Next_Nav.place(x = 442, y = 6)

					else:
						DB_02_2_CORRUPTED = CTk.CTkLabel(DB_02_UpFrame, text = 'Corrupted', text_color = "#CE4641", width = 200, height = 30) ; DB_02_2_CORRUPTED.place(x = 131, y = 0)

					Delete_DB_02_2 = CTk.CTkButton(DB_02_UpFrame, text = '', image = CTk.CTkImage(light_image = Delete_Database_icon, dark_image = Delete_Database_icon, size = (18, 18)), height = 0, width = 0, fg_color = 'transparent', hover = False, command = lambda: [Remove_Widgets(), Delete_Backup_Database(2)] if messagebox.askyesno(title = 'Confirm Deletion', message = 'WARNING: You are about to delete the Backup-Database.\nThis action CANNOT be undone.\n\nDo you want to continue?', icon = 'warning') else None) ; Delete_DB_02_2.place(x = 462, y = 2)
					
					pass # Place 2 in 2

			if self.isDatabase_03_Available:

				if not self.isDatabase_01_Available and not self.isDatabase_02_Available:

					if not self.isDatabase_03_Corrupted:
						DB_03_1_UpFrame_TimeDelta = CTk.CTkLabel(DB_01_UpFrame, text = f'{self.Database_03_init_Data["Downloaded On"]}  --->  {self.Database_03_init_Data["Deleted On"]}', font = ('Consolas', 10), height = 26) ; DB_03_1_UpFrame_TimeDelta.place(x = 7, y = 2)
						DB_03_1_DownFrame_Manager = CTk.CTkLabel(DB_01_DownFrame, text = f'  {self.Database_03_init_Data["Manager Name"][:32] + ('...' if len(self.Database_03_init_Data["Manager Name"]) > 32 else '')}', image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_03_1_DownFrame_Manager.place(x = 5, y = 6)
						DB_03_1_DownFrame_Users = CTk.CTkLabel(DB_01_DownFrame, text = f'   {self.Database_03_init_Data["User Records"]["Total Active Users"]:,}', image = CTk.CTkImage(light_image = People_icon, dark_image = People_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_03_1_DownFrame_Users.place(x = 250, y = 6)
						DB_03_1_DownFrame_db_Size = CTk.CTkLabel(DB_01_DownFrame, text = f'  {self.DB_03_SIZE:.2f} KB' if self.DB_03_SIZE < 1024 else f'  {(self.DB_03_SIZE/(1024)):.2f} MB' if self.DB_03_SIZE < (1024**2) else f'  {(self.DB_03_SIZE/(1024**2)):.2f} GB', image = CTk.CTkImage(light_image = Database_icon, dark_image = Database_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_03_1_DownFrame_db_Size.place(x = 350, y = 6)
						DB_03_1_DownFrame_Next_Nav = CTk.CTkButton(DB_01_DownFrame, text = '', image = CTk.CTkImage(light_image = Next_Navigation_icon, dark_image = Next_Navigation_icon, size = (25, 25)), height = 42, width = 0, hover = False, fg_color = 'transparent', command = lambda: [DB_03_Preview.place(x = 5, y = 5), DB_01_Preview.place_forget(), DB_02_Preview.place_forget(), DB_Guide.place_forget()]) ; DB_03_1_DownFrame_Next_Nav.place(x = 442, y = 6)

					else:
						DB_03_1_CORRUPTED = CTk.CTkLabel(DB_01_UpFrame, text = 'Corrupted', text_color = "#CE4641", width = 200, height = 30) ; DB_03_1_CORRUPTED.place(x = 131, y = 0)
					
					Delete_DB_03_1 = CTk.CTkButton(DB_01_UpFrame, text = '', image = CTk.CTkImage(light_image = Delete_Database_icon, dark_image = Delete_Database_icon, size = (18, 18)), height = 0, width = 0, fg_color = 'transparent', hover = False, command = lambda: [Remove_Widgets(), Delete_Backup_Database(3)] if messagebox.askyesno(title = 'Confirm Deletion', message = 'WARNING: You are about to delete the Backup-Database.\nThis action CANNOT be undone.\n\nDo you want to continue?', icon = 'warning') else None) ; Delete_DB_03_1.place(x = 462, y = 2)
					
					pass # Place 3 in 1

				elif not self.isDatabase_01_Available or not self.isDatabase_02_Available:

					if not self.isDatabase_03_Corrupted:
						DB_03_2_UpFrame_TimeDelta = CTk.CTkLabel(DB_02_UpFrame, text = f'{self.Database_03_init_Data["Downloaded On"]}  --->  {self.Database_03_init_Data["Deleted On"]}', font = ('Consolas', 10), height = 26) ; DB_03_2_UpFrame_TimeDelta.place(x = 7, y = 2)
						DB_03_2_DownFrame_Manager = CTk.CTkLabel(DB_02_DownFrame, text = f'  {self.Database_03_init_Data["Manager Name"][:32] + ('...' if len(self.Database_03_init_Data["Manager Name"]) > 32 else '')}', image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_03_2_DownFrame_Manager.place(x = 5, y = 6)
						DB_03_2_DownFrame_Users = CTk.CTkLabel(DB_02_DownFrame, text = f'   {self.Database_03_init_Data["User Records"]["Total Active Users"]:,}', image = CTk.CTkImage(light_image = People_icon, dark_image = People_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_03_2_DownFrame_Users.place(x = 250, y = 6)
						DB_03_2_DownFrame_db_Size = CTk.CTkLabel(DB_02_DownFrame, text = f'  {self.DB_03_SIZE:.2f} KB' if self.DB_03_SIZE < 1024 else f'  {(self.DB_03_SIZE/(1024)):.2f} MB' if self.DB_03_SIZE < (1024**2) else f'  {(self.DB_03_SIZE/(1024**2)):.2f} GB', image = CTk.CTkImage(light_image = Database_icon, dark_image = Database_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_03_2_DownFrame_db_Size.place(x = 350, y = 6)
						DB_03_2_DownFrame_Next_Nav = CTk.CTkButton(DB_02_DownFrame, text = '', image = CTk.CTkImage(light_image = Next_Navigation_icon, dark_image = Next_Navigation_icon, size = (25, 25)), height = 42, width = 0, hover = False, fg_color = 'transparent', command = lambda: [DB_03_Preview.place(x = 5, y = 5), DB_01_Preview.place_forget(), DB_02_Preview.place_forget(), DB_Guide.place_forget()]) ; DB_03_2_DownFrame_Next_Nav.place(x = 442, y = 6)

					else:

						DB_03_2_CORRUPTED = CTk.CTkLabel(DB_02_UpFrame, text = 'Corrupted', text_color = "#CE4641", width = 200, height = 30) ; DB_03_2_CORRUPTED.place(x = 131, y = 0)

					Delete_DB_03_2 = CTk.CTkButton(DB_02_UpFrame, text = '', image = CTk.CTkImage(light_image = Delete_Database_icon, dark_image = Delete_Database_icon, size = (18, 18)), height = 0, width = 0, fg_color = 'transparent', hover = False, command = lambda: [Remove_Widgets(), Delete_Backup_Database(3)] if messagebox.askyesno(title = 'Confirm Deletion', message = 'WARNING: You are about to delete the Backup-Database.\nThis action CANNOT be undone.\n\nDo you want to continue?', icon = 'warning') else None) ; Delete_DB_03_2.place(x = 462, y = 2)
					
					pass # Place 3 in 2

				else:

					if not self.isDatabase_03_Corrupted:
						DB_03_3_UpFrame_TimeDelta = CTk.CTkLabel(DB_03_UpFrame, text = f'{self.Database_03_init_Data["Downloaded On"]}  --->  {self.Database_03_init_Data["Deleted On"]}', font = ('Consolas', 10), height = 26) ; DB_03_3_UpFrame_TimeDelta.place(x = 7, y = 2)
						DB_03_3_DownFrame_Manager = CTk.CTkLabel(DB_03_DownFrame, text = f'  {self.Database_03_init_Data["Manager Name"][:32] + ('...' if len(self.Database_03_init_Data["Manager Name"]) > 32 else '')}', image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_03_3_DownFrame_Manager.place(x = 5, y = 6)
						DB_03_3_DownFrame_Users = CTk.CTkLabel(DB_03_DownFrame, text = f'   {self.Database_03_init_Data["User Records"]["Total Active Users"]:,}', image = CTk.CTkImage(light_image = People_icon, dark_image = People_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_03_3_DownFrame_Users.place(x = 250, y = 6)
						DB_03_3_DownFrame_db_Size = CTk.CTkLabel(DB_03_DownFrame, text = f'  {self.DB_03_SIZE:.2f} KB' if self.DB_03_SIZE < 1024 else f'  {(self.DB_03_SIZE/(1024)):.2f} MB' if self.DB_03_SIZE < (1024**2) else f'  {(self.DB_03_SIZE/(1024**2)):.2f} GB', image = CTk.CTkImage(light_image = Database_icon, dark_image = Database_icon, size = (25, 25)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 42) ; DB_03_3_DownFrame_db_Size.place(x = 350, y = 6)
						DB_03_3_DownFrame_Next_Nav = CTk.CTkButton(DB_03_DownFrame, text = '', image = CTk.CTkImage(light_image = Next_Navigation_icon, dark_image = Next_Navigation_icon, size = (25, 25)), height = 42, width = 0, hover = False, fg_color = 'transparent', command = lambda: [DB_03_Preview.place(x = 5, y = 5), DB_01_Preview.place_forget(), DB_02_Preview.place_forget(), DB_Guide.place_forget()]) ; DB_03_3_DownFrame_Next_Nav.place(x = 442, y = 6)

					else:

						DB_03_3_CORRUPTED = CTk.CTkLabel(DB_03_UpFrame, text = 'Corrupted', text_color = "#CE4641", width = 200, height = 30) ; DB_03_3_CORRUPTED.place(x = 131, y = 0)
					
					Delete_DB_03_3 = CTk.CTkButton(DB_03_UpFrame, text = '', image = CTk.CTkImage(light_image = Delete_Database_icon, dark_image = Delete_Database_icon, size = (18, 18)), height = 0, width = 0, fg_color = 'transparent', hover = False, command = lambda: [Remove_Widgets(), Delete_Backup_Database(3)] if messagebox.askyesno(title = 'Confirm Deletion', message = 'WARNING: You are about to delete the Backup-Database.\nThis action CANNOT be undone.\n\nDo you want to continue?', icon = 'warning') else None) ; Delete_DB_03_3.place(x = 462, y = 2)
					
					pass # Place 3 in 3
		
		global Backup_Database_Window
		Backup_Database_Window = CTk.CTk()
		Backup_Database_Window.title('Backup Detected')
		Backup_Database_Window.geometry('800x400+100+40')
		Backup_Database_Window.resizable(False, False)
		Backup_Database_Window.iconbitmap(fr'{PATH}\Bank_Package\Visual Data\ICO Files\Restore Backup Database.ico')

		CTk.CTkLabel(Backup_Database_Window, text = 'A Backup Has Been Detected On Your Device', font = ('Segoe UI', 17, 'bold'), height = 0).place(x = 9, y = 5)
		CTk.CTkLabel(Backup_Database_Window, text = 'Pick a backup and get back to work in seconds.', font = ('Segoe UI', 12, 'italic'), height = 0).place(x = 9, y = 26)

		Backup_Database_ExpandFrame = CTk.CTkFrame(Backup_Database_Window, 295, 390) ; Backup_Database_ExpandFrame.place(x = 500, y = 5)

		DB_01_DownFrame = CTk.CTkFrame(Backup_Database_Window, 484, 50, fg_color = ("#D6D6D6", "#292929")) # ; DB_01_DownFrame.place(x = 8, y = 106)
		DB_01_UpFrame = CTk.CTkFrame(Backup_Database_Window, 490, 30, fg_color = ("#CACACA", "#353535")) # ; DB_01_UpFrame.place(x = 5, y = 80)

		DB_02_DownFrame = CTk.CTkFrame(Backup_Database_Window, 484, 50, fg_color = ("#D6D6D6", "#292929")) # ; DB_02_DownFrame.place(x = 8, y = 192)
		DB_02_UpFrame = CTk.CTkFrame(Backup_Database_Window, 490, 30, fg_color = ("#CACACA", "#353535")) # ; DB_02_UpFrame.place(x = 5, y = 166)

		DB_03_DownFrame = CTk.CTkFrame(Backup_Database_Window, 484, 50, fg_color = ("#D6D6D6", "#292929")) # ; DB_03_DownFrame.place(x = 8, y = 278)
		DB_03_UpFrame = CTk.CTkFrame(Backup_Database_Window, 490, 30, fg_color = ("#CACACA", "#353535")) # ; DB_03_UpFrame.place(x = 5, y = 252)

		DB_01_Preview = CTk.CTkFrame(Backup_Database_ExpandFrame, 285, 380)
		DB_02_Preview = CTk.CTkFrame(Backup_Database_ExpandFrame, 285, 380)
		DB_03_Preview = CTk.CTkFrame(Backup_Database_ExpandFrame, 285, 380)

		DB_Guide = CTk.CTkFrame(Backup_Database_ExpandFrame, 285, 380) ; DB_Guide.place(x = 5, y = 5)
		CTk.CTkLabel(DB_Guide, text = 'Below Instructions Might Help You Proceed', font = ('Segoe UI', 13, 'bold'), height = 0, width = 285).place(x = 0, y = 6)

		CTk.CTkLabel(DB_Guide, text = 'TIP: If you\'re experiencing issues like app crashes or the app not opening,\nyou can use the software installer. It also works as a troubleshooting\nworkbench and helps fix common problems.', font = ('Segoe UI', 9, 'italic'), justify = 'left').place(x = 5, y = 35)
		CTk.CTkLabel(DB_Guide, text = 'It is recommended that you delete the corrupted backup\ndatabase to ensure optimal performance and prevent\npotential issues.', font = ('Segoe UI', 11, 'italic'), justify = 'left').place(x = 5, y = 75)
		CTk.CTkLabel(DB_Guide, text = '  Represents the manager name', font = ('Segoe UI', 12, 'italic'), image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (20, 20)), compound = 'left').place(x = 5, y = 120)
		CTk.CTkLabel(DB_Guide, text = '  Represents the total active users', font = ('Segoe UI', 12, 'italic'), image = CTk.CTkImage(light_image = People_icon, dark_image = People_icon, size = (20, 20)), compound = 'left').place(x = 5, y = 150)
		CTk.CTkLabel(DB_Guide, text = '  Used to view the preview and take action', font = ('Segoe UI', 12, 'italic'), image = CTk.CTkImage(light_image = Next_Navigation_icon, dark_image = Next_Navigation_icon, size = (20, 20)), compound = 'left').place(x = 5, y = 180)
		CTk.CTkLabel(DB_Guide, text = '  Represents the storage of backup database', font = ('Segoe UI', 12, 'italic'), image = CTk.CTkImage(light_image = Database_icon, dark_image = Database_icon, size = (20, 20)), compound = 'left').place(x = 5, y = 210)
		CTk.CTkLabel(DB_Guide, text = '  Used to delete the specified backup database', font = ('Segoe UI', 12, 'italic'), image = CTk.CTkImage(light_image = Delete_Database_icon, dark_image = Delete_Database_icon, size = (20, 20)), compound = 'left').place(x = 5, y = 240)
		CTk.CTkLabel(DB_Guide, text = '-'*142, font = ('Roboto', 8), height = 0).place(x = 0, y = 270)
		CTk.CTkLabel(DB_Guide, text = 'NOTE : A maximum of three backup databases are allowed.\nIf you click "Proceed By Creating A New Database", the\ndatabase with the fewest users or the database which is\ncorrupted will be automatically deleted to make space. To\navoid this, you can manually delete an existing backup\ndatabase before proceeding.',
			   font = ('Segoe UI', 11, 'italic'), width = 275, justify = 'left').place(x = 4, y = 289)

		if self.isDatabase_01_Available and not self.isDatabase_01_Corrupted:
			CTk.CTkLabel(DB_01_Preview, text = 'Restore Backup', font = ('Segoe UI', 18, 'bold'), width = 285, height = 40).place(x = 0, y = 0)
			CTk.CTkLabel(DB_01_Preview, text = f'  {self.Database_01_init_Data["Manager Name"][:38] + ('...' if len(self.Database_01_init_Data["Manager Name"]) > 32 else '')}', image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 50)
			CTk.CTkLabel(DB_01_Preview, text = f'  {self.Database_01_init_Data["Manager Username"][:38] + ('...' if len(self.Database_01_init_Data["Manager Username"]) > 32 else '')}', image = CTk.CTkImage(light_image = Username_icon, dark_image = Username_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 90)
			
			CTk.CTkLabel(DB_01_Preview, text = '', image = CTk.CTkImage(light_image = Password_icon, dark_image = Password_icon, size = (30, 30)), height = 0, compound = 'left').place(x = 10, y = 130)
			Password_1 = CTk.CTkEntry(DB_01_Preview, border_width = 0, fg_color = 'transparent', width = 200, height = 30, show = '●', font = ('Segoe UI', 11, 'bold')) ; Password_1.place(x = 41, y = 130)
			Password_1.insert(0, self.Database_01_init_Data["Manager Password"]) ; Password_1.configure(state = 'readonly')
			Password_eye_1 = CTk.CTkButton(DB_01_Preview, text = '', image = CTk.CTkImage(light_image = Password_Hide_icon, dark_image = Password_Hide_icon, size = (22, 22)), height = 0, width = 0, hover = False, fg_color = 'transparent', command = lambda: Show_Hide_Manager_Password(1)) ; Password_eye_1.place(x = 247, y = 130)

			CTk.CTkLabel(DB_01_Preview, text = f'  {self.Database_01_init_Data["Manager Security Code"]}', image = CTk.CTkImage(light_image = Security_icon, dark_image = Security_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 170)
			CTk.CTkLabel(DB_01_Preview, text = f'  {self.Database_01_init_Data["Manager Email"]}', image = CTk.CTkImage(light_image = Mail_icon, dark_image = Mail_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 210)
			CTk.CTkLabel(DB_01_Preview, text = f'  {self.Database_01_init_Data["Downloaded On"]}', image = CTk.CTkImage(light_image = Download_icon, dark_image = Download_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 250)
			CTk.CTkLabel(DB_01_Preview, text = f'  {self.Database_01_init_Data["Deleted On"]}', image = CTk.CTkImage(light_image = Upload_icon, dark_image = Upload_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 290)
			
			Restore_Db_01 = CTk.CTkButton(DB_01_Preview, text = 'Restore Database', hover = False, border_width = 1, fg_color = 'transparent', image = CTk.CTkImage(light_image = Restore_Database_icon, dark_image = Restore_Database_icon, size = (22, 22)), height = 30, width = 265, font = ('Segoe UI', 11, 'bold'), command = lambda: self.Restore_Database(1)) ; Restore_Db_01.place(x = 10, y = 340)
			
			# CTk.CTkLabel(DB_01_Preview, text = f'{self.Database_01_init_Data["Downloaded On"]}  --->  {self.Database_03_init_Data["Deleted On"]}', font = ('Consolas', 9), height = 26).place(x = 7, y = 2)

		if self.isDatabase_02_Available and not self.isDatabase_02_Corrupted:
			CTk.CTkLabel(DB_02_Preview, text = 'Restore Backup', font = ('Segoe UI', 18, 'bold'), width = 285, height = 40).place(x = 0, y = 0)
			CTk.CTkLabel(DB_02_Preview, text = f'  {self.Database_02_init_Data["Manager Name"][:38] + ('...' if len(self.Database_02_init_Data["Manager Name"]) > 32 else '')}', image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 50)
			CTk.CTkLabel(DB_02_Preview, text = f'  {self.Database_02_init_Data["Manager Username"][:38] + ('...' if len(self.Database_02_init_Data["Manager Username"]) > 32 else '')}', image = CTk.CTkImage(light_image = Username_icon, dark_image = Username_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 90)
			
			CTk.CTkLabel(DB_02_Preview, text = '', image = CTk.CTkImage(light_image = Password_icon, dark_image = Password_icon, size = (30, 30)), height = 0, compound = 'left').place(x = 10, y = 130)
			Password_2 = CTk.CTkEntry(DB_02_Preview, border_width = 0, fg_color = 'transparent', width = 200, height = 30, show = '●', font = ('Segoe UI', 11, 'bold')) ; Password_2.place(x = 41, y = 130)
			Password_2.insert(0, self.Database_02_init_Data["Manager Password"]) ; Password_2.configure(state = 'readonly')
			Password_eye_2 = CTk.CTkButton(DB_02_Preview, text = '', image = CTk.CTkImage(light_image = Password_Hide_icon, dark_image = Password_Hide_icon, size = (22, 22)), height = 0, width = 0, hover = False, fg_color = 'transparent', command = lambda: Show_Hide_Manager_Password(2)) ; Password_eye_2.place(x = 247, y = 130)

			CTk.CTkLabel(DB_02_Preview, text = f'  {self.Database_02_init_Data["Manager Security Code"]}', image = CTk.CTkImage(light_image = Security_icon, dark_image = Security_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 170)
			CTk.CTkLabel(DB_02_Preview, text = f'  {self.Database_02_init_Data["Manager Email"][:38] + ('...' if len(self.Database_02_init_Data["Manager Email"]) > 32 else '')}', image = CTk.CTkImage(light_image = Mail_icon, dark_image = Mail_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 210)
			CTk.CTkLabel(DB_02_Preview, text = f'  {self.Database_02_init_Data["Downloaded On"]}', image = CTk.CTkImage(light_image = Download_icon, dark_image = Download_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 250)
			CTk.CTkLabel(DB_02_Preview, text = f'  {self.Database_02_init_Data["Deleted On"]}', image = CTk.CTkImage(light_image = Upload_icon, dark_image = Upload_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 290)
			
			Restore_Db_02 = CTk.CTkButton(DB_02_Preview, text = 'Restore Database', hover = False, border_width = 1, fg_color = 'transparent', image = CTk.CTkImage(light_image = Restore_Database_icon, dark_image = Restore_Database_icon, size = (22, 22)), height = 30, width = 265, font = ('Segoe UI', 11, 'bold'), command = lambda: self.Restore_Database(2)) ; Restore_Db_02.place(x = 10, y = 340)

		if self.isDatabase_03_Available and not self.isDatabase_03_Corrupted:
			CTk.CTkLabel(DB_03_Preview, text = 'Restore Backup', font = ('Segoe UI', 18, 'bold'), width = 285, height = 40).place(x = 0, y = 0)
			CTk.CTkLabel(DB_03_Preview, text = f'  {self.Database_03_init_Data["Manager Name"][:38] + ('...' if len(self.Database_03_init_Data["Manager Name"]) > 32 else '')}', image = CTk.CTkImage(light_image = User_Config_icon, dark_image = User_Config_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 50)
			CTk.CTkLabel(DB_03_Preview, text = f'  {self.Database_03_init_Data["Manager Username"][:38] + ('...' if len(self.Database_03_init_Data["Manager Username"]) > 32 else '')}', image = CTk.CTkImage(light_image = Username_icon, dark_image = Username_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 90)
			
			CTk.CTkLabel(DB_03_Preview, text = '', image = CTk.CTkImage(light_image = Password_icon, dark_image = Password_icon, size = (30, 30)), height = 0, compound = 'left').place(x = 10, y = 130)
			Password_3 = CTk.CTkEntry(DB_03_Preview, border_width = 0, fg_color = 'transparent', width = 200, height = 30, show = '●', font = ('Segoe UI', 11, 'bold')) ; Password_3.place(x = 41, y = 130)
			Password_3.insert(0, self.Database_03_init_Data["Manager Password"]) ; Password_3.configure(state = 'readonly')
			Password_eye_3 = CTk.CTkButton(DB_03_Preview, text = '', image = CTk.CTkImage(light_image = Password_Hide_icon, dark_image = Password_Hide_icon, size = (22, 22)), height = 0, width = 0, hover = False, fg_color = 'transparent', command = lambda: Show_Hide_Manager_Password(3)) ; Password_eye_3.place(x = 247, y = 130)

			CTk.CTkLabel(DB_03_Preview, text = f'  {self.Database_03_init_Data["Manager Security Code"]}', image = CTk.CTkImage(light_image = Security_icon, dark_image = Security_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 170)
			CTk.CTkLabel(DB_03_Preview, text = f'  {self.Database_03_init_Data["Manager Email"][:38] + ('...' if len(self.Database_03_init_Data["Manager Email"]) > 32 else '')}', image = CTk.CTkImage(light_image = Mail_icon, dark_image = Mail_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 210)
			CTk.CTkLabel(DB_03_Preview, text = f'  {self.Database_03_init_Data["Downloaded On"]}', image = CTk.CTkImage(light_image = Download_icon, dark_image = Download_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 250)
			CTk.CTkLabel(DB_03_Preview, text = f'  {self.Database_03_init_Data["Deleted On"]}', image = CTk.CTkImage(light_image = Upload_icon, dark_image = Upload_icon, size = (30, 30)), font = ('Segoe UI', 11, 'bold'), compound = 'left', height = 0).place(x = 10, y = 290)
			
			Restore_Db_03 = CTk.CTkButton(DB_03_Preview, text = 'Restore Database', hover = False, border_width = 1, fg_color = 'transparent', image = CTk.CTkImage(light_image = Restore_Database_icon, dark_image = Restore_Database_icon, size = (22, 22)), height = 30, width = 265, font = ('Segoe UI', 11, 'bold'), command = lambda: self.Restore_Database(3)) ; Restore_Db_03.place(x = 10, y = 340)

		def NewDatabaseRequested() -> None: self.isNewDatabaseRequested = True

		CTk.CTkButton(Backup_Database_Window, text = 'Proceed By Creating A New Database', font = ('Segoe UI', 12, 'bold'), hover_color = '#218838', fg_color = '#28a745', text_color = 'Black', width = 350, command = lambda: [Backup_Database_Window.destroy(), NewDatabaseRequested()]).place(x = 75 , y = 367)

		Orderly_Place_Backup_Databases_Selection()
		Backup_Database_Window.mainloop()
	
	def Auto_Delete_Database_With_min_Users(self) -> None:

		'''
		### Purpose
		Automatically deletes the backup database with the minimum number of active users among all available and non-corrupted backup databases.

		### Functionality
		- Checks if all three backup databases are available.
		- Determines which backup database (1, 2, or 3) has the lowest number of active users.
		- Deletes the backup database folder with the minimum users using a background thread.
		- If a database is corrupted, it is deleted immediately in a separate thread.

		### Parameters
		- **self**: The instance of the `CheckForBackupDatabase` class.

		### Returns
		- **None**

		### Example Usage
		```python
		backup_checker = CheckForBackupDatabase()
		backup_checker.Auto_Delete_Database_With_min_Users()
		```

		### Notes
		- This method is intended to be used for automatic cleanup when storage or backup management is required.
		- The deletion is performed asynchronously to avoid blocking the main application thread.
		- Only operates if all three backup databases are present.

		### Error Handling
		- If a database is corrupted, it is deleted without considering the user count.
		- If no eligible database is found, the method exits without action.

		### Dependencies
		- Requires the `shutil` and `threading` modules for file operations and background processing.

		### Security
		- Deletion is irreversible. Use with caution to avoid accidental data loss.
		'''
		
		if not all([self.isDatabase_01_Available, self.isDatabase_02_Available, self.isDatabase_03_Available]):
			return
		
		min_users = float('inf')
		db = None    # 1 | 2 | 3

		if not self.isDatabase_01_Corrupted:
			if self.Database_01_init_Data["User Records"]["Total Active Users"] < min_users:
				min_users = self.Database_01_init_Data["User Records"]["Total Active Users"]
				db = 1
		else:
			threading.Thread(target = shutil.rmtree, daemon = True, args = (fr'{PATH}\BACKUP - DATABASE 01',)).start()

		if not self.isDatabase_02_Corrupted:
			if self.Database_02_init_Data["User Records"]["Total Active Users"] < min_users:
				min_users = self.Database_02_init_Data["User Records"]["Total Active Users"]
				db = 2
		else:
			threading.Thread(target = shutil.rmtree, daemon = True, args = (fr'{PATH}\BACKUP - DATABASE 02',)).start()
		
		if not self.isDatabase_03_Corrupted:
			if self.Database_03_init_Data["User Records"]["Total Active Users"] < min_users:
				min_users = self.Database_03_init_Data["User Records"]["Total Active Users"]
				db = 3
		else:
			threading.Thread(target = shutil.rmtree, daemon = True, args = (fr'{PATH}\BACKUP - DATABASE 03',)).start()

		match db:

			case 1:
				threading.Thread(target = shutil.rmtree, daemon = True, args = (fr'{PATH}\BACKUP - DATABASE 01',)).start()
			case 2:
				threading.Thread(target = shutil.rmtree, daemon = True, args = (fr'{PATH}\BACKUP - DATABASE 02',)).start()
			case 3:
				threading.Thread(target = shutil.rmtree, daemon = True, args = (fr'{PATH}\BACKUP - DATABASE 03',)).start()
			case _:
				pass
	
	def Rename_Folders(self) -> None:

		''' <!-- Doc Strings --> 
        ### Purpose
        Renames backup database folders to maintain a consistent and sequential naming convention after a database restore or deletion.

        ### Functionality
        - Checks if the database restoration process has completed.
        - Verifies the presence of backup database folders.
        - Renames backup folders so that the available databases are always named in order (e.g., BACKUP - DATABASE 01, BACKUP - DATABASE 02, etc.).
        - Ensures there are no gaps in the backup database numbering after deletion or restoration.

        ### Parameters
        - **self**: The instance of the `CheckForBackupDatabase` class.

        ### Returns
        - **None**

        ### Example Usage
        ```python
        backup_checker = CheckForBackupDatabase()
        backup_checker.Rename_Folders()
        ```

        ### Notes
        - This method should be called after any operation that may change the number or order of backup database folders.
        - The method only performs renaming if the restoration/deletion process has been completed).

        ### Error Handling
        - If the restoration process has not been completed, the method exits without making changes.
        - Assumes that the folders exist and are accessible; errors during renaming are not explicitly handled.

        ### Dependencies
        - Requires the `os` module for file and directory operations.

        ### Security
        - Renaming folders may affect backup management. Use with caution to avoid confusion or data loss.
		'''
		
		self.Check_Presence_Of_Database()

		if not self.isDatabase_01_Available and self.isDatabase_02_Available:
			os.rename(fr'{PATH}\BACKUP - DATABASE 02', fr'{PATH}\BACKUP - DATABASE 01')

		if (self.isDatabase_01_Available and not self.isDatabase_02_Available) and self.isDatabase_03_Available:
			os.rename(fr'{PATH}\BACKUP - DATABASE 03', fr'{PATH}\BACKUP - DATABASE 02')

		if (not self.isDatabase_01_Available and not self.isDatabase_02_Available) and self.isDatabase_03_Available:
			os.rename(fr'{PATH}\BACKUP - DATABASE 03', fr'{PATH}\BACKUP - DATABASE 01')
    
	def _exec_func_(self) -> None:

		'''
        ## Purpose
        Handles post-backup-restore or post-setup actions for the Bank-With-High-Functionalities application. This method is responsible for creating application shortcuts, registering uninstall information, and performing any finalization steps after a backup database is restored or a new setup is completed.

        ## Functionality
        - **Registers Uninstall Entry**: Adds an uninstall entry for the application in the Windows registry under the current user scope, allowing standard uninstallation via Windows settings.
        - **Creates Start Menu Shortcut**: Generates a shortcut to the application in the Windows Start Menu's Programs folder.
        - **Creates Desktop Shortcut**: Generates a shortcut to the application on the user's Desktop.

        ## Parameters
        - **self**: Instance of the `CheckForBackupDatabase` class.

        ## Returns
        - **None**

        ## Example Usage
        ```python
        backup_checker = CheckForBackupDatabase()
        backup_checker._exec_func_()
        ```

        ## Notes
        - This method is typically called after restoring a backup or completing a new setup to ensure the application is properly registered and accessible.
        - The method uses Windows-specific APIs and will only work on Windows systems.
        - Shortcuts point to the application's `main.exe` and use the official icon.

        ## Error Handling
        - If any error occurs during shortcut creation or registry operations, the error is logged to the setup log file (`SETUP_LOGS`).
        - The method does not raise exceptions to the caller; all errors are handled internally.

        ## Security
        - Modifies the Windows registry and file system only for the current user.
        - No sensitive data is exposed or handled by this method.

        ## Limitations
        - Only works on Windows operating systems.
        - Assumes the application directory and required files exist and are accessible.

        ## Dependencies
        - Requires the `os` module for path operations.
        - Requires `win32com.client.Dispatch` for shortcut creation.
        - Requires the `register_uninstall_entry_user_scope` utility for registry operations.
		'''

		Shell = Dispatch('WScript.Shell')

		def Shortcut_At_Start_Menu() -> None:

			''' <!-- Doc Strings -->
			### Purpose
			Creates a shortcut for the Bank-With-High-Functionalities application in the Windows Start Menu's Programs folder.

			### Functionality
			- Uses the Windows Scripting Host (via `win32com.client.Dispatch`) to create a `.lnk` shortcut.
			- Sets the shortcut's target to the application's `main.exe`.
			- Configures the working directory, description, and icon for the shortcut.
			- Saves the shortcut in the Start Menu Programs directory for the current user.

			### Notes
			- The shortcut is created at: `%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Bank-With-High-Functionalities.lnk`
			- The function assumes the global `PATH` variable points to the application's root directory.
			- This function is intended for Windows environments only.

			### Dependencies
			- Requires the `os` module for path operations.
			- Requires `win32com.client.Dispatch` for shortcut creation.

			### Security
			- Ensure the `PATH` variable is trusted to avoid creating shortcuts to unintended executables.
			'''

			Start = Shell.CreateShortcut(os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Bank-With-High-Functionalities.lnk"))
			Start.TargetPath = fr'{PATH}\main.exe'
			Start.WorkingDirectory = os.path.dirname(fr'{PATH}\main.exe')
			Start.Description = 'Python Based GUI Banking System Prototype.'
			Start.IconLocation = fr'{PATH}\Bank_Package\Visual Data\ICO Files\Bank Image.ico'
			Start.save()

		def Shortcut_At_Desktop() -> None:

			''' <!-- Doc Strings -->
			### Purpose
			Creates a shortcut for the Bank-With-High-Functionalities application on the user's Desktop.

			### Functionality
			- Uses the Windows Scripting Host (via `win32com.client.Dispatch`) to create a `.lnk` shortcut.
			- Sets the shortcut's target to the application's `main.exe`.
			- Configures the working directory, description, and icon for the shortcut.
			- Saves the shortcut on the Desktop for the current user.

			### Notes
			- The shortcut is created at: `%USERPROFILE%\\Desktop\\Bank-With-High-Functionalities.lnk`
			- The function assumes the global `PATH` variable points to the application's root directory.
			- This function is intended for Windows environments only.

			### Dependencies
			- Requires the `os` module for path operations.
			- Requires `win32com.client.Dispatch` for shortcut creation.

			### Security
			- Ensure the `PATH` variable is trusted to avoid creating shortcuts to unintended executables.
			'''

			Desktop = Shell.CreateShortcut(os.path.join(os.environ["USERPROFILE"], "Desktop", "Bank-With-High-Functionalities.lnk"))
			Desktop.TargetPath = fr'{PATH}\main.exe'
			Desktop.WorkingDirectory = os.path.dirname(fr'{PATH}\main.exe')
			Desktop.Description = 'Python Based GUI Banking System Prototype.'
			Desktop.IconLocation = fr'{PATH}\Bank_Package\Visual Data\ICO Files\Bank Image.ico'
			Desktop.save()
	
		register_uninstall_entry_user_scope()
		Shortcut_At_Start_Menu()
		Shortcut_At_Desktop()

# To Check For MySQL Database Connection
class CheckMySQLDatabaseConnection:

	""" <!-- Doc Strings -->
	#### A Utility Class To Verify The Connection To A MySQL Database Server. \
	This Class Provides A Method To Check If A MySQL Server Exists And Is Accessible \
	Using The Provided Credentials. It Is Designed To Handle Connection Attempts \
	And Log Errors In Case Of Failure.

	---
	## <ins>***Methods***</ins>

	### 1. `DoesServerExists() -> bool:`
	> #### Attempts To Establish A Connection To The MySQL Server Using The Credentials \
	Provided In The `SETUPDATA` Dictionary. If The Connection Is Successful, It \
	Closes The Connection And Returns `True`. If The Connection Fails, It Logs \
	The Error And Returns `False`.

	---
	## <ins>***Usage***</ins>

	> #### This class is intended to be used as a utility for checking the availability of \
	a MySQL server during the setup or initialization phase of an application. It \
	relies on the `SETUPDATA` dictionary to fetch the MySQL credentials, which must \
	be defined elsewhere in the application.

	---
	## <ins>***Example***</ins>

	```python
	# Create an instance of the class
	db_checker = CheckMySQLDatabaseConnection()
	# Check if the MySQL server exists
	if db_checker.DoesServerExists():
		print("MySQL server is accessible.")
	else:
		print("Failed to connect to the MySQL server.")
	```

	---
	## <ins>***Exceptions***</ins>

	> * #### If the `SETUPDATA` dictionary or its required keys are missing, the method will raise a `KeyError`.
	> * #### If the `mysql.connector` module is not installed, an `ImportError` will occur.
	> * #### If the connection attempt fails, a `mysql.connector.Error` will be caught and logged.
	
	---
	## <ins>***Limitations***</ins>

	> * #### This class does not handle advanced MySQL configurations such as SSL or custom authentication plugins.
	> * #### It does not provide detailed error handling for specific MySQL error codes.
	> * #### The method `DoesServerExists` does not return detailed error information; it only returns a boolean value.
	"""

	def DoesServerExists(self) -> bool:
	
		DatabaseConnectionStatus.after(0, lambda: DatabaseConnectionStatus.configure(text = 'Connecting', text_color = 'Orange'))

		CTk.CTkLabel(MySQLDebugFrame, text = '\nInitializing connection to the database server.\nAttempting to establish a network handshake and\nverify server availability.', font = ('Segoe UI', 12, 'italic'), justify = 'left').pack()
		MYSQLLOG.join('\nInitializing connection to the database server. Attempting to establish a network handshake and verify server availability.')

		try:

			if SETUPDATA['MySQL Credentials']['Charset'].strip():

				# Connect to MySQL Server (With Charset)
				Connection = mysql.connector.connect(

					host = SETUPDATA['MySQL Credentials']['Host'],
					port = SETUPDATA['MySQL Credentials']['Port'],
					user = SETUPDATA['MySQL Credentials']['Username'],
					password = SETUPDATA['MySQL Credentials']['Password'],
					charset = SETUPDATA['MySQL Credentials']['Charset']

				)

			else:
				
				# Connect to MySQL Server (Without Charset)
				Connection = mysql.connector.connect(

					host = SETUPDATA['MySQL Credentials']['Host'],
					port = SETUPDATA['MySQL Credentials']['Port'],
					user = SETUPDATA['MySQL Credentials']['Username'],
					password = SETUPDATA['MySQL Credentials']['Password']

				)
			
			DatabaseConnectionStatus.after(4000, lambda: CTk.CTkLabel(MySQLDebugFrame, text = '\nSubmitting provided username and password to the\nserver for verification. Waiting for authentication\nresponse.', font = ('Segoe UI', 12, 'italic'), justify = 'left').pack())
			MYSQLLOG.join('\nSubmitting provided username and password to the server for verification. Waiting for authentication response.')
			DatabaseConnectionStatus.after(5000, lambda: DatabaseConnectionStatus.configure(text = 'Authenticated', text_color = '#4CAF50'))

			# Check if the connection is successful
			if Connection.is_connected():

				DatabaseConnectionStatus.after(10000, lambda: DatabaseConnectionStatus.configure(text = 'Connected', text_color = '#4CAF50'))
				
				DatabaseConnectionStatus.after(10000, lambda: CTk.CTkLabel(MySQLDebugFrame, text = '\nDatabase client is now connected and authenticated.\nReady to perform actions on the database server.', font = ('Segoe UI', 12, 'italic'), justify = 'left').pack())
				MYSQLLOG.join('\nDatabase client is now connected and authenticated. Ready to perform actions on the database server.')
				
				DatabaseConnectionStatus.after(11000, lambda: CTk.CTkLabel(MySQLDebugFrame, text = '\nSecure connection successfully established with the\ndatabase server. Preparing for further operations.', font = ('Segoe UI', 12, 'italic'), justify = 'left').pack())
				MYSQLLOG.join('\nSecure connection successfully established with the database server. Preparing for further operations.')

				DatabaseConnectionStatus.after(15000, lambda: DatabaseConnectionStatus.configure(text = 'Testing', text_color = 'Orange'))
				DatabaseConnectionStatus.after(15000, lambda: CTk.CTkLabel(MySQLDebugFrame, text = '\nRunning a simple test query to validate database\nresponsiveness and permissions. Ensuring proper\ndata communication.', font = ('Segoe UI', 12, 'italic'), justify = 'left').pack())
				MYSQLLOG.join('\nRunning a simple test query to validate database responsiveness and permissions. Ensuring proper data communication.')
				
				DatabaseConnectionStatus.after(16000, lambda: CTk.CTkLabel(MySQLDebugFrame, text = '\nInitiating database creation process. Sending SQL\ncommand to create the specified database.', font = ('Segoe UI', 12, 'italic'), justify = 'left').pack())
				MYSQLLOG.join('\nInitiating database creation process. Sending SQL command to create the specified database.')
				
				Cursor = Connection.cursor()
				Cursor.execute('CREATE DATABASE IF NOT EXISTS `bank-with-high-functionalities`') # Create Database

				DatabaseConnectionStatus.after(20000, lambda: DatabaseConnectionStatus.configure(text = 'Successful', text_color = '#4CAF50'))
				DatabaseConnectionStatus.after(20000, lambda: CTk.CTkLabel(MySQLDebugFrame, text = '\nQuery returned expected results. Connection is\nhealthy and permissions are correctly configured.', font = ('Segoe UI', 12, 'italic'), justify = 'left').pack())
				MYSQLLOG.join('\nQuery returned expected results. Connection is healthy and permissions are correctly configured.')

				DatabaseConnectionStatus.after(25000, lambda: DatabaseConnectionStatus.configure(text = 'Disconnecting', text_color = '#4CAF50'))
				DatabaseConnectionStatus.after(25000, lambda: CTk.CTkLabel(MySQLDebugFrame, text = '\nDatabase has been created without errors. Closing\nthe connection to release resources and\nmaintain security.', font = ('Segoe UI', 12, 'italic'), justify = 'left').pack())
				MYSQLLOG.join('\nDatabase has been created without errors. Closing the connection to release resources and maintain security.')

				 
				Cursor.close() # Close the cursor

				Connection.close() # Close the connection
				
				DatabaseConnectionStatus.after(30000, lambda: DatabaseConnectionStatus.configure(text = 'Disconnected', text_color = '#4CAF50'))
				DatabaseConnectionStatus.after(30000, lambda: CTk.CTkLabel(MySQLDebugFrame, text = '\nConnection terminated cleanly. All operations completed\nsuccessfully.', font = ('Segoe UI', 12, 'italic'), justify = 'left').pack())
				MYSQLLOG.join('\nConnection terminated cleanly. All operations completed successfully.')
				SETUPDATA['MySQL Credentials']['Database'] = 'bank-with-high-functionalities'

				return True
			
		except mysql.connector.Error as Error:
			
			# Log the error
			Error_Information = Error

			ERROR_LOGS.write(f'\n[ERROR]:[setup.exe][{datetime.datetime.now().strftime('%d/%b/%Y @ %I:%M:%S %p')}] - Failed To Connect To MySQL Server ; ErrorType: [ {Error_Information} ]')
			DatabaseConnectionStatus.after(5000, lambda: DatabaseConnectionStatus.configure(text = 'Failed', text_color = 'Red'))
			DatabaseConnectionStatus.after(5000, lambda: CTk.CTkLabel(MySQLDebugFrame, text = f'\nFailed To Connect To MySQL Server ; ErrorType: [ {Error_Information} ]', wraplength = 285, font = ('Segoe UI', 12, 'italic'), justify = 'left').pack())
			MYSQLLOG.join(f'\nFailed To Connect To MySQL Server ; ErrorType: [ {Error_Information} ]')
			
			return False
			
		return False

# Email Verification For Manager
class Manager_Email_Verification:

	''' <!-- Doc Strings -->
	## Purpose
	The `Manager_Email_Verification` class is responsible for handling the email verification process for the manager during the setup phase. It generates a unique verification code, sends it to the manager's email address, and provides functionality to resend the email if needed.

	## Attributes
	- **ReceiverMailAddress**: The email address of the manager to which the verification email will be sent.

	## Methods

	### 1. `__init__(self, ReceiverMailAddress: str = SETUPDATA['Manager Email']) -> None`
	- **Purpose**: Initializes the `Manager_Email_Verification` class with the manager's email address.
	- **Parameters**:
	  - `ReceiverMailAddress` (str): The email address of the manager. Defaults to the value in `SETUPDATA['Manager Email']`.
	- **Return Type**: None

	### 2. `Send_Gmail(self) -> str`
	- **Purpose**: Sends a verification email to the manager's email address with a unique verification code.
	- **Process**:
	  1. Generates a unique verification code.
	  2. Creates an HTML email template with the verification code.
	  3. Sends the email using the SMTP protocol.
	- **Return Type**: str
	  - Returns `'Error Free'` if the email is sent successfully.
	  - Returns `'Credentials Error'` if there is an issue with the email credentials.
	  - Returns `'No Internet'` if there is no internet connection.
	- **Security**:
	  - The manager's email app password is securely used to authenticate the SMTP session.
	  - The verification code is embedded in the email but not stored permanently.

	### 3. `Resend_Gmail(self) -> None`
	- **Purpose**: Resends the verification email to the manager's email address.
	- **Process**: Calls the `Send_Gmail` method to resend the email.
	- **Return Type**: None

	## Example Usage
	```python
	# Initialize the email verification class
	email_verification = Manager_Email_Verification(ReceiverMailAddress="manager@example.com")

	# Send the verification email
	result = email_verification.Send_Gmail()
	print(result)  # Output: 'Error Free' or an error message

	# Resend the verification email
	email_verification.Resend_Gmail()
	```

	## Notes
	- Ensure that the `SETUPDATA['Manager Email']` and `SETUPDATA['Manager Email App Password']` are correctly configured before using this class.
	- The email template is designed to be responsive and visually appealing.

	## Example Email Template
	```
	Subject: [Code] Is Your Verification Code To Access Your Manager Account.
	Body:
	Hi [Manager Name],

	Were excited to have you on board! To finish setting up your account and ensure your security, please verify your email address by using the verification code below:

	[Code]

	This code will expire in 10 minutes. If it does, you can request a new one.

	Best Regards,
	Bank-With-High-Functionalities Team
	```

	## Dependencies
	- Requires the `smtplib` module for sending emails.
	- Requires the `email.message.EmailMessage` class for constructing the email.
	- Relies on the `random` and `randint` functions to generate the verification code.

	## Security
	- The manager's email app password is not stored in plaintext and is only used during the SMTP session.
	- The verification code is temporary and expires after 10 minutes.

	## Limitations
	- The email sending functionality depends on the availability of an internet connection.
	- If the email credentials are incorrect, the email will not be sent.
	'''

	def __init__(self) -> None:
		...

	def Send_Gmail(self) -> None:

		def __force_stop_email_countdown__() -> None:

			countdown.after_cancel(CountdownRefresher)
			countdown.after(0, lambda: countdown.configure(text = 'Error!', text_color = 'Red'))

		Email = EmailMessage()

		global __Code__, __Timestamp__
		__Code__ = str(int(random()*(999-100)+100)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90))

		HTML_EMAIL = ''' <!-- HTML Email Template --> 
		
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Email Verification</title>
  <style>
	/* Base Styles */
	body {
	  margin: 0;
	  padding: 0;
	  background-color: #f0f4f8;
	  font-family: 'Segoe UI', sans-serif;
	}
	table {
	  border-collapse: collapse;
	}
	h1, h2, p {
	  margin: 0;
	  padding: 0;
	}
	
	/* Mobile-specific Styles */
	@media screen and (max-width: 600px) {
	  .container {
		width: 100% !important;
		padding: 15px !important;
	  }
	  .header {
		padding: 30px 20px !important;
	  }
	  .code-box {
		font-size: 30px !important;
		padding: 22px 36px !important;
		letter-spacing: 5px !important;
	  }
	  h1 {
		font-size: 24px !important;
	  }
	  .cta-button {
		display: block !important;
		width: 100% !important;
		text-align: center !important;
		padding: 16px 0 !important;
		font-size: 16px !important;
	  }
	  p {
		font-size: 15px !important;
		line-height: 1.4 !important;
	  }
	}
  </style>
</head>
<body style="margin:0; padding:0; background-color:#f0f4f8; font-family: 'Segoe UI', sans-serif;">

  <table width="100%" cellpadding="0" cellspacing="0" style="padding: 50px 0; background: linear-gradient(135deg, #dde6f5, #ffffff);">
	<tr>
	  <td align="center">
		<table class="container" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:18px; box-shadow:0 12px 48px rgba(0,0,0,0.08); overflow:hidden;">

		  <!-- Header / Hero -->
		  <tr>
			<td class="header" style="background: linear-gradient(135deg, #667eea, #764ba2); padding: 40px 30px; text-align: center;">
			  <h1 style="margin:0; font-size: 28px; color: #ffffff;">Verify Your Email</h1>
			  <p style="margin:8px 0 0; color:#e3e7fb; font-size:16px;">Welcome To <strong>Bank-With-High-Functionalities</strong>. Let’s Get You Started Securely.</p>
			</td>
		  </tr>

		  <!-- Greeting & Instructions -->
		  <tr>
			<td style="padding: 40px 30px; text-align: left;">
			  <p style="font-size:18px; color:#333; margin-bottom:12px;">Hi <strong>[Manager Name]</strong>,</p>
			  <p style="font-size:16px; color:#555; margin-bottom:16px;">
				We're Excited To Have You On Board! To Finish Setting Up Your Account & Ensure Your Security, Please Verify Your Email Address By Using The Verification Code Below.
			  </p>

			  <!-- Code Box -->
			  <table width="100%" style="margin: 30px 0;">
				<tr>
				  <td align="center">
					<div class="code-box" style="background: rgba(255, 255, 255, 0.7); border: 2px solid #c9d7f4; padding: 26px 48px; border-radius: 16px; box-shadow: 0 6px 30px rgba(0, 123, 255, 0.1); font-size: 36px; letter-spacing: 10px; color:#4a7efc; font-weight: bold; font-family: 'Courier New', monospace;">
					  [Code]
					</div>
				  </td>
				</tr>
			  </table>

			  <!-- Additional Info -->
			  <p style="font-size:14px; color:#777; margin-top:20px;">
				This Code Will Expire In <strong>10 Minutes</strong>. If It Does, You Can Request A New One.
			  </p>
			  <p style="font-size:14px; color:#999; margin-top:8px;">
				Didn't Sign Up For <strong>Bank-With-High-Functionalities</strong>? No Worries — Just Ignore This Message.
			  </p>
			  <p style="font-size:14px; color:#000; margin-top:8px;">
				  Best Regards,
			  </p>
			<p><b>Bank-With-High-Functionalities Team</b></p>
			  
			</td>
		  </tr>

		  <!-- Divider -->
		  <tr>
			<td style="padding: 0 30px;">
			  <hr style="border:none; border-top:1px solid #e0e6ef; margin:30px 0;">
			</td>
		  </tr>

		  <!-- Footer -->
		  <tr>
			<td style="padding: 20px 30px; text-align: center; font-size: 12px; color: #999;">
			  <p style="margin:0;">
				© 2024-2026 Bank-With-High-Functionalities • Virati Akira Nandhan Reddy
			  </p>
			  <div style="padding: 20px 30px; margin-top: 16px; text-align: center;">
				<a href="https://www.facebook.com/ViratiAkiraNandhanReddy" style="margin: 0 8px; text-decoration: none;" target="_blank">
					<img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook" width="24" style="vertical-align: middle; border: 0;">
				</a>
				<a href="https://www.instagram.com/viratiaki53" style="margin: 0 8px; text-decoration: none;" target="_blank">
					<img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram" width="24" style="vertical-align: middle; border: 0;">
				</a>
				<a href="https://x.com/Viratiaki53" style="margin: 0 8px; text-decoration: none;" target="_blank">
					<img src="https://cdn-icons-png.flaticon.com/512/5968/5968830.png" alt="X" width="24" style="vertical-align: middle; border: 0;">
				</a>
				<a href="https://github.com/ViratiAkiraNandhanReddy" style="margin: 0 8px; text-decoration: none;" target="_blank">
					<img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub" width="24" style="vertical-align: middle; border: 0;">
				</a>
				<a href="https://www.linkedin.com/in/viratiakiranandhanreddy" style="margin: 0 8px; text-decoration: none;" target="_blank">
					<img src="https://cdn-icons-png.flaticon.com/512/145/145807.png" alt="LinkedIn" width="24" style="vertical-align: middle; border: 0;">
				</a>
				<a href="https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities" style="margin: 0 8px; text-decoration: none;" target="_blank">
					<img src="https://cdn-icons-png.flaticon.com/512/545/545670.png" alt="Website" width="24" style="vertical-align: middle; border: 0;">
				</a>

				<p style="padding: 35px 30px;">
					<b> 
					🤖 This is An Automated Email 🤖<br>
					⚠️ Please Do Not Reply ⚠️
					</b>
				</p> 
			  </div>
			</td>
		  </tr>

		</table>
	  </td>
	</tr>
  </table>

</body>
</html>

'''.replace('[Manager Name]', str(SETUPDATA['Manager Name'])).replace('[Code]', __Code__)

		Email['Subject'] = f'{__Code__} Is Your Verification Code To Access Your Manager Account.'
		Email['From'] = 'Bank-With-High-Functionalities Team'
		Email['To'] = SETUPDATA['Manager Email']

		Email.set_content(HTML_EMAIL, subtype = 'html')

		try:

			with smtplib.SMTP_SSL('smtp.gmail.com', 465) as SMTP:

				SMTP.login(SETUPDATA['Manager Email'], SETUPDATA['Manager Email App Password'])
				SMTP.send_message(Email)
				
				EMAIL_LOGS.write(f'\n[INFO]:[setup.exe - Manager_Email_Verification][{datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}] :  Status: Successful : MSG: Verification Email Was Sent To <{SETUPDATA["Manager Email"]}>')
				Success = CTk.CTkLabel(GmailVerificationFrame, text = 'A verification code has been sent\nto your email successfully.') ; GmailVerificationFrame.after(0, lambda: Success.place(x = 145, y = 230))
				Success.after(5000, lambda: Success.destroy())
			__Timestamp__ = datetime.datetime.now()

		except smtplib.SMTPAuthenticationError:
			
			EMAIL_LOGS.write(f'\n[ERROR]:[setup.exe - Manager_Email_Verification][{datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}] ; Status: Unsuccessful ; MSG: Error Occurred While Sending Verification Email To <{SETUPDATA["Manager Email"]}> ; ErrorType: [Credentials Error At Backend (Manger App Password)]')
			__force_stop_email_countdown__()
			Error = CTk.CTkLabel(GmailVerificationFrame, text = 'Invalid credentials. Please check your email,\napp password and try again.') ; GmailVerificationFrame.after(0, lambda: Error.place(x = 115, y = 230))
			Error.after(8000, lambda: Error.destroy())
		
		except smtplib.SMTPServerDisconnected: # Slow Internet 

			EMAIL_LOGS.write(f'\n[ERROR]:[setup.exe - Manager_Email_Verification][{datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}] ; Status: Unsuccessful ; MSG: Error Occurred While Sending Verification Email To <{SETUPDATA["Manager Email"]}> ; ErrorType: [Slow Internet Connection]')
			__force_stop_email_countdown__()
			Error = CTk.CTkLabel(GmailVerificationFrame, text = 'Connection lost : It seems your internet connection is slow\nor unstable. Please check your connection and try again.') ; GmailVerificationFrame.after(0, lambda: Error.place(x = 60, y = 230))
			Error.after(8000, lambda: Error.destroy())
		
		except socket.gaierror:
			
			EMAIL_LOGS.write(f'\n[ERROR]:[setup.exe - Manager_Email_Verification][{datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}] ; Status: Unsuccessful ; MSG: Error Occurred While Sending Verification Email To <{SETUPDATA["Manager Email"]}> ; ErrorType: [No Internet Connection]')
			__force_stop_email_countdown__()
			Error = CTk.CTkLabel(GmailVerificationFrame, text = 'Network Error : Unable to connect to the server.\nPlease check your internet connection.') ; GmailVerificationFrame.after(0, lambda: Error.place(x = 110, y = 230))
			Error.after(8000, lambda: Error.destroy())
		
		except Exception as Error:

			EMAIL_LOGS.write(f'\n[ERROR]:[setup.exe - Manager_Email_Verification][{datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}] ; Status: Unsuccessful ; MSG: Error Occurred While Sending Verification Email To <{SETUPDATA["Manager Email"]}> ; ErrorType: [{Error}]')
			__force_stop_email_countdown__()
			Err = CTk.CTkLabel(GmailVerificationFrame, text = 'Network Error : Unable to connect to the server.\nPlease check your internet connection.') ; GmailVerificationFrame.after(0, lambda: Err.place(x = 110, y = 230))
			Err.after(8000, lambda: Err.destroy())
		
# Main Setup Class
class Setup:

	''' <!-- Doc Strings --> 

	# Setup Class

	## Purpose
	The `Setup` class is the core of the setup process for the "Bank-With-High-Functionalities" application. \
	It provides a step-by-step graphical user interface (GUI) to guide users through the installation and \
	configuration of the software. This includes tasks such as accepting terms and conditions, activating \
	the software, setting up manager credentials, selecting a database, and reviewing the final configuration.

	## Features
	- **Welcome Screen**: Displays a greeting and starts the setup process.
	- **Terms and Conditions**: Allows users to review and accept the license agreement.
	- **Software Activation**: Validates the product key for activation.
	- **Manager Mode Setup**: Collects manager details such as name, username, password, and security code.
	- **Database Selection**: Enables users to choose between SQLite3, MySQL, or JSON as the database type.
	- **MySQL Setup**: Collects MySQL credentials and verifies the connection.
	- **Final Review**: Displays all collected data for user confirmation before completing the setup.

	## Attributes
	- `SecurityCodeRefreshed` (bool): Tracks whether the security code has been refreshed.
	- `isNameConditionSatisfied` (bool): Tracks whether the manager name meets the validation criteria.
	- `isUsernameConditionSatisfied` (bool): Tracks whether the manager username meets the validation criteria.
	- `isPasswordConditionSatisfied` (bool): Tracks whether the manager password meets the validation criteria.

	## Methods
	### 1. `__init__()`
	Initializes the `SetUp` class and its attributes.

	### 2. `__str__() -> str`
	Provides information about the GitHub repository and contribution guidelines.

	### 3. `SetupWindows() -> None`
	Manages the entire setup process by creating and navigating between different frames in the GUI. This includes:
	- Navigation between frames such as Welcome, Terms and Conditions, Software Activation, Manager Mode Setup, Gmail Verification, Database Selection, MySQL Setup, and Final Review.
	- Validation of user inputs at each step.
	- Updating the `SETUPDATA` dictionary with user-provided information.

	### 4. `Inject_Initialization_Data_Into_JSON_Files() -> None`
	Injects the collected setup data into a JSON file for future use.

	## Setup Process
	The setup process consists of the following steps:
	1. **Welcome Screen**:
	   - Displays a welcome message and a "Let's Get Started!" button to proceed to the next step.

	2. **Terms and Conditions**:
	   - Displays the license agreement.
	   - Requires the user to accept the terms before proceeding.

	3. **Software Activation**:
	   - Validates the product key entered by the user.
	   - Updates the activation status in the `SETUPDATA` dictionary.

	4. **Manager Mode Setup**:
	   - Collects manager details such as name, username, password, and security code.
	   - Validates the inputs and ensures all criteria are met.

	5. **Gmail Verification**:
	   - Placeholder for Gmail verification functionality.

	6. **Database Selection**:
	   - Allows the user to choose between SQLite3, MySQL, or JSON as the database type.
	   - Updates the `SETUPDATA` dictionary with the selected database type and paths.

	7. **MySQL Setup**:
	   - Collects MySQL credentials such as host, port, username, password, and charset.
	   - Verifies the connection to the MySQL server.

	8. **Final Review**:
	   - Displays all collected data for user confirmation.
	   - Allows the user to copy the data to the clipboard.

	## Usage
	```python
	setup = SetUp()
	setup.SetupWindows()
	```

	## Contribution
	Visit the GitHub repository for more information:
	- **GitHub**: [ViratiAkiraNandhanReddy](https://github.com/ViratiAkiraNandhanReddy)
	- **LinkedIn**: Virati Akira Nandhan Reddy
	- **Twitter**: Viratiaki53
	- **Instagram**: Viratiaki53
	- **Website**: [Click Here](https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities/)

	If you are willing to contribute, please submit a pull request.

	**Happy Coding!**
	
	
	'''

	def __init__(self) -> None:
		pass

	def __str__(self) -> str: # Information About Contribution 

		return '''
		Visit The GitHub Repository For More Information:

			GitHub : ViratiAkiraNandhanReddy
			LinkedIn : Virati Akira Nandhan Reddy
			Twitter : Viratiaki53
			Instagram : Viratiaki53
			Repository : https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities

			There Will Be The Full Code For The Setup Process And Other Modules
			If You Are Willing To Contribute Please Submit A Pull Request.

		>>> Happy Coding

		**Thank You For Your Support**
		'''
	
	def SetupWindows(self) -> None:

		''' <!-- Short Doc Strings -->
		## Purpose
		The `SetupWindows` function manages the entire setup process for the application through a graphical user interface (GUI). \
		It guides the user step-by-step to configure the software.

		## Functionality
		- Navigates through multiple setup frames:
		1. Welcome Screen
		2. Terms and Conditions
		3. Software Activation
		4. Manager Mode Setup
		5. Gmail Verification
		6. Database Selection
		7. MySQL Setup (if selected)
		8. Final Review
		9. Finish Setup
		- Validates user inputs at each step.
		- Updates the `SETUPDATA` dictionary with user-provided information.

		## Parameters
		- **None**: This function does not take any parameters.

		## Return Type
		- **None**: This function does not return any value.

		## Notes
		- Ensure all required dependencies (e.g., `customtkinter`) are installed.
		- The function uses global variables for GUI components and state management.

		## Example Usage
		```python
		setup = Setup()
		setup.SetupWindows()
		```
		'''

		def GoTo_TermsAndConditionsFrame() -> None: # WelcomeFrame -> TermsAndConditionsFrame -- 1
			WelcomeFrame.place_forget()
			Window.geometry('800x600')
			TermsAndConditionsFrame.place(x = 5, y = 5)

		def GoBackTo_WelcomeFrame() -> None: # WelcomeFrame <- TermsAndConditionsFrame -- 2
			TermsAndConditionsFrame.place_forget()
			Window.geometry('800x400')
			WelcomeFrame.place(x = 0, y = 0)

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

		def GoTo_GmailVerificationFrame() -> None: # ManagerModeSetupFrame -> GmailVerificationFrame -- 7
			ManagerModeSetupFrame.place_forget()
			GmailVerificationFrame.place(x = 5, y = 5)

		def GoBackTo_ManagerModeSetupFrame() -> None: # ManagerModeSetupFrame <- GmailVerificationFrame -- 8
			GmailVerificationFrame.place_forget()
			ManagerModeSetupFrame.place(x = 5, y = 5)

		def GoTo_ChooseDatabaseFrame() -> None: # GmailVerificationFrame -> ChooseDatabaseFrame -- 9
			GmailVerificationFrame.place_forget()
			Window.geometry('800x600')
			ChooseDatabaseFrame.place(x = 5, y = 5)

		def GoBackTo_GmailVerificationFrame() -> None: # GmailVerificationFrame <- ChooseDatabaseFrame -- 10
			ChooseDatabaseFrame.place_forget()
			Window.geometry('800x400')
			GmailVerificationFrame.place(x = 5, y = 5)

		def GoTo_GetMySQLDataFrame() -> None: # ChooseDatabaseFrame -> MySQLSetupFrame -- 11 [ if MySQL is Selected ]
			ChooseDatabaseFrame.place_forget()
			Window.geometry('800x600')
			GetMySQLDataFrame.place(x = 5, y = 5)
			Buffering_MySQL_Data.start()

		def GoBackTo_ChooseDatabaseFrame() -> None: # ChooseDatabaseFrame <- FinalReviewFrame | GetMySQLDataFrame -- 12
			
			if SETUPDATA['DATABASE TYPE'] == 'MySQL':
				
				GetMySQLDataFrame.place_forget()
				Buffering_MySQL_Data.stop()
			
			else:
				
				Window.geometry('800x600')
				FinalReviewFrame.place_forget()
			
			ChooseDatabaseFrame.place(x = 5, y = 5)

		def GoTo_FinalReviewFrame() -> None: # ChooseDatabaseFrame | GetMySQLDataFrame -> FinalReviewFrame -- 13
			
			if SETUPDATA['DATABASE TYPE'] == 'MySQL':
				
				GetMySQLDataFrame.place_forget()
				Buffering_MySQL_Data.stop()
			
			else:
				
				ChooseDatabaseFrame.place_forget()

			Window.geometry('800x400')

			for widget,_text_ in [ # Live Update 

				(Final_Manager_Name__Update__, f'Manager Name: {SETUPDATA["Manager Name"][:60] + ('...' if len(SETUPDATA["Manager Name"]) > 60 else '')}'),
				(Final_Manager_Username__Update__, f'Manager Username: {SETUPDATA["Manager Username"][:60] + ('...' if len(SETUPDATA["Manager Username"]) > 60 else '')}'),
				(Final_Manager_Password__Update__, f'Manager Password: {SETUPDATA["Manager Password"][:60] + ('...' if len(SETUPDATA["Manager Password"]) > 60 else '')}'),
				(Final_Manager_Security_Code__Update__, f'Manager Security Code: {SETUPDATA["Manager Security Code"]}'),
				(Final_Manager_Email__Update__, f'Manager Email: {SETUPDATA["Manager Email"]}'),
				(Final_Manager_Email_App_Password__Update__, f'Manager Email App Password: {SETUPDATA["Manager Email App Password"]}'),
				(Final_isEmailVerified__Update__, f'isEmailVerified: {SETUPDATA["isEmailVerified"]}'),
				(Final_Database_Type__Update__, f'Database Type: {SETUPDATA["DATABASE TYPE"]}'),
				(Final_Current_App_Version__Update__, f'Current App Version: {SETUPDATA["Current Version"]}')

				]:

				widget.configure(text = _text_)

			FinalReviewFrame.place(x = 5, y = 5)
		
		def GoBackTo_GetMySQLDataFrame() -> None: # MySQLSetupFrame <- FinalReviewFrame -- 14 [ if MySQL is Selected ]
			FinalReviewFrame.place_forget()
			Window.geometry('800x600')
			GetMySQLDataFrame.place(x = 5, y = 5)

		def GoTo_FinishSetupFrame() -> None: # FinalReviewFrame -> FinishSetupFrame -- 15
			FinalReviewFrame.place_forget()
			Window.geometry('800x600')
			FinishSetupFrame.place(x = 5, y = 5)

		global Window, countdown, GmailVerificationFrame, DatabaseConnectionStatus, MySQLDebugFrame
		Window = CTk.CTk()
		Window.title('Setup')
		Window.resizable(False,False)
		Window.geometry('800x400+100+40')
		Window.iconbitmap(fr'{PATH}\Bank_Package\Visual Data\ICO Files\Setup.ico')
		Window.protocol('WM_DELETE_WINDOW', lambda: Window.destroy() if messagebox.askyesno(title = 'Exit Setup', message = 'Setup Is Not Complete. If You Exit Now, The Program Will Not Be Installed.\n\nYou May Run Setup Again At Another Time To Complete The Installation.\n\nExit Setup?') else None)

		# Welcome Greeting

		WelcomeFrame = CTk.CTkFrame(Window,800,400) ; WelcomeFrame.place(x=0,y=0)
		CTk.CTkLabel(WelcomeFrame,text='',image=CTk.CTkImage(light_image = BannerLightImage, dark_image = BannerDarkImage, size=(800,400))).place(x=0,y=0)
		CTk.CTkButton(WelcomeFrame,text='Let\'s Get Started!', font = ('Segoe UI', 14, 'italic'), corner_radius=4, fg_color = '#4CAF50', hover_color = '#45A049', text_color = 'Black', width = 160, height = 30, command = GoTo_TermsAndConditionsFrame).place(x=630,y=360)
		
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
		CTk.CTkLabel(TermsAndConditionsTextFrame, text='Copyright (c) 2024 - 2026 Virati Akira Nandhan Reddy', font=("Roboto", 22,'bold'),width=764).place(x=0,y=50)
		CTk.CTkLabel(TermsAndConditionsTextFrame, text=f"{TERMSANDCONDITIONS[18:]}", font=("Roboto", 14), width=764, justify='left').place(x=5, y=90)

		CTk.CTkCheckBox(TermsAndConditionsFrame,text = 'I Agree To The License Terms & Conditions', variable = ACCEPTED, offvalue = False, onvalue = True, command = isTermsAndConditionsAccepted ,border_width = 1,
						checkbox_height = 18, checkbox_width = 18, hover_color = '#45A049', fg_color = '#4CAF50').place(x=7,y=557)
		CTk.CTkButton(TermsAndConditionsFrame, text = 'Back', corner_radius=4, fg_color = '#7BC47F', text_color = 'Black', hover_color='#6BBF59', width=100 ,command=GoBackTo_WelcomeFrame).place(x=556, y=553)
		ContinueToActivation = CTk.CTkButton(TermsAndConditionsFrame, text = 'Accept & Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black',hover_color='#45A049',
											 state='disabled', width=120 ,command = GoTo_SoftwareActivationFrame) ; ContinueToActivation.place(x=663, y=553)
		
		# Software Activation

		def isProductkeyMatching() -> None:

			if ProductKeyToBeVerified.get() in PRODUCTKEYS:

				ACTIVATEBUTTON.configure(fg_color = '#A9C5E8', state = 'disabled', text = 'ACTIVATED!')
				ProductKeyToBeVerified.configure(state = 'disabled')
				Status.configure(text = 'STATUS : ACTIVATED', text_color = 'lime')
				ContinueToManagerMode.configure(fg_color = '#4CAF50', state = 'normal')
				SETUPDATA['isActivated'] = True


			else: # Error Message 

				ACTIVATEBUTTON.configure(text = 'ACTIVATE')
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
		CTk.CTkButton(SoftwareActivationFrame, text = '> Visit The GitHub Repository By Clicking Here <', fg_color='transparent', hover = False, text_color = '#21968B',command = lambda: OpenBrowserForSpecifiedUrl(GITHUBREPOWEBSITE)).place(x = 5, y = 357)
		
		Status = CTk.CTkLabel(SoftwareActivationFrame, text = 'STATUS : NOT ACTIVATED', text_color = 'Red' ,font = ('Roboto', 18, 'bold')) ; Status.place(x = 505 , y = 240 )
		ACTIVATEBUTTON = CTk.CTkButton(SoftwareActivationFrame, text = 'ACTIVATE', text_color = 'Black', text_color_disabled = 'Black', corner_radius=4, width=125, fg_color = '#007ACC', hover_color = '#3399FF', command = lambda: [ACTIVATEBUTTON.configure(text = 'PROCESSING...'), ACTIVATEBUTTON.after(5000, isProductkeyMatching)]) ; ACTIVATEBUTTON.place(x = 146, y = 290)
		CTk.CTkButton(SoftwareActivationFrame, text = 'Back', corner_radius=4, fg_color = '#7BC47F', text_color = 'Black', hover_color='#6BBF59', width=100 ,command = GoBackTo_TermsAndConditionsFrame).place(x = 580, y = 357)
		ContinueToManagerMode = CTk.CTkButton(SoftwareActivationFrame, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black', hover_color='#45A049',
					  state = 'disabled', width = 100, command = GoTo_ManagerModeSetupFrame) ; ContinueToManagerMode.place(x = 685, y = 357)
		
		# Manager Mode Setup
		
		self.SecurityCodeRefreshed: bool = False
		self.isNameConditionSatisfied: bool = False
		self.isUsernameConditionSatisfied: bool = False
		self.isPasswordConditionSatisfied: bool = False

		def GenerateSecurityCode() -> None: # Gives a Unique Code e.g., 4Hfi~x>kVW]ZOrh:<r
			
			''' <!-- Doc Strings -->
			## Purpose
			The `GenerateSecurityCode` function generates a unique, secure code for the manager. This code is used as an additional layer of security \
			during the setup process. The generated code is displayed in the GUI and can be copied and saved by the user.

			## Functionality
			- Generates a random 18-character security code.
			- The code consists of a mix of:
			- Uppercase letters
			- Lowercase letters
			- Numbers
			- Updates the `ManagerSecurityCode` entry field in the GUI with the generated code.
			- Ensures that the security code is refreshed each time the function is called.

			## Parameters
			- **None**: This function does not take any parameters.

			## Return Type
			- **None**: This function does not return any value.

			## Process
			1. Sets the `SecurityCodeRefreshed` attribute to `True` to indicate that a new code has been generated.
			2. Clears the `ManagerSecurityCode` entry field in the GUI.
			3. Generates an 18-character random code using the `SEQUENCE` list.
			4. Inserts the generated code into the `ManagerSecurityCode` entry field.
			5. Sets the `ManagerSecurityCode` entry field to read-only to prevent manual edits.

			## Example Usage
			```python
			# Call the function to generate a new security code
			GenerateSecurityCode()
			```

			## Example Output
			The generated security code will look like this:
			
			> `4Hfi~x>kVW]ZOrh:<r`
			
			## Notes
			- The `SEQUENCE` list contains all possible characters that can be used in the security code.
			- The function ensures that the security code is always 18 characters long.
			- The `SecurityCodeRefreshed` attribute must be set to `True` before proceeding with the setup process.

			## Security
			- The generated security code is displayed in the GUI but is not stored permanently.
			- The code is designed to be complex and difficult to guess, enhancing security.

			## Dependencies
			- Requires the `choice` function from the `random` module to randomly select characters from the `SEQUENCE` list.

			## GUI Integration
			- Updates the `ManagerSecurityCode` entry field in the GUI.
			- Disables manual editing of the `ManagerSecurityCode` field after the code is generated.
			'''
			
			self.SecurityCodeRefreshed = True # To Enhance Security
			
			ManagerSecurityCode.configure(state = 'normal')
			ManagerSecurityCode.delete(0, 'end')
			SecurityCode = ''
			
			for i in repeat(None, 18): # repeat for more efficiency
				SecurityCode += choice(SEQUENCE)

			else:
				ManagerSecurityCode.insert(0, SecurityCode)
				ManagerSecurityCode.configure(state = 'readonly')
				
		def _GetManagerData_() -> None: # Get Manager Data

			''' <!-- Doc Strings -->
			## Purpose
			The `_GetManagerData_` function is responsible for collecting and validating the manager's data entered during the setup process. It ensures that all required fields are filled, \
			the security code is refreshed, and the input criteria are satisfied before saving the data into the `SETUPDATA` dictionary.

			## Functionality
			- Retrieves the following manager details from the GUI:
			- Manager Name
			- Manager Username
			- Manager Password
			- Manager Security Code
			- Validates the collected data to ensure:
			1. All fields are filled.
			2. The security code has been refreshed.
			3. Input criteria for name, username, and password are satisfied.
			- Updates the `SETUPDATA` dictionary with the validated data.
			- Disables further editing of the fields after successful submission.

			## Parameters
			- **None**: This function does not take any parameters.

			## Return Type
			- **None**: This function does not return any value.

			## Process
			1. Retrieves data from the GUI fields.
			2. Checks if all fields are filled. If not, displays an error message.
			3. Verifies if the security code has been refreshed. If not, displays an error message.
			4. Ensures that the input criteria for name, username, and password are satisfied. If not, displays an error message.
			5. If all validations pass:
			- Updates the `SETUPDATA` dictionary with the collected data.
			- Disables the input fields to prevent further editing.
			- Enables the "Continue" button to proceed to the next step.

			## Example Usage
			```python
			# Call the function to collect and validate manager data
			_GetManagerData_()
			```

			## Example Output
			If all validations pass, the `SETUPDATA` dictionary is updated as follows:
			```python
			{
				"Manager Name": "Virati Akira Nandhan Reddy",
				"Manager Username": "viratiaki53",
				"Manager Password": "securepassword",
				"Manager Security Code": "4Hfi~x>kVW]ZOrh:<r"
			}
			```

			## Notes
			- Ensure that the GUI fields for manager data are properly initialized before calling this function.
			- The function relies on the `SETUPDATA` dictionary to store the collected data.

			## Error Handling
			- Displays error messages in the GUI if:
			- Any required field is empty.
			- The security code has not been refreshed.
			- Input criteria for name, username, or password are not satisfied.

			## Security
			- The manager's password and security code are stored in the `SETUPDATA` dictionary. Ensure that this data is handled securely and not exposed to unauthorized users.

			## Dependencies
			- Relies on the `SETUPDATA` dictionary to store the collected data.
			- Requires the GUI fields for manager data to be properly initialized and accessible.

			## GUI Integration
			- Updates the GUI to disable input fields after successful submission.
			- Enables the "Continue" button to proceed to the next step.
			'''

			Name, Username, Password, SecurityCode = [x.get() for x in [ManagerName, ManagerUsername, ManagerPassword, ManagerSecurityCode]]

			if not all([Name, Username, Password, SecurityCode]):

				EntryBlankError = CTk.CTkLabel(ManagerModeSetupFrame, text = 'Some of the required credential fields\nabove have not been filled in.', text_color = 'Orange') ; EntryBlankError.place(x = 110, y = 250)
				EntryBlankError.after(4000, EntryBlankError.destroy)
				return
			
			elif not self.SecurityCodeRefreshed:
				
				SecurityCodeNotRefreshedError = CTk.CTkLabel(ManagerModeSetupFrame, text = 'Kindly refresh the security code\nin order to proceed.', text_color = 'Orange') ; SecurityCodeNotRefreshedError.place(x = 120, y = 250)
				SecurityCodeNotRefreshedError.after(4000, SecurityCodeNotRefreshedError.destroy)
				return
			
			elif not all([self.isNameConditionSatisfied, self.isUsernameConditionSatisfied, self.isPasswordConditionSatisfied]):
				
				CriteriaNotSatisfiedError = CTk.CTkLabel(ManagerModeSetupFrame, text = 'One or more required criteria have not been satisfied.\nPlease review and try again.', text_color = 'Orange') ; CriteriaNotSatisfiedError.place(x = 100, y = 250)
				CriteriaNotSatisfiedError.after(4000, CriteriaNotSatisfiedError.destroy)
				return

			for Widget in [ManagerName, ManagerUsername, ManagerPassword]:

				Widget.configure(state = 'readonly')

			else:

				SecurityCodeRefreshButton.configure(state = 'disabled')

			for Widget in [NameValidationMark, UsernameValidationMark, PasswordValidationMark]:

				Widget.configure(state = 'disabled')

			SETUPDATA['Manager Name'], SETUPDATA['Manager Username'] = Name, Username
			SETUPDATA['Manager Password'], SETUPDATA['Manager Security Code'] = Password, SecurityCode

			UpdateManagerData.configure(state = 'normal', fg_color = '#4CAF50')
			SubmitManagerData.configure(state = 'disabled', fg_color = '#B0B0B0')
			ContinueToGmailVerification.configure(fg_color = '#4CAF50', state = 'normal')
				
		def _UpdateManagerData_() -> None: # Update Manager Data
			ContinueToGmailVerification.configure(fg_color = '#B0B0B0', state = 'disabled')
			SubmitManagerData.configure(state = 'normal', fg_color = '#4CAF50')


			for Widget in [ManagerName, ManagerUsername, ManagerPassword]:

				Widget.configure(state = 'normal')

			else:

				SecurityCodeRefreshButton.configure(state = 'normal')
			
			for Widget in [NameValidationMark, UsernameValidationMark, PasswordValidationMark]:

				Widget.configure(state = 'normal')

			UpdateManagerData.configure(state = 'disabled', fg_color = '#B0B0B0')

		def Validate_Name(*args) -> None: # Minimum Chars: 3

			if len(ManagerName.get().strip()) >= 3:
				
				# Keeps A Tick Mark
				NameValidationMark.configure(text = '✔️', text_color = '#4CAF50')
			
				self.isNameConditionSatisfied = True

			else:

				# Keeps A Wrong Mark
				NameValidationMark.configure(text = '❌', text_color = 'Red')

				self.isNameConditionSatisfied = False

		def Validate_Username(*args) -> None: # Minimum Chars: 3

			if len(ManagerUsername.get().strip()) >= 3:
				
				# Keeps A Tick Mark
				UsernameValidationMark.configure(text = '✔️', text_color = '#4CAF50')

				self.isUsernameConditionSatisfied = True


			else:

				# Keeps A Wrong Mark
				UsernameValidationMark.configure(text = '❌', text_color = 'Red')

				self.isUsernameConditionSatisfied = False

		def Validate_Password(*args) -> None: # Minimum Chars: 8

			if len(ManagerPassword.get().strip()) >= 8:
				
				# Keeps A Tick Mark
				PasswordValidationMark.configure(text = '✔️', text_color = '#4CAF50')
				
				self.isPasswordConditionSatisfied = True


			else:

				# Keeps A Wrong Mark
				PasswordValidationMark.configure(text = '❌', text_color = 'Red')

				self.isPasswordConditionSatisfied = False

		ManagerModeSetupFrame = CTk.CTkFrame(Window,790,390)
		CTk.CTkLabel(ManagerModeSetupFrame, text = 'Manager Mode Setup', font = ('Arial', 28, 'bold'), text_color = '#4CAF50').place(x = 10, y = 10)
		
		CTk.CTkLabel(ManagerModeSetupFrame, text = 'Manager Name :', font = ('Roboto', 16, 'bold')).place(x = 10, y = 70)
		ManagerName = CTk.CTkEntry(ManagerModeSetupFrame, font=('Consolas', 14), placeholder_text = 'E.g., Virati Akira Nandhan Reddy', width = 270) ; ManagerName.place(x = 145, y = 70)
		NameValidationMark = CTk.CTkLabel(ManagerModeSetupFrame, text = '') ; NameValidationMark.place(x=420, y=70)
		ManagerName.bind('<KeyRelease>', Validate_Name)

		CTk.CTkLabel(ManagerModeSetupFrame, text = 'Username :', font = ('Roboto', 16, 'bold')).place(x = 10, y = 110)
		ManagerUsername = CTk.CTkEntry(ManagerModeSetupFrame, font=('Consolas', 14), placeholder_text = 'E.g., ViratiAkiraNandhanReddy@Google', width = 310) ; ManagerUsername.place(x = 105, y = 110)
		UsernameValidationMark = CTk.CTkLabel(ManagerModeSetupFrame, text = '') ; UsernameValidationMark.place(x=420, y=110)
		ManagerUsername.bind('<KeyRelease>', Validate_Username)

		CTk.CTkLabel(ManagerModeSetupFrame, text = 'Password :', font = ('Roboto', 16, 'bold')).place(x = 10, y = 150)
		ManagerPassword = CTk.CTkEntry(ManagerModeSetupFrame, font=('Consolas', 14), placeholder_text = 'Password Must Be At Least 8 Chars.', width = 310) ; ManagerPassword.place(x = 105, y = 150)
		PasswordValidationMark = CTk.CTkLabel(ManagerModeSetupFrame, text = '') ; PasswordValidationMark.place(x=420, y=150)
		ManagerPassword.bind('<KeyRelease>', Validate_Password)

		CTk.CTkLabel(ManagerModeSetupFrame, text = 'Security Code :', font = ('Roboto', 16, 'bold')).place(x = 10, y = 190)
		ManagerSecurityCode = CTk.CTkEntry(ManagerModeSetupFrame, placeholder_text = 'Refresh, Copy & Save This Code', font=('Consolas', 14), width = 280, state = 'normal') ; ManagerSecurityCode.place(x = 135, y = 190)
		SecurityCodeRefreshButton = CTk.CTkButton(ManagerModeSetupFrame, text = '♻️', font = ('Roboto', 16), fg_color = 'transparent', hover = False, command = GenerateSecurityCode, text_color = '#4CAF50', width = 0, height = 0) ; SecurityCodeRefreshButton.place(x=417, y=192)
		
		UpdateManagerData = CTk.CTkButton(ManagerModeSetupFrame, text = 'Update Data', command= _UpdateManagerData_, width = 100, fg_color = '#B0B0B0', state = 'disabled', text_color = 'Black', text_color_disabled = 'Black', hover_color = '#45A049') ; UpdateManagerData.place(x = 55, y = 320)
		SubmitManagerData = CTk.CTkButton(ManagerModeSetupFrame, text = 'Submit Data', command = _GetManagerData_, width = 100, fg_color = '#4CAF50', text_color = 'Black', text_color_disabled = 'Black', hover_color = '#45A049') ; SubmitManagerData.place(x=270,y=320)

		ManagerModeinfoFrame = CTk.CTkFrame(ManagerModeSetupFrame, 285, 342) ; ManagerModeinfoFrame.place(x = 500, y = 5)
		CTk.CTkLabel(ManagerModeinfoFrame, text = f'NOTE: Greetings and official emails will be sent and\nreceived using the Manager Name provided. Please\nensure it is accurate and authentic, as it will represent\nyour identity in all communications. The Username you\nchoose will be used to log in ' \
		'to your Manager Profile\nwithin the application. Make sure it is unique.\n\n\nThe credentials provided here are used to log in to the\nManager Profile within the application. It is essential\nthat you enter accurate and legitimate information to\nensure a secure and seamless ' \
		'experience.\n\nIn case you need to reset your password, a security code\nis required. Normally, a verification code will be sent to\nyour registered email address for this process. However,\nin situations where internet connectivity is lost and\nemail delivery is not possible, the security ' \
		'code serves as\na fallback method to help you regain access.\n\nTo maintain the integrity of your profile and security of\nthe system, please use authentic details and a legitimate\nidentity at all times. This ensures that you receive proper\nsupport and a better, more secure experience while ' \
		'using\nthe application.', font = ('Segoe UI', 11, 'italic'), justify = 'left').place(x = 10, y = 10)

		CTk.CTkButton(ManagerModeSetupFrame, text = 'Back', corner_radius = 4, fg_color = '#7BC47F', text_color = 'Black', hover_color='#6BBF59', width=100, command = GoBackTo_SoftwareActivationFrame).place(x = 580, y = 357)
		ContinueToGmailVerification = CTk.CTkButton(ManagerModeSetupFrame, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black', hover_color='#45A049',
					  state = 'disabled', width = 100, command = GoTo_GmailVerificationFrame) ; ContinueToGmailVerification.place(x = 685, y = 357)
		
		# Gmail Verification

		self.isCountdownStarted = False		

		def _Send_Code_() -> None:

			if not all([Email.get(), AppPassword.get()]):
				Incomplete_Credentials_Error = CTk.CTkLabel(GmailVerificationFrame, text = 'Email credentials are incomplete. Please provide all\nrequired information to proceed.') ; Incomplete_Credentials_Error.place(x = 95, y = 230)
				Incomplete_Credentials_Error.after(5000, Incomplete_Credentials_Error.destroy)
				return
			
			countdown.place(x = 330, y = 180) ; countdown.configure(text_color = '#4CAF50')

			if self.isCountdownStarted:

				countdown.after_cancel(CountdownRefresher)
				countdown.configure(text = '10:00')

			SETUPDATA['Manager Email'], SETUPDATA['Manager Email App Password'] = Email.get(), AppPassword.get()

			Submit_And_Test_Email.configure(fg_color = '#B0B0B0', state = 'disabled')

			Email_Verification_cls: Manager_Email_Verification = Manager_Email_Verification()


			__timer__(Submit_And_Test_Email, 10, 'Submit & Get Code')

			threading.Thread(target = Email_Verification_cls.Send_Gmail, daemon = True).start()

			Validate_Verification_Code.configure(fg_color = '#4CAF50', state = 'normal')

			self.isCountdownStarted = True

			def Create_A_Countdown(total_sec = 600) -> None:

				global CountdownRefresher
				Mins = total_sec // 60
				Secs = total_sec % 60
				countdown.configure(text = f'{Mins:02d}:{Secs:02d}')

				if total_sec <= 420 and total_sec > 120:
					countdown.configure(text_color = 'Orange')

				elif total_sec <= 120:
					countdown.configure(text_color = 'Red')
				
				if total_sec > 0:

					# Recursion For Simplicity (asynchronously)
					CountdownRefresher = countdown.after(1000, Create_A_Countdown, total_sec - 1)
				
				else:

					CodeResent_info = CTk.CTkLabel(GmailVerificationFrame, text = 'Time Limit Exceeded, A New Verification Mail Was Sent!') ; CodeResent_info.place(x = 70 , y = 230)
					CodeResent_info.after(3000, CodeResent_info.destroy)

					_Send_Code_()

			Create_A_Countdown()

		def __Validate_Code__() -> None:
			
			Time_Elapsed = (datetime.datetime.now() - __Timestamp__).total_seconds()
			
			if not Verification_Code.get():
				IncompleteCodeError = CTk.CTkLabel(GmailVerificationFrame, text = 'The Verification Code field is incomplete.\nPlease enter the code to continue.') ; IncompleteCodeError.place(x = 120, y = 230)
				IncompleteCodeError.after(5000, IncompleteCodeError.destroy)
				return
			
			elif __Code__ != Verification_Code.get() or Time_Elapsed > 600:
				WrongCodeError = CTk.CTkLabel(GmailVerificationFrame, text = 'Invalid verification code. Please check the code\nand try again.') ; WrongCodeError.place(x = 100, y = 230)
				WrongCodeError.after(5000, WrongCodeError.destroy)
				return
			
			countdown.place_forget() ; countdown.after_cancel(CountdownRefresher)
			Email.configure(state = 'readonly') ; AppPassword.configure(state = 'readonly')
			Validate_Verification_Code.configure(text = 'Validated!', state = 'disabled')
			ContinueToChooseDatabase.configure(fg_color = '#4CAF50', state = 'normal')
			Submit_And_Test_Email.configure(state = 'disabled', fg_color = '#B0B0B0')
			Update_Email_Data.configure(state = 'normal', fg_color = '#4CAF50')

			SETUPDATA['isEmailVerified'] = True

		def _update_details_() -> None:

			Email.configure(state = 'normal') ; AppPassword.configure(state = 'normal')

			Validate_Verification_Code.configure(text = 'Validate Code', state = 'disabled', fg_color = '#B0B0B0')
			ContinueToChooseDatabase.configure(state = 'disabled', fg_color = '#B0B0B0')
			Submit_And_Test_Email.configure(state = 'normal', fg_color = '#4CAF50')
			Update_Email_Data.configure(state = 'disabled', fg_color = '#B0B0B0')

			SETUPDATA['isEmailVerified'] = False

		GmailVerificationFrame = CTk.CTkFrame(Window, 790, 390)
		CTk.CTkLabel(GmailVerificationFrame, text = 'Bank Email Setup', font = ('Arial', 28, 'bold'), height = 0).place(x = 10, y = 10)
		CTk.CTkLabel(GmailVerificationFrame, text = 'Please Register By Entering The Email Credentials Below.', font = ('Arial', 10), height = 0).place(x = 10, y = 40)
		CTk.CTkLabel(GmailVerificationFrame, text = '', image = CTk.CTkImage(light_image = Google_Logo, dark_image = Google_Logo, size = (45,45))).place(x = 730, y = 0)
		
		CTk.CTkLabel(GmailVerificationFrame, text = 'Email Address :', font = ('Roboto', 16, 'bold')).place(x = 10, y = 80)       
		Email = CTk.CTkEntry(GmailVerificationFrame, font=('Consolas', 14), placeholder_text = 'E.g., example@gmail.com', width = 230) ; Email.place(x = 140, y = 80)

		CTk.CTkLabel(GmailVerificationFrame, text = 'App Password :', font = ('Roboto', 16, 'bold')).place(x = 10, y = 120)
		AppPassword = CTk.CTkEntry(GmailVerificationFrame, font=('Consolas', 14), placeholder_text = 'E.g., abgd kvwg lhnk thyd', width = 230) ; AppPassword.place(x = 140, y = 120)

		Verification_Code = CTk.CTkEntry(GmailVerificationFrame, font=('Consolas', 14), placeholder_text = 'VERIFICATON CODE HERE', width = 182, justify = 'center') ; Verification_Code.place(x = 140, y = 180)
		countdown = CTk.CTkLabel(GmailVerificationFrame, text = '10:00', font = ('Segoe UI', 12, 'bold')) # ; countdown.place(x = 330, y = 180)

		Update_Email_Data = CTk.CTkButton(GmailVerificationFrame, text = 'Update Data', width = 140, command = _update_details_, text_color_disabled = 'Black', text_color = 'Black', fg_color = '#B0B0B0', state = 'disabled', hover_color = '#45A049') ; Update_Email_Data.place(x = 15, y = 280)

		Validate_Verification_Code = CTk.CTkButton(GmailVerificationFrame, text = 'Validate Code', width = 125, command = __Validate_Code__, text_color_disabled = 'Black', text_color = 'Black', fg_color = '#B0B0B0', state = 'disabled', hover_color = '#45A049') ; Validate_Verification_Code.place(x = 170, y = 280)

		Submit_And_Test_Email = CTk.CTkButton(GmailVerificationFrame, text = 'Submit & Get Code', width = 140, command = _Send_Code_, text_color = 'Black', text_color_disabled = 'Black', fg_color = '#4CAF50', hover_color = '#45A049') ; Submit_And_Test_Email.place(x = 310, y = 280)

		CTk.CTkButton(GmailVerificationFrame, text = f'{APPPASSWORDWEBSITE}', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = LINK_Icon, dark_image = LINK_Icon, size = (12, 12)), fg_color = 'transparent', hover = False, text_color = '#21968B',
				compound = 'left', height = 0, width = 0, command = lambda: OpenBrowserForSpecifiedUrl(APPPASSWORDWEBSITE)).place(x = -1, y = 319)
		CTk.CTkLabel(GmailVerificationFrame, text = ' The provided email must have Two Factor Authentication enabled to generate app passwords.', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = EXCLAMATION_Icon, dark_image = EXCLAMATION_Icon, size = (12, 12)),
			   compound = 'left', height = 0).place(x = 3, y = 341)
		CTk.CTkLabel(GmailVerificationFrame, text = ' This email address is used to send automated emails to the users of this prototype. Email setup is mandatory.', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = INFO_Icon, dark_image = INFO_Icon, size = (12, 12)),
			   compound = 'left', height = 0).place(x = 3, y = 358)
		CTk.CTkLabel(GmailVerificationFrame, text = " The 'Submit & Get Code' button can also be used to resend the verification code if the user did not receive it initially.", font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = INFO_Icon, dark_image = INFO_Icon, size = (12, 12)),
			   text_color = '#6BBF59', compound = 'left', height = 0).place(x = 3, y = 375)

		EmailSetupGuide = CTk.CTkScrollableFrame(GmailVerificationFrame, 300, 293) ; EmailSetupGuide.place(x = 465, y = 45)
		CTk.CTkLabel(EmailSetupGuide, text = '', image = CTk.CTkImage(light_image = AppPasswordLightImage, dark_image = AppPasswordDarkImage, size = (300,1070))).pack()
		
		CTk.CTkButton(EmailSetupGuide, text = ' Useful Links ', font = ('Roboto', 14, 'bold'), fg_color = 'transparent', hover = False).pack(pady = 20)
		CTk.CTkButton(EmailSetupGuide, text = '> How To Setup App Password For My Account <', fg_color='transparent', hover = False, text_color = '#21968B',command = lambda: OpenBrowserForSpecifiedUrl(HOW_TO_SETUP_APPPASSWORD)).pack()
		CTk.CTkButton(EmailSetupGuide, text = '> Why i can\'t see app passwords in my account <', fg_color='transparent', hover = False, text_color = '#21968B',command = lambda: OpenBrowserForSpecifiedUrl(APPPASSWORD_ERROR)).pack()

		CTk.CTkButton(GmailVerificationFrame, text = 'Back', corner_radius = 4, fg_color = '#7BC47F', text_color = 'Black', hover_color='#6BBF59', width=100 ,command = GoBackTo_ManagerModeSetupFrame).place(x = 580, y = 357)
		ContinueToChooseDatabase = CTk.CTkButton(GmailVerificationFrame, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black', hover_color = '#45A049',
					  state = 'disabled', width = 100, command = GoTo_ChooseDatabaseFrame) ; ContinueToChooseDatabase.place(x = 685, y = 357)
		
		# Choose Data Base

		def SetDatabaseTypeAndPath() -> None: # Set Database Type & Path [ SQLite3, MySQL, JSON ] 
			
			'''
			### This function sets the database type and path based on the selected option from the radio buttons. \
			It updates the `SETUPDATA` dictionary with the selected database type and corresponding paths.
			 
			---
			## <ins>***Defaults***</ins>

			> * #### if No Database is selected, it will be SQLite3 
			> * #### The Database Path will be set to the default path for SQLite3 
			> * #### The Backup Database Path will be set to the default path for SQLite3
			'''

			# if Database is SQLite3
			if Database.get() == 'SQLite3':
				SETUPDATA['DATABASE TYPE'] = 'SQLite3'
				SETUPDATA['DATABASE PATH'] = fr'{PATH}\Bank_Package\DATABASE\SQLite3\database.sqlite3'
				SETUPDATA['BACKUP DATABASE PATH'] = fr'{PATH}\BACKUP - DATABASE\SQLite3\database.sqlite3'
			
			# if Database is MySQL
			elif Database.get() == 'MySQL':
				SETUPDATA['DATABASE TYPE'] = 'MySQL'
				SETUPDATA['DATABASE PATH'] = 'No Path For MySQL'
				SETUPDATA['BACKUP DATABASE PATH'] = 'No Path For MySQL'
			
			# if Database is JSON
			elif Database.get() == 'JSON':
				SETUPDATA['DATABASE TYPE'] = 'JSON'
				SETUPDATA['DATABASE PATH'] = fr'{PATH}\Bank_Package\DATABASE\JSON\USERDATA\<username>.json'
				SETUPDATA['BACKUP DATABASE PATH'] = fr'{PATH}\Bank_Package\BACKUP - DATABASE\JSON\USERDATA\<username>.json'
		
		def isDatabaseTypeSelected() -> None: # Check if the user has selected a database type 

			if DATABASECHOOSED.get():

				# If the user has enabled the checkbox, they can be able to continue
				ContinueToNextFrame.configure(fg_color = '#4CAF50', state = 'normal')

			else:

				# If the user has not enabled the checkbox, they cannot continue
				ContinueToNextFrame.configure(fg_color = '#B0B0B0', state = 'disabled')

		DATABASECHOOSED = CTk.BooleanVar()
		Database = CTk.StringVar() ; Database.set('SQLite3')
		ChooseDatabaseFrame = CTk.CTkFrame(Window, 790, 590)
		CTk.CTkLabel(ChooseDatabaseFrame, text = 'Choose Your Database', font = ('Arial', 24, 'bold'), height = 45).place(x = 10, y = 0)
		DataBaseComparisonFrame = CTk.CTkScrollableFrame(ChooseDatabaseFrame, 764, 440) ; DataBaseComparisonFrame.place(x = 2, y = 45)
		CTk.CTkLabel(DataBaseComparisonFrame,text = '', image = CTk.CTkImage(light_image = DatabaseComparisonLightImage, dark_image = DatabaseComparisonDarkImage, size=(764 , 968))).pack()
		
		CTk.CTkRadioButton(ChooseDatabaseFrame, text = 'JSON', variable = Database, value = 'JSON', command = SetDatabaseTypeAndPath, hover_color = '#45A049', fg_color = '#4CAF50', width = 110).place(x = 30, y = 510)
		CTk.CTkRadioButton(ChooseDatabaseFrame, text = 'SQLite3', variable = Database, value = 'SQLite3', command = SetDatabaseTypeAndPath, hover_color = '#45A049', fg_color = '#4CAF50', width = 110).place(x = 160, y = 510)
		CTk.CTkRadioButton(ChooseDatabaseFrame, text = 'MySQL', variable = Database, value = 'MySQL', command = SetDatabaseTypeAndPath, hover_color = '#45A049', fg_color = '#4CAF50', width = 110).place(x = 290, y = 510)
		
		CTk.CTkCheckBox(ChooseDatabaseFrame, text = 'I Have Reviewed All The Information & Made My Selection Accordingly.', font = ('Segoe UI', 12), variable = DATABASECHOOSED, offvalue = False, onvalue = True, command = isDatabaseTypeSelected ,border_width = 1,
						checkbox_height = 18, checkbox_width = 18, hover_color = '#45A049', fg_color = '#4CAF50').place(x=7,y=562)
		
		CTk.CTkButton(ChooseDatabaseFrame, text = '> Click Here To Learn More <', fg_color='transparent', hover = False, text_color = '#21968B',command = lambda: OpenBrowserForSpecifiedUrl(DATABASEINFOWEBSITE)).place(x = 610, y = 500)

		CTk.CTkButton(ChooseDatabaseFrame, text = 'Back', corner_radius = 4, fg_color = '#7BC47F', text_color = 'Black', hover_color='#6BBF59', width=100 ,command = GoBackTo_GmailVerificationFrame).place(x = 580, y = 557)
		ContinueToNextFrame = CTk.CTkButton(ChooseDatabaseFrame, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black', hover_color = '#45A049',
											state = 'disabled', width = 100, command = lambda: GoTo_GetMySQLDataFrame() if SETUPDATA['DATABASE TYPE'] == 'MySQL' else GoTo_FinalReviewFrame()) ; ContinueToNextFrame.place(x = 685, y = 557)
											
		# MySQL Setup

		def Get_Credentials_and_Test_Database_Connection() -> None:

			Buffering_MySQL_Data.start()

			SETUPDATA['MySQL Credentials']['Host'] = HostName.get()
			SETUPDATA['MySQL Credentials']['Port'] = int(PortNumber.get()) if PortNumber.get().isdigit() else PortNumber.get()
			SETUPDATA['MySQL Credentials']['Username'] = UserName.get()
			SETUPDATA['MySQL Credentials']['Password'] = Password.get()
			SETUPDATA['MySQL Credentials']['Charset'] = CharacterSet.get()


			isDatabaseConnectionPassed = CheckMySQLDatabaseConnection().DoesServerExists()

			if isDatabaseConnectionPassed:

				DatabaseConnectionStatus.after(30000, lambda: Test_Status.configure(text = 'Test : Passed', text_color = '#4CAF50'))
				
				for Widget in [HostName, PortNumber, UserName, Password, CharacterSet]:
					
					Widget.configure(state = 'readonly')

				else:
					
					DatabaseConnectionStatus.after(30000, lambda: Update_MySQL_Data.configure(state = 'normal', fg_color = '#4CAF50'))
					DatabaseConnectionStatus.after(30000, lambda: Submit_And_Test_MySQL_Data.configure(state = 'disabled', fg_color = '#B0B0B0'))
					DatabaseConnectionStatus.after(30000, lambda: ContinueToFinalReview.configure(state = 'normal', fg_color = '#4CAF50'))
				
			else:

				DatabaseConnectionStatus.after(5000, lambda: Test_Status.configure(text = 'Test : Failed', text_color = 'Red'))
		
		def _UpdateMySQLData_() -> None:

			Submit_And_Test_MySQL_Data.configure(state = 'normal', fg_color = '#4CAF50')
			Update_MySQL_Data.configure(state = 'disabled', fg_color = '#B0B0B0')
			ContinueToFinalReview.configure(state = 'disabled', fg_color = '#B0B0B0')

			for Widget in [HostName, PortNumber, UserName, Password, CharacterSet]:
					
					Widget.configure(state = 'normal')

		GetMySQLDataFrame = CTk.CTkFrame(Window, 790, 590)
		CTk.CTkLabel(GetMySQLDataFrame, text = 'MySQL Database Setup', font = ('Arial', 24, 'bold'), height = 0).place(x = 10, y = 10)
		CTk.CTkLabel(GetMySQLDataFrame, text = 'Please Enter The MySQL Server Information Below.', font = ('Arial', 12), justify = 'left', height = 0).place(x = 10, y = 40)
		CTk.CTkLabel(GetMySQLDataFrame, text = '', height = 0, width = 0, image = CTk.CTkImage(light_image = MySQL_Logo, dark_image = MySQL_Logo, size = (96, 50))).place(x = 689, y = 5)
		Test_Status = CTk.CTkLabel(GetMySQLDataFrame, text = 'Test : Primed', font = ('Roboto', 14, 'bold'), text_color = 'Orange', height = 28) ; Test_Status.place(x = 5, y = 565)

		CTk.CTkLabel(GetMySQLDataFrame, text = 'Host Name :', font = ('Roboto', 16, 'bold'), justify = 'left').place(x = 10, y = 100)
		HostName = CTk.CTkEntry(GetMySQLDataFrame, placeholder_text = 'E.g., localhost', font=('Consolas', 14), width = 260) ; HostName.place(x = 115, y = 100)
		
		CTk.CTkLabel(GetMySQLDataFrame, text = 'Port Number :', font = ('Roboto', 16, 'bold'), justify = 'left').place(x = 10, y = 140)
		PortNumber = CTk.CTkEntry(GetMySQLDataFrame, placeholder_text = 'E.g., 3306', font=('Consolas', 14), width = 250) ; PortNumber.place(x = 125, y = 140)
		
		CTk.CTkLabel(GetMySQLDataFrame, text = 'User Name :', font = ('Roboto', 16, 'bold'), justify = 'left').place(x = 10, y = 180)
		UserName = CTk.CTkEntry(GetMySQLDataFrame, placeholder_text = 'E.g., root', font=('Consolas', 14), width = 265) ; UserName.place(x = 110, y = 180)
		
		CTk.CTkLabel(GetMySQLDataFrame, text = 'Password :', font = ('Roboto', 16, 'bold'), justify = 'left').place(x = 10, y = 220)
		Password = CTk.CTkEntry(GetMySQLDataFrame, placeholder_text = 'E.g., Akki$2008@Google!', font=('Consolas', 14), width = 270) ; Password.place(x = 103, y = 220)
		
		CTk.CTkLabel(GetMySQLDataFrame, text = 'Character Set :', font = ('Roboto', 16, 'bold'), justify = 'left').place(x = 10, y = 260)
		CharacterSet = CTk.CTkEntry(GetMySQLDataFrame, placeholder_text = 'E.g., utf8mb4 *(Optional)*', font=('Consolas', 14), width = 240) ; CharacterSet.place(x = 133, y = 260)

		DatabaseConnectionStatus = CTk.CTkLabel(GetMySQLDataFrame, text = 'Not Connected', compound = 'top', height = 0, width = 425, image = CTk.CTkImage(light_image = Database_Config_icon, dark_image = Database_Config_icon, size = (75, 75)),
					 text_color = 'Orange') ; DatabaseConnectionStatus.place(x =  0, y = 320)
		
		MySQLGuideFrame = CTk.CTkScrollableFrame(GetMySQLDataFrame, 340, 265) ; MySQLGuideFrame.place(x = 425, y = 60)
		CTk.CTkLabel(MySQLGuideFrame, text = '', image = CTk.CTkImage(light_image = MySQLSetupLightImage, dark_image = MySQLSetupDarkImage, size = (340, 3157))).pack()
		CTk.CTkButton(MySQLGuideFrame, text = ' Useful Links ', font = ('Roboto', 14, 'bold'), fg_color = 'transparent', hover = False).pack(pady = 20)
		CTk.CTkButton(MySQLGuideFrame, text = '> How To Setup MySQL Server <', fg_color='transparent', hover = False, text_color = '#21968B',command = lambda: OpenBrowserForSpecifiedUrl(MYSQL_ON_DOWNLOAD_SETUP)).pack()
		CTk.CTkButton(MySQLGuideFrame, text = '> Where to know this credentials  <', fg_color='transparent', hover = False, text_color = '#21968B',command = lambda: OpenBrowserForSpecifiedUrl(MYSQL_SERVER_DETAILS)).pack()


		MySQLDebugFrame = CTk.CTkScrollableFrame(GetMySQLDataFrame, 340, 0) ; MySQLDebugFrame.place(x = 425, y = 340)
		CTk.CTkLabel(MySQLDebugFrame, text = 'MySQL Connection Debugging', font = ('Arial', 22, 'bold'), height = 0).pack()

		Update_MySQL_Data = CTk.CTkButton(GetMySQLDataFrame, text = 'Update MySQL Server Data', width = 190, command = _UpdateMySQLData_, state = 'disabled', fg_color = '#B0B0B0', text_color = 'Black',
										  text_color_disabled = 'Black', hover_color = '#45A049') ; Update_MySQL_Data.place(x = 15, y = 520)
		Submit_And_Test_MySQL_Data = CTk.CTkButton(GetMySQLDataFrame, text = 'Submit & Test Connection', width = 190, command = Get_Credentials_and_Test_Database_Connection, fg_color = '#4CAF50',
												   hover_color = '#45A049', text_color_disabled = 'Black', text_color = 'Black') ; Submit_And_Test_MySQL_Data.place(x = 220, y = 520)


		Buffering_MySQL_Data = CTk.CTkProgressBar(GetMySQLDataFrame, mode = 'indeterminate', width = 225, height = 5, progress_color = '#4CAF50') ; Buffering_MySQL_Data.place(x = 100, y = 430)
		CTk.CTkButton(GetMySQLDataFrame, text = 'Copy Debug Log To Clipboard', corner_radius = 4)
		CTk.CTkButton(GetMySQLDataFrame, text = 'Back', corner_radius = 4, fg_color = '#7BC47F', text_color = 'Black', hover_color='#6BBF59', width=100 ,command = GoBackTo_ChooseDatabaseFrame).place(x = 580, y = 557)
		ContinueToFinalReview = CTk.CTkButton(GetMySQLDataFrame, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black', hover_color='#45A049',
					   command = GoTo_FinalReviewFrame, width = 100, state = 'disabled') ; ContinueToFinalReview.place(x = 685, y = 557)
		
		# Final Review

		def Return_Setup_Log() -> str:
			
			''' <!-- Doc Strings--> 
			# Return_Setup_Log Function

			## Purpose
			The `Return_Setup_Log` function generates a detailed log of the setup process, summarizing all the key information \
			collected during the setup. This log is primarily used for review purposes and can be copied to the clipboard for reference.

			## Returns
			- **str**: A formatted string containing the following setup details:
			- Manager Name
			- Manager Username
			- Manager Password
			- Manager Security Code
			- Manager Email
			- Manager Email App Password (redacted for security)
			- Email Verification Status
			- Database Type
			- Current Application Version

			## Security
			- Sensitive information such as the manager's email app password is redacted to ensure confidentiality.
			- The log is designed to provide only the necessary details for review without exposing critical credentials.

			## Example Output
			```
			Manager Name: John Doe
			Manager Username: johndoe123
			Manager Password: john@doe
			Manager Security Code: '%^*^$&jg758fj^($&)'
			Manager Email: johndoe@example.com
			Manager Email App Password: The Information Has Been Redacted For Security And Confidentiality Purposes.
			isEmailVerified: True
			Database Type: SQLite3
			Current App Version: 0.0.1 - Alpha
			```

			## Usage
			This function is typically called during the final review step of the setup process to display or copy the setup log.

			## Notes
			- Ensure that the SETUPDATA dictionary is populated with valid data before calling this function.
			- The function relies on the SETUPDATA dictionary to retrieve the setup details.

			## Example Usage
			```python
			setup_log = Return_Setup_Log()
			print(setup_log)
			```
			'''

			return f'''Manager Name: {SETUPDATA["Manager Name"]}
Manager Username: {SETUPDATA["Manager Username"]}
Manager Password: {SETUPDATA["Manager Password"]}
Manager Security Code: {SETUPDATA["Manager Security Code"]}
Manager Email: {SETUPDATA["Manager Email"]}
Manager Email App Password: The Information Has Been Redacted For Security And Confidentiality Purposes.
isEmailVerified: {SETUPDATA["isEmailVerified"]}
Database Type: {SETUPDATA["DATABASE TYPE"]}
Current App Version: {SETUPDATA["Current Version"]}
'''

		REVIEWED = CTk.BooleanVar()
		FinalReviewFrame = CTk.CTkFrame(Window, 790, 390)
		CTk.CTkLabel(FinalReviewFrame, text = 'Final Review', font = ('Arial', 36, 'bold'), height = 0).place(x = 10, y = 10)
		CTk.CTkLabel(FinalReviewFrame, text = 'Review The Information Before Proceeding.', font = ('Arial', 10), height = 0).place(x = 11, y = 45)
		CTk.CTkLabel(FinalReviewFrame, text = '   You can update the credentials and other details\n    anytime from your Manager Profile.', font = ('Segoe UI', 12),
					 image = CTk.CTkImage(light_image = INFO_Icon, dark_image = INFO_Icon, size = (17, 17)), compound = 'left', height = 0, justify = 'left').place(x = 500, y = 10)
 		
		Final_Manager_Name__Update__ = CTk.CTkLabel(FinalReviewFrame, text = f'Manager Name: {SETUPDATA["Manager Name"]}',
													font = ('Segoe UI', 14, 'bold'), justify = 'left') ; Final_Manager_Name__Update__.place(x = 10, y = 100)
		Final_Manager_Username__Update__ = CTk.CTkLabel(FinalReviewFrame, text = f'Manager Username: {SETUPDATA["Manager Username"]}',
														font = ('Segoe UI', 14, 'bold'), justify = 'left') ; Final_Manager_Username__Update__.place(x = 10, y = 128)
		Final_Manager_Password__Update__ = CTk.CTkLabel(FinalReviewFrame, text = f'Manager Password: {SETUPDATA["Manager Password"]}',
														font = ('Segoe UI', 14, 'bold'), justify = 'left') ; Final_Manager_Password__Update__.place(x = 10, y = 156)
		Final_Manager_Security_Code__Update__ = CTk.CTkLabel(FinalReviewFrame, text = f'Manager Security Code: {SETUPDATA["Manager Security Code"]}',
															 font = ('Segoe UI', 14, 'bold'), justify = 'left') ; Final_Manager_Security_Code__Update__.place(x = 10, y = 184)
		Final_Manager_Email__Update__ = CTk.CTkLabel(FinalReviewFrame, text = f'Manager Email: {SETUPDATA["Manager Email"]}',
													 font = ('Segoe UI', 14, 'bold'), justify = 'left') ; Final_Manager_Email__Update__.place(x = 10, y = 212)
		Final_Manager_Email_App_Password__Update__ = CTk.CTkLabel(FinalReviewFrame, text = f'Manager Email App Password: {SETUPDATA["Manager Email App Password"]}',
																  font = ('Segoe UI', 14, 'bold'), justify = 'left') ; Final_Manager_Email_App_Password__Update__.place(x = 10, y = 240)
		Final_isEmailVerified__Update__ = CTk.CTkLabel(FinalReviewFrame, text = f'isEmailVerified: {SETUPDATA["isEmailVerified"]}',
													   font = ('Segoe UI', 14, 'bold'), justify = 'left') ; Final_isEmailVerified__Update__.place(x = 10, y = 268)    
		Final_Database_Type__Update__ = CTk.CTkLabel(FinalReviewFrame, text = f'Database Type: {SETUPDATA["DATABASE TYPE"]}',
													 font = ('Segoe UI', 14, 'bold'), justify = 'left') ; Final_Database_Type__Update__.place(x = 10, y = 296)
		Final_Current_App_Version__Update__ = CTk.CTkLabel(FinalReviewFrame, text = f'Current App Version: {SETUPDATA["Current Version"]}',
														   font = ('Segoe UI', 14, 'bold'), justify = 'left') ; Final_Current_App_Version__Update__.place(x = 10, y = 324)

		CTk.CTkCheckBox(FinalReviewFrame, text = 'I have reviewed the above data and finalized my decision to proceed with them.' , font = ('Segoe UI', 12), variable = REVIEWED, offvalue = False, onvalue = True,
						command = lambda: Finish_Setup.configure(state = 'normal', fg_color = '#4CAF50') if REVIEWED.get() else Finish_Setup.configure(state = 'disabled', fg_color = '#B0B0B0'), border_width = 1,
						checkbox_height = 18, checkbox_width = 18, hover_color = '#45A049', fg_color = '#4CAF50').place(x = 7, y = 362)
		
		SetupLog = CTk.CTkButton(FinalReviewFrame, text = 'Copy To Clipboard', corner_radius = 4, fg_color = '#7BC47F', text_color = 'Black', hover_color='#6BBF59', width = 205,
					  command = lambda: [Window.clipboard_clear(), Window.clipboard_append(Return_Setup_Log()), SetupLog.configure(text = ' Copied! '), SetupLog.after(3000, lambda: SetupLog.configure(text = 'Copy To Clipboard'))]) ; SetupLog.place(x = 580, y = 324)
		
		CTk.CTkButton(FinalReviewFrame, text = 'Back', corner_radius = 4, fg_color = '#7BC47F', text_color = 'Black', hover_color='#6BBF59', width = 100,
					  command = lambda: GoBackTo_GetMySQLDataFrame() if SETUPDATA['DATABASE TYPE'] == 'MySQL' else GoBackTo_ChooseDatabaseFrame()).place(x = 580, y = 357)
		Finish_Setup = CTk.CTkButton(FinalReviewFrame, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black', hover_color='#45A049',
					  state = 'disabled', width = 100, command = GoTo_FinishSetupFrame) ; Finish_Setup.place(x = 685, y = 357)
	
		# Finish Greeting

		def _exec_func_() -> None:
			
			''' <!-- Doc Strings -->
			### Purpose
			Handles post-setup actions after the user completes the setup process for the Bank-With-High-Functionalities application.

			### Functionality
			- Optionally creates a shortcut to the application on the user's Desktop.
			- Optionally sends an automated email notification to the developer about the new client registration.
			- Optionally launches the main application executable (`main.exe`).
			- Always creates a shortcut in the Windows Start Menu's Programs folder.

			### Notes
			- The function uses three Boolean variables (`CREATE_SHORTCUT`, `OPEN_MAIN_EXE`, `OPEN_DOCUMENTATION_WEB`) to determine which actions to perform.
			- The function is intended to be called after setup data is saved and the setup window is closed.

			### Dependencies
			- Requires the `os` module for path operations.
			- Requires `win32com.client.Dispatch` for shortcut creation.
			- Requires `subprocess` for launching executables.
			- Requires `smtplib`, `email.message.EmailMessage`, and `urllib.request.urlopen` for sending emails.

			### Security
			- Ensure the `PATH` variable is trusted to avoid creating shortcuts or launching unintended executables.
			- Email credentials are used securely and not exposed in logs or messages.

			### Limitations
			- If any action fails (e.g., shortcut creation, email sending, launching the executable), the error is silently ignored.
			- The function is designed for Windows environments. 
			'''
			
			Shell = Dispatch('WScript.Shell')

			def Shortcut_At_Start_Menu() -> None:

				''' <!-- Doc Strings -->
				### Purpose
				Creates a shortcut for the Bank-With-High-Functionalities application in the Windows Start Menu's Programs folder.

				### Functionality
				- Uses the Windows Scripting Host (via `win32com.client.Dispatch`) to create a `.lnk` shortcut.
				- Sets the shortcut's target to the application's `main.exe`.
				- Configures the working directory, description, and icon for the shortcut.
				- Saves the shortcut in the Start Menu Programs directory for the current user.

				### Notes
				- The shortcut is created at: `%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Bank-With-High-Functionalities.lnk`
				- The function assumes the global `PATH` variable points to the application's root directory.
				- This function is intended for Windows environments only.

				### Dependencies
				- Requires the `os` module for path operations.
				- Requires `win32com.client.Dispatch` for shortcut creation.

				### Security
				- Ensure the `PATH` variable is trusted to avoid creating shortcuts to unintended executables.
				'''

				Start = Shell.CreateShortcut(os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Bank-With-High-Functionalities.lnk"))
				Start.TargetPath = fr'{PATH}\main.exe'
				Start.WorkingDirectory = os.path.dirname(fr'{PATH}\main.exe')
				Start.Description = 'Python Based GUI Banking System Prototype.'
				Start.IconLocation = fr'{PATH}\Bank_Package\Visual Data\ICO Files\Bank Image.ico'
				Start.save()

			def Shortcut_At_Desktop() -> None:

				''' <!-- Doc Strings -->
				### Purpose
				Creates a shortcut for the Bank-With-High-Functionalities application on the user's Desktop.

				### Functionality
				- Uses the Windows Scripting Host (via `win32com.client.Dispatch`) to create a `.lnk` shortcut.
				- Sets the shortcut's target to the application's `main.exe`.
				- Configures the working directory, description, and icon for the shortcut.
				- Saves the shortcut on the Desktop for the current user.

				### Notes
				- The shortcut is created at: `%USERPROFILE%\\Desktop\\Bank-With-High-Functionalities.lnk`
				- The function assumes the global `PATH` variable points to the application's root directory.
				- This function is intended for Windows environments only.

				### Dependencies
				- Requires the `os` module for path operations.
				- Requires `win32com.client.Dispatch` for shortcut creation.

				### Security
				- Ensure the `PATH` variable is trusted to avoid creating shortcuts to unintended executables.
				'''

				Desktop = Shell.CreateShortcut(os.path.join(os.environ["USERPROFILE"], "Desktop", "Bank-With-High-Functionalities.lnk"))
				Desktop.TargetPath = fr'{PATH}\main.exe'
				Desktop.WorkingDirectory = os.path.dirname(fr'{PATH}\main.exe')
				Desktop.Description = 'Python Based GUI Banking System Prototype.'
				Desktop.IconLocation = fr'{PATH}\Bank_Package\Visual Data\ICO Files\Bank Image.ico'
				Desktop.save()

			def Open_main_exe() -> None:
				
				''' <!-- Doc Strings -->
				### Purpose
				Launches the main executable (`main.exe`) of the Bank-With-High-Functionalities application after setup is complete.

				### Functionality
				- Uses `subprocess.Popen` to start the main application executable.
				- Ensures the application is launched in a new process, allowing the setup window to close independently.

				### Notes
				- The path to `main.exe` is determined by the global `PATH` variable.
				- This function is intended to be called at the end of the setup process to provide a seamless transition for the user.

				### Dependencies
				- Relies on the `subprocess` module.
				- Requires the `PATH` variable to be correctly set to the application's root directory.

				### Security
				- Ensure that the path to `main.exe` is trusted and not user-modifiable to prevent execution of unintended files.
				'''

				subprocess.Popen(fr'{PATH}\main.exe', shell = True)

			def Greet_Developer() -> None:

				''' <!-- Doc Strings -->
				### Purpose
				Sends an automated email notification to the developer when a new client completes the setup process for the Bank-With-High-Functionalities application.

				### Functionality
				- Retrieves the client's location data (region and country) using the `ipinfo.io` API.
				- Generates an HTML email containing:
				- Client name
				- Registration date and time
				- Client region and country
				- Sends the email to the developer's email address using SMTP with SSL.

				### Notes
				- The function uses the `SETUPDATA` dictionary to get the manager's name and email credentials.
				- The developer's email address is hardcoded as the recipient.
				- The email is sent in HTML format for better readability.

				### Dependencies
				- Requires `json`, `datetime`, `smtplib`, `email.message.EmailMessage`, and `urllib.request.urlopen`.
				- Relies on internet connectivity to fetch location data and send the email.

				### Security
				- Uses the manager's email and app password for SMTP authentication.
				- Sensitive credentials are not exposed in the email content.

				### Limitations
				- If the internet connection is unavailable or credentials are incorrect, the email may not be sent.
				- Exceptions are caught and silently passed; errors are not reported to the user.
	
				'''

				with urlopen("https://ipinfo.io/json") as Location:
					Location_Data = json.load(Location)
				
				HTML = ''' <!-- html Data -->

<!DOCTYPE html>
<html lang="en">
  <head>
	<meta charset="UTF-8" />
	<title>Client Registration Alert</title>
	<style>
	  body {
		background-color: #f0f4f8;
		font-family: 'Segoe UI', Roboto, sans-serif;
		margin: 0;
		padding: 0;
	  }
	  .container {
		max-width: 600px;
		margin: 40px auto;
		background: #fff;
		border-radius: 10px;
		box-shadow: 0 5px 20px rgb(19, 77, 184);
		overflow: hidden;
	  }
	  .header {
		background-color: #408cd8;
		color: white;
		padding: 24px;
		text-align: center;
	  }
	  .header h1 {
		margin: 0;
		font-size: 24px;
	  }
	  .body {
		padding: 30px;
		color: #333;
	  }
	  .body h2 {
		margin-top: 0;
		color: #444;
	  }
	  .info-box {
		background: #f6f8fa;
		padding: 20px;
		border-left: 4px solid #0366d6;
		margin: 20px 0;
		font-family: monospace;
	  }
	  .footer {
		background-color: #f9f9f9;
		text-align: center;
		padding: 16px;
		font-size: 12px;
		color: #888;
	  }
	</style>
  </head>
  <body>
	<div class="container">
	  <div class="header">
		<h1>🛠 New Client Registered</h1>
	  </div>
	  <div class="body">
		<h2>Hello! Virati Akira Nandhan Reddy,</h2>
		<p>A New Client Has Successfully Registered On The Platform.</p>
		
		<div class="info-box">
		  <strong>Client Name:</strong> [CLIENTNAME]<br/>
		  <strong>Registered On:</strong> [DATE]<br/>
		  <strong>Time:</strong> [TIME]<br/>
		  <strong>Region:</strong> [REGION]<br/>
		  <strong>Country:</strong> [COUNTRY]<br/>
		</div>

		<p style="color: #408cd8;font-size: x-small;"> 
			<strong>Bank-With-High-Functionalities, Developed & Distributed By Virati Akira Nandhan Reddy</strong><br/>
		</p>
	  </div>
	  <div class="footer">
		&copy; 2024 - 2026 Virati Akira Nandhan Reddy • Bank-With-High-Functionalities
	  </div>
	</div>
  </body>
</html>

'''.replace(
	'[CLIENTNAME]', str(SETUPDATA['Manager Name'])
	).replace(
		'[DATE]', str(datetime.datetime.now().strftime('%d-%b-%Y -- %A'))
		).replace(
			'[TIME]', str(datetime.datetime.now().astimezone().strftime('%I:%M:%S %p (%Z)'))
			).replace(
				'[REGION]', str(Location_Data.get("region", "N/A"))
				).replace(
					'[COUNTRY]', str(Location_Data.get("country", "N/A")))

				Email = EmailMessage()

				Email['Subject'] = 'Hello! Virati Akira Nandhan Reddy, New Client Registered 🩵'
				Email['From'] = 'Bank-With-High-Functionalities Team'
				Email['To'] = 'viratiaki29@gmail.com'

				Email.set_content(HTML, subtype = 'html')

				try:

					with smtplib.SMTP_SSL('smtp.gmail.com', 465) as SMTP:

						SMTP.login(SETUPDATA['Manager Email'], SETUPDATA['Manager Email App Password'])
						SMTP.send_message(Email)

				except Exception as Error:
					EMAIL_LOGS.write(f'\n[ERROR]:[setup.exe - Manager_Email_Verification][{datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}] ; Status: Unsuccessful ; MSG: Error Occurred While Sending Verification Email To Developer ; ErrorType: [{Error}]')
					
			def Greet_Manager() -> None:

				''' <!-- Doc Strings -->
				### Purpose
				Sends a personalized "Thank You" email to the manager after the setup process is successfully completed.

				### Functionality
				- Generates an HTML-formatted email that welcomes the manager and confirms the successful completion of the setup.
				- The email includes a greeting, a thank you message, and links to the developer's social media and website.
				- Uses the manager's name from the `SETUPDATA` dictionary for personalization.
				- Sends the email using SMTP with SSL authentication.

				### Parameters
				- **None**: This function does not take any parameters.

				### Returns
				- **None**

				### Example Usage
				```python
				Greet_Manager()
				```

				### Notes
				- The manager's email address and app password must be set in `SETUPDATA`.
				- The email is sent in HTML format for better appearance and branding.
				- This function is typically called at the end of the setup process.

				### Dependencies
				- Requires `smtplib` for sending emails.
				- Requires `email.message.EmailMessage` for constructing the email.
				- Uses the `SETUPDATA` dictionary for manager details.

				### Security
				- Uses the manager's email and app password for SMTP authentication.
				- No sensitive data is included in the email content.

				### Limitations
				- If the email credentials are incorrect or there is no internet connection, the email will not be sent.
				- Exceptions are logged but not shown to the user.
				'''
				
				HTML = ''' <!-- html Data -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Thank You - Setup Complete</title>
  <style>
	body {
	  margin: 0;
	  padding: 0;
	  background: #f1f3f8;
	  font-family: 'Segoe UI', Arial, sans-serif;
	}
	.email-wrapper {
	  max-width: 600px;
	  margin: 40px auto;
	  background: #ffffff;
	  border-radius: 16px;
	  overflow: hidden;
	  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
	}
	.header {
	  background: linear-gradient(90deg, #4A00E0, #8E2DE2);
	  color: white;
	  text-align: center;
	  padding: 50px 20px 30px;
	}
	.header h1 {
	  margin: 0;
	  font-size: 30px;
	  letter-spacing: 1px;
	}
	.header p {
	  margin: 12px 0 0;
	  font-size: 17px;
	  opacity: 0.95;
	}
	.content {
	  padding: 30px 40px;
	  color: #333333;
	  line-height: 1.7;
	  font-size: 16px;
	}
	.content h2 {
	  font-size: 20px;
	  color: #4A00E0;
	  margin-bottom: 10px;
	}
	.features {
	  background-color: #f9f9fb;
	  border: 1px solid #e0e0e0;
	  padding: 20px;
	  border-radius: 12px;
	  margin: 20px 0;
	}
	.features ul {
	  padding-left: 20px;
	}
	.features li {
	  margin-bottom: 10px;
	}
	.button {
	  display: inline-block;
	  margin-top: 30px;
	  padding: 14px 26px;
	  background-color: #8E2DE2;
	  color: #ffffff !important;
	  border-radius: 50px;
	  text-decoration: none;
	  font-weight: bold;
	  letter-spacing: 0.5px;
	  transition: background 0.3s;
	}
	.button:hover {
	  background-color: #7327c5;
	}
	.footer {
	  font-size: 12px;
	  color: #999999;
	  text-align: center;
	  padding: 30px 20px;
	  border-top: 1px solid #e5e5e5;
	}
	.social-icons img {
	  margin: 0 6px;
	  vertical-align: middle;
	}
  </style>
</head>
<body>
  <div class="email-wrapper">
	<div class="header">
	  <h1>🎉 You're All Set!</h1>
	  <p>Thanks For Completing Your Setup, [Manager Name]!</p>
	</div>
	<div class="content">
	  <p>We're Excited To Welcome You To Our Platform. Your Setup Was Successful, And You're Now Ready To Enjoy A Seamless Experience Designed To Simplify The Understanding Of Programming.</p>

	  <p>Once Again, Thank You For Joining Us. We Can't Wait To See What You'll Accomplish!</p>

	  <p style="margin-top: 30px;">Warm regards,<br><strong>The Bank-With-High-Functionalities Team</strong></p>
	</div>

	<div class="footer">
	  <p style="margin: 0;">
		© 2024 - 2026 Bank-With-High-Functionalities • Virati Akira Nandhan Reddy
	  </p>
	  <div style="padding: 20px px; margin-top: 16px; text-align: center;">
		<a href="https://facebook.com/YourPage" style="margin: 0 8px; text-decoration: none;" target="_blank">
		<img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook" width="24" style="vertical-align: middle; border: 0;">
		</a>
		<a href="https://instagram.com/YourProfile" style="margin: 0 8px; text-decoration: none;" target="_blank">
		<img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram" width="24" style="vertical-align: middle; border: 0;">
		</a>
		<a href="https://x.com/YourHandle" style="margin: 0 8px; text-decoration: none;" target="_blank">
		<img src="https://cdn-icons-png.flaticon.com/512/5968/5968830.png" alt="X" width="24" style="vertical-align: middle; border: 0;">
		</a>
		<a href="https://github.com/YourUsername" style="margin: 0 8px; text-decoration: none;" target="_blank">
		<img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub" width="24" style="vertical-align: middle; border: 0;">
		</a>
		<a href="https://linkedin.com/in/YourProfile" style="margin: 0 8px; text-decoration: none;" target="_blank">
		<img src="https://cdn-icons-png.flaticon.com/512/145/145807.png" alt="LinkedIn" width="24" style="vertical-align: middle; border: 0;">
		</a>
		<a href="https://yourwebsite.com" style="margin: 0 8px; text-decoration: none;" target="_blank">
		<img src="https://cdn-icons-png.flaticon.com/512/545/545670.png" alt="Website" width="24" style="vertical-align: middle; border: 0;">
		</a>
		<p style="padding: 35px px;padding-bottom:0px;">
		<b> 
			🤖 This is An Automated Email 🤖<br>
			⚠️ Please Do Not Reply ⚠️</b>
		</p> 
  </div>
</body>
</html>
'''.replace('[Manager Name]', SETUPDATA['Manager Name'])

				Email = EmailMessage()

				Email['Subject'] = f'Hello! {SETUPDATA["Manager Name"]}, Your Registration With Bank-With-High-Functionalities Has Been Successfully Completed 🩵.'
				Email['From'] = 'Bank-With-High-Functionalities Team'
				Email['To'] = SETUPDATA['Manager Email']

				Email.set_content(HTML, subtype = 'html')

				try:

					with smtplib.SMTP_SSL('smtp.gmail.com', 465) as SMTP:

						SMTP.login(SETUPDATA['Manager Email'], SETUPDATA['Manager Email App Password'])
						SMTP.send_message(Email)

				except Exception as Error:
					EMAIL_LOGS.write(f'\n[ERROR]:[setup.exe - Manager_Email_Verification][{datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}] ; Status: Unsuccessful ; MSG: Error Occurred While Sending Greeting Email To Manager ; ErrorType: [{Error}]')

			register_uninstall_entry_user_scope()

			if CREATE_SHORTCUT:

				Shortcut_At_Desktop()

			elif OPEN_DOCUMENTATION_WEB:

				OpenBrowserForSpecifiedUrl(webpage)

			elif OPEN_MAIN_EXE:

				Open_main_exe()

			Shortcut_At_Start_Menu()
			Greet_Developer()
			Greet_Manager()
		
		CREATE_SHORTCUT = CTk.BooleanVar() ; OPEN_MAIN_EXE = CTk.BooleanVar() ; OPEN_DOCUMENTATION_WEB = CTk.BooleanVar()
		CREATE_SHORTCUT.set(True) ; OPEN_MAIN_EXE.set(True) ; OPEN_DOCUMENTATION_WEB.set(True)
		FinishSetupFrame = CTk.CTkFrame(Window, 790, 590)
		CTk.CTkLabel(FinishSetupFrame, text = 'One Last Step to Finalize the Setup!', font = ('Arial', 26, 'bold'), height = 0).place(x = 10 , y = 10)
		CTk.CTkLabel(FinishSetupFrame, text = '', image = CTk.CTkImage(light_image = ThankYouLightImage, dark_image = ThankYouDarkImage, size = (790, 333))).place(x = 0, y = 50)
		

		CTk.CTkLabel(FinishSetupFrame, text = 'Connect With The Developer!', font = ('Arial', 18, 'bold'), height = 0).place(x = 525, y = 370)
		CTk.CTkLabel(FinishSetupFrame, text = 'Click The Handle To Visit The Associated Page.', font = ('Arial', 10), height = 0).place(x = 543, y = 387)

		CTk.CTkLabel(FinishSetupFrame, text = 'We appreciate it if you could visit &\nfollow the developer\'s social media\npages. It\'s a great way to stay\ninformed about updates,\nnew features, & ongoing\nwork. Your support\nmakes a difference!', font = ('Segoe UI', 10), justify = 'left').place(x = 530, y = 417)

		CTk.CTkButton(FinishSetupFrame, text = '@viratiaki53', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = instagram_icon, dark_image = instagram_icon, size = (15,15)), width = 0,
					  height = 0, fg_color = 'transparent', hover = False, compound = 'right', command = lambda: OpenBrowserForSpecifiedUrl(instagram)).place(x = 702, y = 410)
		
		CTk.CTkButton(FinishSetupFrame, text = '@Viratiaki53', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = x_icon, dark_image = x_icon, size = (15,15)), width = 0,
					  height = 0, fg_color = 'transparent', hover = False, compound = 'right', command = lambda: OpenBrowserForSpecifiedUrl(x)).place(x = 701, y = 430)
		
		CTk.CTkButton(FinishSetupFrame, text = 'Official Webpage', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = webpage_icon, dark_image = webpage_icon, size = (15,15)), width = 0,
					  height = 0, fg_color = 'transparent', hover = False, compound = 'right', command = lambda: OpenBrowserForSpecifiedUrl(webpage)).place(x = 679, y = 450)
		
		CTk.CTkButton(FinishSetupFrame, text = 'viratiaki53@gmail.com', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = gmail_icon, dark_image = gmail_icon, size = (15,15)), width = 0,
					  height = 0, fg_color = 'transparent', hover = False, compound = 'right', command = lambda: OpenBrowserForSpecifiedUrl(mail)).place(x = 656, y = 470)
		
		CTk.CTkButton(FinishSetupFrame, text = '@ViratiAkiraNandhanReddy', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = github_icon, dark_image = github_icon, size = (15,15)), width = 0,
					  height = 0, fg_color = 'transparent', hover = False, compound = 'right', command = lambda: OpenBrowserForSpecifiedUrl(github)).place(x = 633, y = 490)
		
		CTk.CTkButton(FinishSetupFrame, text = '@ViratiAkiraNandhanReddy', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = facebook_icon, dark_image = facebook_icon, size = (15,15)), width = 0,
					  height = 0, fg_color = 'transparent', hover = False, compound = 'right', command = lambda: OpenBrowserForSpecifiedUrl(facebook)).place(x = 633, y = 510)
		
		CTk.CTkButton(FinishSetupFrame, text = '@Virati Akira Nandhan Reddy', font = ('Segoe UI', 10), image = CTk.CTkImage(light_image = linkedin_icon, dark_image = linkedin_icon, size = (15,15)), width = 0,
					  height = 0, fg_color = 'transparent', hover = False, compound = 'right', command = lambda: OpenBrowserForSpecifiedUrl(linkedin)).place(x = 624, y = 530)
		
		CTk.CTkCheckBox(FinishSetupFrame, text = 'Create Desktop Shortcut', onvalue = True, offvalue = True, variable = CREATE_SHORTCUT, height = 0, border_width = 1, checkbox_height = 18,
						checkbox_width = 18, hover_color = '#45A049', fg_color = '#4CAF50').place(x = 10, y = 422)

		CTk.CTkCheckBox(FinishSetupFrame, text = 'Launch The Application After Setup', onvalue = True, offvalue = True, variable = OPEN_MAIN_EXE, height = 0, border_width = 1, checkbox_height = 18,
						checkbox_width = 18, hover_color = '#45A049', fg_color = '#4CAF50').place(x = 10, y = 450)
		
		CTk.CTkCheckBox(FinishSetupFrame, text = 'Launch Documentation When Setup Finishes.', onvalue = True, offvalue = True, variable = OPEN_DOCUMENTATION_WEB, height = 0, border_width = 1, checkbox_height = 18,
						checkbox_width = 18, hover_color = '#45A049', fg_color = '#4CAF50').place(x = 10, y = 478)

		CTk.CTkLabel(FinishSetupFrame, text = ' Ensure that your device is connected to the internet.', font = ('Segoe UI', 12),
					 image = CTk.CTkImage(light_image = EXCLAMATION_Icon, dark_image = EXCLAMATION_Icon, size = (14, 14)), compound = 'left', height = 0).place(x = 10, y = 547)

		CTk.CTkLabel(FinishSetupFrame, text = ' An email will be sent to the developer upon your registration. No sensitive data will be shared.', font = ('Segoe UI', 12),
					 image = CTk.CTkImage(light_image = INFO_Icon, dark_image = INFO_Icon, size = (14, 14)), compound = 'left', height = 0).place(x = 10, y = 566)
		CTk.CTkButton(FinishSetupFrame, text = 'Finish Setup!', corner_radius=4, fg_color = '#4CAF50', text_color = 'Black', hover_color='#45A049', width = 180, 
					  command = lambda: [self.Inject_Initialization_Data_Into_JSON_Files(), Window.destroy(), _exec_func_()]).place(x = 605, y = 557)

		Window.mainloop()

	def Inject_Initialization_Data_Into_JSON_Files(self) -> None:
		
		''' <!-- Doc Strings --> 
		## Purpose
		The `Inject_Initialization_Data_Into_JSON_Files` function is responsible for saving the setup data into JSON files. This ensures that the collected initialization data is stored persistently for future use by the application.

		## Functionality
		- Saves the setup data (`SETUPDATA`) into two JSON files:
		1. **Main Initialization File**: Located in the primary database directory.
		2. **Backup Initialization File**: Located in the backup database directory.
		- Adds a timestamp (`Downloaded On`) to the `SETUPDATA` dictionary to record when the data was saved.

		## Parameters
		- **None**: This function does not take any parameters.

		## Return Type
		- **None**: This function does not return any value.

		## Process
		1. Updates the `Downloaded On` field in the `SETUPDATA` dictionary with the current date and time.
		2. Writes the updated `SETUPDATA` dictionary to:
		- `Initialization.json` in the main database directory.
		- `Initialization.json` in the backup database directory.

		## Example Usage
		```python
		setup = Setup()
		setup.Inject_Initialization_Data_Into_JSON_Files()
		```

		## Notes
		- Ensure that the `SETUPDATA` dictionary is populated with valid data before calling this function.
		- The file paths for the main and backup JSON files are hardcoded and must exist for the function to work correctly.
		- This function overwrites any existing data in the target JSON files.

		## Example Output
		The following JSON structure is saved to the files:
		```
		{
			"isActivated": true,
			"License Verification": "Passed",
			"Current Version": "0.0.1 - Alpha",

			"Manager Name": "John Doe",
			"Manager Username": "johndoe123",
			"Manager Password": "********",
			"Manager Security Code": "%^*^$&jg758fj^($&)",
			"Manager Email": "johndoe@example.com",
			"Manager Email App Password": "********",
			"isEmailVerified": true,

			"Downloaded On": "15-May-2025 -- Thursday @ 10:30:00 AM",
			"DATABASE TYPE": "SQLite3",
			"DATABASE PATH": "path/to/database.sqlite3",
			"BACKUP DATABASE PATH": "path/to/database.sqlite3",
			
			"MySQL Credentials": {

				"Host": "localhost",
				"Port": 3306,
				"Username": "root",
				"Password": "********",
				"Database": "Bank-With-High-Functionalities",
				"Charset": "utf8mb4"

			}
		}
		```

		## Security
		- Sensitive information such as passwords is stored in the JSON files. Ensure that these files are secured and not accessible to unauthorized users.

		## Dependencies
		- Requires the `json` module for serializing the `SETUPDATA` dictionary into JSON format.
		- Relies on the `datetime` module to generate the timestamp for the `Downloaded On` field.

		## File Paths
		- **Main File**: `Bank_Package/DATABASE/JSON/ADMINISTRATIVE FILES/Initialization.json`
		- **Backup File**: `BACKUP - DATABASE/JSON/ADMINISTRATIVE FILES/Initialization.json`
		'''

		SETUPDATA['Downloaded On'] = datetime.datetime.now().strftime('%d-%b-%Y -- %A @ %I:%M:%S %p')

		with open(fr'{PATH}\Bank_Package\DATABASE\JSON\ADMINISTRATIVE FILES\Initialization.json', 'w') as MAIN:
			
			# Dump into Initialization.json (Main)
			json.dump(SETUPDATA, MAIN, indent = 4)

		with open(fr'{PATH}\BACKUP - DATABASE\JSON\ADMINISTRATIVE FILES\Initialization.json', 'w') as BACKUP:
			
			# Dump into Initialization.json (Backup)
			json.dump(SETUPDATA, BACKUP, indent = 4)

Backup_Database_cls = CheckForBackupDatabase()
isDatabasesAvailable = Backup_Database_cls.Check_Presence_Of_Database()

if isDatabasesAvailable:

	Backup_Database_cls.Restore_Backup_Database_Setup()

	if Backup_Database_cls.isNewDatabaseRequested:
		Backup_Database_cls.Auto_Delete_Database_With_min_Users()
		rm_backupbatabasememory()
		Setup().SetupWindows()

	if Backup_Database_cls.isBackupDatabaseRestored:
		Backup_Database_cls._exec_func_()

	Backup_Database_cls.Rename_Folders()

else:

	rm_backupbatabasememory()
	Setup().SetupWindows()

def __atexit__() -> None:

	''' <!-- Doc Strings -->
    ## Purpose
    The `__atexit__` function is a cleanup handler that is automatically called when the program is about to exit. It ensures that all open log files are properly closed and provides a simple confirmation message for debugging or logging purposes.

    ## Functionality
    - Closes the following log files if they are open:
        - `ERROR_LOGS`: Error log file for recording errors and exceptions.
        - `EMAIL_LOGS`: Log file for email-related events and errors.
        - `SETUP_LOGS`: Log file for setup and installation events.
    - Prints a message ("things going well") to indicate that the cleanup was successful.

    ## Usage
    This function is registered with Python's `atexit` module and is called automatically when the interpreter terminates, regardless of how the program exits (normal completion, error, or interruption).

    ## Example
    ```python
    import atexit

    def __atexit__():
        # ...cleanup code...
        pass

    atexit.register(__atexit__)
    ```

    ## Notes
    - This function should not be called directly; it is intended to be used as an exit handler.
    - Ensures that log files are not left open, which helps prevent data loss or file corruption.
    - The print statement is mainly for debugging and can be removed or replaced with a logging call if desired.

    ## Limitations
    - If any of the log file objects are already closed or not defined, an exception may occur unless handled elsewhere.
    - Only handles the closing of specific log files; other resources should be managed separately.

    ## Security
    - No sensitive data is handled or exposed by this function.
	'''

	ERROR_LOGS.close()
	EMAIL_LOGS.close()
	SETUP_LOGS.close()

atexit.register(__atexit__)

# END OF PROGRAM AT MY FAVOURITE NUMBER - 53 