from DnD.Races._Race import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *
from DnD.Common._Constants import *

class Tiefling(Race):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.CHA] += 2
        self.AbilityScoreModifiers[AbilityType.INT] += 1
        self.__name = "Tiefling"
        self.__speed = 30
        self.__aveLife = 85
        self.__adultAge = 18
        self.__size = SIZE.MEDIUM
        self.__languages.extend((Language.COMMON, Language.INFERNAL))
        self.__abilities.extend((
            HellishResistance(),
            InfernalLegacy()))
            
        self.__traits.append(Darkvision())
        
        