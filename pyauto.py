import pyautogui
import time


im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('my_screenshot.png')
pyautogui.alert('you have successfully takeen the screenshot.')
time.sleep(2)
pyautogui.confirm('you have succeessfully taken the screenshot.')
time.sleep(2)
x = pyautogui.prompt('you have successfully taken the screenshot.')
print(x)
