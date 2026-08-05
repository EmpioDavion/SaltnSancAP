from typing import Tuple
import json

from BaseClasses import Location
from worlds.salt_and_sanctuary.Names.RegionName import *

class SaltnSancLocation(Location):
    game = "Salt and Sanctuary"

# json data only
class SaltnSancItemData:
    name: str = ""
    count: int = 1
    category: int = 0
    code: int = 0

# json data only
class SaltnSancLocationData:
    description: str = ""
    position: Tuple[float, float] = (0.0, 0.0)
    items: list[SaltnSancItemData]

# dict[region_name, dict[location_name, location_data]]
locations_per_region: dict[str, dict[str, SaltnSancLocationData]]

# TODO: set location ids

with open("locations.json", "r", encoding="utf-8") as file:
    locations_per_region = json.load(file)

locations_concat = (
    locations_per_region[RegionName.ship] |
    locations_per_region[RegionName.shivering_shore] |
    locations_per_region[RegionName.the_festering_banquet] |
    locations_per_region[RegionName.bandits_pass] |
    locations_per_region[RegionName.village_of_smiles] |
    locations_per_region[RegionName.the_watching_woods] |
    locations_per_region[RegionName.sunken_keep] |
    locations_per_region[RegionName.castle_of_storms] |
    locations_per_region[RegionName.red_hall_of_cages] |
    locations_per_region[RegionName.hagers_cavern] |
    locations_per_region[RegionName.mire_of_stench] |
    locations_per_region[RegionName.fort_beyond_the_mire] |
    locations_per_region[RegionName.the_far_beach] |
    locations_per_region[RegionName.dome_of_the_forgotten] |
    locations_per_region[RegionName.ziggurat_of_dust] |
    locations_per_region[RegionName.the_ruined_temple] |
    locations_per_region[RegionName.crans_pass] |
    locations_per_region[RegionName.mals_floating_castle] |
    locations_per_region[RegionName.pitchwoods] |
    locations_per_region[RegionName.the_blackest_vault] |
    locations_per_region[RegionName.siam_lake] |
    locations_per_region[RegionName.salt_alkymancery] |
    locations_per_region[RegionName.crypt_of_dead_gods] |
    locations_per_region[RegionName.the_still_palace]
)

locations_items: dict[str, list[SaltnSancItemData]] = {name: data.items for name, data in locations_concat.items()}

locations: dict[str, SaltnSancItemData] = {}

for name, data in locations_items.items():
    for i, item in enumerate(data):
        locations[f"{name}_{i}"] = item
