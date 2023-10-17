import random

import pygame as pg

from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = self.get_starting_position()
        self.angle = PLAYER_ANGLE
        self.rel = 0
        self.shot = False

    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx -= speed_cos
            dy -= speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy -= speed_cos
        if keys[pg.K_d]:
            dx -= speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time

        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        pg.draw.circle(self.game.screen, 'green', (self.x * 10, self.y * 10), 7)
        pg.draw.line(self.game.screen, 'yellow', (self.x * 10, self.y * 10),
                     (self.x * 10 + WIDTH * math.cos(self.angle),
                      self.y * 10 + WIDTH * math.sin(self.angle)), 2)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()

        if MOUSE_BORDER_LEFT > mx or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])

        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def get_starting_position(self):

        if self.game.map.generator.is_there_a_one_connection_room():
            spawn_room = self.game.map.generator.get_one_connection_room()
        else:
            rooms = self.game.map.generator.ROOMS
            room_count = len(rooms)
            random_room_index = random.randint(0, room_count - 1)
            spawn_room = rooms[random_room_index]

        spawn_room.is_spawn_room = True

        return self.get_random_spawn_point(spawn_room)

    @staticmethod
    def get_random_spawn_point(room):
        x_min_pos = room.x + 1
        x_max_pos = room.x + room.width - 1

        y_min_pos = room.y + 1
        y_max_pos = room.y + room.height - 1

        x_pos = random.randint(x_min_pos, x_max_pos)
        y_pos = random.randint(y_min_pos, y_max_pos)

        return y_pos, x_pos
