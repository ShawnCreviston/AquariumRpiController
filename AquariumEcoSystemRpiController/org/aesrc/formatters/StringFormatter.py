'''
Created on Jan 6, 2014

@author: Shawn
'''
def padString(padding, stringToPad):
    if len(stringToPad) < len(padding):
        stringToPad = padding + stringToPad
        return stringToPad[len(stringToPad) - len(padding):len(stringToPad)]
    # nothing to pad
    return stringToPad