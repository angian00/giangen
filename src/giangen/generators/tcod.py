import random
import math

from giangen.dungeon_map import TileType


n_tot_rooms = 9
max_isect_loops = 20
room_min_size = 5
room_max_size = 9


def generate_dungeon(d_map):
	tiles = d_map.tiles
	rooms = []

	n_rooms = 0
	loop_check = 0
	while (n_rooms < n_tot_rooms) and (loop_check < max_isect_loops):
		room_w = random.randint(room_min_size, room_max_size)
		room_h = random.randint(room_min_size, room_max_size)

		x = random.randint(0, d_map.w - room_w - 1)
		y = random.randint(0, d_map.h - room_h - 1)

		new_room = { "x1": x, "x2": x + room_w, "y1": y, "y2": y + room_h }
		loop_check = loop_check + 1

		failed = False
		for i_room in range(n_rooms):
			if (check_room_isect(new_room, rooms[i_room])):
				failed = True
				break

		if not failed:
			print(new_room)
			create_room(tiles, new_room)

			curr_center = get_room_center(new_room)

			if n_rooms > 0:
				#all rooms after the first:
				#connect it to the previous room with a tunnel

				prev_center = get_room_center(rooms[n_rooms-1])

				#draw a coin
				if random.randint(0, 1) == 1:
					#first move horizontally, then vertically
					create_h_tunnel(tiles, prev_center["x"], curr_center["x"], prev_center["y"])
					create_v_tunnel(tiles, prev_center["y"], curr_center["y"], curr_center["x"])
					pass

				else:
					#first move vertically, then horizontally
					create_v_tunnel(tiles, prev_center["y"], curr_center["y"], prev_center["x"])
					create_h_tunnel(tiles, prev_center["x"], curr_center["x"], curr_center["y"])
					pass

			#finally, append the new room to the list
			rooms.append(new_room)
			n_rooms = n_rooms + 1
			loop_check = 0
 


def check_room_isect(room1, room2):
	return (
		(room1["x1"] <= room2["x2"]) and
		(room1["x2"] >= room2["x1"]) and
		(room1["y1"] <= room2["y2"]) and
		(room1["y2"] >= room2["y1"])
	)

def get_room_center(room):
	return {
		"x": math.floor((room["x1"] + room["x2"]) / 2),
		"y": math.floor((room["y1"] + room["y2"]) / 2)
	}


def create_room(tiles, room):
	for x in range(room["x1"] + 1, room["x2"]):
		for y in range(room["y1"] + 1, room["y2"]):
			#print("create_room: {}, {}".format(x, y))
			tiles[x][y] = TileType.ROOM

def create_h_tunnel(tiles, x1, x2, y):
	for x in range(min(x1, x2), max(x1, x2) + 1):
		if tiles[x][y] != TileType.ROOM: 
			tiles[x][y] = TileType.CORRIDOR

def create_v_tunnel(tiles, y1, y2, x):
	for y in range(min(y1, y2), max(y1, y2) + 1):
		if tiles[x][y] != TileType.ROOM: 
			tiles[x][y] = TileType.CORRIDOR
