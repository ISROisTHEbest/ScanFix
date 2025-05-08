import customtkinter as ctk
from screens.mainscreen import MainScreen
from screens.editorscreen import EditorScreen

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
        self.current_screen = MainScreen(self, self.show_editor_screen)
        self.current_screen.pack(fill="both", expand=True)
        
    def show_editor_screen(self):
        self.clear_screen()
        self.current_screen = EditorScreen(self)
        self.current_screen.pack(fill="both", expand=True)

if __name__ == '__main__':
    app = App()
    app.mainloop()