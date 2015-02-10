'''
Created on Jan 6, 2014

@author: Shawn
'''
import math
from org.aesrc.formulas import DayCycleFormula

def getDayLightIntensity(decimalMoonTime):
    # Intensity, -1 to 1
    
    # Moonlight Hours Formula
    # Calculate the intensity for the moon cycle
    i = 0.5+ 0.5*math.cos(2.0*math.pi*decimalMoonTime/30.416667);
    
    return i
    
    
def getDecimalMoonTime(dayOfYear, hourOfDay, minute):
    # Not sure if I need to adjust this yet, for now forward to DayTimeFormula
    return DayCycleFormula.getDecimalDayTime(dayOfYear, hourOfDay, minute)
    
# eof