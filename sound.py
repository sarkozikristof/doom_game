import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + '/shotgun.mp3')
        self.theme = pg.mixer.Sound(self.path + '/theme.ogg')
        self.theme.set_volume(0.2)

        # NPC
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_pain.set_volume(0.2)
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')

        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
