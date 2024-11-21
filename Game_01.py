import pygame as pg


RES = WIDTH, HEIGHT =1200,1200
FPS=60
pg.init()
surface= pg.display.set_mode(RES)
clock = pg.time.Clock()

while True:
    surface.fill(pg.Color("black"))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    pg.display.flip()
    clock.tick(FPS)