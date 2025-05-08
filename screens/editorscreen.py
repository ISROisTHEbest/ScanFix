import customtkinter as ctk
from backend import *

class EditorScreen(ctk.CTkFrame):
    def __init__(self, master, file):
        super().__init__(master)
        
        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        canvas = self.scroll_frame._parent_canvas
        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", self._on_mousewheel))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
        
        height = self.winfo_screenheight() - 100
        
        with open(file, "rb") as f:
            pdf = f.read()
            
        png_data = pdftopng(pdf)
        
        for png in png_data:
            aspect_ratio = png.width/png.height
            width = int(height * aspect_ratio)
            image = ctk.CTkImage(light_image=png, dark_image=png, size=(width, height))
            ctk.CTkLabel(self.scroll_frame, image=image, text="").grid(row=png_data.index(png), column=1, pady=10)

    def _on_mousewheel(self, event):
        canvas = self.scroll_frame._parent_canvas
        canvas.yview_scroll(-int(event.delta * 1.5), "units")