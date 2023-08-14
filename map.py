import pygame as pg
from map_gen.simple_room_placement import Generator

_ = False

mini_map_v1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, 3],
    [1, _, _, 3, _, _, _, _, _, _, _, _, 2, _, _, 3],
    [1, _, _, _, _, _, _, _, _, _, _, _, 5, _, _, 3],
    [1, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, 3],
    [1, _, _, _, _, _, 3, _, _, _, _, _, 2, _, _, 3],
    [1, _, _, _, _, _, 3, 3, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

mini_map = Generator().generate()


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for i in self.world_map:
            pg.draw.rect(self.game.screen, 'red', (i[0] * 100, i[1] * 100, 100, 100), 2)
