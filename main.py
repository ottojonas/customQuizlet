import customtkinter
from icecream import ic

ic("Quizlet Initialized")


class MainPage:
    def __init__(self):
        self.mainWindow = customtkinter.CTk()
        self.mainWindow.attributes("-fullscreen", True)
        self.mainFrame = customtkinter.CTkFrame(self.mainWindow)
        self.mainFrame.pack_propagate(False)
        self.mainFrame.pack(anchor="center")
