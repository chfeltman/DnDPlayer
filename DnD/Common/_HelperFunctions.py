from DnD.Common._Constants import *

def LevelForExp(exp):
    for key in sorted(Experience, reverse = True):
        if exp >= key:
            return Experience[key]
            
def isNumeric(value):
    values = value

    if not isinstance(value, type([])):
        values = [value]
        
    aggregate = True
    for item in values:
        aggregate = aggregate and isinstance(item, (int, float, complex))
            
    return aggregate