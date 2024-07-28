import pyautogui
import time

#Esse script é responsável por pegar a posição do cursor(mouse)
try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição atual do mouse: ({x}, {y})", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
