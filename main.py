import sys
import pygame as pg

from settings import *
from map import Map
from player import Player
from raycasting import RayCasting


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.enable_mini_map = False
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        pg.display.set_caption(f'{self.clock.get_fps() :.2f}')

    def draw(self):
        self.screen.fill('black')
        if self.enable_mini_map is True:
            self.screen.fill('grey')
            self.map.draw()
            self.player.draw()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_TAB and self.enable_mini_map is False:
                self.enable_mini_map = True

            if event.type == pg.KEYDOWN and event.key == pg.K_m and self.enable_mini_map is True:
                self.enable_mini_map = False



    def run(self):
        while True:
            self.draw()
            self.update()
            self.check_event()


if __name__ == '__main__':
    game = Game()
    game.run()
