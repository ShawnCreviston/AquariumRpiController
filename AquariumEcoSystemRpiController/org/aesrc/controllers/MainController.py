'''
Created on Jan 6, 2014

@author: Shawn
'''
from org.aesrc.valueObjects import LightModule
from org.aesrc.controllers.DayCycleController import DayCycleController
from org.aesrc.enums.RelayStatus import RelayStatus

class MainController(object):
    '''
    classdocs
    '''
    # Main Daylight cycle controller
    mainDayController = 0
    
    # Lists for lights
    actinicLights = []
    mainLights = []
    moonLights = []
    sumpLights = []
    allLights = []

    def __init__(self):
        '''
        Constructor
        '''
        
    def initMainController(self):
        self.mainDayController = DayCycleController()
        
        # Actinics
        lm = LightModule.LightModule()
        lm.relayPin = 3
        lm.pwmPin = 3
        self.actinicLights.append(lm)
        self.allLights.append(lm)
        
        lm = LightModule.LightModule()
        lm.relayPin = 5
        lm.pwmPin = 5
        self.actinicLights.append(lm)
        self.allLights.append(lm)
        
        lm = LightModule.LightModule()
        lm.relayPin = 7
        lm.pwmPin = 6
        self.actinicLights.append(lm)
        self.allLights.append(lm)
        
        # Main Lights
        lm = LightModule.LightModule()
        lm.relayPin = 11
        lm.pwmPin = 9
        self.mainLights.append(lm)
        self.allLights.append(lm)
        
        lm = LightModule.LightModule()
        lm.relayPin = 13
        lm.pwmPin = 10
        self.mainLights.append(lm)
        self.allLights.append(lm)
        
        lm = LightModule.LightModule()
        lm.relayPin = 15
        lm.pwmPin = 11
        self.mainLights.append(lm)
        self.allLights.append(lm)
        
        # Moon Lights
        lm = LightModule.LightModule()
        lm.relayPin = 19
        self.moonLights.append(lm)
        self.allLights.append(lm)
        
        # Sump Lights
        lm = LightModule.LightModule()
        lm.relayPin = 21
        self.sumpLights.append(lm)
        self.allLights.append(lm)
        
    def runMainController(self):
        # Update Lights
        self.mainDayController.updateLightModules(self.actinicLights, self.mainLights, self.moonLights, self.sumpLights)
        
        # Update relays and PWM
        for lm in self.allLights:
            if lm.relayPin > -1:
                if lm.prevRelayStatus != lm.relayStatus:
                    lm.prevRelayStatus = lm.relayStatus
                    
                    if (lm.relayStatus == RelayStatus.RELAY_ON):
                        # Add code here to toggle relay
                        foo = 1
                    elif (lm.relayStatus == RelayStatus.RELAY_OFF):
                        # Add code here to toggle relay
                        foo = 2
                
                if lm.pwmPin > -1:
                    pwmI = self.mainDayController.roundToPercentage(lm.intensity*255)
                    
                    # Double validation check to ensure correct range for PWM
                    if pwmI < 0:
                        pwmI = 0
                    elif pwmI > 255:
                        pwmI = 255
                        
                    # Add code here to toggle pwm
                    foo = 3
                    
#eof
        