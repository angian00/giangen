from giangen.dungeon_map import TileType

x_start = 12
y_start = 8
room_size = 7

def generate_dungeon(d_map):	
	for x in range(x_start, x_start + room_size):
		for y in range(y_start, y_start + room_size):
			#print("create_room: {}, {}".format(x, y))
			d_map.tiles[x][y] = TileType.ROOM
