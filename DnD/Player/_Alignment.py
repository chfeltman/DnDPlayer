from DnD.Common._Decorators import *
from DnD.Common._Constants import Temperment as Temper
from DnD.Common._Constants import Morality as Moral

class Alignment(object):
    def __init__(self, temperment, morality):
        self.Temperment = temperment                
        self.Morality = morality
        
    @property
    def Temperment(self):
        return self.__temperment
        
    @Temperment.setter
    @ValidateType(Temper)
    def Temperment(self, value):
        self.__temperment = value
        
    @property
    def Morality(self):
        return self.__morality
        
    @Morality.setter
    @ValidateType(Moral)
    def Morality(self, value):        
        self.__morality = value
        