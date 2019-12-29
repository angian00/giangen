#!/usr/bin/env python3

from time import time


from giangen.dungeon_map import *

#from giangen.generators.single_fixed import generate_dungeon
from giangen.generators.basic import generate_dungeon
#from giangen.generators.cell_automa import generate_dungeon


###### params ######
img_path = "./output/dungeon_00.png"
map_w = 48
map_h = 36
#map_w = 96
#map_h = 72
#map_w = 60
#map_h = 60

####################


def run():
	print()
	print("-- giangen")
	print("-- a Python dungeon generator")
	print()

	start_ts = time()
	
	d_map = DungeonMap(map_w, map_h)
	generate_dungeon(d_map)
	#print(d_map)
	d_map.export(img_path)
	print("saved image as {}".format(img_path))
	
	end_ts = time()

	print("execution time: {0:.2f} seconds".format(end_ts-start_ts))
	print()

