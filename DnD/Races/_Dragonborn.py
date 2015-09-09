from DnD.Races._Race import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *
from DnD.Common._Constants import *

class Dragonborn(Race):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.STR] += 2
        self.__name = "Dragonborn"
        self.__speed = 30
        self.__aveLife = 80
        self.__adultAge = 15
        self.__size = SIZE.MEDIUM
        self.__languages.extend((Language.COMMON, Language.DRACONIC))
        self.__abilities.extend(( 
            DraconicAncestry(), 
            BreathWeapon(), 
            DraconicDamageResistance()))
        