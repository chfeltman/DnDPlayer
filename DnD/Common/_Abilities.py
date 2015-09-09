from DnD.Common._Description import *

class Ability(object):
    def __init__(self, name):
        self.__name = name
        self.__desc = Description()
        
    @property
    def Name(self):
        return self.__name
    
    @property
    def Description(self):
        return self.__desc
        
    def Apply(self, player):
        raise NotImplementedError()
        
class DwarvenResilience(Ability):
    def __init__(self):
        super().__init__("Dwarven Resilience")
        self.__desc.Brief = "Advantage and resistance (Poison)"
        self.__desc.Full = (
            "You have advantage on saving throws against poison and" 
            "resistance against poison damage")        
    
class DwarvenCombatTraining(Ability):
    def __init__(self):
        super().__init__("Dwarven Combat Training")
        self.__desc.Brief = "Weapon Proficiencies"
        self.__desc.Full = (
            "You have proficiency with the battleaxe, handaxe, light hammer"
            "and warhammer") 

class ToolProficiency(Ability):
    def __init__(self, toolType):
        raise NotImplementedError()
            
class SmithToolProficiency(Ability):
    def __init__(self, toolType):
        super().__init__("Smith Tool Proficiency")
        self.__desc.Brief = "Proficient with Smilth's Tools"
        self.__desc.Full = "Proficient with Smilth's Tools"

class BrewerToolProficiency(Ability):
    def __init__(self, toolType):
        super().__init__("Brewer Tool Proficiency")
        self.__desc.Brief = "Proficient with Brewer's Tools"
        self.__desc.Full = "Proficient with Brewer's Tools"

class MasonToolProficiency(Ability):
    def __init__(self, toolType):
        super().__init__("Mason Tool Proficiency")
        self.__desc.Brief = "Proficient with Mason's Tools"
        self.__desc.Full = "Proficient with Mason's Tools"
        
class DwarvenToughness(Ability):
    def __init__(self):
        super().__init__("Dwarven Toughness")
        self.__desc.Brief = "Increase max hit points every level"
        self.__desc.Full = (
            "Your hit point maximum increases by , and it increases"
            " by 1 every time you gain a level")
            
class DwarvenArmorTraining(Ability):
    def __init__(self):
        super().__init__("Dwarven Armor Training")
        self.__desc.Brief = "Proficiency with light and medium armor"
        self.__desc.Full = "Proficiency with light and medium armor"