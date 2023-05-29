import pygame as pg
import sys

print('hello world!')

pg.init()
gui_size = (500,500)
screen = pg.display.set_mode(gui_size)
pg.display.set_caption('Project 1')

img1 = pg.image.load('../assets/city1.png').convert_alpha()
img1 = pg.transform.scale(img1, gui_size)


def loop():
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				return
		screen.blit(img1, (0,0))
		pg.display.flip()

loop()
pg.quit()