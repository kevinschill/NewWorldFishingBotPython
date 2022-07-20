from time import time
from tkinter import Checkbutton, Frame, Radiobutton, StringVar, Toplevel, Canvas, IntVar, Label, LabelFrame, Button, Scale, Entry, HORIZONTAL, Widget
from functools import partial
from tkinter import Tk
import tkinter as tk
from tkinter.constants import S
from gui.rect import *
import yaml
import pyautogui
import time
from PIL import ImageGrab, Image
import numpy as np
import cv2 as cv
import random



class MainGui():
    def __init__(self, bothandle):
        self.bothandle = bothandle
        self.root = Tk()
        self.root.title('Yooo')
        self.root.geometry("420x200")

        self.time_calc = []
        self.total_catch_counter = 0
        self.repair_counter = 0

    def startGui(self):
        self.root.mainloop()

    def catchRectangle(self):
        app = RectShow()
        app.mainloop()
        temp_region = app.getCoords()
        self.bothandle.catch_fish_region = temp_region

        #self.dataMap = None
        with open('settings.yaml') as f:
    # use safe_load instead load
            dataMap = yaml.safe_load(f)

        with open('settings.yaml', 'w') as outfile:

            dataMap['Fish']['x'] = temp_region[0]
            dataMap['Fish']['y'] = temp_region[1]
            dataMap['Fish']['x2'] = temp_region[2]
            dataMap['Fish']['y2'] = temp_region[3]

            yaml.dump(dataMap, outfile, default_flow_style=False)

        self.coordinate_x_var.set("X: " + str(temp_region[0]))
        self.coordinate_y_var.set("Y: " + str(temp_region[1]))
        self.coordinate_width_var.set("X2: " + str(temp_region[2]))
        self.coordinate_height_var.set("Y2: " + str(temp_region[3]))

        del app

    def repairRectangle(self):
        app = RectShow()
        app.mainloop()
        temp_region = app.getCoords()
        self.bothandle.repair_region = temp_region

        with open('settings.yaml') as f:
    # use safe_load instead load
            dataMap = yaml.safe_load(f)

        with open('settings.yaml', 'w') as outfile:

            dataMap['Repair']['x'] = temp_region[0]
            dataMap['Repair']['y'] = temp_region[1]
            dataMap['Repair']['x2'] = temp_region[2]
            dataMap['Repair']['y2'] = temp_region[3]

            yaml.dump(dataMap, outfile, default_flow_style=False)

        self.repair_coordinate_x_var.set("X: " + str(temp_region[0]))
        self.repair_coordinate_y_var.set("Y: " + str(temp_region[1]))
        self.repair_coordinate_width_var.set("X2: " + str(temp_region[2]))
        self.repair_coordinate_height_var.set("Y2: " + str(temp_region[3]))
        
        del app

    def baitRechtangle(self):
        app = RectShow()
        app.mainloop()
        
        temp_region = app.getCoords()
        self.bothandle.bait_region = temp_region

        with open('settings.yaml') as f:
        # use safe_load instead load
            dataMap = yaml.safe_load(f)

        with open('settings.yaml', 'w') as outfile:

            dataMap['Bait']['x'] = temp_region[0]
            dataMap['Bait']['y'] = temp_region[1]
            dataMap['Bait']['x2'] = temp_region[2]
            dataMap['Bait']['y2'] = temp_region[3]

            yaml.dump(dataMap, outfile, default_flow_style=False)  

        del app

    def baitButtonRectangle(self):
        app = RectShow()
        app.mainloop()
        
        temp_region = app.getCoords()
        self.bothandle.bai_button_region = temp_region
        with open('settings.yaml') as f:

            dataMap = yaml.safe_load(f)

        with open('settings.yaml', 'w') as outfile:

            dataMap['BaitButton']['x'] = temp_region[0]
            dataMap['BaitButton']['y'] = temp_region[1]
            dataMap['BaitButton']['x2'] = temp_region[2]
            dataMap['BaitButton']['y2'] = temp_region[3]

            yaml.dump(dataMap, outfile, default_flow_style=False)  

        del app

    def SettingTab(self):
        self.coordinate_x_var = tk.StringVar(value='X: 0')
        self.coordinate_y_var = tk.StringVar(value='Y: 0')
        self.coordinate_width_var = tk.StringVar(value='X2: 0')
        self.coordinate_height_var = tk.StringVar(value='Y2: 0')

        self.repair_coordinate_x_var = tk.StringVar(value='X: 0')
        self.repair_coordinate_y_var = tk.StringVar(value='Y: 0')
        self.repair_coordinate_width_var = tk.StringVar(value='X2: 0')
        self.repair_coordinate_height_var = tk.StringVar(value='Y2: 0')

        lf = LabelFrame(self.root, text='Scan Settings', width=200, height=200)

        lf.grid(column=0, row=0, padx=5, pady=5)
        lf.configure(width=200, height=180)

        scan_button = Button(lf, text="Setup Catch",
                             command=self.catchRectangle)
        scan_button.place(x=2, y=70)

        repair_button = Button(lf, text="Setup Repair",
                               command=self.repairRectangle)
        repair_button.place(x=110, y=70)

        use_bait = IntVar()
        use_bait_check = Checkbutton(lf, text="Use Bait", variable=use_bait)
        use_bait_check.place(x=2, y=100)

        bait_button = Button(lf, text="Setup Bait",
                             command=self.baitRechtangle)
        bait_button.place(x=2, y=130)

        bait_button_button = Button(
            lf, text="Setup Bait Button", command=self.baitButtonRectangle)
        bait_button_button.place(x=80, y=130)

        coordinate_x = Label(lf, textvariable=self.coordinate_x_var)
        coordinate_x.place(x=6, y=5)
        coordinate_y = Label(lf, textvariable=self.coordinate_y_var)
        coordinate_y.place(x=6, y=20)

        coordinate_width = Label(lf, textvariable=self.coordinate_width_var)
        coordinate_width.place(x=6, y=35)
        coordinate_height = Label(lf, textvariable=self.coordinate_height_var)
        coordinate_height.place(x=6, y=50)

        repair_coordinate_x = Label(
            lf, textvariable=self.repair_coordinate_x_var)
        repair_coordinate_x.place(x=110, y=5)
        repair_coordinate_y = Label(
            lf, textvariable=self.repair_coordinate_y_var)
        repair_coordinate_y.place(x=110, y=20)

        repair_coordinate_width = Label(
            lf, textvariable=self.repair_coordinate_width_var)
        repair_coordinate_width.place(x=110, y=35)
        repair_coordinate_height = Label(
            lf, textvariable=self.repair_coordinate_height_var)
        repair_coordinate_height.place(x=110, y=50)

    def BotSettings(self):
        bot_settings = LabelFrame(
            self.root, text='Bot Settings', width=200, height=120)

        bot_settings.grid(column=3, row=0, padx=5, pady=5)

        repair_val = IntVar()
        R1 = Checkbutton(bot_settings, text="Repair", variable=repair_val)

        def doSomething(event):
            with open('settings.yaml') as f:
                dataMap = yaml.safe_load(f)

            with open('settings.yaml', 'w') as outfile:

                dataMap['RepairCast']['amount'] = int(event.widget.get())

                yaml.dump(dataMap, outfile, default_flow_style=False)

        R1.place(x=6, y=6)
        Label(bot_settings, text="after: ").place(x=65, y=8)
        self.repair_amount = StringVar()
        repair_amount_entry = Entry(
            bot_settings, width=4, textvariable=self.repair_amount)

        repair_amount_entry.place(x=100, y=9)
        repair_amount_entry.bind('<FocusOut>', doSomething)

        total_catch_fish = tk.StringVar(value='Total Catch: 0')
        calc_total_catch_fish = tk.StringVar(value="Catch Hour: 0")

        Label(bot_settings, text="Casts").place(x=125, y=8)
        total_catch_label = Label(bot_settings, textvariable=total_catch_fish)
        total_catch_label.place(x=6, y=28)

        calc_total_catch_label = Label(
            bot_settings, textvariable=calc_total_catch_fish)
        calc_total_catch_label.place(x=6, y=45)
        botStatus = False

        def start_bot():
            self.bothandle.botStatus = True

        def stop_bot():
            self.bothandle.botStatus = False

        start_bot = Button(bot_settings, text="Start Bot", command=start_bot)
        start_bot.place(x=6, y=70)
        stop_bot = Button(bot_settings, text="Stop Bot", command=stop_bot)
        stop_bot.place(x=80, y=70)

    def LoadConfig(self):
        with open('settings.yaml') as f:
            # use safe_load instead load
            dataMap = yaml.safe_load(f)

            self.bothandle.catch_fish_region = dataMap['Fish']
            self.bothandle.repair_region = dataMap['Repair']
            self.bothandle.bait_region = dataMap['Bait']
            self.bothandle.bai_button_region = dataMap['BaitButton']

            self.coordinate_x_var.set("X: " + str(dataMap['Fish']['x']))
            self.coordinate_y_var.set("Y: " + str(dataMap['Fish']['y']))
            self.coordinate_width_var.set("X2: " + str(dataMap['Fish']['x2']))
            self.coordinate_height_var.set("Y2: " + str(dataMap['Fish']['y2']))

            self.repair_coordinate_x_var.set("X: " + str(dataMap['Repair']['x']))
            self.repair_coordinate_y_var.set("Y: " + str(dataMap['Repair']['y']))
            self.repair_coordinate_width_var.set("X2: " + str(dataMap['Repair']['x2']))
            self.repair_coordinate_height_var.set("Y2: " + str(dataMap['Repair']['y2']))
            
            x,y,x2,y2 = dataMap['Fish']['x'],dataMap['Fish']['y'],dataMap['Fish']['x2'],dataMap['Fish']['y2']
            self.bothandle.catch_fish_region = (x,y,x2,y2)
            
            x,y,x2,y2 = dataMap['Repair']['x'],dataMap['Repair']['y'],dataMap['Repair']['x2'],dataMap['Repair']['y2']
            self.bothandle.repair_region = (x,y,x2,y2)
            
            x,y,x2,y2 = dataMap['Bait']['x'],dataMap['Bait']['y'],dataMap['Bait']['x2'],dataMap['Bait']['y2']
            self.bothandle.bait_region = x,y,x2,y2
            
            x,y,x2,y2 = dataMap['BaitButton']['x'],dataMap['BaitButton']['y'],dataMap['BaitButton']['x2'],dataMap['BaitButton']['y2']
            self.bothandle.bai_button_region = x,y,x2,y2

            self.repair_amount.set(str(dataMap['RepairCast']['amount']))
    
    def MainThread(self):
        
        if self.bothandle.botStatus is True:

            img = ImageGrab.grab(bbox=self.bothandle.catch_fish_region)
            img_cv = cv.cvtColor(np.array(img),cv.COLOR_RGB2BGR)

            if self.bothandle.foundFish is False:
                start_time = time.time()
                if self.bothandle.warteAufFisch(img_cv) is True:
                    self.bothandle.foundFIsh = True
                    pyautogui.keyDown('v')
            
            if self.bothandle.foundFish is True:
                self.bothandle.fischEinholen(img_cv)
                
                res_2 = cv.matchTemplate(img_cv,self.bothandle.erfolg_fish,cv.TM_CCOEFF_NORMED )
                if (res_2 >= 0.7).any():
                    pyautogui.leftClick()
                    pyautogui.mouseUp(button='left')

                    time.sleep(self.rnd(2,3.3))

                    pyautogui.keyUp('v')

                    if self.repair_val.get() == 1:
                        self.repair_counter += 1
                        if self.repair_counter >= int(self.repair_amount.get()):
                            self.bothandle.repair()
                            self.repair_counter = 0

                    if self.use_bait.get() == 1:
                        self.bothandle.checkKoeder(img_cv)
                        time.sleep(1.6)

                    self.total_catch_counter+=1

                    self.total_catch_fish.set("Total Catch: " + str(self.total_catch_counter))
                    
                    end = time.time()
                    self.time_calc.append(round(end-start_time,2))
                    avg = round(sum(self.time_calc) / len(self.time_calc),2)
                    self.calc_total_catch_fish.set("Catch Hour: " + str(round((3600 / avg),2)))


                    pyautogui.mouseDown(button='left')
                    time.sleep(self.rnd(1,1.9))
                    pyautogui.mouseUp(button='left')

                    self.bothandle.found_fish = False

                          
        


        self.root.after(1,self.MainThread)