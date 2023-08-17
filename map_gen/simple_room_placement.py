import random

WIDTH = 10
HEIGHT = 10
ROOM_COUNT = 1
MIN_ROOM_WIDTH = 4
MAX_ROOM_WIDTH = 4
MIN_ROOM_HEIGHT = 4
MAX_ROOM_HEIGHT = 4


class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Generate:
    MAP = []
    ROOMS = []

    def __init__(self):
        self._generate_base_map_boundaries()

    def generate(self):
        while len(self.ROOMS) != ROOM_COUNT:
            room = self._get_room()
            if self._is_correct_position(room):
                self._place_room(room)
                self.ROOMS.append(room)

        return self.MAP

    @staticmethod
    def _get_room():
        r_w = random.randint(MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
        r_h = random.randint(MIN_ROOM_HEIGHT, MAX_ROOM_HEIGHT)
        r_x = random.randint(1, WIDTH - r_w - 1)
        r_y = random.randint(1, HEIGHT - r_h - 1)

        return Room(r_x, r_y, r_w, r_h)

    def _is_correct_position(self, room):
        if self._is_out_of_map_boundaries(room) and self._is_overlapping_other_room(room):
            return True
        return False

    @staticmethod
    def _is_out_of_map_boundaries(room):
        if room.x + room.width > WIDTH:
            return False
        if room.y + room.height > HEIGHT:
            return False
        return True

    def _is_overlapping_other_room(self, room):
        for width_step in range(room.width):
            for height_step in range(room.height):
                if self.MAP[room.x + width_step][room.y + height_step] == 1:
                    return False
        return True

    def _place_room(self, room):
        for width_step in range(room.width):
            for height_step in range(room.height):
                self.MAP[room.x + width_step][room.y + height_step] = False

    def _generate_base_map_boundaries(self):
        for col in range(WIDTH):
            _row = []
            for row in range(HEIGHT):
                _row.append(1)
            self.MAP.append(_row)


mini_map = Generate().generate()
