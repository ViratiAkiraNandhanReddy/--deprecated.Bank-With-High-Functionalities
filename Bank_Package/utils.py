import os
import datetime
import subprocess, platform

PATH = r'D:\GitHub\Bank-With-High-Functionalities' # str(os.environ.get('LOCALAPPDATA')) + r'\Bank-With-High-Functionalities'



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
	
	ERRORLOGS = open(fr'{PATH}\Logs\ErrorLogs.txt', 'a')

	try:

		if platform.system() == 'Windows':
			subprocess.run(f"Start {URL}", shell = True)

		elif platform.system() == 'Mac':
			subprocess.run(f"open {URL}", shell = True)

		elif platform.system() == 'Linux':
			subprocess.run(f"xdg-open {URL}", shell = True)

	except Exception as Error: # Logging and fallback

		ERRORLOGS.write(f'\n[ERROR]:[Setup.py][{datetime.datetime.now().strftime('%d/%b/%Y @ %I:%M:%S %p')}] - Failed To Open {URL} ; ErrorType: [ {Error} ]')
		ERRORLOGS.close()

def GenSecurityCode() -> str:
	Code = ''
	
	return Code