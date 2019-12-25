#!/usr/bin/env python3

from enum import Enum
import math
import random

from PIL import Image
from PIL import ImageDraw


class TileType(Enum):
	WALL      = 0
	ROOM      = 1
	CORRIDOR  = 2

	def __str__(self):
		if self == TileType.WALL:
			return "W"
		elif self == TileType.ROOM:
			return "R"
		elif self == TileType.CORRIDOR:
			return "C"
		else:
			return "?"


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


def main():
	print()
	print(" -- giangen --")
	print(" a Python dungeon generator")
	print()


	tiles = init_map()
	generate_rooms(tiles)
	#print_map(tiles)
	save_map(tiles, img_path)
	print("saved image as {}".format(img_path))

	print()


def init_map():
	tiles = []
	for x in range(map_w):
		tiles.append([])
		for y in range(map_h):
			tiles[x].append(TileType.WALL)

	return tiles

def generate_rooms(tiles):
	#draw_rooms_fixed(img)
	generate_rooms_tcod(tiles)


def draw_rooms_fixed(img):
	draw = ImageDraw.Draw(img)
	x_start = 3
	y_start = 5
	draw.rectangle(((x_start*tile_size, y_start*tile_size), 
		((x_start+room_size)*tile_size, (y_start+room_size)*tile_size)), 
		fill=room_color)

#--------------------------------------
n_tot_rooms = 9
max_isect_loops = 20
room_min_size = 5
room_max_size = 9

def generate_rooms_tcod(tiles):
	rooms = []

	n_rooms = 0
	loop_check = 0
	while (n_rooms < n_tot_rooms) and (loop_check < max_isect_loops):
		w = random.randint(room_min_size, room_max_size)
		h = random.randint(room_min_size, room_max_size)

		x = random.randint(0, map_w - w - 1)
		y = random.randint(0, map_h - h - 1)

		new_room = { "x1": x, "x2": x + w, "y1": y, "y2": y + h }
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

#--------------------------------------

def print_map(tiles):
	for x in range(map_w):
		print("[{}]".format(x), end =" ")
		for y in range(map_h):
			print("{}".format(tiles[x][y]), end =" ")
		print()

def save_map(tiles, img_path):
	img = Image.new('RGB', (map_w*tile_size, map_h*tile_size), color = "black")
	draw = ImageDraw.Draw(img)

	for x in range(map_w):
		for y in range(map_h):
			#print("{}, {} --> {}".format(x, y, colors[tiles[x][y]]))
			draw.rectangle((
				(x*tile_size, y*tile_size), 
				((x+1)*tile_size, (y+1)*tile_size) ),
				fill=colors[tiles[x][y]])
	img.save(img_path)


if __name__ == '__main__':
	main()
