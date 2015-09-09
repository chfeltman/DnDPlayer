from DnD.Common._Description import *

class Trait(object):
    def __init__(self, name):
        self.__name = name
        self.__desc = Description()
        
    @property
    def Name(self):
        return self.__name
    
    @property
    def Description(self):
        return self.__desc
        
class Darkvision(Trait):
    def __init__(self):
        super().__init__("Darkvision")
        self.__desc.Brief = "You can see clearly in dim light within 60 ft"
        
class Stonecunning(Trait):
    def __init__(self):
        super().__init__("Stonecunning")
        self.__desc.Brief = "Double proficient in history for stone checks"
    