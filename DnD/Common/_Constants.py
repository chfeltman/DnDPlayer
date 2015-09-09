from enum import Enum, unique

@unique
class Proficiency(Enum):
    LIGHTARMOR = 0
    MEDIUMARMOR = 1
    HEAVYARMOR = 2
    SHIELDS = 4
    SIMPLEWEAPONS = 5
    MARTIALWEAPONS = 6

@unique 
class Dice(Enum):
    D4 = 0
    D6 = 1
    D8 = 2
    D10 = 3
    D20 = 4
    PERCENTILE = 5   

@unique
class Temperment(Enum):
    Chaotic = 0
    Neutral = 1
    Lawful = 2

@unique
class Morality(Enum):
    Evil = 0
    Neutral = 1
    Good = 2

@unique
class AbilityType(Enum):
    STR = 0
    DEX = 1
    CON = 2
    INT = 3
    WIS = 4
    CHA = 5
    
@unique
class Size(Enum):
    TINY = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    HUGE = 4
    GARGANTUAN = 5
    COLOSSAL = 6

@unique    
class Language(Enum):
    COMMON = 0
    DWARVISH = 1
    ELVISH = 2
    HALFLING = 3
    DRACONIC = 4
    GNOMISH = 5
    ORC = 6
    INFERNAL = 7
    
@unique
class SpellClass(Enum):
    ANY = 0
    WIZARD = 1
    BARD = 2
    CLERIC = 3
    DRUID = 4
    
AbilityModifiers = [
-5,                 #1
-4, -4,             #2-3
-3, -3,             #4-5
-2, -2,             #6-7
-1, -1,             #8-9
0, 0,               #10-11
1, 1,               #12-13
2, 2,               #14-15
3, 3,               #16-17
4, 4,               #18-19
5, 5]               #20-21

Experience = {
    355000 : 20,
    305000 : 19,
    265000 : 18,
    225000 : 17,
    195000 : 16,
    165000 : 15,
    140000 : 14,
    120000 : 13,
    100000 : 12,
    85000 : 11,
    64000 : 10,
    48000 : 9,
    34000 : 8,
    23000 : 7,
    14000 : 6,
    6500 : 5,
    2700 : 4,
    900 : 3,
    300 : 2,
    0 : 1
}
