# Regions are areas in your game that you travel to.
from typing import TYPE_CHECKING, Mapping

from BaseClasses import Region
from . import locations
from .Names.RegionName import *
from .events import create_all_events

if TYPE_CHECKING:
    from . import SaltnSancWorld

def create_locations(world: "SaltnSancWorld", region: Region) -> None:
    locs = locations.locations_per_region.get(region.name, {})
    for location_name, location_data in locs.items():

        location_range: Mapping[str, int] = {f"{location_name}_{index}": location_data.items[index].code
                                             for index, item in enumerate(location_data.items)}

        region.add_locations(location_range, locations.SaltnSancLocation)


# Creates a new Region with the locations found in `location_region_mapping` and adds them to the world.
def create_region(world: "SaltnSancWorld", region_name: str) -> Region:
    new_region = Region(region_name, world.player, world.multiworld)
    create_locations(world, new_region)
    return new_region


def create_regions(world: "SaltnSancWorld", saltnsanc_regions: list[str]) -> dict[str, Region]:
    return {name: create_region(world, name) for name in saltnsanc_regions}


# Creates connections based on our access mapping in `saltnsanc_connections`.
def create_connections(world: SaltnSancWorld, regions: dict[str, Region], saltnsanc_connections: dict[str, list[str]]) -> None:
    for source, destinations in saltnsanc_connections.items():
        for destination in destinations:
            regions[source].connect(regions[destination])


# Creates all regions and connections. Called from SaltnSancWorld.
def create_all_regions_and_connections(world: "SaltnSancWorld") -> None:
    if world.options.pathing.value == 0: # normal
        saltnsanc_connections = saltnsanc_connections_normal
    elif world.options.pathing.value == 1: # hard
        saltnsanc_connections = saltnsanc_connections_hard
    else:
        saltnsanc_connections = saltnsanc_connections_brutal

    saltnsanc_regions = sorted(set(saltnsanc_connections.keys()).union(*saltnsanc_connections.values()))

    created_regions = create_regions(world, saltnsanc_regions)
    create_connections(world, created_regions, saltnsanc_connections)
    create_all_events(world, created_regions)

    world.multiworld.regions += created_regions.values()


#   maybe add fog wall checks for region locking?
#   make boatman require a check?

# strong restriction for being sent to harder places early
# Notes about artificial spheres:
#   some connections are one-way, usually by falling
#   the festering banquet to shivering shore is not specified due to forced pathing through shivering shore first
#   village of smiles to shivering shore is not specified due to forced pathing through shivering shore first
#   sunken keep to hager's cavern is not specified due to difficulty
#   castle of storms to mal's floating castle is not specified due to difficulty
#   red hall of cages to dome of the forgotten is not specified due to difficulty
#   red hall of cages to the ruined temple is not specified due to difficulty
#   red hall of cages to cran's pass is not specified due to difficulty
#   red hall of cages to mal's floating castle is not specified due to difficulty
#   red hall of cages to salt alkymancery is not specified due to difficulty
#   hagers cavern to crypt of dead gods is not specified due to difficulty
#   mire of stench to hagers cavern is not specified due to forced pathing through hagers cavern first
#   fort beyond the mire to hagers cavern is not specified due to forced pathing through hagers cavern first
#   the far beach to fort beyond the mire is not specified due to forced pathing through fort beyond the mire first
#   the far beach to pitchwoods is not specified due to difficulty
#   dome of the forgotten to the far beach is not specified due to forced pathing through the far beach first
#   ziggurat of dust to the far beach is not specified due to forced pathing through the far beach first
#   the ruined temple to red hall of cages is not specified due to forced pathing through red hall of cages first
#   the ruined temple to the far beach is not specified due to forced pathing through the far beach first
#   crans pass to red hall of cages is not specified due to forced pathing through red hall of cages first
#   pitchwoods to the far beach is not specified due to forced pathing through the far beach first
#   pitchwoods connects directly to crypt of dead gods, as rear exit salt alkymancery access is only the boss fight
#   siam lake to the ruined temple is not specified due to forced pathing through the ruined temple first
#   siam lake connects directly to crypt of dead gods, as rear exit salt alkymancery access is only the boss fight
#   salt alkymancery to red hall of cages is not specified due to forced pathing through red hall of cages first
#   crypt of dead gods to hagers cavern is not specified due to forced pathing through hagers cavern first
#   unlucky pathing would be ss>tfb>bp>cos>rhoc, skipping vos/sk/tww
saltnsanc_connections_normal: dict[str, list[str]] = {
    "Menu": [ship, shivering_shore],                # free access
    ship: [shivering_shore],                        # free access
    shivering_shore: [the_festering_banquet,        # free access
                      village_of_smiles],           # TODO: check door
    the_festering_banquet: [# shivering_shore,      # free access
                            village_of_smiles,      # free access
                            sunken_keep,            # difficult? ~2 areas early, TODO: needs ? key/lever
                            bandits_pass],          # free access
    village_of_smiles: [# shivering_shore,          # TODO: check door
                        the_festering_banquet,      # free access
                        the_watching_woods],        # free access
    the_watching_woods: [village_of_smiles,         # free access
                         sunken_keep],              # free access
    sunken_keep: [the_festering_banquet,            # via the false jester or green key
                  the_watching_woods,               # via kraekan cyclops lift or short drop
                  bandits_pass,                     # requires TODO: lift
                  red_hall_of_cages,                # requires TODO: red hall of cages mega lift remotely
                  # hagers_cavern,                  # requires TODO: ? key/lever/flag
                  ],
    bandits_pass: [the_festering_banquet,           # free access
                   sunken_keep,                     # requires TODO: ? lift/lever remotely
                   castle_of_storms],               # requires vertigo
    castle_of_storms: [bandits_pass,                # requires vertigo
                       red_hall_of_cages,           # requires TODO: ? lever
                       # mals_floating_castle       # requires hardlight+dart
                       ],
    red_hall_of_cages: [castle_of_storms,           # requires TODO: ? lever remotely
                        sunken_keep,                # maybe survive long drop, or take TODO: mega lift (lever)
                        hagers_cavern,              # via tree of men or redshift
                        # dome_of_the_forgotten,    # free access
                        # the_ruined_temple         # requires TODO: ? key/lever/door or shadowflip
                        # crans_pass,               # requires redshift+shadowflip and (hardlight or dart)
                        # mals_floating_castle,     # requires hardlight+dart+shadowflip
                        # salt_alkymancery          # requires TODO: ? lever and short drop
                        ],
    hagers_cavern: [sunken_keep,                    # requires TODO: ? lever
                    mire_of_stench,                 # requires TODO: spiked key?
                    fort_beyond_the_mire,           # requires hardlight
                    # crypt_of_dead_gods            # requires TODO: ? key/lever/flag
                    ],
    mire_of_stench: [# hagers_cavern,               # requires TODO: spiked key?
                     fort_beyond_the_mire],         # requires redshift
    fort_beyond_the_mire: [# hagers_cavern,         # requires hardlight
                           mire_of_stench,          # requires redshift
                           the_far_beach],          # free access
    the_far_beach: [# fort_beyond_the_mire,         # free access
                    dome_of_the_forgotten,          # requires hardlight and TODO: ? lift
                    ziggurat_of_dust,               # TODO: free access? west side
                    the_ruined_temple,              # requires redshift
                    # pitchwoods                    # requires dart
                    ],
    dome_of_the_forgotten: [# the_far_beach,        # requires hardlight
                            the_ruined_temple,      # requires TODO: door?
                            mals_floating_castle],  # requires hardlight+dart+shadowflip
    ziggurat_of_dust: [# the_far_beach,             # requires dart+shadowflip
                       the_ruined_temple],          # requires dart
    the_ruined_temple: [castle_of_storms,           # requires redshift from the far beach, else dart+shadowflip
                        # red_hall_of_cages,        # requires redshift from the far beach, else nothing
                        # the_far_beach,            # requires redshift from dotf, else redshift+dart+shadowflip
                        dome_of_the_forgotten,      # requires redshift from the far beach, else dart+shadowflip
                        ziggurat_of_dust,           # requires dart and TODO: ? lift to access almost all the ziggurat
                        crans_pass,                 # free access
                        mals_floating_castle,       # requires hardlight+dart+shadowflip, +redshift from the far beach
                        pitchwoods,                 # free access, difficult?
                        siam_lake],                 # free access, difficult?
    crans_pass: [# red_hall_of_cages,               # requires redshift
                 the_ruined_temple,                 # free access
                 salt_alkymancery],                 # requires hardlight (and redshift if from red hall of cages)
    mals_floating_castle: [castle_of_storms],       # requires hardlight+dart and TODO: leap of faith off roof?
    pitchwoods: [# the_far_beach,                   # requires hardlight+dart+shadowflip
                 the_blackest_vault,                # free access
                 crypt_of_dead_gods],               # requires TODO: ? lever remotely, via salt alkymancery rear exit
    the_blackest_vault: [],                         # drops are one-way
    siam_lake: [# the_ruined_temple,                # free access
                the_blackest_vault,                 # free access
                salt_alkymancery,                   # free access, may require dart for most access, check ducts
                crypt_of_dead_gods],                # requires TODO: ? lever remotely, via salt alkymancery rear exit
    salt_alkymancery: [# red_hall_of_cages,         # dart from crans pass, dart+shadowflip from siam lake, else blocked
                       crans_pass,                  # requires hardlight+dart, +shadowflip from siam lake, via siam lake
                       siam_lake,                   # requires dart or TODO: long drop?
                       crypt_of_dead_gods,          # requires dart+shadowflip
                       the_still_palace],           # requires dart+shadowflip
    crypt_of_dead_gods: [# hagers_cavern,           # requires dart+shadowflip from the still space, else dart
                         pitchwoods,                # requires TODO: ? lever + dart+shadowflip, via salt alkymancery rear exit
                         siam_lake,                 # requires TODO: ? lever + dart+shadowflip, via salt alkymancery rear exit
                         the_still_palace],         # requires dart or long drop
    the_still_palace: [pitchwoods,                  # requires TODO: ? lever + dart+shadowflip, via salt alkymancery rear exit
                       siam_lake,                   # requires TODO: ? lever + dart+shadowflip, via salt alkymancery rear exit
                       crypt_of_dead_gods],         # requires dart+shadowflip for most access
}

# weak restriction for being sent to harder places early
# Notes about artificial spheres:
saltnsanc_connections_hard: dict[str, list[str]] = {}

# no restriction for being sent to harder places early
# Notes about artificial spheres:
saltnsanc_connections_brutal: dict[str, list[str]] = {}

