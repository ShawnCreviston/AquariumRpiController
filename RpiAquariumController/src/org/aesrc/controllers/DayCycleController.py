'''
Created on Jan 5, 2014

@author: Shawn
'''
import datetime
from org.aesrc.formulas import MoonCycleFormula, DayCycleFormula,\
    TideCycleFormula
from org.aesrc.enums.RelayStatus import RelayStatus

class DayCycleController(object):
    '''
    classdocs
    '''

    # Full power limit, a way to cap the maximum intensity if you don't
    # want to run the lights at 100% strength.
    maxPower = 0
    
    # Minimum power limit, the cut off threshold to turn off the lights
    # and main power relays.
    minPower = 0
    
    # Full Moon power, roughly 7% of the suns brightness on a good day.
    maxFullMoonPower = 0
    
    # % of full power drop in winter
    winterDrop = 0

    # The shift values below are a shift in time not intensity
    # See the bottom of file for the time formula
    
    # Sunrise shift, so light can come on around a desired time
    sunriseShift = 0
    
    # Actinic shift, lights follow same pattern as main lights but are
    # on just before and after main lights.
    actinicShift = 0
    
    # Adjust the amount of delay between each module, this is to simulate
    # sunrise on the left end of the tank and sunset on the right end
    moduleShift = 0

    overrideActinic = False
    overrideMain = False
    overrideMoon = False
    overrideSump = False

    def __init__(self):
        '''
        Constructor
        '''
        self.maxPower = 0.90;
        self.minPower = 0.004;
        self.maxFullMoonPower = 0.01;
        
        self.winterDrop = 0.2;
        
        self.sunriseShift = 0.82;
        self.actinicShift = 0.06;
        self.moduleShift = 0.01;
    
    
    def updateLightModules(self, actinicLights, mainLights, moonLights, sumpLights):
        # Intensity 
        i = 0
        # Moon intensity
        mi = 0
        
        # Current Date and Time
        curTime = datetime.datetime.now()
        
        #print "Date: " + str(curTime.timetuple().tm_year)+"-"+ \
        #      StringFormatter.padString("00", str(curTime.timetuple().tm_mon)) +"-"+ \
        #      StringFormatter.padString("00", str(curTime.timetuple().tm_mday))+" Time: "+ \
        #      StringFormatter.padString("00", str(curTime.timetuple().tm_hour))+":"+ \
        #      StringFormatter.padString("00", str(curTime.timetuple().tm_min))
        
        # Start with moon light so that the main lights can be adjusted after sunset
        dt = MoonCycleFormula.getDecimalMoonTime(curTime.timetuple().tm_yday-1, curTime.timetuple().tm_hour, curTime.timetuple().tm_min)
        
        # Update Moon lights
        cnt = 0
        for light in moonLights:
            mi = MoonCycleFormula.getDayLightIntensity(dt)
            
            light.setIntensity(self.limitIntensityRange(mi*self.maxPower))
            
            #print "Moon Intensity "+str(cnt)+": "+str(self.roundToPercentage(light.intensity))+"%"
            
            if light.intensity < self.minPower:
                if light.relayStatus != RelayStatus.RELAY_OFF:
                    light.relayStatus = RelayStatus.RELAY_OFF
                    #print "Relay Off"
            elif light.relayStatus != RelayStatus.RELAY_ON:
                light.relayStatus = RelayStatus.RELAY_ON
                #print "Relay On"

            if self.overrideMoon:
                if light.overrideRelayStatus != RelayStatus.RELAY_ON:
                    light.overrideRelayStatus = RelayStatus.RELAY_ON
            elif light.overrideRelayStatus != RelayStatus.RELAY_OFF:
                light.overrideRelayStatus = RelayStatus.RELAY_OFF
            
            # Update moon intensity for main light use below
            #mi = 0
            mi = mi*self.maxFullMoonPower
            cnt += 1
            
        # Update main lights
        dt = DayCycleFormula.getDecimalDayTime(curTime.timetuple().tm_yday-1, curTime.timetuple().tm_hour, curTime.timetuple().tm_min)
        #dt = DayCycleFormula.getDecimalDayTime(curTime.timetuple().tm_yday-1, 9, 7)        

        # Update Actinic Lights
        cnt = 0
        for light in actinicLights:
            i = DayCycleFormula.getDayLightIntensity(dt, self.sunriseShift - self.moduleShift*cnt, self.winterDrop) + self.actinicShift
            
            # Compare to moon light, using main lights as moon light
            i = max(i, mi)
            
            light.setIntensity(self.limitIntensityRange(i*self.maxPower))
            
            #print "Actinic Intensity "+str(cnt)+": "+str(self.roundToPercentage(light.intensity))+"%"
            
            if light.intensity < self.minPower:
                if light.relayStatus != RelayStatus.RELAY_OFF:
                    light.relayStatus = RelayStatus.RELAY_OFF
                    #print "Relay Off"
            elif light.relayStatus != RelayStatus.RELAY_ON:
                light.relayStatus = RelayStatus.RELAY_ON
                #print "Relay On"

            if self.overrideActinic:
                if light.overrideRelayStatus != RelayStatus.RELAY_ON:
                    light.overrideRelayStatus = RelayStatus.RELAY_ON
            elif light.overrideRelayStatus != RelayStatus.RELAY_OFF:
                light.overrideRelayStatus = RelayStatus.RELAY_OFF
            
            cnt += 1
            
        # Update Main Lights
        cnt = 0
        for light in mainLights:
            i = DayCycleFormula.getDayLightIntensity(dt, self.sunriseShift - self.moduleShift*cnt, self.winterDrop)
            
            # Compare to moon light, using main lights as moon light
            #i = max(i, mi-0.04)
            
            light.setIntensity(self.limitIntensityRange(i*self.maxPower))
            
            #print "Main Intensity "+str(cnt)+": "+str(self.roundToPercentage(light.intensity))+"%"
            
            if light.intensity < self.minPower:
                if light.relayStatus != RelayStatus.RELAY_OFF:
                    light.relayStatus = RelayStatus.RELAY_OFF
                    #print "Relay Off"
            elif light.relayStatus != RelayStatus.RELAY_ON:
                light.relayStatus = RelayStatus.RELAY_ON
                #print "Relay On"

            if self.overrideMain:
                if light.overrideRelayStatus != RelayStatus.RELAY_ON:
                    light.overrideRelayStatus = RelayStatus.RELAY_ON
            elif light.overrideRelayStatus != RelayStatus.RELAY_OFF:
                light.overrideRelayStatus = RelayStatus.RELAY_OFF
            
            cnt += 1
            
        # Update Sump lights, which run opposite the main lights
        cnt = 0
        for light in sumpLights:
            i = -DayCycleFormula.getDayLightIntensity(dt, self.sunriseShift - self.moduleShift*cnt, self.winterDrop)
            
            light.setIntensity(self.limitIntensityRange(i*self.maxPower))
            
            #print "Sump Intensity "+str(cnt)+": "+str(self.roundToPercentage(light.intensity))+"%"
            
            if light.intensity < self.minPower:
                if light.relayStatus != RelayStatus.RELAY_OFF:
                    light.relayStatus = RelayStatus.RELAY_OFF
                    #print "Relay Off"
            elif light.relayStatus != RelayStatus.RELAY_ON:
                light.relayStatus = RelayStatus.RELAY_ON
                #print "Relay On"

            if self.overrideSump:
                if light.overrideRelayStatus != RelayStatus.RELAY_ON:
                    light.overrideRelayStatus = RelayStatus.RELAY_ON
            elif light.overrideRelayStatus != RelayStatus.RELAY_OFF:
                light.overrideRelayStatus = RelayStatus.RELAY_OFF
            
            cnt += 1
            
        # Calculate Tides
        dt = TideCycleFormula.getDecimalTideTime(curTime.timetuple().tm_yday-1, curTime.timetuple().tm_hour, curTime.timetuple().tm_min)
        
        i = TideCycleFormula.getTideHeightIntensity(dt)
        #print "Tide Levels: " + str(self.roundToPercentage(i))+"%"
        
        i = TideCycleFormula.getTideFlowIntensity(dt)
        #print "Tide Flow: " + str(self.roundToPercentage(i))+"%"
            
    def limitIntensityRange(self, i):
        return max(0.0, min(1.0, i))
        
    def roundToPercentage(self, intensity):
        return int(round(intensity*100.0))


# eof

