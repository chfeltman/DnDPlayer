from DnD.Common._Constants import *
from DnD.Common._Decorators import *
from DnD.Common._HelperFunctions import *
from DnD.Player._AbilityScore import *
from DnD.Player._Alignment import Alignment as Align
from DnD.Races._Race import *

class PlayerModel:
    def __init__(self):
        self.__exp = 0
        self.__str = AbilityScore(AbilityType.STR)
        self.__int = AbilityScore(AbilityType.INT)
        self.__dex = AbilityScore(AbilityType.DEX)
        self.__wis = AbilityScore(AbilityType.WIS)
        self.__cha = AbilityScore(AbilityType.CHA)
        self.__con = AbilityScore(AbilityType.CON)
        self.__age = 20
        self.__alignment = Align(Temperment.Neutral, Morality.Neutral)
        self.__languages = [Language.COMMON]
        self.__name = None
        # self.__armor = 
        # self.__race = 
        # self.__class = 
        self.__hitPoints = 0

    # READ ONLY PROPERTIES
    @property
    def Level(self):
        return LevelForExp(self.__exp)
    
    @property
    def ArmorClass(self):
        return 10 + self.Dex.Modifier

    # READ WRITE PROPERTIES
    
    @property
    def Alignment(self):
        return self.__alignment

    @Alignment.setter
    @ValidateType(Align)
    def Alignment(self, value):
        self.__alignment = value
    
    @property
    def Age(self):
        return self.__age
    
    @Age.setter
    @ValidateType(int)
    @ValidateMinimum(1)
    def Age(self, value):
        self.__age = value
        
    @property
    def Exp(self):
        return self.__exp
    
    @Exp.setter
    @ValidateType(int)
    @ValidateMinimum(0)
    def Exp(self, value):            
        self.__exp = value
                
    @property
    def Str(self):
        return self.__str
        
    @Str.setter
    def Str(self, value):
        self.__str.Value = value

    @property
    def Int(self):
        return self.__int
        
    @Int.setter
    def Int(self, value):
        self.__int.Value = value

    @property
    def Dex(self):
        return self.__dex
        
    @Dex.setter
    def Dex(self, value):
        self.__dex.Value = value

    @property
    def Wis(self):
        return self.__wis
        
    @Wis.setter
    def Wis(self, value):
        self.__wis.Value = value

    @property
    def Cha(self):
        return self.__cha
        
    @Cha.setter
    def Cha(self, value):
        self.__cha.Value = value

    @property
    def Con(self):
        return self.__con
        
    @Con.setter
    def Str(self, value):
        self.__con.Value = value
        