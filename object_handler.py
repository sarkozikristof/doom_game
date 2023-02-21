from sprite_object import SpriteObject, AnimatedSprite


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static_sprites'
        self.animated_sprite_path = 'resources/sprites/animated_sprites'

        self.add_sprite(SpriteObject(game))
        self.add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        self.add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
