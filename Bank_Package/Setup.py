import customtkinter as CTk
import socket, time
import webbrowser, subprocess, json

class SetUp:

    def __init__(self) -> None:
        pass

    def Browser(self) -> None:
        subprocess.run(r'C:\Program Files\Google\Chrome\Application\chrome.exe',)
        time.sleep(2)
        webbrowser.open('www.google.com')

    def SetupWindows(self) -> None:

        Window = CTk.CTk()
        Window.title('Setup')
        Window.geometry('')
        Window.resizable(False,False)

        Window.mainloop()

SetUp().Browser()