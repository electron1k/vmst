import pyautogui
import time
import subprocess
import re

files = ['51for_delete.txt', '52for_delete.txt', '53for_delete.txt']

def create_files_add_mon():
    subprocess.call('./add_to_monitor.sh',  shell=True)

def start_app():
    proc = subprocess.Popen('osnova-file-shred', shell=False)
    print("proc running")

def get_result(filename):
    pattern = 'proctitle=.+'
    result = subprocess.run(f"./get_one_result.sh {filename}",  shell=True, stdout=subprocess.PIPE)
    out_res = result.stdout.decode()
    print(out_res)

    with open('result.txt', '+a') as dest:
        dest.write(str(re.findall(pattern=pattern, string=out_res)[-1])+'\n')

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
    time.sleep(0.5)
    pyautogui.click(769, 521, button='left')#file name
    time.sleep(0.5)
    pyautogui.click(1118,727, button='left')#delete file
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')

    get_result(f'{files[0]}')

def second_case():
    pyautogui.click(1094, 415, button='left')
    time.sleep(0.5)
    pyautogui.click(800, 693, button='left') # activate field name
    pyautogui.write(f'{files[1]}')#write path and filename
    pyautogui.press('enter')

    pyautogui.click(959, 457, button='left')
    pyautogui.click(959, 457, button='left')

    pyautogui.press('backspace')
    pyautogui.write('5')
    time.sleep(0.5)
    # pyautogui.click(773, 491, button='left')#file size
    time.sleep(0.5)
    pyautogui.click(769, 521, button='left')#file name
    time.sleep(0.5)
    pyautogui.click(1118,727, button='left')#delete file
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    get_result(f'{files[1]}')

def third_case():
    pyautogui.click(1094, 415, button='left')
    time.sleep(0.5)
    pyautogui.click(800, 693, button='left') # activate field name
    pyautogui.write(f'{files[2]}')#write path and filename
    pyautogui.press('enter')

    pyautogui.click(959, 457, button='left')
    pyautogui.click(959, 457, button='left')

    pyautogui.press('backspace')
    pyautogui.write('5')
    time.sleep(0.5)
    pyautogui.click(773, 491, button='left')#file size
    time.sleep(0.5)
    # pyautogui.click(769, 521, button='left')#file name
    time.sleep(0.5)
    pyautogui.click(1118,727, button='left')#delete file
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')

    get_result(f'{files[2]}')


def close_app():
    pyautogui.hotkey('Alt','f4')


if __name__ == "__main__":
    create_files_add_mon()
    start_app()
    time.sleep(2)
    first_case()
    time.sleep(2)
    second_case()
    time.sleep(2)
    third_case()
    time.sleep(2)
    # get_results()
    close_app()
