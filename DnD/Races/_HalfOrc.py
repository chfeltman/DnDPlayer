from DnD.Races._Race import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *
from DnD.Common._Constants import *

class HalfOrc(Race):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.STR] += 2
        self.AbilityScoreModifiers[AbilityType.CON] += 1
        self.__name = "Half-Orc"
        self.__speed = 30
        self.__aveLife = 75
        self.__adultAge = 14
        self.__size = SIZE.MEDIUM
        self.__languages.extend((Language.COMMON, Language.ORC))
        self.__abilities.extend((
            Menacing(),
            RelentlessEndurance(),
            SavageAttacks()))        
            
        self.__traits.append(Darkvision())
        
        