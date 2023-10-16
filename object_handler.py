import random
from sprite_object import SpriteObject, AnimatedSprite
from npc import SoldierNPC, CacoDemonNPC, CyberDemonNPC


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites'
        self.animated_sprite_path = 'resources/sprites/animated_sprites'

        self.add_sprite(SpriteObject(game))
        self.add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        self.add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))

        self.spawn_enemies()

    def spawn_enemies(self):
        for room in self.game.map.generator.ROOMS:
            self.spawn_in_room(room)
        print(len(self.npc_list))

    def spawn_in_room(self, room):
        for width_step in range(room.width):
            for height_step in range(room.height):
                if self.is_spawning():
                    self.spawn(room)

    @staticmethod
    def is_spawning():
        r = random.randint(0, 10)

        if r > 9:
            return True
        return False

    def spawn(self, room):
        difficulty = room.difficulty * random.randint(0, 2)

        if difficulty < 2:
            return
        elif 2 <= difficulty < 5:
            return
        elif 5 <= difficulty < 9:
            return
        else:
            return

    def spawn_soldier(self, position):
        self.add_npc(SoldierNPC(game=self.game,
                                pos=position))

    def spawn_caco_demon(self, position):
        self.add_npc(CacoDemonNPC(game=self.game,
                                  pos=position))

    def spawn_cyber_demon(self, position):
        self.add_npc(CyberDemonNPC(game=self.game,
                                   pos=position))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)
