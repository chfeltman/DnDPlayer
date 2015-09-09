from DnD.Races._Race import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *
from DnD.Common._Constants import *

class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.CON] += 2
        self.__name = "Dwarf"
        self.__speed = 25
        self.__aveLife = 350
        self.__adultAge = 50
        self.__size = SIZE.MEDIUM
        self.__languages.extend((Language.COMMON, Language.DWARVISH))
        self.__abilities.extend(( 
            DwarvenRisilience(), 
            DwarvenCombatTraining(), 
            ToolProficiency(),
            Stonecunning()))
             
        self.__traits.append(Darkvision())
        
class HillDwarf(Dwarf):
    def __inti__(self):
        super().__init__()
        self.__name = "Hill Dwarf"
        self.AbilityScoreModifiers[AbilityType.WIS] += 1
        self.__abilities.append(DwarvenToughness())
        
class MountainDwarf(Dwarf):
    def __init__(self):
        super().__init__()
        self.__name = "Mountain Dwarf"
        self.AbilityScoreModifiers[AbilityType.STR] += 2
        self.__abilities.append(DwarvenArmorTraining())