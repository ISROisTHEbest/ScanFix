import customtkinter as ctk
from backend import *

# app = ctk.CTk()
# app.title('ScanFix')
# app.after(10, lambda: app.state("zoomed"))
# ctk.set_default_color_theme("blue")

class MainScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.main_label = ctk.CTkLabel(self, text="ScanFix", fg_color="transparent", font=('Segoe UI', 50), padx=0, pady=3)
        self.upload_file_button = ctk.CTkButton(self, text='Upload a File', font=('Roboto', 30), image=iconConvert('plus.svg', (40, 40)), corner_radius=10, cursor='hand2', command=selectFile)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.main_label.grid(row=0, column=0)
        self.upload_file_button.grid(row=1, column=0)