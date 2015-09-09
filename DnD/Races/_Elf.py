from DnD.Races._Race import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *
from DnD.Common._Constants import *

class Elf(Race):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.DEX] += 2
        self.__name = "Elf"
        self.__speed = 30
        self.__aveLife = 700
        self.__adultAge = 100
        self.__size = SIZE.MEDIUM
        self.__languages.extend((Language.COMMON, Language.ELVISH))
        self.__abilities.extend(( 
            KeenSenses(), 
            FeyAncestry()))
             
        self.__traits.extend((
            Darkvision(), 
            Trance()))
        
class HighElf(Elf):
    def __inti__(self):
        super().__init__()
        self.__name = "High Elf"
        self.AbilityScoreModifiers[AbilityType.INT] += 1
        self.__abilities.extend(( 
            ElfWeaponTraining(), 
            (ChooseCantrip(), (1, SpellClass.WIZARD, AbilityType.INT)), 
            (ChooseLanguage(), (1))))
        
class WoodElf(Elf):
    def __init__(self):
        super().__init__()
        self.__name = "Wood Elf"
        self.AbilityScoreModifiers[AbilityType.WIS] += 1
        self.__speed = 35
        self.__abilities.append(ElfWeaponTraining())        
        self.__traits.append(MaskofTheWind())

class DarkElf(Elf):
    def __init__(Self):
        super().__init__()
        self.__name = "Dark Elf"
        self.AbilityScoreModifiers[AbilityType.CHA] += 1
        self.__abilities.extend(( 
            SunlightSensitivity(), 
            DrowMagic(), 
            DrowWeaponTraining()))
        
        self.__traits.append(SuperiorDarkvision())        
        
        