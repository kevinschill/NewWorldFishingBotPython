import tkinter as tk




class RectShow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.resizable(False, False)
        self.attributes('-fullscreen', True)
        self.wm_attributes('-alpha', 0.1)
        self.canvas = tk.Canvas(self, width=512, height=512, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.bind("<Return>",self.enterPress)
        self.rect = None

        self.start_x = None
        self.start_y = None

        self.final_coords = None
    def enterPress(self,event):
        self.quit()
        self.destroy()

    def getCoords(self):
        return self.final_coords

        self.quit()
        self.destroy()

    def close(self):
        self.quit()
        self.destroy()  

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline="red", width=3)

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)
    


    def on_button_release(self, event):
        self.final_coords = (self.start_x,self.start_y,event.x,event.y)