'''
Created on Jan 6, 2014

@author: Shawn
'''
from Tkinter import Tk, Label, Button
from org.aesrc.gui import AesrcMain

print "Aquarium Eco System Controller startup..."

# Create main thread to run controller
mainThread = AesrcMain()

# Create main GUI window
topWin = Tk()

# Fancy Label
topWinLbl = Label(text="Aquarium Controller")
topWinLbl.pack()

# Quit button for gui
# Create button action
def endApp():
    mainThread.running = False
    topWin.quit()

# Create actual button
topWinBtn = Button(text="Quit", command= endApp)
topWinBtn.pack()

# Start controller thread
mainThread.start();

#run gui
topWin.mainloop()
topWin.destroy()

mainThread.join()