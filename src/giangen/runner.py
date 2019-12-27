#!/usr/bin/env python3


from giangen.dungeon_map import *

#from giangen.generators.single_fixed import generate_dungeon
from giangen.generators.tcod import generate_dungeon


###### params ######
img_path = "./output/dungeon_00.png"
map_w = 48
map_h = 36

tile_size = 20

colors = {
	TileType.WALL: "black",
	TileType.ROOM: "white",
	TileType.CORRIDOR: "grey"
}

####################


def run():
	print()
	print(" -- giangen --")
	print(" a Python dungeon generator")
	print()


	d_map = DungeonMap(map_w, map_h)
	generate_dungeon(d_map)
	print(d_map)
	d_map.export(img_path, tile_size, colors)
	print("saved image as {}".format(img_path))

	print()

