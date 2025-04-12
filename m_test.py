import pywinctl
import time

while True:
    window = pywinctl.getActiveWindow()
    print(window)
    time.sleep(1)
