import customtkinter as ctk
from threading import Thread
from backend import *
import queue
import fitz
import io

class EditorScreen(ctk.CTkFrame):
    def __init__(self, master, file, mainScreen):
        super().__init__(master)
        
        self.mainScreen = mainScreen
        
        self.grid(row=0, column=0, sticky="nsew")

        self.columnconfigure((0,2), weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        canvas = self.scroll_frame._parent_canvas
        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", self._on_mousewheel))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
        self.scroll_frame.grid_columnconfigure((0,2), weight=1)
        self.scroll_frame.grid_columnconfigure(1, weight=3)

        self.back_button = ctk.CTkButton(self, text='', image=iconConvert('back.svg', (40, 40)), cursor='hand2', command=self.backButton)
        self.back_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        
        self.page_no_label = ctk.CTkLabel(self, text='Pg 1/1')
        self.page_no_label.grid(row=0, column=2, sticky="ne", padx=10, pady=10)

        self.progress_bar = ctk.CTkProgressBar(self, width=300, height=20, mode='determinate')
        self.progress_bar.grid(row=1, column=1, pady=10)
        self.progress_bar.set(0)

        with open(file, "rb") as f:
            pdf = f.read()

        Thread(target=self.pdftopng, args=(pdf,), daemon=True).start()

    def _on_mousewheel(self, event):
        canvas = self.scroll_frame._parent_canvas
        canvas.yview_scroll(-int(event.delta * 1.5), "units")

    def pdftopng(self, pdf_bytes):
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        total_pages = len(doc)

        height = self.winfo_screenheight() - 120
        width = self.winfo_screenwidth() * 0.5
        for page_num, page in enumerate(doc):
            pix = page.get_pixmap(dpi=200)
            png = pix.tobytes("png")
            png = Image.open(io.BytesIO(png))

            aspect_ratio = png.height / png.width

            if aspect_ratio < 1:
                height = int(width * aspect_ratio)
            else:
                width = int(height * 1 / aspect_ratio)

            image = ctk.CTkImage(light_image=png, dark_image=png, size=(width, height))

            ctk.CTkLabel(self.scroll_frame, image=image, text="").grid(row=page_num, column=1, sticky="nsew", padx=10, pady=10)

            progress = (page_num + 1) / total_pages
            self.progress_bar.set(progress)

        self.progress_bar.destroy()

    def backButton(self):
        self.mainScreen()
