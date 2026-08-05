from dataclasses import dataclass
from Options import Choice, Toggle, DefaultOnToggle, DeathLink, PerGameCommonOptions, StartInventoryPool, OptionGroup, \
    Range
import random

# TODO: implement rules
# TODO: implement victory event for ending/goal
# TODO: implement locations and locations names

class ChoiceIsRandom(Choice):
    randomized: bool

    def __init__(self, value: int, randomized: bool = False):
        super().__init__(value)
        self.randomized = randomized

    @classmethod
    def from_text(cls, text: str) -> Choice:
        text = text.lower()
        if text == "random":
            return cls(random.choice(list(cls.name_lookup)), True)
        for option_name, value in cls.options.items():
            if option_name == text:
                return cls(value)
        raise KeyError(
            f'Could not find option "{text}" for "{cls.__name__}", '
            f'known options are {", ".join(f"{option}" for option in cls.name_lookup.values())}')


class Traps(Toggle):
    """
    Whether negative effects in the Salt and Sanctuary world are added to the item pool.
    """
    display_name = "Traps"


class Pathing(Choice):
    """
    Specify the potential difficulty of the zone to zone pathing.

    Normal keeps the game pathing similar to what is expected for the order the player visits each zone.
    Hard allows the game pathing to send players to harder zones earlier, within reason.
    Brutal allows the game pathing to send players to any connected zone, regardless of difficulty.
    """
    display_name = "Pathing"
    option_normal = 0
    option_hard = 1
    option_brutal = 2
    default = 0


class Goal(Choice):
    """
    Choose the goal to be achieved.

    Kill the Final Boss: Goal is met once the boss in The Still Palace is dead.
    The final boss might not be The Nameless God if bosses are randomized.

    All Bosses: Goal is met once every boss is dead.
    Endings are disabled until goal is met.

    Any Ending: Goal is met once getting the Salvation ending or the Domination ending.

    Ending Salvation: Ignore the Scarecrow and go down the well.
    Domination ending is disabled.

    Ending Domination: Speak to the Scarecrow at every location, and choose to "take helm" at the final location.
    Salvation ending is disabled.
    """
    display_name = "Goal"
    option_kill_the_final_boss = 0
    option_all_bosses = 1
    option_any_ending = 2
    option_ending_salvation = 3
    option_ending_domination = 4
    default = 2


class RetryUnspeakableDeep(Toggle):
    """
    If dying on the ship respawns the player on the ship, instead of sending them to Shivering Shore.
    """
    display_name = "Retry Unspeakable Deep"


class StartingLocation(Choice):
    """
    Choose where to start the randomizer.
    Note that some starting locations cannot be chosen with certain other options.

    Overridden if the "Retry Unspeakable Deep" option is used (forced Ship).
    """
    display_name = "Starting Location"
    option_ship = 0
    option_island = 1
    default = 0


class StartingEquipmentRando(Choice):
    """
    Whether starting equipment is randomized. Only equipment you can wield will be chosen.

    If the "No Skill Requirements" option is set to "On", any valid equipment can be chosen.

    The player will always be given at least one mêlée weapon.

    Class Relevant will only pick from equipment related to your starting class.
    Chaotic will pick any equipment.
    """
    display_name = "Starting Equipment Rando"
    option_off = 0
    option_class_relevant = 1
    option_chaotic = 2
    default = 0


class Creedsanity(Toggle):
    """
    Whether joining creeds are checks.
    Players will be unable to join creeds until they are unlocked.
    A starting creed will still be available from the Old Man in Shivering Shore.
    """
    display_name = "Creedsanity"


class CreedRando(Choice):
    """
    Creeds that are joinable by speaking to NPCs are randomized.
    This also affects the options given by the Old Man in Shivering Shore.

    Shown will give information regarding the creed that is being offered.
    Hidden will have give no information about what creed is being offered. You will find out after joining.
    """
    display_name = "Creed Rando"
    option_off = 0
    option_shown = 1
    option_hidden = 2
    default = 0


class Sanctuarysanity(Toggle):
    """
    If claiming sanctuaries are checks.

    The player will be unable to rest or respawn at each sanctuary until it is unlocked.
    """
    display_name = "Sanctuarysanity"


class Bosssanity(Choice):
    """
    Makes defeating bosses count as checks.

    Optional bosses are Queen of Smiles, Tree of Men, Disemboweled Husk, That Stench Most Foul, Murdiella Mal,
    Bloodless Prince, The Coveted, Carsejaw the Cruel, Ronin Cran, and Forgotten King/Knight/Judge.
    The Untouched Inquisitor is also optional as it is possible to skip it by taking a long fall.

    Kraekan Cyclops, Mad Alchemist, and False Jester are treated as required.
    Technically these bosses can be optional, but the base game requires you
    to kill some of them to progress depending on which path you take.

    Unspeakable Deep will be included if this option and Retry Unspeakable Deep is used.
    """
    display_name = "Bosssanity"
    option_off = 0
    option_required = 1
    option_optional = 2
    option_all_bosses = 3
    default = 0


class Questsanity(Choice):
    """
    The NPC quests are checks.

    Completion: Quest completion rewards are checks.

    Dialogue: Each interaction is a check, except interactions that would fail quests.

    All: Completion and Dialogue combined.

    Overrides the "Quests Cannot Fail" option.
    """
    display_name = "Questsanity"
    option_off = 0
    option_completion = 1
    option_dialogue = 2
    option_all = 3
    default = 0


class QuestsCannotFail(Toggle):
    """
    Prevents quest failure if an NPC is answered incorrectly or if certain bosses are killed before speaking to them.
    Simply interact with the NPC again if the wrong answer was chosen.
    NPCs will remain in their quest step spot for progression, even if quest failure conditions are met.

    Overridden if the "Questsanity" option is used (forced on).
    """
    display_name = "Quests Cannot Fail"


class Chestsanity(Toggle):
    """
    If items from chests are checks.
    The sacks spawned by the chests need to be picked up.
    This option still affects the same locations even if the Mimic Rando option is used.
    """
    display_name = "Chestsanity"


class Sacksanity(Toggle):
    """
    If items from statically placed sacks are checks.
    Does not include sacks spawned by chests and mimics.
    """
    display_name = "Sacksanity"


class Mimicsanity(Toggle):
    """
    If items from mimics are checks.
    The sacks spawned by the mimics need to be picked up.
    This option still affects the same locations even if the Mimic Rando option is used.
    """
    display_name = "Mimicsanity"


class MimicRando(Choice):
    """
    Randomizes which chests are actually mimics (Mimku).
    If the "Oops All Monster" option is used and this option isn't used,
    mimics will also be replaced by the "Oops All Monster" option.

    Vanilla keeps no randomization.
    Jumbled keeps the same number of mimics as the base game, but swaps them around.
    All Mimics replaces every chest with a mimic.
    """
    display_name = "Mimic Rando"
    option_off = 0
    option_vanilla = 1
    option_jumbled = 2
    option_all_mimics = 3
    default = 0


class Skillsanity(Range):
    """
    Spending black pearls to learn skills are checks.
    Checks are unlocked in order regardless of which skill node is unlocked.

    Set the number of checks that may be progression items. Skills will be unlocked by finding them.

    Any additional skill tree nodes will reward filler items.

    Expect to finish the game around level 80-90.

    Set to zero to disable.

    Overrides the "Skill Rando" option.
    """
    display_name = "Skillsanity"
    range_start = 0
    range_end = 120
    default = 0


class SkillRando(Toggle):
    """
    Randomizes the skill tree nodes.

    Overridden if the "Skill Sanity" option is used (forced off).
    """
    display_name = "Skill Randomizer"


class NoSkillRequirements(Toggle):
    """
    Allows the player to equip any items without requiring the necessary skill.
    """
    display_name = "No Skill Requirements"


class Shopsanity(Choice):
    """
    Whether shop items are randomized. Dev NPC "The Shell Market" is not included.

    Creedless randomizes items in only non-creed shops.
    Creeds randomizes items in only creed shops.
    All randomizes items in both non-creed and creed shops.
    """
    display_name = "Shopsanity"
    option_off = 0
    option_creedless = 1
    option_creeds = 2
    option_all = 3
    default = 0


class AutoShopHints(Toggle):
    """
    If free hints are given for the shop items when the player opens each shop for the first time.

    If the "Creed Shops Max Rank" option isn't used, only hints for unlocked ranks will be given.
    You will have to open the shop again to receive the hints for newly unlocked ranks.

    Overridden if the "Shopsanity" option isn't used (forced off).
    """
    display_name = "Auto Shop Hints"


class Leversanity(Toggle):
    """
    If lever pulls for unlocking gates and doors are checks.
    To have lifts as checks, use the Liftsanity option.
    """
    display_name = "Leversanity"


class Liftsanity(Toggle):
    """
    If lift activations are checks, whether by pulling a lever or simply stepping on the lift for the first time.
    """
    display_name = "Liftsanity"


class TransmutationRando(Toggle):
    """
    Whether the items created through transmuting boss materials are randomized.
    """
    display_name = "Transmutation Rando"


class Bestiarysanity(Toggle):
    """
    If unlocking entries in the bestiary are checks.

    Overridden if the "Oops All Monster" option is used (forced off).
    """
    display_name = "Bestiarysanity"


class CreedMaxRank(Toggle):
    """
    If joined creeds are considered max rank giving access to purchase all of their shop items.

    Vanilla requires you to rank up the creed as normal.
    Max Rank makes a creed max rank upon joining the creed.
    """
    display_name = "Creed Shops Max Rank"


class EquipmentRankRando(Choice):
    """
    Whether equipment can drop at varying ranks.

    Off has equipment drop at base rank.
    Balanced has equipment drop at a rank based on the sphere it is found in.
    Chaotic has equipment drop at random ranks
    """
    display_name = "Equipment Rank Rando"
    option_off = 0
    option_balanced = 1
    option_chaotic = 2
    default = 0


class OopsAllMonster(Choice):
    """
    Replaces every normal enemy spawn with a single type of enemy.
    Chest mimics are also affected unless the Mimic Rando option is used.

    Overrides the "Bestiarysanity" option.
    """
    display_name = "Oops All Monster"
    option_off                         = 1000
    option_chest                       = 0
    option_soldier                     = 1
    option_raider                      = 2
    option_hero                        = 3
    option_bull                        = 4
    option_archer                      = 5
    option_dread                       = 6
    option_priest                      = 7
    option_priest_cleric               = 8
    option_smith                       = 9
    option_merchant                    = 10
    option_mage                        = 11
    option_rags                        = 12
    option_drowned                     = 13
    option_dog                         = 14
    option_switch                      = 15
    option_knight                      = 16
    option_wraith                      = 17
    option_blob                        = 18
    option_cutqueen                    = 19
    option_ogre                        = 20
    option_masterless                  = 21
    option_nomad                       = 22
    option_peasant                     = 23
    option_bandit                      = 24
    option_sorceror                    = 25
    option_bat                         = 26
    option_golem                       = 27
    option_tripwire                    = 28
    option_xbow                        = 29
    option_ropetrap                    = 30
    option_raketrap                    = 31
    option_leviathan                   = 32
    option_dragon                      = 33
    option_fiend                       = 34
    option_deadprop                    = 35
    option_smith_iron                  = 36
    option_crusher                     = 37
    option_hawk                        = 38
    option_gaoler                      = 39
    option_phantasm                    = 40
    option_captain                     = 41
    option_torturer                    = 42
    option_imp                         = 43
    option_alchemist                   = 44
    option_torturetree                 = 45
    option_tortured                    = 46
    option_flamejet                    = 47
    option_hookman                     = 48
    option_skeleton                    = 49
    option_skeleton_tribe              = 50
    option_poisonrocktrap              = 51
    option_crab                        = 52
    option_pirate                      = 53
    option_wisewoman                   = 54
    option_mage_fire                   = 55
    option_merchant_cleric             = 56
    option_smith_cleric                = 57
    option_merchant_iron               = 58
    option_priest_iron                 = 59
    option_mage_iron                   = 60
    option_mage_cleric                 = 61
    option_obelisk                     = 62
    option_zombie                      = 63
    option_zombow                      = 64
    option_jester                      = 65
    option_broken                      = 66
    option_despondent                  = 67
    option_sack                        = 68
    option_skull                       = 69
    option_witch                       = 70
    option_gasbag                      = 71
    option_smith_woods                 = 72
    option_cleric_woods                = 73
    option_mage_woods                  = 74
    option_merchant_woods              = 75
    option_gasface                     = 76
    option_bandages                    = 77
    option_lakewitch                   = 78
    option_oldman                      = 79
    option_spider                      = 80
    option_marauder                    = 81
    option_sailor                      = 82
    option_skeleton_archer             = 83
    option_torturer_bow                = 84
    option_spider_blue                 = 85
    option_blue_blob                   = 86
    option_hippogriff                  = 87
    option_ghost                       = 88
    option_knight_axe                  = 89
    option_piranha                     = 90
    option_unicorn                     = 91
    option_littlecorn                  = 92
    option_poisonspin                  = 93
    option_lich                        = 94
    option_clay                        = 95
    option_oldgreg                     = 96
    option_memories                    = 97
    option_fauxjester                  = 98
    option_zenfern                     = 99
    option_stonetrip                   = 100
    option_littrap                     = 101
    option_mummy                       = 102
    option_troll                       = 103
    option_bluetroll                   = 104
    option_bluewraith                  = 105
    option_betus                       = 106
    option_choppy                      = 107
    option_chemist                     = 108
    option_guide                       = 109
    option_leader                      = 110
    option_chemist_cleric              = 111
    option_chemist_iron                = 112
    option_chemist_woods               = 113
    option_chemist_fire                = 114
    option_guide_cleric                = 115
    option_guide_iron                  = 116
    option_guide_woods                 = 117
    option_guide_fire                  = 118
    option_leader_cleric               = 119
    option_leader_iron                 = 120
    option_leader_woods                = 121
    option_leader_fire                 = 122
    option_smith_fire                  = 123
    option_inquisitor                  = 124
    option_sellsword                   = 125
    option_shellshop                   = 126
    option_split                       = 127
    option_guardian                    = 128
    option_gold_archer                 = 129
    option_guardmage                   = 130
    option_guardian_cleric             = 131
    option_guardmage_cleric            = 132
    option_guardian_rotten             = 133
    option_hangman                     = 134
    option_catmerch                    = 135
    option_scarecrow                   = 136
    option_eyeball                     = 137
    option_horseman                    = 138
    option_horseknight                 = 139
    option_eyescorpion                 = 140
    option_squidface                   = 141
    option_guardian_gen                = 142
    option_monster                     = 143
    option_monsterwitch                = 144
    option_angler                      = 145
    option_shipcaptain                 = 146
    option_boatman                     = 147
    option_rightboatman                = 148
    option_domefriend                  = 149
    option_swampfriend                 = 150
    option_saltbat                     = 151
    option_saltknight                  = 152
    option_bouldertrap                 = 153
    option_arms                        = 154
    option_crow                        = 155
    option_treelady                    = 156
    option_ruinaxe                     = 157
    option_ruinghost                   = 158
    option_ruinknight                  = 159
    option_greenspider                 = 160
    option_cult                        = 161
    option_stonesoul                   = 162
    option_cryptkeeper                 = 163
    option_priest_dark                 = 164
    option_smith_dark                  = 165
    option_mage_dark                   = 166
    option_leader_dark                 = 167
    option_merchant_dark               = 168
    option_guide_dark                  = 169
    option_chemist_dark                = 170
    option_ghostwitch                  = 171
    option_squiddragon                 = 172
    option_doll                        = 173
    option_nameless                    = 174
    option_nightmare                   = 175
    option_salad                       = 176
    option_priest_woods                = 177
    option_horsehead                   = 178
    option_headhorse                   = 179
    option_cloak                       = 180
    option_priest_splendor             = 181
    option_smith_splendor              = 182
    option_mage_splendor               = 183
    option_leader_splendor             = 184
    option_merchant_splendor           = 185
    option_guide_splendor              = 186
    option_chemist_splendor            = 187
    option_dark_gatekeeper             = 188
    option_butterfly                   = 189
    option_deadlord                    = 190
    option_deadknight                  = 191
    option_deadking                    = 192
    option_deadjudge                   = 193
    option_maraudzom                   = 194
    option_princess                    = 195
    option_princess_maid               = 196
    option_zomblack                    = 197
    option_knight_white                = 198
    option_birdy                       = 199
    option_priest_fire                 = 200
    option_merchant_fire               = 201
    option_squidmimic                  = 202
    option_summoner                    = 203
    default                            = 1000


class SaltnSancDeathLink(DeathLink):
    __doc__ = DeathLink.__doc__


@dataclass
class SaltnSancOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    traps: Traps
    pathing: Pathing
    goal: Goal
    retry_unspeakable_deep: RetryUnspeakableDeep
    starting_location: StartingLocation
    starting_equipment_rando: StartingEquipmentRando
    creedsanity: Creedsanity
    creed_rando: CreedRando
    sanctuarysanity: Sanctuarysanity
    bosssanity: Bosssanity
    questsanity: Questsanity
    quests_cannot_fail: QuestsCannotFail
    chestsanity: Chestsanity
    sacksanity: Sacksanity
    mimicsanity: Mimicsanity
    mimic_rando: MimicRando
    skillsanity: Skillsanity
    skill_rando: SkillRando
    no_skill_requirements: NoSkillRequirements
    shopsanity: Shopsanity
    auto_shop_hints: AutoShopHints
    leversanity: Leversanity
    liftsanity: Liftsanity
    transmutation_rando: TransmutationRando
    bestiarysanity: Bestiarysanity
    creed_max_rank: CreedMaxRank
    equipment_rank_rando: EquipmentRankRando
    oops_all_monster: OopsAllMonster
    death_link: SaltnSancDeathLink


option_groups = [
    OptionGroup(
        "Gameplay",
        [Pathing, Goal, RetryUnspeakableDeep, SaltnSancDeathLink, Traps, StartingLocation,
         Sanctuarysanity, Leversanity, Liftsanity]
    ),
    OptionGroup(
        "Skills",
        [Skillsanity, SkillRando, NoSkillRequirements]
    ),
    OptionGroup(
        "Pickups",
        [Chestsanity, Sacksanity]
    ),
    OptionGroup(
        "Monsters",
        [Mimicsanity, MimicRando, Bestiarysanity, OopsAllMonster]
    ),
    OptionGroup(
        "Equipment",
        [StartingEquipmentRando, EquipmentRankRando, TransmutationRando]
    ),
    OptionGroup(
        "Quests",
        [Questsanity, QuestsCannotFail]
    ),
    OptionGroup(
        "Creeds",
        [Creedsanity, CreedRando, CreedMaxRank]
    ),
    OptionGroup(
        "Shops",
        [Shopsanity, AutoShopHints]
    )
]