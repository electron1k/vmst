from PIL import ImageGrab, Image, ImageChops
import time
import subprocess
import pywinctl
import pyautogui

# time.sleep(5)
# sc = ImageGrab.grab(bbox=(0,0, 1920, 1005))
# sc.save(f'temp.jpg')

# pic_1 = Image.open('waste/ref_calc.jpg')
# pic_2 = Image.open('waste/temp.jpg')

# # pic_1.thumbnail((400, 300))
# # pic_2.thumbnail((400, 300))

# # res = ImageChops.difference(pic_1, pic_2).getbbox()
# res = ImageChops.difference(pic_1, pic_2)
# res.save('result.jpg')
# print(res)


# width="415", height="360"
def start_app():
    proc = subprocess.Popen('kate', shell=False)
    print("proc running")


start_app()
time.sleep(2)
window = pywinctl.getActiveWindow()
# w = pywinctl.getScreenSize()
window.maximize() #works
time.sleep(5)
btn = pyautogui.locateOnScreen('waste/choose.png')

print(btn)

