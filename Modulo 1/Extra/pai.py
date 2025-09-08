import pyautogui
import time
import platform


pyautogui.hotkey('win', 'r')
time.sleep(1)  # Pausa para a barra de pesquisa aparecer
pyautogui.write('Inkscape')
time.sleep(1)
pyautogui.press('enter')
