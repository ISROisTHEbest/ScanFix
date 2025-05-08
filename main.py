import customtkinter as ctk
from screens.mainscreen import MainScreen

# app = ctk.CTk()
# app.title('ScanFix')
# app.after(10, lambda: app.state("zoomed"))
# # ctk.set_default_color_theme("blue")


# main_label = ctk.CTkLabel(app, text="ScanFix", fg_color="transparent", font=('Segoe UI', 50), padx=0, pady=3)
# upload_file_button = ctk.CTkButton(app, text='Upload a File', font=('Roboto', 30), image=iconConvert('plus.svg', (40, 40)), corner_radius=10, cursor='hand2', command=selectFile)


# app.grid_columnconfigure(0, weight=1)
# app.grid_rowconfigure(1, weight=1)

# main_label.grid(row=0, column=0)
# upload_file_button.grid(row=1, column=0)

# app.mainloop()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('ScanFix')
        self.after(10, lambda: self.state("zoomed"))
        
        self.current_screen = None
        
        self.show_main_screen()
    
    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
    
    def show_main_screen(self):
        self.clear_screen()
        self.current_screen = MainScreen(self)
        self.current_screen.pack(fill="both", expand=True)

if __name__ == '__main__':
    app = App()
    app.mainloop()