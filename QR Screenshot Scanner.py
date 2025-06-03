import threading
import 
import tkinter
from PIL import ImageGrab

# Ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Variables para coordenadas
x_ini, y_ini, x_fin, y_fin = None, None, None, None
