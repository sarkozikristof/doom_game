import sys
import pygame as pg

from settings import *
from map import Map
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectRenderer
from object_handler import ObjectHandler
from weapon import Weapon
from sound import Sound


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.enable_mini_map = False
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()
        print()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        # self.sound.theme.play(loops=-1)

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        pg.display.set_caption(f'{self.clock.get_fps() :.2f}')

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()
        if self.enable_mini_map is True:
            self.screen.fill('grey')
            self.map.draw()
            self.player.draw()

    def check_event(self):
        self.global_event = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            elif event.type == self.global_event:
                self.global_trigger = True

            if event.type == pg.KEYDOWN and event.key == pg.K_TAB and self.enable_mini_map is False:
                self.enable_mini_map = True

            if event.type == pg.KEYUP and event.key == pg.K_TAB:
                self.enable_mini_map = False

            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.draw()
            self.update()
            self.check_event()


if __name__ == '__main__':
    game = Game()
    game.run()
