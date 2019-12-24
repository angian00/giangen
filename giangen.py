#!/usr/bin/env python3

from PIL import Image
from PIL import ImageDraw

###### params ######
img_path = "./output/maze_00.png"
world_w = 20
world_h = 15

room_size = 5
tile_size = 40

bkg_color = "black"
room_color = "white"

####################



def main():
	print()
	print(" -- giangen --")
	print(" a Python maze generator")
	print()

	img = init_image()
	draw_rooms(img)
	save_image(img, img_path)
	print("saved image as {}".format(img_path))

	print()


def init_image():
	return Image.new('RGB', (world_w*tile_size, world_h*tile_size), color = bkg_color)

def draw_rooms(img):
	draw = ImageDraw.Draw(img)
	x_start = 3
	y_start = 5
	draw.rectangle(((x_start*tile_size, y_start*tile_size), 
		((x_start+room_size)*tile_size, (y_start+room_size)*tile_size)), 
		fill=room_color)

def save_image(img, img_path):
	img.save(img_path)


if __name__ == '__main__':
	main()
