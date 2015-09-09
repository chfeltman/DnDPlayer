from DnD.Common._Constants import *

class ClassTableEntry(object):
    def __init__(self, proficiencyBonus, features):
        self.__proficiencyBonus = profieciencyBonus
        self.__features = features
        
    @property
    def Level(self):
        return self.__level
        
    @property
    def ProficiencyBonus(self):
        return self.__proficiencyBonus
        
    @property
    def Features(self):
        return self.__features

class MagicTableEntry(object):
    def __init__(self, proficiencyBonus, features, spellSlots):
        super().__init__(proficiencyBonus, features)
        self.__slots = spellSlots
    
    @property
    def Slots(self):
        return self.__slots
        
class Class(object):
    def __init__(self):
        self.__name = None
        self.__classTable = {}
        self.__hitDice = DICE.D6
        self.__proficiencies = []
        self.__savingThrows = []
        self.__skills = []
        self.__startingEquipment = []
        
    @property 
    def Name(self):
        return self.__name
        
    @property
    def ClassTable(self):
        return self.__classTable
        