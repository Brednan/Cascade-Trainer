import ctypes
from time import time
import cv2
from Screenshot import ScreenShot
from Generate_Negative_File import generate_negative_desc_file

monitor = int(input('Choose monitor'))

while True:
    if ctypes.windll.user32.GetKeyState(0x51) not in [0,1] or ctypes.windll.user32.GetKeyState(0x71) not in [0,1]:
        break

    if ctypes.windll.user32.GetKeyState(0x52) not in [0, 1] or ctypes.windll.user32.GetKeyState(0x72) not in [0, 1]:
        ScreenShot().take_screenshot(type=1, monitor=monitor)
    
    if ctypes.windll.user32.GetKeyState(0x6E) not in [0, 1] or ctypes.windll.user32.GetKeyState(0x4E) not in [0, 1]:
        ScreenShot().take_screenshot(type=0, monitor=monitor)

generate_negative_desc_file()
