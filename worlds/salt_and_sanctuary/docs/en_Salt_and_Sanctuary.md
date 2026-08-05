# Salt and Sanctuary

## Where is the options page?

The [player options page for this game](../player-options) contains all the options you need to configure and export a
config file.

## What does randomization do to this game?

Salt and Sanctuary can have items retrieved from chests or fixed pickups

## What is the goal of Salt and Sanctuary?

The goal of Salt and Sanctuary is to kill the final boss The Nameless God, then interact with
the Scarecrow found shortly after the boss room. The goal may be changed to require the Domination ending,
which requires speaking to the Scarecrow at every location he appears, then selecting "Take Helm"
when speaking to him at his final location. 

## What Salt and Sanctuary items can appear in other players' worlds?

Items required for progression, such as keys and brands.

Activation of levers for lifts, opening portcullises, gates and doors.

Weapons, armor pieces, charms, magics, consumable items and ammo.

Creed items, such as those needed for claiming sanctuaries, and healing items that replenish on rest.

Black pearls, which are used to acquire skills.

Skills, such as those need to equip certain weapons and armor.

Positive filler items:
* `Gold (100, 200, 500, 1000)`
* `Full Health`
* `Full Mana`
* `Invulnerablity`  Player takes no damage (10 seconds)
* `Torches`

Traps:
* `Slow Trap`       Player moves 30% slower (10 seconds)
* `Fast Trap`       Player moves 100% faster (10 seconds)
* `Poison Trap`     Player is poisoned (~25% over 10 seconds)
* `Blind Trap`      Player is blinded (super vignette, 10 seconds)
* `Pacifism Trap`   Player cannot attack (10 seconds)
* `Mana Drain Trap` Player loses mana (~25% over 5 seconds)
* `Weight Trap`     Player functions as if they are near weight limit (fat roll, 10 seconds)
* `Chromatic Trap`  Player deals random element damage on hit (10 seconds)
* `Acid Trap`       Screen colors shift hue over time (10 seconds)
* `Gravity Trap`    Player jumps higher and is floaty (fall damage disabled, 10 seconds)
* `Cat Trap`        Cat merchant blocks UI

## How many location checks are there?

TODO: 
When using the default options, there are ? location checks.

## What does another world's item look like in Salt and Sanctuary?

Pickups and chests will look the same.

In shops, other players' items will look like the Archipelago logo.

## Is Archipelago compatible with other Salt and Sanctuary mods?

Any Salt and Sanctuary mod should work with some caveats if the mod affects:
* `Map Layout`      Changing zone connections may result in softlock.
* `Item Placement`  A progression item may be permanently unreachable, or missing.
* `Menuing`         May cause the AP menu to become unreachable/unusable.
