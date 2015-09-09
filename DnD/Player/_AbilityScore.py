from DnD.Common._Constants import *
from DnD.Common._Decorators import *

class AbilityScore:
    def __init__(self, abilityType):
        
        if not (isinstance(abilityType, AbilityType)):
            raise ValueError("Must be of type AbilityType")
                
        self.__type = abilityType

    @property
    def Modifier(self):
        return AbilityModifiers[self.Value]

    @property
    def Type(self):
        return self.__type
                
    @property
    def Value(self):
        return self.__value
        
    @Value.setter
    @ValidateType(int)
    @ValidateRange([1, 21])
    def Value(self, value):            
        self.__value = value
