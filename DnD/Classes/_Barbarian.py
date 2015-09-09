from DnD.Classes._Class import *
from DnD.Common._Abilities import *
from DnD.Common._Constants import *
from DnD.Common._Skills import *

class BardTableEntry(ClassTableEntry):
    def __init__(self, proficiencyBonus, features, cantrips, spells, spellSlots):
        super().__init__(proficiencyBonus, features)
        self.__cantrips = cantrips
        self.__rageDamage = rageDamage

class Barbarian(Class):
    def __init__(self):
        super().__init__()
        self.__name = "Barbarian"
        self.__classTable.update({
               1 : BarbarianTableEntry(2, [Rage(), UnarmoredDefence()], 2, 2),
               2 : BarbarianTableEntry(2, [RecklessAttack(), DangerSense()], 2, 2),
               3 : BarbarianTableEntry(2, [(PrimalPath(), (3))], 3, 2),
               4 : BarbarianTableEntry(2, [(ChooseAbilityScore(), (2, 1))], 3, 2),
               5 : BarbarianTableEntry(3, [ExtraAttack(), FastMovement()], 3, 2),
               6 : BarbarianTableEntry(3, [(PathFeature(), (6))], 4, 2),
               7 : BarbarianTableEntry(3, [FeralInstinct()], 4, 2),
               8 : BarbarianTableEntry(3, [(ChooseAbilityScore(), (2, 1))], 4, 2),
               9 : BarbarianTableEntry(4, [(BrutalCritical(), (1))], 4, 3),
              10 : BarbarianTableEntry(4, [(PathFeature(), (6))], 4, 3),
              11 : BarbarianTableEntry(4, [RelentlessRage()], 4, 3),
              12 : BarbarianTableEntry(4, [(ChooseAbilityScore(), (2, 1))], 5, 3),
              13 : BarbarianTableEntry(5, [(BrutalCritical(), (2))], 5, 3),
              14 : BarbarianTableEntry(5, [(PathFeature(), (6))], 5, 3),
              15 : BarbarianTableEntry(5, [PersistentRage()], 5, 3),
              16 : BarbarianTableEntry(5, [(ChooseAbilityScore(), (2, 1))], 5, 4),
              17 : BarbarianTableEntry(6, [(BrutalCritical(), (1))], 6, 4),
              18 : BarbarianTableEntry(6, [IndomitableMight()], 6, 4),
              19 : BarbarianTableEntry(6, [(ChooseAbilityScore(), (2, 1))], 6, 4),
              20 : BarbarianTableEntry(6, [PrimalChampion()], -1, 4)})
        
        self.__hitDice = Dice.D12
        self.__proficiencies.extend((
            Proficiency.LIGHTARMOR,
            Proficiency.MEDIUMARMOR,
            Proficiency.SHIELDS,
            Proficiency.SIMPLEWEAPONS,
            Proficiency.MARTIALWEAPONS))
            
        self.__savingThrows.extend((Ability.STR, Ability.CON))
        
        self.__skills.append((ChooseSkill(), (2, (AnimalHusbandry(), Athletics(), Intimidation(), Nature(), Perception(), Survival()))))
        
        self.__equiptment.extend(((ChooseItem(), (Item.GREATAXE, Item.MARTIALMELEE)), 
                                               (ChooseItem(), ((2, Item.HANDAXE), Item.SIMPLEWEAPON)),
                                               Item.EXPLORERSPACK,
                                               (4, Item.JAVELIN)))
        
class BarbarianPath(object):
    def __init__(self, name):
        self.__name = name
        self.__features = {}
        
class Berserker(BarbarianPath):
    def __init__(self):
        super().__init__("Berserker")
        self.__features.update({
            3 : Frenzy(),
            6 : MindlessRage(),
            10 : IntimidatingPresence(),
            14 : Retaliation()})
            
class TotemWarrior(BarbarianPath):
    def __init__(self):
        super().__init__("TotemWarrior")
        self.__features.update({
            3 : (SpiritSeeker(), TotemSpirit()),
            6 : AspectoftheBeast(),
            10 : SpiritWalker(),
            14 : TotemicAttunement()})
            
         