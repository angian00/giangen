
import random
from copy import deepcopy

from giangen.dungeon_map import TileType



start_wall_perc = 0.45
n_gens = 5

def generate_dungeon(d_map):
	tiles = d_map.tiles

	for x in range(1, d_map.w-1):
		for y in range(1, d_map.h-1):
			if random.random() <= (1-start_wall_perc):
				tiles[x][y] = TileType.ROOM

	#DEBUG
	#print("-- After initial seeding")
	#print(d_map) 
	#

	for i_gen in range(n_gens):
		old_tiles = deepcopy(tiles)

		for x in range(1, d_map.w-1):
			for y in range(1, d_map.h-1):
				n_neigh_1 = count_neighbours(old_tiles, x, y, 1)
				n_neigh_2 = count_neighbours(old_tiles, x, y, 2)

				if ( ((old_tiles[x][y] == TileType.WALL) 
					and (n_neigh_1 >= 4 or ((i_gen == (n_gens-2)) and (n_neigh_2 <= 2)) or ((i_gen == (n_gens-1)) and (n_neigh_2 <= 1))) ) 
					or (n_neigh_1 >= 5) ):
					
					tiles[x][y] = TileType.WALL
				else:
					tiles[x][y] = TileType.ROOM

		#DEBUG
		#print("-- After step #{}".format(i_gen+1))
		#print(d_map)
		#


def count_neighbours(tiles, x, y, r=1):
	res = 0

	for dx in range(-r, r+1):
		for dy in range(-r, r+1):
			nx = x + dx
			ny = y + dy
			if (nx == x) and (ny == y):
				#skip same tile
				continue

			if (nx < 0) or (ny < 0):
				# NB: negative indices are valid in python, 
				# but give undesired results in our case
				continue

			try:
				if tiles[nx][ny] == TileType.WALL:
					res = res + 1

			except IndexError:
				# no neighbour in that direction
				pass

	return res
