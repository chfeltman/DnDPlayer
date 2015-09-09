from DnD.Races._Race import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *
from DnD.Common._Constants import *

class Gnome(Race):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.INT] += 2
        self.__name = "Gnome"
        self.__speed = 25
        self.__aveLife = 425
        self.__adultAge = 40
        self.__size = SIZE.SMALL
        self.__languages.extend((Language.COMMON, Language.GNOMISH))
        self.__abilities.append(GnomeCunning())
            
        self.__traits.append(Darkvision())

class ForestGnome(Gnome):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.DEX] += 1
        self.__name = "Forest Gnome"
        self.__abilities.append(NaturalIllusionist())
        self.__traits.append(SpeakWithSmallBeasts())
        
class RockGnome(Gnome):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.CON] += 1
        self.__name = "Rock Gnome"
        self.__abilities.extend((
            ArtificersLore(),
            Tinker()))