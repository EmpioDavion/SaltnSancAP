import itertools
from collections import Counter
from typing import NamedTuple, TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .Names.ItemName import *
from locations import locations
from .options import *

if TYPE_CHECKING:
    from . import SaltnSancWorld
else:
    SaltnSancWorld = object


class ItemData(NamedTuple):
    code: int
    group: str
    classification: ItemClassification = ItemClassification.progression


class SaltnSancItem(Item):
    game: str = "Salt and Sanctuary"


def create_item(player: int, name: str) -> Item:
    item_data = item_table[name]
    return SaltnSancItem(name, item_data.classification, item_data.code, player)


def create_random_items(world: SaltnSancWorld, count: int) -> list[str]:
    filler_items: list[str]

    if world.options.traps.value:
        filler_items = all_filler
    else:
        filler_items = safe_filler

    return world.random.choices(population=list(filler_items), k = count)


def create_all_items(world: SaltnSancWorld) -> None:
    player = world.player
    unfilled = len(world.multiworld.get_unfilled_locations(player))

    itempool: list[str] = list(item_table.keys())
    itempool += create_random_items(world, unfilled)

    world.multiworld.itempool += [create_item(player, name) for name in itempool]


def to_item_data_dict(data: dict[str, str], group: str, item_classification: ItemClassification, base_value: int) -> dict[str, ItemData]:
    result: dict[str, ItemData] = {}

    index: int = 0

    for (k, v) in data.items():
        result[k] = ItemData(base_value + index, group, item_classification)
        index += 1

    return result


key_items = to_item_data_dict(KeyItems.__dict__, "Key Items", ItemClassification.progression, 1000)
consumables_basic = to_item_data_dict(ConsumablesBasic.__dict__, "Consumables Basic", ItemClassification.filler, 2000)
consumables_creed = to_item_data_dict(ConsumablesCreed.__dict__, "Consumables Creed", ItemClassification.useful, 3000)
consumables_debug = to_item_data_dict(ConsumablesDebug.__dict__, "Consumables Debug", ItemClassification.filler, 4000)
materials = to_item_data_dict(Materials.__dict__, "Materials", ItemClassification.useful, 5000)
daggers = to_item_data_dict(Daggers.__dict__, "Daggers", ItemClassification.useful, 6000)
swords = to_item_data_dict(Swords.__dict__, "Swords", ItemClassification.useful, 7000)
hammers = to_item_data_dict(Hammers.__dict__, "Hammers", ItemClassification.useful, 8000)
axes = to_item_data_dict(Axes.__dict__, "Axes", ItemClassification.useful, 9000)
whips = to_item_data_dict(Whips.__dict__, "Whips", ItemClassification.useful, 10000)
poleaxes = to_item_data_dict(Poleaxes.__dict__, "Poleaxes", ItemClassification.useful, 11000)
spears = to_item_data_dict(Spears.__dict__, "Spears", ItemClassification.useful, 12000)
reapers = to_item_data_dict(Reapers.__dict__, "Reapers", ItemClassification.useful, 13000)
greatswords = to_item_data_dict(Greatswords.__dict__, "Greatswords", ItemClassification.useful, 14000)
greathammers = to_item_data_dict(Greathammers.__dict__, "Greathammers", ItemClassification.useful, 15000)
greataxes = to_item_data_dict(Greataxes.__dict__, "Greataxes", ItemClassification.useful, 16000)
crossbows = to_item_data_dict(Crossbows.__dict__, "Crossbows", ItemClassification.useful, 17000)
pistols = to_item_data_dict(Pistols.__dict__, "Pistols", ItemClassification.useful, 18000)
wands = to_item_data_dict(Wands.__dict__, "Wands", ItemClassification.useful, 19000)
staves = to_item_data_dict(Staves.__dict__, "Staves", ItemClassification.useful, 20000)
shields_small = to_item_data_dict(ShieldsSmall.__dict__, "Shields Small", ItemClassification.useful, 21000)
shields_medium = to_item_data_dict(ShieldsMedium.__dict__, "Shields Medium", ItemClassification.useful, 22000)
shields_large = to_item_data_dict(ShieldsLarge.__dict__, "Shields Large", ItemClassification.useful, 23000)
rings = to_item_data_dict(Rings.__dict__, "Rings", ItemClassification.useful, 24000)
charms = to_item_data_dict(Charms.__dict__, "Charms", ItemClassification.useful, 25000)
armor_light = to_item_data_dict(ArmorLight.__dict__, "Armor Light", ItemClassification.useful, 26000)
armor_heavy = to_item_data_dict(ArmorHeavy.__dict__, "Armor Heavy", ItemClassification.useful, 27000)
spells = to_item_data_dict(Spells.__dict__, "Spells", ItemClassification.useful, 28000)
prayers = to_item_data_dict(Prayers.__dict__, "Prayers", ItemClassification.useful, 29000)
incantations = to_item_data_dict(Incantations.__dict__, "Incantations", ItemClassification.useful, 30000)
brands = to_item_data_dict(Incantations.__dict__, "Brands", ItemClassification.progression, 30000)
filler = to_item_data_dict(Filler.__dict__, "Filler", ItemClassification.filler, 31000)
levers = to_item_data_dict(Incantations.__dict__, "Incantations", ItemClassification.progression, 32000)
lifts = to_item_data_dict(Incantations.__dict__, "Incantations", ItemClassification.progression, 33000)
traps = to_item_data_dict(Traps.__dict__, "Traps", ItemClassification.trap, 34000)

items = (
    consumables_basic |
    consumables_creed |
    materials
)

one_handed_weapons = (
    daggers |
    swords |
    hammers |
    axes |
    whips |
    pistols |
    wands
)

two_handed_weapons = (
    poleaxes |
    spears |
    reapers |
    greatswords |
    greathammers |
    greataxes |
    crossbows |
    staves
)

melee_weapons = (
    daggers |
    swords |
    hammers |
    axes |
    whips |
    poleaxes |
    spears |
    reapers |
    greatswords |
    greathammers |
    greataxes
)

weapons = (
    one_handed_weapons |
    two_handed_weapons
)

shields = (
    shields_small |
    shields_medium |
    shields_large
)

armors = (
    armor_light |
    armor_heavy
)

magics = (
    spells |
    prayers |
    incantations
)

# TODO: add levers, lifts
item_table: dict[str, ItemData] = (
    key_items |
    items |
    weapons |
    shields |
    rings |
    charms |
    armors |
    magics |
    brands |
    filler
)

safe_filler: list[str] = list[str](consumables_basic.keys() | materials.keys() | filler.keys())
all_filler: list[str] = list[str](consumables_basic.keys() | materials.keys() | filler.keys() | traps.keys())

item_name_to_id: dict[str, int] = {name: data.code for name, data in item_table.items()}
location_name_to_id: dict[str, int] = {name: item_table[data.name].code for name, data in locations.items()}

item_name_groups: dict[str, set[str]] = {
    group: set(item_names) for group, item_names in itertools.groupby(item_table, lambda item: item_table[item].group)
}
