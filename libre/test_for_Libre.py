import subprocess
import pywinctl
import pyautogui
import time
import os
import pathlib
from PIL import Image, ImageGrab, ImageChops


script_path = path_for_save = pathlib.Path().resolve()


def clear_sys_buffer_kde():
    proc = subprocess.call(['qdbus', 'org.kde.klipper', '/klipper', 'clearClipboardHistory'])

def run_app(app_name):
    proc = subprocess.Popen(['soffice', f'{app_name}'], shell=False)
    time.sleep(3)
    print(app_name)
    mod = app_name.strip('-')
    window = pywinctl.getActiveWindow()
    if "Libre" in str(window):
        sc = ImageGrab.grab(bbox=(0,0, 520, 1005))
        sc.save('temp.jpg')

        geted = Image.open('temp.jpg')
        referent = Image.open(f'ref_img/{mod}.jpg')

        diff = ImageChops.difference(geted, referent).getbbox()

        if diff == None:
            print('image matches')
            return True

        else:
            return False
    else:
        print("wrong active window")
        return False

def actions(app_name):

    window = pywinctl.getActiveWindow()
    print(window)
    if "Libre" in str(window):
        sc = ImageGrab.grab(bbox=(0,0, 1920, 1005))
        sc.save(f'screenshots/{app_name}.jpg')
        time.sleep(1)
        pyautogui.hotkey('Ctrl', 's')
        time.sleep(1)
        pyautogui.write(f'{script_path}/testfiles')
        pyautogui.press('Enter')
        time.sleep(0.5)
        pyautogui.write('test_libre')
        pyautogui.press('Enter')


def check():
    results = os.listdir(f'{script_path}/testfiles')
    print(results)
    if len(results) == 4:
        with open('result.txt', "+a") as dest:
            for row in list(results):
                dest.write(row + '\n')
    

def close_app():
    pyautogui.hotkey('Alt','f4')



if __name__ == "__main__":

    apps = ['--calc', '--writer', '--draw', '--math'] 
    clear_sys_buffer_kde()

    for app in apps:
        if run_app(app) == True:
            time.sleep(2)
            actions(app)
            time.sleep(2)
            close_app()
            time.sleep(2)
        else:
            close_app()
            print('app not running')
            break

    check()

