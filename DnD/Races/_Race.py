from DnD.Common._Constants import *
from DnD.Common._Decorators import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *

class Race(object):
    def __init__(self):
        self.__name = None
        self.__scoreMod = {
            AbilityType.STR : 0, 
            AbilityType.DEX : 0, 
            AbilityType.CON : 0, 
            AbilityType.INT : 0, 
            AbilityType.WIS : 0, 
            AbilityType.CHA : 0
        }
        
        self.__adultAge = 0
        self.__aveLife = 0
        self.__traits = []
        self.__speed = 0
        self.__size = Size.MEDIUM
        self.__languages = []
        self.__abilities = []
        self.__traits = []
        
    @property
    def AbilityScoreModifiers(self):
        return self.__scoreMod
    
    @property
    def Name(self):
        return self.__name

    @property
    def AgeOfAdulthood(self):
        return self.__adultAge
    
    @property
    def AverageLifespan(self):
        return self.__aveLife
        
    @property
    def Speed(self):
        return self.__speed
        
    @property
    def Size(self):
        return self.__size
        
    @property
    def RacialLanguages(self):
        return self.__languages
    
    @property
    def Abilites(self):
        return self.__abilities
    
    @property
    def Traits(self):
        return self.__traits
        
        
        