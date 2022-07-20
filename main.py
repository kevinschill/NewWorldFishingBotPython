from gui.gui import *
from gui.rect import *
from bot import *


botHandle = Bot()
guiHandle = MainGui(botHandle)








guiHandle.SettingTab()
guiHandle.BotSettings()
guiHandle.LoadConfig()

guiHandle.root.after(1, guiHandle.MainThread)
guiHandle.startGui()