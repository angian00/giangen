import math
from enum import Enum

from PIL import Image
from PIL import ImageDraw



class TileType(Enum):
	WALL      = 0
	ROOM      = 1
	CORRIDOR  = 2

	# def __str__(self):
	# 	if self == TileType.WALL:
	# 		return "W"
	# 	elif self == TileType.ROOM:
	# 		return "R"
	# 	elif self == TileType.CORRIDOR:
	# 		return "C"
	# 	else:
	# 		return "?"

	def __str__(self):
		if self == TileType.WALL:
			return "#"
		elif self == TileType.ROOM:
			return "."
		elif self == TileType.CORRIDOR:
			return "."
		else:
			return "?"
#--------------------

tile_size = 40


#--------------------

class DungeonMap:
	def __init__(self, w, h):
		self.w = w
		self.h = h

		self.tiles = []

		for x in range(w):
			self.tiles.append([])
			for y in range(h):
				self.tiles[x].append(TileType.WALL)


	def __str__(self):
		res = "DungeonMap ({}x{}) \n".format(self.w, self.h)
		for x in range(self.w):
			#res = res + "[{}] ".format(x)
			for y in range(self.h):
				res = res + "{} ".format(self.tiles[x][y])
			res = res + "\n"

		return res

	def export(self, img_path):
		#self.export_1(img_path)
		#self.export_2(img_path)
		self.export_3(img_path)


	def export_1(self, img_path):
		colors = {
			TileType.WALL: "black",
			TileType.ROOM: "white",
			TileType.CORRIDOR: "grey"
		}

		img = Image.new('RGB', (self.w*tile_size, self.h*tile_size), color = "black")
		draw = ImageDraw.Draw(img)

		for x in range(self.w):
			for y in range(self.h):
				draw.rectangle((
					(x*tile_size, y*tile_size), 
					((x+1)*tile_size, (y+1)*tile_size) ),
					fill=colors[self.tiles[x][y]])

				draw.line((
					(x*tile_size, y*tile_size), 
					((x+1)*tile_size, y*tile_size) ),
					fill=colors[TileType.WALL])
				draw.line((
					(x*tile_size, y*tile_size), 
					(x*tile_size, (y+1)*tile_size) ),
					fill=colors[TileType.WALL])

		img.save(img_path)


	def export_2(self, img_path):
		colors = {
			TileType.WALL: "#f2ecbd",
			TileType.ROOM: "#e0e0e0",
			TileType.CORRIDOR: "#c0c0c0"
		}

		img = Image.new('RGB', (self.w*tile_size, self.h*tile_size), color = colors[TileType.WALL])
		draw = ImageDraw.Draw(img)

		n_lines = max(self.w, self.h) * 6
		line_space_x = math.ceil( self.w * tile_size / (n_lines/2) )
		line_space_y = math.ceil( self.h * tile_size / (n_lines/2) )

		for i_line in range(n_lines):
			draw.line((
				(i_line*line_space_x, 0),
				(0, i_line*line_space_y) ),
				fill="black", width=1)


		for x in range(self.w):
			for y in range(self.h):
				if not self.tiles[x][y] == TileType.WALL:
					draw.rectangle((
						(x*tile_size, y*tile_size), 
						((x+1)*tile_size-1, (y+1)*tile_size-1) ),
						fill=colors[self.tiles[x][y]])

		img.save(img_path)


	def export_3(self, img_path):
		img = Image.new('RGB', (self.w*tile_size, self.h*tile_size), color = "#c0c0c0")
		draw = ImageDraw.Draw(img)

		for x in range(self.w):
			for y in range(self.h):
				if not self.tiles[x][y] == TileType.WALL:
					draw.rectangle((
						(x*tile_size, y*tile_size), 
						((x+1)*tile_size-1, (y+1)*tile_size-1) ),
						fill='white')

					for dir in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
					#for dir in [ (0, 1) ]:
						nx = x + dir[0]
						ny = y + dir[1]

						if (nx < 0) or (nx >= self.w) or (ny < 0) or (ny >= self.h) or (self.tiles[nx][ny] == TileType.WALL):
							line_color = 'black'
							line_width = int(tile_size / 10)
						else:
							line_color = 'grey'
							line_width = 1

						if x == nx:
							x1 = x
							x2 = x + 1
							y1 = max(y, ny)
							y2 = y1
						else:
							x1 = max(x, nx)
							x2 = x1
							y1 = y
							y2 = y + 1

						draw.line((
							(x1 * tile_size, y1 * tile_size), 
							(x2 * tile_size, y2 * tile_size) ),
							fill=line_color, width=line_width)

		img.save(img_path)
