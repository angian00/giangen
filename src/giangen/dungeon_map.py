from enum import Enum

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
		res = "DungeonMap ({}x{})".format(self.w, self.h)
		for x in range(self.w):
			res = res + "[{}] ".format(x)
			for y in range(self.h):
				res = res + "{} ".format(self.tiles[x][y])
			res = res + "\n"

		return res


	def export(self, img_path, tile_size, colors):
		img = Image.new('RGB', (self.w*tile_size, self.h*tile_size), color = "black")
		draw = ImageDraw.Draw(img)

		for x in range(self.w):
			for y in range(self.h):
				#print("{}, {} --> {}".format(x, y, colors[tiles[x][y]]))
				draw.rectangle((
					(x*tile_size, y*tile_size), 
					((x+1)*tile_size, (y+1)*tile_size) ),
					fill=colors[self.tiles[x][y]])
		img.save(img_path)


