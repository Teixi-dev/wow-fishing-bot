from tkinter.constants import NO
import pyautogui
import time as tm
import sounddevice as sd
import numpy as np
import random

def sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    soundLVL = volume_norm
    if(soundLVL >= 2):
        print("Recogiendo anzuelo")
        pyautogui.click(button='right')


def randomNum(num1, num2):
    num =random.randint(num1,num2)
    return num

while True:
    pescandobar = pyautogui.locateOnScreen('pescando_bar.png')
    if pescandobar != None:
        print("Barra de pesca detectada")
        anzuelo = pyautogui.locateOnScreen('anzuelo.png',confidence=0.4)
        if anzuelo != None:
            print("Anzuelo detectado")
            anzueloPoint = pyautogui.center(anzuelo)
            print('Esperando sonido de chapuzon')
            pyautogui.moveTo(anzueloPoint.x - random.random(), anzueloPoint.y - random.random(), 2, pyautogui.easeOutQuad)
            with sd.Stream(callback=sound):
                sd.sleep(10000)
    else:
        
        sl = randomNum(1,2)
        if sl > 9:
            num = randomNum(1, 5)
            print("Descansando " + str(num) + "m")
            tm.sleep(60*num)
        num2 = randomNum(1,4)
        print('Esperando para lanzar anzuelo ' + str(num2) + "s")
        tm.sleep(num2)
        num3 = randomNum(1,2)
        print('Lanzando anzuelo ' + str(num3) + "s")
        pyautogui.press('+')
        tm.sleep(num3)
