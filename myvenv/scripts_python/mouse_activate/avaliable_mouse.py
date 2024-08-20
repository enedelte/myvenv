import pyautogui
import time


def mantener_disponible(intervalo=20):
    while True:
        # Obtener la posición actual del mouse
        x, y = pyautogui.position()

        pyautogui.moveTo(x + 10, y)
        pyautogui.click()
        pyautogui.moveTo(x, y)
        pyautogui.click()
        
        
        time.sleep(intervalo)

if __name__ == "__main__":
    print('En funcionamiento')
    mantener_disponible(intervalo=20)
