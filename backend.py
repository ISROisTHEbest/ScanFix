from customtkinter import CTkImage
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtGui import QImage, QPainter
from tkinter import filedialog
from tkinter.messagebox import showinfo
from PIL import Image

dark_icon_color = '#EBEBEB'
light_icon_color = '#2B2B2B'

def iconConvert(svg_file, size):
    with open(f"assets/images/{svg_file}", "r", encoding="utf-8") as f:
        svg_data = f.read()

    svg_data = svg_data.replace("currentColor", dark_icon_color)
    renderer = QSvgRenderer(svg_data.encode("utf-8"))

    image = QImage(size[0], size[1], QImage.Format_ARGB32)
    image.fill(0x00000000)
    painter = QPainter(image)
    renderer.render(painter)
    painter.end()
    image = Image.fromqimage(image)
    
    
    icon = CTkImage(light_image=image, dark_image=image, size=size)
    return icon