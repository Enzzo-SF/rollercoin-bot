from ast import While
import pyautogui
import numpy
import time
import keyboard
from functions import *

#64, 117, 1539, 1013
def mouse_click(x, y, wait=0.2):
    pyautogui.click(x, y)
    time.sleep(wait)

def coinclick(a):
    print("START GRY")
    while a==1:
        pic = pyautogui.screenshot(region=(530, 430, 828, 417))
        width, height = pic.size
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r, g, b = pic.getpixel((x, y))

                #Fine
                if b == 228 and r == 3 and g == 225:
                    print(f"Fine at ({x},{y}): R={r}, G={g}, B={b}")
                    a = 0
                    break

                 # eth coin
                if b == 207 and r == 66 and g==105:
                    print(f"eth at ({x},{y}): R={r}, G={g}, B={b}")
                    mouse_click(x + 535, y + 440, wait=0)
                    break

                # blue coin
                if b == 183 and r == 0:
                    print(f"dash at ({x},{y}): R={r}, G={g}, B={b}")
                    mouse_click(x + 530, y + 440, wait=0)
                    break

                # yellow coin
                if b == 64 and r == 200:
                    print(f"doge at ({x},{y}): R={r}, G={g}, B={b}")
                    mouse_click(x + 530, y + 440, wait=0)
                    break

                # orange coin
                if b == 33 and r == 231:
                    print(f"btc at ({x},{y}): R={r}, G={g}, B={b}")
                    mouse_click(x + 530, y + 440, wait=0)
                    break

                # grey coin
                if b == 230 and r == 230:
                    print(f"ltc at ({x},{y}): R={r}, G={g}, B={b}")
                    mouse_click(x + 535, y + 440, wait=0)
                    break
                
    print("FINE GRY")
    start()

def start():
    print("Premi Enter per iniziare, naciścialo solo quando è in corso il conto alla rovescia")
    keyboard.wait("enter")
    a = 1
    coinclick(a)

start()
