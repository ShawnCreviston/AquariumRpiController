'''
Created on Jan 6, 2014

@author: Shawn
'''
from nanpy import Arduino
from nanpy import serial_manager
import RPi.GPIO as gpio
import time
from org.aesrc.valueObjects import LightModule
from org.aesrc.controllers.DayCycleController import DayCycleController
from org.aesrc.enums.RelayStatus import RelayStatus
from org.aesrc.gui import GuiOutputs

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

    guiOut = 0

    runDemoCycle = False

    def __init__(self):
        '''
        Constructor
        '''
        
    def initMainController(self, guiOut):
        self.guiOut = guiOut
        self.mainDayController = DayCycleController()
        
        print "Connecting to Arduino"
        # serial connection to Arduino
        serial_manager.connect('/dev/ttyACM0')
        time.sleep(1)
        Arduino.pinMode(3, Arduino.OUTPUT)
        Arduino.pinMode(5, Arduino.OUTPUT)
        Arduino.pinMode(6, Arduino.OUTPUT)
        Arduino.pinMode(9, Arduino.OUTPUT)
        Arduino.pinMode(10, Arduino.OUTPUT)
        Arduino.pinMode(11, Arduino.OUTPUT)
        time.sleep(1)

        print "Settip up rpi GPIO pins"
        gpio.setmode(gpio.BOARD)
        gpio.setup(3, gpio.OUT)
        gpio.setup(5, gpio.OUT)
        gpio.setup(7, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)
        gpio.setup(19, gpio.OUT)
        gpio.setup(21, gpio.OUT)
        time.sleep(2)
        
        print "Setting up light modules"
        # Actinics
        lm = LightModule.LightModule()
        lm.relayPin = 19
        lm.pwmPin = 3
        self.actinicLights.append(lm)
        self.allLights.append(lm)
        
        lm = LightModule.LightModule()
        lm.relayPin = 15
        lm.pwmPin = 6
        self.actinicLights.append(lm)
        self.allLights.append(lm)
        
        lm = LightModule.LightModule()
        lm.relayPin = 11
        lm.pwmPin = 10
        self.actinicLights.append(lm)
        self.allLights.append(lm)
        
        # Main Lights
        lm = LightModule.LightModule()
        lm.relayPin = 21
        lm.pwmPin = 5
        self.mainLights.append(lm)
        self.allLights.append(lm)
        
        lm = LightModule.LightModule()
        lm.relayPin = 13
        lm.pwmPin = 9
        self.mainLights.append(lm)
        self.allLights.append(lm)
        
        lm = LightModule.LightModule()
        lm.relayPin = 7
        lm.pwmPin = 11
        self.mainLights.append(lm)
        self.allLights.append(lm)
        
        # Moon Lights
        lm = LightModule.LightModule()
        lm.relayPin = 5
        self.moonLights.append(lm)
        self.allLights.append(lm)
        
        # Sump Lights
        lm = LightModule.LightModule()
        lm.relayPin = 3
        self.sumpLights.append(lm)
        self.allLights.append(lm)
            
        time.sleep(2)
    
    def runMainController(self):
        # Update Lights
        self.mainDayController.updateLightModules(self.actinicLights, self.mainLights, self.moonLights, self.sumpLights)
        # Update Relays and PWM
        self.updateRelaysAndPWM()

    def updateRelaysAndPWM(self):    
        # Update relays and PWM
        for lm in self.allLights:
            if lm.relayPin > -1:
                if lm.overrideRelayStatus == RelayStatus.RELAY_ON:
                    lm.prevRelayStatus = lm.overrideRelayStatus

                    # Set pin low to turn on relay
                    gpio.output(lm.relayPin, 0)
                    if lm.pwmPin > -1:
                        pwmI = int(round(.8*255))
                    
                        # Double validation check to ensure correct range for PWM
                        if pwmI < 0:
                            pwmI = 0
                        elif pwmI > 255:
                            pwmI = 255
                        
                        # Add code here to toggle pwm
                        #print str(lm.pwmPin) + ">" + str(pwmI)
                        Arduino.analogWrite(lm.pwmPin, pwmI)
                    
                elif lm.prevRelayStatus != lm.relayStatus:
                    lm.prevRelayStatus = lm.relayStatus
                    
                    if (lm.relayStatus == RelayStatus.RELAY_ON):
                        # Set pin low to turn on relay
                        gpio.output(lm.relayPin, 0)
                    elif (lm.relayStatus == RelayStatus.RELAY_OFF):
                        # Set pin high to turn off relay
                        gpio.output(lm.relayPin, 1)
                
                if lm.pwmPin > -1:
                    pwmI = int(round(lm.intensity*255))
                    
                    # Double validation check to ensure correct range for PWM
                    if pwmI < 0:
                        pwmI = 0
                    elif pwmI > 255:
                        pwmI = 255
                        
                    # Add code here to toggle pwm
                    #print str(lm.pwmPin) + ">" + str(pwmI)
                    Arduino.analogWrite(lm.pwmPin, pwmI)

    def updateGui(self):
        cnt = 0
        forceStr = ""
        for light in self.actinicLights:
            if cnt == 0:
                if light.overrideRelayStatus == RelayStatus.RELAY_ON:
                    forceStr = " (F ON)"
                self.guiOut.actinicLightValue1.set(str(self.roundToPercentage(light.intensity))+"%"+forceStr)
            elif cnt == 1:
                self.guiOut.actinicLightValue2.set(str(self.roundToPercentage(light.intensity))+"%"+forceStr)
            elif cnt == 2:
                self.guiOut.actinicLightValue3.set(str(self.roundToPercentage(light.intensity))+"%"+forceStr)
            cnt += 1

        cnt = 0
        forceStr = ""
        for light in self.mainLights:
            if cnt == 0:
                if light.overrideRelayStatus == RelayStatus.RELAY_ON:
                    forceStr = " (F ON)"
                self.guiOut.mainLightValue1.set(str(self.roundToPercentage(light.intensity))+"%"+forceStr)
            elif cnt == 1:
                self.guiOut.mainLightValue2.set(str(self.roundToPercentage(light.intensity))+"%"+forceStr)
            elif cnt == 2:
                self.guiOut.mainLightValue3.set(str(self.roundToPercentage(light.intensity))+"%"+forceStr)
            cnt += 1

        forceStr = ""
        for light in self.moonLights:
            if light.overrideRelayStatus == RelayStatus.RELAY_ON:
                    forceStr = " (F ON)"
            self.guiOut.moonLightValue.set(str(self.roundToPercentage(light.intensity))+"%"+forceStr)

        #for light in self.moonLightsmainLights:
        #   self.guiOut.moonLightValue.set(str(self.roundToPercentage(light.intensity))+"%")

    def roundToPercentage(self, intensity):
        return int(round(intensity*100.0))
#eof
        
