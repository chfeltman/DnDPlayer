from DnD.Common._Constants import *

class Skill(object):
    def __init__(self, name, check):
        self.__name = name
        self.__type = check
        
    @property
    def Name(self):
        return self.__name
        
    @property
    def Check(self):
        return self.__check
        
class Athletics(Skill):
    def __init__(self):
        super().__init__("Athletics", AbilityType.STR)
         
class Acrobatics(Skill):
    def __init__(self):
        super().__init__("Acrobatics", AbilityType.DEX)
        
class SleightofHand(Skill):
    def __init__(self):
        super().__init__("Sleight of Hand", AbilityType.DEX)
        
class Stealth(Skill):
    def __init__(self):
        super().__init__("Stealth", AbilityType.DEX)
        
class Arcana(Skill):
    def __init__(self):
        super().__init__("Arcana", AbilityType.INT)
        
class History(Skill):
    def __init__(self):
        super().__init__("History", AbilityType.INT)
        
class Investigation(Skill):
    def __init__(self):
        super().__init__("Investigation", AbilityType.INT)
        
class Nature(Skill):
    def __init__(self):
        super().__init__("Nature", AbilityType.INT)
        
class Religion(Skill):
    def __init__(self):
        super().__init__("Religion", AbilityType.INT)
        
class AnimalHandling(Skill):
    def __init__(self):
        super().__init__("Animal Handling", AbilityType.WIS)
        
class Insight(Skill):
    def __init__(self):
        super().__init__("Insight", AbilityType.WIS)
        
class Medicine(Skill):
    def __init__(self):
        super().__init__("Medicine", AbilityType.WIS)
        
class Perception(Skill):
    def __init__(self):
        super().__init__("Perception", AbilityType.WIS)
        
class Survival(Skill):
    def __init__(self):
        super().__init__("Survival", AbilityType.WIS)

class Deception(Skill):
    def __init__(self):
        super().__init__("Deception", AbilityType.CHA)

class Intimidation(Skill):
    def __init__(self):
        super().__init__("Intimidation", AbilityType.CHA)

class Performance(Skill):
    def __init__(self):
        super().__init__("Performance", AbilityType.CHA)

class Persuasion(Skill):
    def __init__(self):
        super().__init__("Persuasion", AbilityType.CHA)
