import pyautogui
import subprocess
from PIL import Image, ImageGrab
import numpy as np
import time
import asyncio

proc = subprocess.Popen(["VBoxManage", "startvm", "yellow_kde"], shell=False)

def monitor(img):
    flag = ''
    while True:
        time.sleep(1)
        sc = ImageGrab.grab(bbox=(0,0, 600, 700))
        sc.save('temp.jpg')
        geted = np.array(Image.open('temp.jpg'))
        print(f'screens/{img}')
        referent = np.array(Image.open(f'screens/{img}'))
        if referent.shape == geted.shape and np.all(referent == geted):
            flag = 'ok'
            break


def one_shot():
        time.sleep(1)
        sc = ImageGrab.grab(bbox=(0,0, 600, 700))
        sc.save('temp.jpg')
        geted = np.array(Image.open('temp.jpg'))


monitor('start_screen.jpg')
print('state checked')
pyautogui.press('enter')
monitor('licence.jpg')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(20)
one_shot()

# pyautogui.press('Enter')