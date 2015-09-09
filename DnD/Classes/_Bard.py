from DnD.Classes._Class import *
from DnD.Common._Abilities import *
from DnD.Common._Constants import *
from DnD.Common._Skills import *

class Bard(Class):
    def __init__(self):
        super().__init__()
        self.__name = "Bard"
        self.__classTable.update({
               1 : MagicTableEntry(2, [(ChooseCantrip(), (2, SpellClass.BARD, AbilityType.CHA)), 
                                                   (ChooseSpell(), (4, SpellClass.BARD, 1)), 
                                                   (BardicInspiration(), (Dice.D6)),
                                                   RitualCasting(),
                                                   (ChooseInstrument(), (3)),
                                                   (SpellcastingFocus(), (SpellClass.BARD))], 
                                                   (2)),
               2 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 1)),
                                                    JackofAllTrades(),
                                                    (SongofRest(), (Dice.D6))], 
                                                   (3)),
               3 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 2)),
                                                    (BardCollege(), (3)), 
                                                    Expertise()],
                                                    (4, 2)),
               4 : MagicTableEntry(2, [(ChooseCantrip(), (1, SpellClass.BARD, AbilityType.CHA)),
                                                    (ChooseSpell(), (1, SpellClass.BARD, 2)),
                                                    (ChooseAbilityScore(), (2, 1)), 
                                                    Expertise()],
                                                    (4, 3)),
               5 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 3)),
                                                    (BardicInspiration, (Dice.D8)), 
                                                    FontofInspiration()],
                                                    (4, 3, 2)),
               6 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 3)),
                                                    CounterCharm(), 
                                                    (CollegeFeature(), (6))],
                                                    (4, 3, 3)),
               7 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 4))],
                                                    (4, 3, 3, 1)),
               8 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 4)),
                                                    (ChooseAbilityScore(), (2, 1))],
                                                    (4, 3, 3, 2)),
               9 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 5)),
                                                    (SongofRest(), (Dice.D8))],
                                                    (4, 3, 3, 3, 1)),
              10 : MagicTableEntry(2, [(ChooseCantrip(), (1, SpellClass.BARD, AbilityType.CHA)),
                                                    MagicalSecrets(),
                                                    (BardicInspiration(), (Dice.D10)), 
                                                    Expertise() ],
                                                    (4, 3, 3, 3, 2)),
              11 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 6))],
                                                    (4, 3, 3, 3, 2, 1)),
              12 : MagicTableEntry(2, [(ChooseAbilityScore(), (2, 1))],
                                                    (4, 3, 3, 3, 2, 1)),
              13 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 7)),
                                                    (SongofRest(), (Dice.D10))],
                                                    (4, 3, 3, 3, 2, 1, 1)),
              14 : MagicTableEntry(2, [MagicalSecrets(), 
                                                    (CollegeFeature(), (14))],
                                                    (4, 3, 3, 3, 2, 1, 1)),
              15 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 8)),
                                                    (BardicInspiration(), (Dice.D12))],
                                                    (4, 3, 3, 3, 2, 1, 1, 1)),
              16 : MagicTableEntry(2, [(ChooseAbilityScore(), (2, 1))],
                                                    (4, 3, 3, 3, 2, 1, 1, 1)),
              17 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.BARD, 9)),
                                                    (SongofRest(), (Dice.D12))],
                                                    (4, 3, 3, 3, 2, 1, 1, 1, 1)),
              18 : MagicTableEntry(2, [MagicalSecrets()],
                                                    (4, 3, 3, 3, 3, 1, 1, 1, 1)),
              19 : MagicTableEntry(2, [(ChooseAbilityScore(), (2, 1))],
                                                    (4, 3, 3, 3, 3, 2, 1, 1, 1)),
              20 : MagicTableEntry(2, [SuperiorInspiration()],
                                                    (4, 3, 3, 3, 3, 2, 2, 1, 1)),
               })
        
        self.__hitDice = Dice.D8
        self.__proficiencies.extend((
            Proficiency.LIGHTARMOR,
            Proficiency.SIMPLEWEAPONS,
            Proficiency.HANDCROSSBOWS,
            Proficiency.LONGSWORDS,
            Proficiency.RAPIERS,
            Proficiency.SHORTSWORDS))
            
        self.__savingThrows.extend((Ability.DEX, Ability.CHA))
        
        self.__skills.append((ChooseSkill(), (3)))
        
        self.__equiptment.extend(((ChooseItem(), (Item.RAPIER, Item.LONGSWORD, Item.SIMPLEWEAPON)), 
                                       (ChooseItem(), (Item.DIPLOMATSPACK, Item.ENTERTAINERSPACK)),
                                       (ChooseItem(), (Item.LUTE, Item.MUSICALINSTRUMENT)),
                                       Item.LEATHERARMOR,
                                       Item.DAGGER))

class BardicCollege(object):
    def __init__(self, name):
        self.__name = name
        self.__features = {}
        
class CollegeofLore(BardicCollege):
    def __init__(self):
        super().__init__("College of Lore")
        self.__features.update({
            3 : ((ChooseSkill(), (3)), CuttingWords()),
            6 : AdditionalMagicSecrets(),
            14 : PeerlessSkill()})
            
class CollegeofValor(BardicCollege):
    def __init__(self):
        super().__init__("College of Valor")
        self.__features.update({
            3 : ((GainProficiency(), (Proficiency.MEDIUMARMOR, Proficiency.SHIELDS, Proficiency.MARTIALWEAPONS)), CombatInspiration()),
            6 : ExtraAttack(),
            14 : BattleMagic()})
            
         