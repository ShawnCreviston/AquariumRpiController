'''
Created on Jan 6, 2014

@author: Shawn
'''
import math
from org.aesrc.formulas import MoonCycleFormula


def getTideHeightIntensity(decimalTideTime):
    # Intensity, -1 to 1
    
    # Tide height Formula
    # Calculate the intensity for the semi-diurnal tide cycle
    i = .93*math.cos((4.0*math.pi*decimalTideTime))
    
    # Calculate the intensity for the mixed tide cycle cycle
    # With two tides per day one is larger on the side of the earth facing
    # the moon, this formula simulates that shift by reducing the main
    # mid day high tide by about 20%. Likewise the low tide is adjusted.
    i += .1*math.cos(2*math.pi*(decimalTideTime+0.125))
    
    # Calculate the intensity for the moon phase
    # Moon time = 0 is Full moon
    i *= 0.75+ 0.25*math.cos(4.0*math.pi*decimalTideTime/30.416667)
    
    return i
    
def getTideFlowIntensity(decimalTideTime):
    # Intensity, -1 to 1
    
    # Tide flow Formula
    # This is the same as the tide height formula, but shifted
    # so that at peak high/low tide the flow intensity is 0
    # Calculate the intensity for the semi-diurnal tide cycle
    i = .93*math.cos((4.0*math.pi*(decimalTideTime+0.125)));
                
    #Calculate the intensity for the mixed tide cycle cycle
    # With two tides per day one is larger on the side of the earth facing
    # the moon, this formula simulates that shift by reducing the main
    # mid day high tide by about 20%. Likewise the low tide is adjusted.
    i += .1*math.cos(2*math.pi*(decimalTideTime+0.25));
        
    # Calculate the intensity for the moon phase
    # Moon time = 0 is Full moon
    i *= 0.75+ 0.25*math.cos(4.0*math.pi*decimalTideTime/30.416667);
        
    return i;
    
def getDecimalTideTime(dayOfYear, hourOfDay, minute):
    # The tidal changes lag behind the moon phase by a couple days
    return MoonCycleFormula.getDecimalMoonTime(dayOfYear-2, hourOfDay, minute)
    
# eof