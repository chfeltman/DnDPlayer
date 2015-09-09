from DnD.Races._Race import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *
from DnD.Common._Constants import *

class HalfElf(Race):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.CHA] += 2
        self.__name = "Half-Elf"
        self.__speed = 30
        self.__aveLife = 180
        self.__adultAge = 20
        self.__size = SIZE.MEDIUM
        self.__languages.extend((Language.COMMON, Language.ELVISH))
        self.__abilities.extend((
            (ChooseAbilityScore(), (2, 1)),
            (ChooseLanguage(), (1)),
            FeyAncestry(),
            (ChooseSkill(), (2))))        
            
        self.__traits.append(Traits.Darkvision())
        
        