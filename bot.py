import pyautogui
import time
from PIL import ImageGrab, Image
import numpy as np
import cv2 as cv
import random


class Bot():
    def __init__(self):
        

        self.botStatus = False


        self.catch_fish_region = None
        self.repair_region = None
        self.bait_region = None
        self.bai_button_region = None


        self.foundFish = False
        self.catch_fish_img = cv.imread('res/fish_klein.png')
        self.ab_fish = cv.imread('res/ab_klein.png')
        self.koeder_img = cv.imread('res/koeder.png')


    def rnd(a,b):
        return round(random.uniform(a, b), 1)

    def warteAufFisch(self,img_cv):
        res = cv.matchTemplate(img_cv, self.catch_fish_img, cv.TM_CCOEFF_NORMED)

        if (res >= 0.7).any():
            pyautogui.leftClick()
            time.sleep(self.rnd(1,2))
            return True
        return False

    def fischEinholen(self,img_cv):
        pyautogui.mouseDown(button='left')
        res_1 = cv.matchTemplate(img_cv, self.ab_fish, cv.TM_CCOEFF_NORMED)
        if (res_1 >= 0.7).any():
            pyautogui.mouseUp(button='left')
            time.sleep(self.rnd(0.5,1.8))

    def checkKoeder(self,img_cv):
        res_1 = cv.matchTemplate(img_cv, self.koeder_img, cv.TM_CCOEFF_NORMED)
        if (res_1 >= 0.7).any():
            (x,y) = (self.bait_region[2] + self.bait_region[0])/2, (self.bait_region[3]+self.bait_region[1])/2
            pyautogui.press('R')
            time.sleep(1)
            pyautogui.moveTo(x,y)
            time.sleep(0.3)
            pyautogui.leftClick()
            time.sleep(0.5)
            (x,y) = (self.bai_button_region[2] + self.bai_button_region[0])/2, (self.bai_button_region[3]+self.bai_button_region[1])/2
            pyautogui.moveTo(x,y)
            time.sleep(0.3)
            pyautogui.leftClick()
            time.sleep(1)
            
    def repair(self):
        (x,y) = (self.repair_region[2] + self.repair_region[0])/2, (self.repair_region[3]+self.repair_region[1])/2
        pyautogui.press('TAB')
        time.sleep(2)
        #rute_position = pyautogui.locateCenterOnScreen('res/repair.png',confidence = 0.7)
        time.sleep(0.3)   
        pyautogui.keyDown('r')
        time.sleep(0.5)   
        pyautogui.moveTo(x,y)
        time.sleep(0.3)
        pyautogui.leftClick()
        time.sleep(0.5)   
        pyautogui.keyUp('r')
        time.sleep(0.5)
        pyautogui.press('e')
        time.sleep(0.5)
        pyautogui.press('TAB')
        time.sleep(2)
        pyautogui.press('F3')
        time.sleep(1)