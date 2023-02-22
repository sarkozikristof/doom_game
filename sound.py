import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound'
        self.shotgun = pg.mixer.Sound(self.path + '/shotgun.mp3')
        self.theme = pg.mixer.Sound(self.path + '/theme.ogg')
