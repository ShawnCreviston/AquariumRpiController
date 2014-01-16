'''
Created on Jan 6, 2014

@author: Shawn
'''
import math

def getDayLightIntensity(decimalDayTime, sunriseShift, winterDrop):
    # Intensity, -1 to 1
    
    # Daylight Hours Formula
    # Calculate the intensity for the daily sun cycle
    i = math.cos((2.0*math.pi*decimalDayTime)+sunriseShift*math.pi)
    
    # Calculate the seasonal shift for intensity and hours of daylight
    i -= (winterDrop*math.cos(2.0*math.pi*decimalDayTime/365.0))
    
    return i
    
    
def getDecimalDayTime(dayOfYear, hourOfDay, minute):
    return dayOfYear + ((hourOfDay*60.0 + minute)/1440.0)
    
# eof