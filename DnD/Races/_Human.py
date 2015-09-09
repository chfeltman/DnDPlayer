from DnD.Races._Race import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *
from DnD.Common._Constants import *

class Human(Race):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.STR] += 1
        self.AbilityScoreModifiers[AbilityType.CON] += 1
        self.AbilityScoreModifiers[AbilityType.DEX] += 1
        self.AbilityScoreModifiers[AbilityType.INT] += 1
        self.AbilityScoreModifiers[AbilityType.WIS] += 1
        self.AbilityScoreModifiers[AbilityType.CHA] += 1
        self.__name = "Human"
        self.__speed = 30
        self.__aveLife = 75
        self.__adultAge = 18
        self.__size = SIZE.MEDIUM
        self.__languages.append(Language.COMMON)
        self.__abilities.append((ChooseLanguage(), (1)))
        