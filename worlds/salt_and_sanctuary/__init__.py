from BaseClasses import Item, Tutorial
from worlds.AutoWorld import WebWorld, World
from typing import Dict, Any
from . import events, items, locations, regions, rules
from .options import SaltnSancOptions


class SaltnSancWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Salt and Sanctuary integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["EmpioDavion"]
    )]
    bug_report_page = "https://github.com/EmpioDavion/SaltnSancAP/issues"


# Keeping World slim so that it's easier to comprehend
class SaltnSancWorld(World):
    """
    Explore a haunting, punishing island in this stylized 2D action RPG.
    Salt and Sanctuary combines fast and brutal 2D combat with richly developed RPG mechanics
    in a cursed realm of forgotten cities, blood-soaked dungeons, and desecrated monuments.
    """

    game = "Salt and Sanctuary"
    web = SaltnSancWeb()

    options: SaltnSancOptions
    options_dataclass = SaltnSancOptions

    item_name_to_id = items.item_name_to_id
    location_name_to_id = locations.location_name_to_id

    item_name_groups = items.item_name_groups
    location_name_groups = locations.location_name_groups

    required_client_version = (0, 4, 7)

    def generate_early(self) -> None:
        if not self.player_name.isascii():
            raise Exception("SaltnSanc yaml's slot name has invalid character(s).")


    # Returned items will be sent over to the client
    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict("death_link", "victory_condition")


    def create_regions(self) -> None:
        regions.create_all_regions_and_connections(self)


    def create_item(self, name: str) -> Item:
        return items.create_item(self.player, name)


    def create_items(self) -> None:
        items.create_all_items(self)


    def set_rules(self) -> None:
        rules.create_all_rules(self)


    def get_filler_item_name(self) -> str:
        return self.random.choice(items.filler_items)

