'''
Created on Jan 6, 2014

@author: Shawn
'''
from org.aesrc.enums.RelayStatus import RelayStatus

class LightModule(object):
    '''
    classdocs
    '''
    # Current LIght Intensity, -1 to 1
    intensity = 0
    
    # Main power relay status
    # From RelayStatus enum class
    relayStatus = RelayStatus.RELAY_UNKNOWN
    prevRelayStatus = RelayStatus.RELAY_UNKNOWN
    
    # Override main power relay status
    overrideRelayStatus = RelayStatus.RELAY_UNKNOWN
    
    # Raspberry PI GPIO pin for main relay
    relayPin = -1
    
    # Arduino Uno PWM pin for dimming
    pwmPin = -1

    def __init__(self):
        '''
        Constructor
        '''
        
    
    def setIntensity(self, intensity):
        if intensity < -1:
            intensity = -1
        elif intensity > 1:
            intensity = 1
            
        self.intensity = intensity