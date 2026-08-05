from Names.RegionName import *
from worlds.salt_and_sanctuary.Names.BossName import BossName
from worlds.salt_and_sanctuary.Names.ItemName import KeyItems, Sequences, Brands
from worlds.salt_and_sanctuary.Names.RegionName import RegionName


class Connection:
	region: str			# connecting region
	items: list[str]	# required items
	difficulty: int

	def __init__(self, region, items:list[str]=[], difficulty:int=0):
		self.region = region
		self.items = items
		self.difficulty = difficulty


class Area:
	connections: list[Connection]

	def __init__(self, connections):
		self.connections = connections

# maybe remove bosses from logic as their arena flags aren't jumbled
region_data: dict[str, Area] = {
	RegionName.menu: Area([
		Connection(RegionName.ship),
		Connection(RegionName.shivering_shore)
	]),
	RegionName.ship: Area([
		Connection(RegionName.shivering_shore)
	]),
	RegionName.shivering_shore: Area([
		Connection(RegionName.the_festering_banquet, [KeyItems.sanctuary_key]),
		Connection(RegionName.village_of_smiles, [KeyItems.sanctuary_key]) # check if door also needed
	]),
	RegionName.the_festering_banquet: Area([
		Connection(RegionName.village_of_smiles),
		Connection(RegionName.sunken_keep, [Sequences.], 1),
		Connection(RegionName.bandits_pass)
	]),
	RegionName.village_of_smiles: Area([
		Connection(RegionName.the_festering_banquet),
		Connection(RegionName.the_watching_woods),
	]),
	RegionName.the_watching_woods: Area([
		Connection(RegionName.village_of_smiles),
		Connection(RegionName.sunken_keep)
	]),
	RegionName.sunken_keep: Area([
		Connection(RegionName.the_festering_banquet, [BossName.the_false_jester]),
		Connection(RegionName.the_festering_banquet, [KeyItems.green_key]),
		Connection(RegionName.the_watching_woods),
		Connection(RegionName.bandits_pass, [Sequences.]),
		Connection(RegionName.red_hall_of_cages, [Sequences.]),
		Connection(RegionName.hagers_cavern, [Sequences.], 1)
	]),
	RegionName.bandits_pass: Area([
		Connection(RegionName.the_festering_banquet),
		Connection(RegionName.sunken_keep, [Sequences.]),
		Connection(RegionName.castle_of_storms, [Brands.vertigo])
	]),
	RegionName.castle_of_storms: Area([
		Connection(RegionName.bandits_pass, [Brands.vertigo]),
		Connection(RegionName.red_hall_of_cages, [Sequences.]),
		Connection(RegionName.mals_floating_castle, [Brands.hardlight, Brands.dart], 2)
	]),
	RegionName.red_hall_of_cages: Area([
		Connection(RegionName.castle_of_storms, [Sequences.]),
		Connection(RegionName.sunken_keep, [Sequences.]),
		Connection(RegionName.hagers_cavern, [BossName.the_tree_of_men]),
		Connection(RegionName.hagers_cavern, [Brands.redshift]),
		Connection(RegionName.dome_of_the_forgotten, [], 1),
		Connection(RegionName.the_ruined_temple_upper, [Brands.redshift, Sequences.], 2), # by mals floating castle
		Connection(RegionName.the_ruined_temple_lower, [Sequences.], 2), # by mals floating castle
		Connection(RegionName.the_ruined_temple_lower, [Sequences.], 2), # above crans pass
		Connection(RegionName.crans_pass, [Brands.shadowflip, Brands.redshift, Brands.hardlight], 2),
		Connection(RegionName.crans_pass, [Brands.shadowflip, Brands.redshift, Brands.dart], 2),
		Connection(RegionName.mals_floating_castle, [Brands.shadowflip, Brands.hardlight, Brands.dart], 2),
		Connection(RegionName.salt_alkymancery_upper, [Sequences.], 2)
	]),
	RegionName.hagers_cavern: Area([
		Connection(RegionName.sunken_keep, [Sequences.]),
		Connection(RegionName.red_hall_of_cages, [Brands.redshift]),
		Connection(RegionName.red_hall_of_cages, [Brands.dart]),
		Connection(RegionName.mire_of_stench, [KeyItems.spiked_key]), # TODO: is this spiked key?
		Connection(RegionName.fort_beyond_the_mire, [Brands.hardlight]),
		Connection(RegionName.crypt_of_dead_gods_upper, [Sequences.], 2)
	]),
	RegionName.mire_of_stench: Area([
		Connection(RegionName.hagers_cavern, [KeyItems.spiked_key]), # TODO: is this spiked key?
		Connection(RegionName.fort_beyond_the_mire, [Brands.redshift])
	]),
	RegionName.fort_beyond_the_mire: Area([
		Connection(RegionName.hagers_cavern, [Brands.hardlight]),
		Connection(RegionName.mire_of_stench, [Brands.redshift]),
		Connection(RegionName.the_far_beach)
	]),
	RegionName.the_far_beach: Area([
		Connection(RegionName.fort_beyond_the_mire),
		Connection(RegionName.dome_of_the_forgotten, [Brands.hardlight, Sequences.]),
		Connection(RegionName.ziggurat_of_dust_upper), # TODO: check west entrance open?
		Connection(RegionName.the_ruined_temple_upper, [Brands.redshift]),
		Connection(RegionName.pitchwoods, [Brands.dart])
	]),
	RegionName.dome_of_the_forgotten: Area([
		Connection(RegionName.the_far_beach, [Brands.hardlight]),
		Connection(RegionName.the_ruined_temple_upper, [Brands.redshift]),
		Connection(RegionName.the_ruined_temple_lower, [Sequences.]),
		Connection(RegionName.mals_floating_castle, [Brands.shadowflip, Brands.hardlight, Brands.dart])
	]),
	RegionName.ziggurat_of_dust_upper: Area([
		Connection(RegionName.the_far_beach), # TODO: check west entrance open?
		Connection(RegionName.ziggurat_of_dust_lower, [Brands.dart])
	]),
	RegionName.ziggurat_of_dust_lower: Area([
		Connection(RegionName.ziggurat_of_dust_upper, [Brands.shadowflip, Brands.dart]),
		Connection(RegionName.the_ruined_temple_lower,
				   [BossName.the_forgotten_knight, BossName.the_forgotten_king, BossName.the_forgotten_judge])
	]),
	RegionName.the_ruined_temple_upper: Area([
		Connection(RegionName.red_hall_of_cages, [Brands.redshift]),
		Connection(RegionName.the_far_beach, [Brands.redshift]),
		Connection(RegionName.dome_of_the_forgotten, [Brands.redshift]),
		Connection(RegionName.the_ruined_temple_lower, [Brands.redshift]) # TODO: also needs gate/door?
	]),
	RegionName.the_ruined_temple_lower: Area([
		Connection(RegionName.red_hall_of_cages),
		Connection(RegionName.the_far_beach),
		Connection(RegionName.dome_of_the_forgotten),
		Connection(RegionName.ziggurat_of_dust_lower),
		Connection(RegionName.the_ruined_temple_upper, [Brands.redshift]), # TODO: also needs gate/door?
		Connection(RegionName.crans_pass),
		Connection(RegionName.mals_floating_castle, [Brands.shadowflip, Brands.hardlight, Brands.dart]),
		Connection(RegionName.pitchwoods),
		Connection(RegionName.siam_lake)
	]),
	RegionName.crans_pass: Area([
		Connection(RegionName.red_hall_of_cages, [Brands.redshift]),
		Connection(RegionName.the_ruined_temple_lower, [Brands.redshift, Brands.hardlight]),
		Connection(RegionName.the_ruined_temple_lower, [Brands.redshift, Brands.shadowflip, Brands.dart]),
		Connection(RegionName.salt_alkymancery_upper, [Brands.hardlight, Brands.dart])
	]),
	RegionName.mals_floating_castle: Area([
		Connection(RegionName.castle_of_storms, [Brands.hardlight, Brands.dart])
	]),
	RegionName.pitchwoods: Area([
		Connection(RegionName.the_far_beach, [Brands.shadowflip, Brands.hardlight, Brands.dart]),
		Connection(RegionName.the_blackest_vault),
		Connection(RegionName.salt_alkymancery_lower, [Sequences.]),
		Connection(RegionName.the_still_palace, [Sequences.])
	]),
	RegionName.the_blackest_vault: Area([]),
	RegionName.siam_lake: Area([
		Connection(RegionName.the_ruined_temple_lower),
		Connection(RegionName.the_blackest_vault),
		Connection(RegionName.salt_alkymancery_upper, [BossName.the_witch_of_the_lake]),
		Connection(RegionName.salt_alkymancery_lower, [Sequences.]),
		Connection(RegionName.the_still_palace, [Sequences.])
	]),
	RegionName.salt_alkymancery_upper: Area([
		Connection(RegionName.red_hall_of_cages, [Brands.shadowflip, Brands.dart]),
		Connection(RegionName.crans_pass, [Brands.shadowflip, Brands.hardlight, Brands.dart]),
		Connection(RegionName.siam_lake),
		Connection(RegionName.salt_alkymancery_lower, [Brands.shadowflip, Brands.dart]),
	]),
	RegionName.salt_alkymancery_lower: Area([
		Connection(RegionName.pitchwoods, [Sequences.]),
		Connection(RegionName.siam_lake, [Sequences.]),
		Connection(RegionName.crypt_of_dead_gods_upper, [Brands.shadowflip]),
		Connection(RegionName.the_still_palace)
	]),
	RegionName.crypt_of_dead_gods_upper: Area([
		Connection(RegionName.hagers_cavern, [Brands.dart]), # TODO: requires door or fake wall?
		Connection(RegionName.salt_alkymancery_lower, [Brands.dart]),
		Connection(RegionName.crypt_of_dead_gods_lower)	# can reach by falling down east side
	]),
	RegionName.crypt_of_dead_gods_lower: Area([
		Connection(RegionName.crypt_of_dead_gods_upper, [Brands.shadowflip, Brands.dart]), # TODO: can get up?
		Connection(RegionName.the_still_palace, [BossName.kraekan_dragon_skourzh])
	]),
	RegionName.the_still_palace: Area([
		Connection(RegionName.crypt_of_dead_gods_lower), # assuming not coming from the nameless god
	]) # you will be stuck at the bottom if you don't have shadowflip and dart, save and reload if this happens
	}
