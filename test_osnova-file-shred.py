import pyautogui
import time
import subprocess

files = ['41for_delete.txt', '42for_delete.txt', '43for_delete.txt']

def create_files_add_mon():
    subprocess.call("./add_to_monitor.sh",  shell=True)

def start_app():
    proc = subprocess.Popen('osnova-file-shred', shell=False)
    print("proc running")

def first_case():
    pyautogui.click(1094, 415, button='left')
    time.sleep(0.5)
    pyautogui.click(800, 693, button='left') # activate field name
    pyautogui.write(f'{files[0]}')#write path and filename
    pyautogui.press('enter')

    pyautogui.click(959, 457, button='left')
    pyautogui.click(959, 457, button='left')

    pyautogui.press('backspace')
    pyautogui.write('5')
    time.sleep(0.5)
    pyautogui.click(773, 491, button='left')#file size
    pyautogui.click(769, 521, button='left')#file name
    pyautogui.click(1118,727, button='left')#delete file
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')

def get_results():
    subprocess.call("./get_results.sh",  shell=True)


if __name__ == "__main__":
    create_files_add_mon()
    start_app()
    time.sleep(2)
    first_case()
    time.sleep(10)
    get_results()