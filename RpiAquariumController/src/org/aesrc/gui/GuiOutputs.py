'''
Created on Jan 6, 2014

@author: Shawn
'''
from Tkinter import StringVar

class GuiOutputs(object):
    actinicLightValue1 = 0
    actinicLightValue2 = 0
    actinicLightValue3 = 0
    
    mainLightValue1 = 0
    mainLightValue2 = 0
    mainLightValue3 = 0

    moonLightValue = 0

    #tideLevelValue = 0

    def __init__(self):
        '''
        Constructor
        '''
 
    def setupStringVars(self, topWin):
        self.actinicLightValue1 = StringVar(topWin, "xxxx")
        self.actinicLightValue2 = StringVar(topWin, "xxxx")
        self.actinicLightValue3 = StringVar(topWin, "xxxx")

        self.mainLightValue1 = StringVar(topWin, "xxxx")
        self.mainLightValue2 = StringVar(topWin, "xxxx")
        self.mainLightValue3 = StringVar(topWin, "xxxx")

        self.moonLightValue = StringVar(topWin, "xxxx")

        #self.tideLevelValue = StringVar(topWin, "xxxx")

