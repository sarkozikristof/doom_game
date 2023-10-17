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
            if not room.is_spawn_room:
                self.spawn(room)

    def spawn(self, room):
        difficulty = room.difficulty * random.random() * 2

        if difficulty < 1:
            return
        elif 1 <= difficulty < 2:
            self.spawn_soldier(room)
        elif 2 <= difficulty < 5:
            self.spawn_soldier(room)
            self.spawn_soldier(room)
        elif 5 <= difficulty < 7:
            self.spawn_caco_demon(room)
            self.spawn_soldier(room)
        elif 7 <= difficulty < 9:
            self.spawn_caco_demon(room)
            self.spawn_caco_demon(room)
        else:
            self.spawn_cyber_demon(room)

    def spawn_soldier(self, room):
        position = self.get_random_spawn_position(room)
        self.add_npc(SoldierNPC(game=self.game,
                                pos=position))

    def spawn_caco_demon(self, room):
        position = self.get_random_spawn_position(room)
        self.add_npc(CacoDemonNPC(game=self.game,
                                  pos=position))

    def spawn_cyber_demon(self, room):
        position = self.get_random_spawn_position(room)
        self.add_npc(CyberDemonNPC(game=self.game,
                                   pos=position))

    @staticmethod
    def get_random_spawn_position(room):
        x_min_pos = room.x + 1
        x_max_pos = room.x + room.width - 1

        y_min_pos = room.y + 1
        y_max_pos = room.y + room.height - 1

        x_pos = random.randint(x_min_pos, x_max_pos)
        y_pos = random.randint(y_min_pos, y_max_pos)

        return y_pos, x_pos

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)
