from DnD.Races._Race import *
from DnD.Common._Abilities import *
from DnD.Common._Traits import *
from DnD.Common._Constants import *

class Halfling(Race):
    def __init__(self):
        super().__init__()
        self.AbilityScoreModifiers[AbilityType.DEX] += 2
        self.__name = "Halfling"
        self.__speed = 25
        self.__aveLife = 150
        self.__adultAge = 20
        self.__size = SIZE.SMALL
        self.__languages.extend((Language.COMMON, Language.HALFLING))
        self.__abilities.extend(( 
            Lucky(), 
            Brave()))
             
        self.__traits.append(HalflingNimbleness())
        
class Lightfoot(Halfling):
    def __inti__(self):
        super().__init__()
        self.__name = "Lightfoot"
        self.AbilityScoreModifiers[AbilityType.CHA] += 1
        self.__traits.append(NaturallyStealthy())
        
class Stout(Halfling):
    def __init__(self):
        super().__init__()
        self.__name = "Stout"
        self.AbilityScoreModifiers[AbilityType.CON] += 1
        self.__abilities.append(StoutResilience())

        