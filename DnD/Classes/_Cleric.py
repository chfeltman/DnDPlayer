from DnD.Classes._Class import *
from DnD.Common._Abilities import *
from DnD.Common._Constants import *
from DnD.Common._Skills import *

class Cleric(Class):
    def __init__(self):
        super().__init__()
        self.__name = "Cleric"
        self.__classTable.update({
               1 : MagicTableEntry(2, [(ChooseCantrip(), (3, SpellClass.CLERIC, AbilityType.WIS)), 
                                                   (ChooseSpell(), (2, SpellClass.BARD, 1)), 
                                                   DivineDomain(),
                                                   RitualCasting(),
                                                   (SpellcastingFocus(), (SpellClass.CLERIC))], 
                                                   (2)),
               2 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 1)),
                                                    (ChannelDivinity(), (1)),
                                                    (DomainFeature(), (3))], 
                                                   (3)),
               3 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 2))],
                                                    (4, 2)),
               4 : MagicTableEntry(2, [(ChooseCantrip(), (1, SpellClass.CLERIC, AbilityType.WIS)),
                                                    (ChooseSpell(), (1, SpellClass.CLERIC, 2)),
                                                    (ChooseAbilityScore(), (2, 1))],
                                                    (4, 3)),
               5 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 3)),
                                                    (DestroyUndead(), (0.5))],
                                                    (4, 3, 2)),
               6 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 3)),
                                                    (ChannelDivinity(), (2)), 
                                                    (DomainFeature(), (6))],
                                                    (4, 3, 3)),
               7 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 4))],
                                                    (4, 3, 3, 1)),
               8 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 4)),
                                                    (ChooseAbilityScore(), (2, 1)),
                                                    (DestoryUndead(),(1)),
                                                    (DomainFeature(), (8))],
                                                    (4, 3, 3, 2)),
               9 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 5))],
                                                    (4, 3, 3, 3, 1)),
              10 : MagicTableEntry(2, [(ChooseCantrip(), (1, SpellClass.CLERIC, AbilityType.WIS)),
                                                    DivineIntervention()],
                                                    (4, 3, 3, 3, 2)),
              11 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 6)),
                                                    (DestoryUndead(), (2))],
                                                    (4, 3, 3, 3, 2, 1)),
              12 : MagicTableEntry(2, [(ChooseAbilityScore(), (2, 1))],
                                                    (4, 3, 3, 3, 2, 1)),
              13 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 7))],
                                                    (4, 3, 3, 3, 2, 1, 1)),
              14 : MagicTableEntry(2, [(DestoryUndead(), (3))],
                                                    (4, 3, 3, 3, 2, 1, 1)),
              15 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 8))],
                                                    (4, 3, 3, 3, 2, 1, 1, 1)),
              16 : MagicTableEntry(2, [(ChooseAbilityScore(), (2, 1))],
                                                    (4, 3, 3, 3, 2, 1, 1, 1)),
              17 : MagicTableEntry(2, [(ChooseSpell(), (1, SpellClass.CLERIC, 9)),
                                                    (DestoryUndead(), (4)),
                                                    (DomainFeature(), (17))],
                                                    (4, 3, 3, 3, 2, 1, 1, 1, 1)),
              18 : MagicTableEntry(2, [(ChannelDivinity(), (3))],
                                                    (4, 3, 3, 3, 3, 1, 1, 1, 1)),
              19 : MagicTableEntry(2, [(ChooseAbilityScore(), (2, 1))],
                                                    (4, 3, 3, 3, 3, 2, 1, 1, 1)),
              20 : MagicTableEntry(2, [DivineInterventionImprovement()],
                                                    (4, 3, 3, 3, 3, 2, 2, 1, 1))
               })
        
        self.__hitDice = Dice.D8
        self.__proficiencies.extend((
            Proficiency.LIGHTARMOR,
            Proficiency.MEDIUMARMOR,
            Proficiency.SHIELDS,
            Proficiency.SIMPLEWEAPONS))
            
        self.__savingThrows.extend((Ability.WIS, Ability.CHA))
        
        self.__skills.append((ChooseSkill(), (2, (History(), Insight(), Medicine(), Persuasion(), Religion()))))
        
        self.__equiptment.extend(((ChooseItem(), (Item.MACE, Item.WARHAMMER)), 
                                       (ChooseItem(), (Item.SCALEMAIL, Item.LEATHERARMOR, Item.CHAINMAIL)),
                                       (ChooseItem(), ((Item.LIGHTCROSSBOW, (20, Item.BOLTS)), Item.SIMPLEWEAPON)),
                                       (ChooseItem(), Item.PRIESTSPACK, Item.EXPLORERSPACK),
                                       Item.SHIELD,
                                       Item.HOLYSYMBOL))

class ClericDivineDomain(object):
    def __init__(self, name):
        self.__name = name
        self.__features = {}
        self.__spells = {}
        
class KnowledgeDomain(ClericDivineDomain):
    def __init__(self):
        super().__init__("Knowledge Domain")
        self.__spells.update({
            1 : (Command(), Identify()),
            3 : (Augury(), Suggestion()),
            5 : (Nondetection(), SpeakWithDead()),
            7 : (ArcaneEye(), Confusion()),
            9 : (LegendLore(), Scrying())})

        self.__features.update({
            1 : BlessingsofKnowledge(),
            2 : KnowledgeoftheAges(),
            6 : ReadThoughts(),
            8 : PotentSpellcasting(),
            17 : VisionsofthePast()})
                        
class LifeDomain(ClericDivineDomain):
    def __init__(self):
        super().__init__("Life Domain")
        self.__spells.update({
            1 : (Bless(), CureWounds()),
            3 : (LesserRestoration(), SpiritualWeapon()),
            5 : (BeaconofHope(), Revivify()),
            7 : (DeathWard(), GuardianofFaith()),
            9 : (MassCureWounds(), RaiseDead())})

        self.__features.update({
            1 : (ChooseProficiency(), (1)),
            2 : PreserveLife(),
            6 : BlessedHealer(),
            8 : DivineStrike(),
            17 : SupremeHealing()})
                         
class LightDomain(ClericDivineDomain):
    def __init__(self):
        super().__init__("Light Domain")
        self.__spells.update({
            1 : (BurningHands(), FaerieFire()),
            3 : (FlamingSphere(), ScorchingRay()),
            5 : (Daylight(), Fireball()),
            7 : (GuardianofFaith(), WallofFire()),
            9 : (FlameStrike(), Scrying())})

        self.__features.update({
            1 : (GainCantrip(), (Light())),
            2 : RadianceoftheDawn(),
            6 : ImprovedFlare(),
            8 : PotentSpellcasting(),
            17 : CoronaofLight()})
                         
class NatureDomain(ClericDivineDomain):
    def __init__(self):
        super().__init__("Nature Domain")
        self.__spells.update({
            1 : (AnimalFriendship(), SpeakWithAnimals()),
            3 : (Barkskin(), SpikeGrowth()),
            5 : (PlantGrowth(), WindWall()),
            7 : (DominateBeast(), GraspingVine()),
            9 : (InsectPlague(), TreeStride())})

        self.__features.update({
            1 : ((ChooseCantrip(), (1, SpellClass.DRUID, AbilityType.WIS)), 
                   (ChooseSkill(), (1, (AnimalHandling(), Nature(), Survival()))), 
                   (GainProficiency(), (Proficiency.HEAVYARMOR))),
            2 : CharmAnimalsandPlants(),
            6 : DampenElements(),
            8 : DivineStrike(),
            17 : MasterofNature()})
                         
class TempestDomain(ClericDivineDomain):
    def __init__(self):
        super().__init__("Tempest Domain")
        self.__spells.update({
            1 : (FogCloud(), Thunderwave()),
            3 : (GustofWind(), Shatter()),
            5 : (CallLightning(), SleetStorm()),
            7 : (ControlWeather(), IceStorm()),
            9 : (DestructiveWave(), InsectPlague())})

        self.__features.update({
            1 : ((GainProficiency(), (Proficiency.MARTIALWEAPONS)), WrathoftheStorm()),
            2 : DestructiveWrath(),
            6 : ThunderboltStrike(),
            8 : DivineStrike(),
            17 : Stormborn()})
                         
class TrickeryDomain(ClericDivineDomain):
    def __init__(self):
        super().__init__("Trickery Domain")
        self.__spells.update({
            1 : (CharmPerson(), DisguiseSelf()),
            3 : (MirrorImage(), PassWithoutTrace()),
            5 : (Blink(), DispelMagic()),
            7 : (DimensionDoor(), Polymorph()),
            9 : (DominatePerson(), ModifyMemory())})

        self.__features.update({
            1 : BlessingoftheTrickster(),
            2 : InvokeDuplicity(),
            6 : CloakofShadows(),
            8 : DivineStrike(),
            17 : ImprovedDuplicity()})
                         
class WarDomain(ClericDivineDomain):
    def __init__(self):
        super().__init__("War Domain")
        self.__spells.update({
            1 : (DivineFavor(), ShieldofFaith()),
            3 : (MagicWeapon(), SpiritualWeapon()),
            5 : (CrusadersMantle(), SpiritGuardians()),
            7 : (FreedomofMovement(), Stoneskin()),
            9 : (FlameStrike(), HoldMonster())})

        self.__features.update({
            1 : (WarPriest(),(GainProficiency(), (Proficiency.MARTIALWEAPONS, Proficiency.HEAVYARMOR))),
            2 : GuidedStrike(),
            6 : WarGodsBlessing(),
            8 : DivineStrike(),
            17 : AvatarofBattle()})
         