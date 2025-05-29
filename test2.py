
import keyboard
import pyautogui
import time

pyautogui.press('win')
time.sleep(2)

pyautogui.write('google',interval=0.2)
time.sleep(2)

pyautogui.press('enter')
time.sleep(1)

pyautogui.write('https://sig.ifc.edu.br/sigaa/',interval=0.2)
time.sleep(9)

pyautogui.press('enter')
time.sleep(2)

pyautogui.write('jrsvieira',interval=0.2)
time.sleep(5)

pyautogui.press('enter')