from typing import NamedTuple, TYPE_CHECKING
from BaseClasses import Item, ItemClassification

# the list of items that may be sent from other players/games

""" [key items] """
class KeyItems:
    bag_of_earth        = "Bag of Earth"    # 1000
    bloody_writ         = "Bloody Writ"     # 1001
    bone_key            = "Bone Key"        # 1002
    bronze_key          = "Bronze Key"      # 1003
    cellar_key          = "Cellar Key"      # 1004
    fortress_key        = "Fortress Key"    # 1005
    green_key           = "Green Key"       # 1006
    jagged_key          = "Jagged Key"      # 1007
    mossy_key           = "Mossy Key"       # 1008
    sanctuary_key       = "Sanctuary Key"   # 1009
    spiked_key          = "Spiked Key"      # 1010

""" [consumables (basic)] """
class ConsumablesBasic:
    antidote            = "Antidote"        # 2000
    arrow               = "Arrow"           # 2001
    bag_of_salt         = "Bag of Salt"     # 2002
    bell_of_return      = "Bell Of Return"  # 2003
    birian_firepot      = "Birian Firepot"  # 2004
    blessed_page        = "Blessed Page"    # 2005
    bolt                = "Bolt"            # 2006
    box_of_salt         = "Box of Salt"     # 2007
    bundle_of_salt      = "Bundle Of Salt"
    calling_horn        = "Calling Horn"
    case_of_salt        = "Case of Salt"
    chest_of_salt       = "Chest of Salt"
    crate_of_salt       = "Crate of Salt"
    crystal_sphere      = "Crystal Sphere"
    dragons_tooth       = "Dragon's Tooth"
    egg_of_wrath        = "Egg of Wrath"
    expunged_heart      = "Expunged Heart"
    flame_arrow         = "Flame Arrow"
    flame_bolt          = "Flame Bolt"
    flintlock_shot      = "Flintlock Shot"
    forestfang          = "Forest Fang"
    glowing_shot        = "Glowing Shot"
    grenado             = "Grenado"
    jurney_bottle       = "Jurney Bottle"
    lightvessel         = "Lightvessel"
    pack_of_salt        = "Pack of Salt"
    pessmud             = "Pessmud"
    phial_of_undersight = "Phial Of Undersight"
    pitchfire           = "Pitchfire"
    poison_arrow        = "Poison Arrow"
    poison_bolt         = "Poison Bolt"
    potato              = "Potato"
    pouch_of_salt       = "Pouch of Salt"
    red_shard           = "Red Shard"
    sack_of_salt        = "Sack of Salt"
    satchel_of_salt     = "Satchel of Salt"
    sellswords_bell     = "Sellsword's Bell"
    shockstone          = "Shockstone"
    sky_frostgel        = "Sky Frostgel"
    stained_page        = "Stained Page"
    tainted_shot        = "Tainted Shot"
    throwing_dagger     = "Throwing Dagger"
    torch               = "Torch"
    warhorn             = "Warhorn"

""" [consumables (creed)] """
class ConsumablesCreed:
    red_flask               = "Red Flask"               # 3000
    water_of_blessing = "Water Of Blessing"
    hearty_roll = "Hearty Roll"
    red_grass = "Red Grass"
    flask_of_fire = "Flask of Fire"
    lilyred_wine = "Lilyred Wine"
    blood_vial = "Blood Vial"
    spiced_mead = "Spiced Mead"
    cloth_of_blessing = "Cloth Of Blessing"
    blue_crystal = "Blue Crystal"
    blue_grass = "Blue Grass"
    bottled_sky = "Bottled Sky"
    iris_wine = "Iris Wine"
    black_salt = "Black Salt"
    imperial_pitchfire = "Imperial Pitchfire"
    imperial_shockstone = "Imperial Shockstone"
    orange_phial = "Orange Phial"
    page_of_light = "Page of Light"
    metal_shockstone = "Metal Shockstone"
    mountain_warhorn = "Mountain Warhorn"
    mossy_pessmud = "Mossy Pesmud"
    wraithfang = "Wraithfang"
    sky_crystal = "Sky Crystal"
    clarity = "Clarity"
    goldenwine = "Goldenwine"
    cleansing_cloth = "Cleansing Cloth"
    page_of_suffering = "Page of Suffering"
    flask_of_defilement = "Flask of Defilement"
    candelabra_of_the_three = "Candelabra of the Three"
    earthen_vessel = "Earthen Vessel"
    metal_icon = "Metal Icon"
    stone_acorn = "Stone Acorn"
    living_tome = "Living Tome"
    golden_face = "Golden Face"
    skull_trophy = "Skull Trophy"

""" [consumables (debug)] """
class ConsumablesDebug:
    frostgel = "Frost Gel" # 4000
    repair_kit = "Repair Kit"
    sky_shard = "Sky Shard"
    steel_arrow = "Steel Arrow"
    tree_of_bones = "Tree of Bones"
    wooden_bottle = "Wooden Bottle"

""" [materials] """
class Materials:
    a_kings_orders = "A King's Orders" # 5000
    a_lords_orders = "A Lord's Orders"
    a_soldiers_poem = "A Soldier's Poem"
    alkymancery_knights_ashes = "Alkymancery Knight's Ashes"
    amber_idol = "Amber Idol"
    angsty_bones_rib = "Angsty Bones' Rib"
    armor_guardians_ashes = "Armor Guardian's Ashes"
    armor_mite_chitin = "Armor Mite Chitin"
    arroxs_ear = "Arrox's Ear"
    bedspiders_tusk = "Bedspider's Tusk"
    black_pearl = "Black Pearl"
    blade_wraith_rib = "Blade Wraith Rib"
    bloated_monstrositys_ear = "Bloated Monstrosity's Ear"
    bola_eye_nerves = "Bola Eye Nerves"
    bronze_axe_knights_ashes = "Bronze Axe Knight's Ashes"
    bronze_knight_ashes = "Bronze Knight Ashes"
    caged_mans_ear = "Caged Man's Ear"
    carsejaw_the_cruels_ashes = "Carsjaw_the_Cruel's Ashes"
    cave_keepers_ear = "Cave Keeper's Ear"
    charred_doll = "Charred Doll"
    charred_locket = "Charred Locket"
    charred_reliquary = "Charred Reliquary"
    charred_tome = "Charred Tome"
    clay_phantoms_ashes = "Clay Phantom's Ashes"
    court_sorcerers_ear = "Court Sorcerer's Ear"
    crypt_keepers_ashes = "Crypt Keeper's Ashes"
    diamond_cluster = "Diamond Cluster"
    disemboweled_husks_doll = "Disemboweled Husk's Doll"
    dread_horsemans_ashes = "Dread Horseman's Ashes"
    dropspiders_tusk = "Dropspider's Tusk"
    drowned_Archers_ear = "Drowned Archer's Ear"
    drowned_bandits_ear = "Drowned Bandit's Ear"
    drowned_berzerkers_ear = "Drowned Berzerker's Ear"
    drowned_censer = "Drowned Censer"
    drowned_idol = "Drowned Idol"
    drowned_locket = "Drowned Locket"
    drowned_peasants_ear = "Drowned Peasant's Ear"
    drowned_porcelains_ashes = "Drowned Porcelain's Ashes"
    drowned_raiders_ear = "Drowned Raider's Ear"
    drowned_soldiers_ear = "Drowned Soldier's Ear"
    drowned_tome = "Drowned Tome"
    emberskulls_ashes = "Emberskull's Ashes"
    endless_fang = "Endless Fang"
    enduring_skull = "Enduring Skull"
    feral_beast_tooth = "Feral Beast Tooth"
    flying_spiders_tusk = "Flying Spider's Tusk"
    frozen_doll = "Frozen Doll"
    frozen_locket = "Frozen Locket"
    frozen_reliquary = "Frozen Reliquary"
    frozen_tome = "Frozen Tome"
    gaolers_ear = "Gaoler's Ear"
    gravewalkers_ashes = "Gravewalker's Ashes"
    gray_pearl = "Gray Pearl"
    hanged_mans_rope = "Hanged Man's Rope"
    hateful_jawbone = "Hateful Jawbone"
    heartseeker_nerves = "Heartseeker Nerves"
    hornet_steels_ashes = "Hornet Steel's Ashes"
    horseheads_ear = "Horsehead's Ear"
    hunting_bones_rib = "Hunting Bones' Rib"
    kraekan_cyclops_horn = "Kraekan Cyclops' Horn"
    kraekan_wyrms_horn = "Kraekan Wyrm's Horn"
    lepris_ear = "Lepris' Ear"
    lietch_rib = "Lietch Rib"
    lock_of_hair = "Lock of Hair"
    mother_merles_beak = "Mother Merle's Beak"
    murdiella_mals_ashes = "Murdiella Mal's Ashes"
    pale_witchs_ear = "Pale Witch's Ear"
    poison_cytoplasm_gel = "Poison Cytoplasm Gel"
    primitive_bones_rib = "Primitive Bones' Rib"
    red_lords_ear = "Red Lord's Ear"
    retchfeeder_maw = "Retchfeeder Maw"
    ronin_crans_ashes = "Ronin Cran's Ashes"
    rotten_raiders_ear = "Rotten Raider's Ear"
    rotten_walkers_ear = "Rotten Walker's Ear"
    saltless_ashes = "Saltless' Ashes"
    sanctuary_guards_ear = "Sanctuary Guard's Ear"
    shimmering_pearl = "Shimmering Pearl"
    silver_leaf = "Silver Leaf"
    skourzhs_horn = "Skourzh's Horn"
    skullbat_wing = "Skullbat Wing"
    spear_imps_horn = "Spear Imp's Horn"
    split_swordsmans_ear = "Split Swordsman's Ear"
    stone_alchemist = "Stone Alchemist"
    stone_blacksmith = "Stone Blacksmith"
    stone_cleric = "Stone Cleric"
    stone_guide = "Stone Guide"
    stone_leader = "Stone Leader"
    stone_mage = "Stone Mage"
    stone_merchant = "Stone Merchant"
    stone_sellsword = "Stone Sellsword"
    that_stench_most_fouls_tooth = "That Stench Most Foul's Tooth"
    the_architects_ear = "The Architect's Ear"
    the_bloodless_princes_ashes = "The Bloodless Prince's Ashes"
    the_coveteds_ashes = "The Coveted's Ashes"
    the_dried_kings_ashes = "The Dried King's Ashes"
    the_false_jesters_ear = "The False Jester's Ear"
    the_forgotten_judges_ear = "The Forgotten Judge's Ear"
    the_forgotten_kings_ear = "The Forgotten King's Ear"
    the_forgotten_knights_ear = "The Forgotten Knight's Ear"
    the_mad_alchemists_ear = "The Mad Alchemist's Ear"
    the_nameless_gods_ashes = "The Nameless God's Ashes"
    the_queen_of_smiles_ear = "The Queen Of Smile's Ear"
    the_sodden_knights_ashes = "The Sodden Knight's Ashes"
    the_third_lambs_beak = "The Third Lamb's Beak"
    the_tree_of_mens_ashes = "The Tree of Men's Ashes"
    the_unskinneds_liver ="The Unskinned's Liver"
    the_untouched_inquisitors_ashes = "The Untouched Inquisitor's Ashes"
    the_witch_of_the_lakes_ear = "The Witch of The Lake's Ear"
    thing_of_arms_ear = "Thing Of Arms' Ear"
    torturers_ear = "Torturer's Ear"
    twisted_heart = "Twisted Heart"
    vacant_blades_ashes = "Vacant Blades' Ashes"
    vexing_brats_ear = "Vexing Brat's Ear"
    vile_guards_ear = "Vile Guard's Ear"
    vilehawks_ear = "Vilehawk's Ear"
    whisperladys_ashes = "Whisperlady's Ashes"
    whispermans_ashes = "Whisperman's Ashes"
    wrathful_deads_bindings = "Wrathful Dead's Bindings"

""" [weapons (daggers)] """
class Daggers:
    midshipmans_dirk = "Midshipman's Dirk" # 6000
    cutpurse_shiv = "Cutpurse Shiv"
    kaltic_razor = "Kaltic Razor"
    pessklaw = "Pessklaw"
    eviscerator = "Eviscerator"
    opal_tusk = "Opal Tusk"

""" [weapons (swords)] """
class Swords:
    arming_sword = "Arming Sword" # 7000
    corsairs_backsword = "Corsair's Backsword"
    varangian_spatha = "Varangian Spatha"
    tachi = "Tachi"
    flint_and_steel = "Flint & Steel"
    virulent_scimitar = "Virulent Scimitar"
    lowlanders_greatknife = "Lowlander's Greatknife"
    kraekan_longsword = "Kraekan Longsword"
    branding_iron = "Branding Iron"
    shikeimaru = "Shikeimaru"
    leviathan = "Leviathan"

""" [weapons (hammers)] """
class Hammers:
    flanged_mace = "Flanged Mace" # 8000
    iron_pot = "Iron Pot"
    lump_hammer = "Lump Hammer"
    morning_star = "Morning Star"
    harmen_mace = "Harmen Mace"
    barbarians_cudgel = "Barbarian's Cudgel"
    cephalopounder = "Cephalopounder"
    tetruncheon = "Tetruncheon"
    mountain_breaker = "Mountain Breaker"

""" [weapons (axes)] """
class Axes:
    woodsmans_axe = "Woodsman's Axe" # 9000
    battle_axe = "Battle Axe"
    raider_axe = "Raider Axe"
    batsuichi_tsuka = "Batsuichi Tsuka"
    stone_cleaver = "Stone Cleaver"
    red_guillotine = "Red Guillotine"
    aster_monolith = "Aster Monolith"
    venom_arbelos = "Venom Arbelos"
    kraekan_axe = "Kraekan Axe"
    axe_of_splendor = "Axe of Splendor"

""" [weapons (whips)] """
class Whips:
    bullwhip = "Bullwhip" # 10000
    martial_flail = "Martial Flail"
    wraithclaw = "Wraithclaw"
    steel_centipede = "Steel Centipede"
    searing_manacle = "Searing Manacle"
    scorpion_tail = "Scorpion Tail"
    sacrificial_garrote = "Sacrificial Garrote"
    construct_coil = "Construct Coil"
    phoenix_tail = "Phoenix Tail"

""" [weapons (poleaxes)] """
class Poleaxes:
    oar = "Oar" # 11000
    infantry_pollaxe = "Infantry Pollaxe"
    guardsmans_halberd = "Guardsman's Halberd"
    naginata = "Naginata"
    kumo_sasumata = "Kumo Sasumata"
    headsmans_voulge = "Headsman's Voulge"
    tainted_ranseur = "Tainted Ranseur"
    trinity_bardiche = "Trinity Bardiche"

""" [weapons (spears)] """
class Spears:
    pitchfork = "Pitchfork"
    soldiers_spear = "Soldier's Spear"
    trident = "Trident"
    breach_pike = "Breach Pike"
    razorback = "Razorback"
    stardust_spire = "Stardust Spire"
    adder_fang = "Adder Fang"
    umbral_partisan = "Umbral Partisan"
    overlords_bident = "Overlord's Bident"

""" [weapons (reapers)] """
class Reapers:
    haymaker = "Haymaker"
    war_scythe = "War Scythe"
    red_eclipse = "Red Eclipse"
    purifier = "Purifier"
    rusted_greatladle = "Rusted Greatladle"
    gravedigger = "Gravedigger"
    saltreaver = "Saltreaver"

""" [weapons (greatswords)] """
class Greatswords:
    kureimoa = "Kureimoa"
    shrouded_bulwark = "Shrouded Bulwark"
    chitin_obelisk = "Chitin Obelisk"
    black_widow = "Black Widow"
    jaws_of_death = "Jaws of Death"
    seawolf_cutlass = "Seawolf Cutlass"
    northern_cross = "Northern Cross"
    scharfrichter = "Scharfrichter"
    trinity_greatsword = "Trinity Greatsword"
    blade_of_envy = "Blade Of Envy"

""" [weapons (greathammers)] """
class Greathammers:
    warhammer = "Warhammer"
    monstrous_mace = "Monstrous Mace"
    obsidian_pillar = "Obsidian Pillar"
    bonecrusher = "Bonecrusher"
    trinity_scepter = "Trinity Scepter"

""" [weapons (greataxes)] """
class Greataxes:
    outlaw_greataxe = "Outlaw Greataxe"
    headtaker = "Headtaker"
    iron_butterfly = "Iron Butterfly"
    earthsplitter = "Earthsplitter"
    the_coveted_weapon = "The Coveted"
    castaways_greatadze = "Castaway's Greatadze"
    self_bow = "Self Bow"
    vilehawk_bow = "Vilehawk Bow"
    bloodwood_bow = "Bloodwood Bow"
    aegis_greatbow = "Aegis Greatbow"
    recurve_bow = "Recurve Bow"
    gravewalker_greatbow = "Gravewalker Greatbow"

""" [weapons (crossbows)] """
class Crossbows:
    platoon_crossbow = "Platoon Crossbow"
    bloodwood_crossbow = "Bloodwood Crossbow"
    hellfire_arbalest = "Hellfire Arbalest"
    predator_lockbow = "Predator Lockbow"
    adrasteia = "Adrasteia"

""" [weapons (pistols)] """
class Pistols:
    flintlock_pistol = "Flintlock Pistol"
    dragoon_espingole = "Dragoon Espingole"
    lucent_musketoon = "Lucent Musketoon"
    mephitic_arquebus = "Mephitic Arquebus"
    mosaic_culverin = "Mosaic Culverin"

""" [weapons (wands)] """
class Wands:
    saltwood_branch = "Saltwood Branch"
    antler_baton = "Antler Baton"
    necromancers_virge = "Necromancer's Virge"
    rostrum_scepter = "Rostrum Scepter"
    cocoon_battledore = "Cocoon Battledore"

""" [weapons (staves)] """
class Staves:
    scrimshaw_cane = "Scrimshaw Cane"
    rowan_crosier = "Rowan Crosier"
    channelers_rod = "Channeler's Rod"
    purgatory_scepter = "Purgatory Scepter"
    sairas_staff = "Saira's Staff"

""" [shields (small)] """
class ShieldsSmall:
    buckler = "Buckler"
    silver_shield = "Silver Shield"
    wooden_targe = "Wooden Targe"

""" [shields (medium)] """
class ShieldsMedium:
    bloodbrow_scutum = "Bloodbrow Scutum"
    clerics_kite_shield = "Cleric's Kite Shield"
    escutcheon = "Escutcheon"
    heater_shield = "Heater Shield"
    mirror_shield = "Mirror Shield"
    palatine_kite_shield = "Palatine Kite Shield"
    pendragon_targe = "Pendragon Targe"
    phoenix_rondache = "Phoenix Rondache"
    raiders_targe = "Raider's Targe"
    sunset_kite_shield = "Sunset Kite Shield"
    teuthis_shield = "Teuthis Shield"
    umbral_aegis = "Umbral Aeis"
    vinemesh_peltarion = "Vinemesh Peltarion"

""" [shields (large)] """
class ShieldsLarge:
    askarian_scutum = "Askarian Scutum"
    ashen_effigy = "Ashen Effigy"
    boeotian_greatshield = "Boeotian Greatshield"
    carapace_pavise = "Carapace Pavise"
    flayers_rack = "Flayers Rack"
    gangplank_mantlet = "Gangplank Mantlet"
    iron_rampart = "Iron Rampart"
    kraekan_greatshield = "Kraekan Greatshield"
    oppressors_greatshield = "Oppressor's Greatshield"
    pruina_scutum = "Pruina Scutum"
    tainted_greatshield = "Tainted Greatshield"
    type_46_tower_shield = "Type 46 Tower Shield"

""" [rings] """
class Rings:
    bandaged_ring = "Bandaged Ring"
    bloodflower_ring = "Bloodflower Ring"
    bloodlusters_ring = "Bloodluster's Ring"
    brightcoral_ring = "Brightcoral Ring"
    burning_sky_ring = "Burning Sky Ring"
    charged_ring = "Charged Ring"
    conduit_of_mind = "Conduit of Mind"
    crystalmoat_ring = "Crystalmoat Ring"
    dancing_ring = "Dancing Ring"
    defenders_ring = "Defender's Ring"
    faithful_ring = "Faithful Ring"
    fused_metal_ring = "Fused Metal Ring"
    goldenstone_ring = "Goldenstone Ring"
    grasping_ring = "Grasping Ring"
    impen_crest_ring = "Impen Crest Ring"
    kismet_stone = "Kismet Stone"
    link_of_fire_and_sky = "Link of Fire and Sky"
    mending_band = "Mending Band"
    mossy_ring = "Mossy Ring"
    plated_band = "Plate Band"
    relentless_ring = "Relentless Ring"
    ring_of_brilliance = "Ring of Brilliance"
    ring_of_meditation = "Ring of Meditation"
    salt_seekers_ring = "Salt Seeker's Ring"
    shroud_ring = "Shroud Ring"
    sparkling_ring = "Sparkling Ring"
    storm_ring = "Storm Ring"
    symbol_of_affluence = "Symbol of Affluence"
    tricksters_band = "Trickster's Band"
    vile_vines_ring = "Vile Vines Ring"
    wrapped_link = "Wrapped Link"

    """ unused """
    band_of_the_humble = "Band of The Humble"
    flukes_ward = "Fluke's Ward"
    heartspent_ring = "Heartspent Ring"
    stone_ring = "Stone Ring"
    twinmetal_ring = "Twinmetal Ring"

""" [charms] """
class Charms:
    bloodflower_charm = "Bloodflower Charm"
    frozen_charm = "Frozen Charm"
    goldenstone_charm = "Goldenstone Charm"
    impens_charm = "Impen's Charm"
    lantern_charm = "Lantern Charm"
    mireheart_charm = "Mireheart Charm"
    mossy_charm = "Mossy Charm"
    pale_charm = "Pale Charm"
    redhair_charm = "Redhair Charm"
    saper_charm = "Saper Charm"
    shroud_charm = "Shroud Charm"
    silversalt_charm = "Silversalt Charm"
    stone_charm = "Stone Charm"
    templars_charm = "Templar's Charm"
    vile_charm = "Vile Charm"
    voracious_charm = "Voracious Charm"
    whistlebone_charm = "Whistlebone Charm"

""" [armor (light)] """
class ArmorLight:
    """ no hat """
    acolytes_kontusz = "Acolyte's Kontusz"
    acolytes_gloves = "Acolyte's Gloves"
    acolytes_boots = "Acolyte's Boots"

    alchemists_mask = "Alchemist's Mask"
    alchemists_coverall = "Alchemist's Coverall"
    """ no gloves """
    alchemists_apron = "Alchemist's Apron"

    alkymancers_veil = "Alkymancer's Veil"
    alkymancers_simar = "Alkymancer's Simar"
    """ no gloves """
    alkymancers_gown = "Alkymancer's Gown"

    amethyst_hood = "Amethyst Hood"
    amethyst_bodice = "Amethyst Bodice"
    """ no gloves """
    amethyst_skirt = "Amethyst Skirt"

    aristocrats_veil = "Aristocrat's Veil"
    aristocrats_corset = "Aristocrat's Corset"
    """ no gloves """
    aristocrats_crinolette = "Aristocrat's Crinolette"

    assassins_cowl = "Assassin's Cowl"
    assassins_tunic = "Assassin's Tunic"
    assassins_gauntlets = "Assassin's Gauntlets"
    assassins_leggings = "Assassin's Leggings"

    beggars_hood = "Beggar's Hood"
    beggars_rags = "Beggar's Rags"
    beggars_gloves = "Beggar's Gloves"
    beggars_breeches = "Beggar's Breeches"

    top_hat = "Top Hat"
    black_tailcoat = "Black Tailcoat"
    black_silk_gloves = "Black Silk Gloves"
    black_slacks = "Black Slacks"

    """ no hat """
    blacksmiths_apron = "Blacksmith's Apron"
    blacksmiths_gloves = "Blacksmith's Gloves"
    blacksmiths_boots = "Blacksmith's Boots"

    bloodbrow_barbute = "Bloodbrow Barbute"
    bloodbrow_cuirass = "Bloodbrow Cuiras"
    """ no gloves """
    bloodbrow_greaves = "Bloodbrow Greaves"

    boatmans_sugegasa = "Boatman's Sugegasa"
    boatmans_mino = "Boatman's Mino"
    """ no gloves """
    boatmans_waraji = "Boatman's Waraji"

    chefs_toque = "Chef's Toque"
    chefs_apron = "Chef's Apron"
    """ no gloves """
    chefs_trousers = "Chef's Trousers"

    clay_mask = "Clay Mask"
    """ no shirt """
    """ no gloves """
    """ no pants """

    corsairs_bandana = "Corsair's Bandana"
    corsairs_vest = "Corsair's Vest"
    """ no gloves """
    corsairs_boots = "Corsair's Boots"

    """ no hat """
    cotton_tunic = "Cotton Tunic"
    """ no gloves """
    cotton_trousers = "Cotton Trousers"

    crimson_hood = "Crimson Hood"
    crimson_tabard = "Crimson Tabard"
    crimson_gloves = "Crimson Gloves"
    crimson_culottes = "Crimson Culottes"

    evanescent_cowl = "Evanescent Cowl"
    evanescent_cassock = "Evanescent Cassock"
    """ no gloves """
    evanescent_cincture = "Evanescent Cincture"

    steepled_hat = "Steepled Hat"
    fleshbound_basque = "Fleshbound Basque"
    """ no gloves"""
    fleshbound_frock = "Fleshbound Frock"

    ghastly_gourd = "Ghastly Gourd"
    """ no shirt """
    """ no gloves """
    """ no pants """

    grim_headdress = "Grim Headdress"
    grim_justacorps = "Grim Justacorps"
    grim_bracelets = "Grim Bracelets"
    grim_tassets = "Grim Tassets"

    guides_cap = "Guide's Cap"
    guides_tunic = "Guide's Tunic"
    guides_gloves = "Guide's Gloves"
    guides_trousers = "Guide's Trousers"

    jesters_crown = "Jester's Crown"
    jesters_motley = "Jester's Motley"
    """ no gloves """
    jesters_slippers = "Jester's Slippers"

    """ no hat """
    jute_tunic = "Jute Tunic"
    """ no gloves """
    jute_breeches = "Jute Breeches"

    malva_koukoulion = "Malva Koukoulion"
    malva_tabard = "Malva Tabard"
    malva_cuffs = "Malva Cuffs"
    malva_pigaciae = "Malva's Pigaciae"

    merchants_fez = "Merchant's Fez"
    merchants_dolman = "Merchant's Dolman"
    merchants_gloves = "Merchant's Gloves"
    merchants_fistan = "Merchant's Fistan"

    tarnished_coronet = "Tarnished Coronet"
    mildewed_chemise = "Mildewed Chemise"
    mildewed_caraco = "Mildewed Caraco"
    mildewed_polonaise = "Mildewed Polonaise"

    palatine_coif = "Palatine Coif"
    """ Palatine Chainmail is heavy armor """
    """ Palatine Gauntlets is heavy armor """
    """ Palatine Chausses is heavy armor """

    patched_hood = "Patched Hood"
    patched_rags = "Patched Rags"
    patched_gloves = "Patched Gloves"
    patched_skirt = "Patched Skirt"

    pigeon_mask = "Pigeon Mask"
    """ no shirt """
    """ no gloves """
    """ no pants """

    priests_zucchetto = "Priest's Zucchetto"
    priests_dalmatic = "Priest's Dalmatic"
    """ no gloves """
    priests_sabots = "Priest's Sabots"

    frayed_sugegasa = "Frayed Sugegasa"
    ragged_hanten = "Ragged Hanten"
    silver_udewa = "Silver Udewa"
    ragged_hakama = "Ragged Hakama"

    raptor_visor = "Raptor Visor"
    raptor_brigandine = "Raptor Brigandine"
    """ no gloves """
    raptor_sabatons = "Raptor Sabatons"

    rogues_mask = "Rogue's Mask"
    rogues_jacket = "Rogue's Jacket"
    rogues_gloves = "Rogue's Gloves"
    rogues_highboots = "Rogue's Highboots"

    sadists_veil = "Sadist's Veil"
    """ no shirt """
    """ no gloves """
    """ no pants """

    """ no hat """
    sohei_kesa = "Sohei Kesa"
    juzu_udewa = "Juzu-udewa"
    sohei_tabi = "Sohei Tabi"

    """ no hat """
    sorcerers_kurta = "Sorcerer's Kurta"
    """ no gloves """
    sorcerers_lungi = "Sorcerer's Lungi"

    mask_of_splendor = "Mask of Splendor"
    """ no shirt """
    """ no gloves """
    """ no pants """

    stella_triregno = "Stella Triregno"
    stella_soprana = "Stella Soprana"
    stella_guanti = "Stella Guanti"
    stella_cincture = "Stella Cincture"

    torturers_veil = "Torturer's Veil"
    """ no shirt """
    """ no gloves """
    """ no pants """

    yokai_mask = "Yokai Mask"
    """ no shirt """
    """ no gloves """
    """ no pants """

""" [armor (heavy)] """
class ArmorHeavy:
    cavaliers_armet = "Cavalier's Armet"
    cavaliers_cuirass = "Cavalier's Cuirass"
    cavaliers_manifers = "Cavalier's Manifers"
    cavaliers_sabatons = "Cavalier's Sabatons"

    chain_coif = "Chain Coif"
    chain_hauberk = "Chain Hauberk"
    chain_gauntlets = "Chain Gauntlets"
    chain_chausses = "Chain Chausses"

    demon_kabuto = "Demon Kabuto"
    demon_domaru = "Demon Domaru"
    demon_kote = "Demon Kote"
    demon_haidate = "Demon Haidate"

    doppelsoldner_barbut = "Doppelsoldner Barbut"
    doppelsoldner_cuirass = "Doppelsoldner Cuirass"
    doppelsoldner_gauntlets = "Doppelsoldner Gauntlets"
    doppelsoldner_cuisses = "Doppelsoldner Cuisses"

    golems_head = "Golem's Head"
    golems_torso = "Golem's Torso"
    golems_arms = "Golem's Arms"
    golems_legs = "Golem's Legs"

    hunters_tricorne = "Hunter's Tricorne"
    hunters_cloak = "Hunter's Cloak"
    hunters_gloves = "Hunter's Gloves"
    hunters_boots = "Hunter's Boots"

    kraekan_helm = "Kraekan Helm"
    kraekan_armor = "Kraekan Armor"
    kraekan_gloves = "Kraekan Gloves"
    kraekan_greaves = "Kraekan Greaves"

    lamprey_barbut = "Lamprey Barbut"
    lamprey_cuirass = "Lamprey Cuirass"
    lamprey_gauntlets = "Lamprey Gauntlets"
    Lamprey_greaves = "Lamprey Greaves"

    leather_sallet = "Leather Sallet"
    leather_cuirass = "Leather Cuirass"
    leather_gauntlets = "Leather Gauntlets"
    leather_cuisses = "Leather Cuisses"

    """ no hat """
    officers_frock_coat = "Officer's Frock Coat"
    """ no gloves """
    officers_jackboots = "Officer's Jackboots"

    onyx_burgeonet = "Onyx Burgeonet"
    onyx_cuirass = "Onyx Cuirass"
    onyx_manifers = "Onyx Manifers"
    onyx_sabatons = "Onyx Sabatons"

    overlords_turban = "Overlord's Turban"
    overlords_candelabra = "Overlord's Candelabra"
    overlords_gauntlets = "Overlord's Gauntlets"
    overlords_greaves = "Overlord's Greaves"

    """ Palatine Coif is light armor """
    palatine_chainmail = "Palatine Chainmail"
    palatine_gauntlets = "Palatine Gauntlets"
    palatine_chausses = "Palatine Chausses"

    """ no hat """
    plate_mail = "Plate Mail"
    plate_gauntlets = "Plate Gauntlets"
    plate_greaves = "Plate Greaves"

    predator_bascinet = "Predator Bascinet"
    predator_cuirass = "Predator Cuirass"
    predator_gauntlets = "Predator Gauntlets"
    predator_sabatons = "Predator Sabatons"

    raiders_ushanka = "Raider's Ushanka"
    raiders_harness = "Raider's Harness"
    """ no gloves """
    raiders_portyanki = "Raider's Portyanki"

    resplendent_armet = "Resplendent Armet"
    resplendent_cuirass = "Resplendent Cuirass"
    resplendent_gauntlets = "Resplendent Gauntlets"
    resplendent_cuisses = "Resplendent Cuisses"

    russet_mask = "Russet Mask"
    russet_doublet = "Russet Doublet"
    russet_sleeves = "Russet Sleeves"
    russet_leggings = "Russet Leggings"

    scorpion_migfer = "Scorpion Migfer"
    scorpion_krug = "Scorpion Krug"
    scorpion_kolluk = "Scorpion Kolluk"
    scorpion_dizcek = "Scorpion Dizcek"

    split_mask = "Split Mask"
    split_cuirass = "Split Cuirass"
    split_manifers = "Split Manifers"
    split_sabatons = "Split Sabatons"

    steel_armet = "Steel Armet"
    steel_cuirass = "Steel Cuirass"
    steel_manifers = "Steel Manifers"
    steel_greaves = "Steel Greaves"

    tainted_armet = "Tainted Armet"
    tainted_cuirass = "Tainted Cuirass"
    tainted_gauntlets = "Tainted Gauntlets"
    tainted_greaves = "Tainted Greaves"

    titan_armet = "Titan Armet"
    titan_cuirass = "Titan Cuirass"
    titan_gauntlets = "Titan Gauntlets"
    titan_greaves = "Titan Greaves"

    umbral_visor = "Umbral Visor"
    umbral_shroud = "Umbral Shroud"
    umbral_gauntlets = "Umbral Gauntlets"
    umbral_rhinegraves = "Umbral Rhinegraves"

    wardens_branks = "Warden's Branks"
    wardens_smock = "Warden's Smock"
    wardens_gloves = "Warden's Gloves"
    wardens_chaps = "Warden's Chaps"

    royalists_armet = "Royalist's Armet"
    white_plate_armor = "White Plate Armor"
    white_gauntlets = "White Gauntlets"
    white_greaves = "White Greaves"

""" [spells] """
class Spells:
    """ class 1 """
    dark_coil = "Dark Coil"
    flashfire = "Flashfire"
    lightning_barrage = "Lightning Barrage"

    """ class 2 """
    dark_reach = "Dark Reach"
    fireball = "Fireball"
    flamestar = "Flamestar"
    lightning_ball = "Lightning Ball"
    lightning_bolt = "Lightning Bolt"

    """ class 3 """
    flame_barrage = "Flame Barrage"
    lightning_arc = "Lightning Arc"

    """ class 4 """
    dark_arrows = "Dark Arrows"
    dragonfire = "Dragonfire"

""" [prayers] """
class Prayers:
    """ class 1 """
    divine_armor = "Divine Armor"
    light = "Light"
    mend = "Mend"
    sacred_linens = "Sacred Linens"

    """ class 2 """
    blessed_weapon = "Blessed Weapon"
    cleanse = "Cleanse"
    divine_will = "Divine Will"
    revive = "Revive"
    spirited_mend = "Spirited Mend"

    """ class 3 """
    ethereal_intervention = "Ethereal Intervention"
    rejuvenate = "Rejuvenate"
    sprites = "Sprites"

    """ class 4 """
    divine_blessed_weapon = "Divine Blessed Weapon"
    ray_of_searing = "Ray of Searing"

    """ class 5 """
    guardian_blade = "Guardian's Blade"

""" [incantations] """
class Incantations:
    """ class 1 """
    venomous_blade = "Venomous Blade"

    """ class 2 """
    arcane_weapon = "Arcane Weapon"
    lightning_pod = "Lightning Pod"
    poison_gas = "Poison Gas"
    undersight = "Undersight"
    wildfire = "Wildfire"

    """ class 3 """
    dark_swarm = "Dark Swarm"
    flame_guardian = "Flame Guardian"
    flame_orbiters = "Flame Orbiters"
    lightning_storm = "Lightning Storm"

    """ class 4 """
    static_geist = "Static Geist"

    """ unused """
    rock_shield = "Rock Shield"

""" [brands] """
class Brands:
    vertigo     = "Vertigo Brand"       # rune_upside_down
    shadowflip  = "Shadowflip Brand"    # rune_wall_jump
    redshift    = "Redshift Brand"      # rune_red_block
    hardlight   = "Hardlight Brand"     # rune_blue_ether
    dart        = "Dart Brand"          # rune_dash


# anything in ConsumablesBasic and optionally Traps will also be considered filler
class Filler:
    gold_100        = "100 Gold"
    gold_200        = "200 Gold"
    gold_500        = "500 Gold"
    gold_1000       = "1000 Gold"
    full_health     = "Full Health"
    full_mana       = "Full Mana"
    invulnerability = "Invulnerability"
    torch_5         = "Torch/5"


# TODO: track CharScript.DoScript where command is 37 (activate switch) - line 726
""" [levers] """
class Levers:
    rhoc_to_outdoor = "Red Hall of Cages, leads outside"    # dungeonmidshrtf

# TODO: track CharScript.DoScript where command is 37 (activate switch) - line 726
""" [lifts] """
class Lifts:
    rhoc_mega_lift = "Red Hall of Cages mega lift"          # dungeon_double_plat1


# TODO: figure out relevance of sequences and where each one is
""" [sequences] """
class Sequences:
    castledoor = "" #
    castlegate = "" #
    castleladder = "" #
    cavedoor = "" #
    sancdoor = "" #
    sancexit = "" #
    castleexit = "" #
    castledungeongate = "" #
    secretundervillagegate = "" #
    tunneltoforesttop = "" #
    tunneltoforestbottom = "" #
    castledrawdoor = "" #
    castlebridgedrop = "" #
    forttoundervillagegate = "" #
    treestocave = "" #
    bluecaveentrance = "" #
    cavefortdoor = "" #
    bluvillagesecret = "" #
    dungeonsecpos = "" #
    ccaverollingrock = "" #
    villagerollingrock = "" #
    dungeonsec2 = "" #
    villageenter = "" #
    skycastleleftdoor = "" #
    skycastlerightdoor = "" #
    skycastlegate = "" #
    bodiespit1 = "" #
    bodiespit2 = "" #
    cavebossdoor = "" #
    ruinstwinleft = "" #
    ruinstwinright = "" #
    domegate = "" #
    castlekeydoor = "" #
    cavespidoor = "" #
    cavespigate = "" #
    cavedungeondoor = "" #
    cavemagestatue = "" #
    zigguratgates = "" #
    zigguratupgate = "" #
    swampgate = "" #
    dungeon2cave = "" #
    pyramidrightout = "" #
    swampgate2 = "" #
    inquisitor = "" #
    zigguratshortgate = "" #
    dungeontolab = "" #
    dungeontoruins = "" #
    labladder = "" #
    labtunnelgate = "" #
    lakelabruins = "" #
    cave2dungeonb = "" #
    cavetombgate2 = "" #
    labsecretlake = "" #
    tombbackgate = "" #
    pitchwoodcut = "" #
    lpitchlakeshortcut = "" #
    rpitchlakeshortcut = "" #
    nameless = "" #
    stormdualgate = "" #
    darkruinsdoor = "" #
    villageatkexit = "" #
    bladebanditgate = "" #
    bladebanditrock = "" #
    dungeontopdoor = "" #
    dungeonbotdoor = "" #
    fortblackset = "" #
    cryptgodswall = "" #
    zigropes1 = "" #
    zigropes2 = "" #
    ruincaveshort1 = "" #
    ruincaveshort2 = "" #
    labtogold = "" #
    caveswampshrine = "" #
    dungeonshrtdr = "" #
    dungeonmidshrt = "" #
    forestkeygate = "" #
    forestshrinegate = "" #
    skyladdershrt = "" #
    skysideshrt = "" #
    ruinblockfloor = "" #
    palaceescape = "" #


""" [traps] """
class Traps:
    slow_trap       = "Slow Trap"       # player moves 30% slower (10 seconds)
    fast_trap       = "Fast Trap"       # player moves 100% faster (10 seconds)
    poison_trap     = "Poison Trap"     # player is poisoned (~25% over 10 seconds)
    blind_trap      = "Blind Trap"      # player is blinded (super vignette, 10 seconds)
    pacifism_trap   = "Pacifism Trap"   # player cannot attack (10 seconds)
    mana_drain_trap = "Mana Drain Trap" # player loses mana (~25% over 5 seconds)
    weight_trap     = "Weight Trap"     # player functions as if they are near weight limit (fat roll, 10 seconds)
    chromatic_trap  = "Chromatic Trap"  # player deals random element damage on hit (10 seconds)
    acid_trap       = "Acid Trap"       # screen colors shift hue over time (10 seconds)
    gravity_trap    = "Gravity Trap"    # player jumps higher and is floaty (fall damage disabled, 10 seconds)
    cat_trap        = "Cat Trap"        # cat merchant blocks UI
