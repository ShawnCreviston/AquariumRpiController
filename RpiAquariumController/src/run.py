'''
Created on Jan 6, 2014

@author: Shawn
'''
from Tkinter import Tk, Label, Button, StringVar
from org.aesrc.gui import AesrcMain

print"Aquarium Eco System Controller startup..."

# Create main thread to run controller
mainThread = AesrcMain.AesrcMain()

# Create main GUI window
topWin = Tk()

mainThread.guiOut.setupStringVars(topWin)

# Fancy Label
Label(text="Aquarium Controller").pack()
Label(text="Actinic Lights").pack()

Label(topWin, textvariable=mainThread.guiOut.actinicLightValue1).pack()
Label(topWin, textvariable=mainThread.guiOut.actinicLightValue2).pack()
Label(topWin, textvariable=mainThread.guiOut.actinicLightValue3).pack()
# Create button action
def actToggle():
    if mainThread.mainController.mainDayController.overrideActinic:
        mainThread.mainController.mainDayController.overrideActinic = False
    else:
        mainThread.mainController.mainDayController.overrideActinic = True

# Create actual button
Button(text="Force On", command= actToggle).pack()

Label(text="MainLights").pack()
Label(topWin, textvariable=mainThread.guiOut.mainLightValue1).pack()
Label(topWin, textvariable=mainThread.guiOut.mainLightValue2).pack()
Label(topWin, textvariable=mainThread.guiOut.mainLightValue3).pack()
# Create button action
def mainToggle():
    if mainThread.mainController.mainDayController.overrideMain:
        mainThread.mainController.mainDayController.overrideMain = False
    else:
        mainThread.mainController.mainDayController.overrideMain = True

# Create actual button
Button(text="Force On", command= mainToggle).pack()

Label(text="Moon Lights").pack()
Label(topWin, textvariable=mainThread.guiOut.moonLightValue).pack()
# Create button action
def moonToggle():
    if mainThread.mainController.mainDayController.overrideMoon:
        mainThread.mainController.mainDayController.overrideMoon = False
    else:
        mainThread.mainController.mainDayController.overrideMoon = True

# Create actual button
Button(text="Force On", command= moonToggle).pack()

Label(text="Sump Lights").pack()
# Create button action
def sumpToggle():
    if mainThread.mainController.mainDayController.overrideSump:
        mainThread.mainController.mainDayController.overrideSump = False
    else:
        mainThread.mainController.mainDayController.overrideSump = True

# Create actual button
Button(text="Force On", command= sumpToggle).pack()

# Quit button for gui
# Create button action
def endApp():
    mainThread.running = False
    topWin.quit()

# Create actual button
Button(text="Quit", command= endApp).pack()

# Start controller thread
mainThread.start();

#run gui
topWin.mainloop()

mainThread.join()

topWin.destroy()

print "Shutdown"
