#!/usr/bin/env python3

from PIL import Image


img_path = "./output/maze_00.png"
img_w = 800
img_h = 600


def main():
	print(" ------------ giangen ------------")
	print(" ---- a Python maze generator ----")
	print()

	save_image(img_path)
	print("saved image as {}".format(img_path))

	print()



def save_image(img_path):
	img = Image.new('RGB', (img_w, img_h), color = 'red')
	img.save(img_path)


if __name__ == '__main__':
	main()
