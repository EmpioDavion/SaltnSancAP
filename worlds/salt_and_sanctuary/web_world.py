from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups


class SaltnSancWebWorld(WebWorld):
    game = "Salt and Sanctuary"
    theme = "ocean"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Salt and Sanctuary for Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["NewSoupVi"]
    )
    tutorials = [setup_en]
    option_groups = option_groups
