import random

WIDTH = 64
HEIGHT = 64
MAX_ROOMS = 10
MIN_ROOM_WIDTH = 4
MAX_ROOM_WIDTH = 10
MIN_ROOM_HEIGHT = 4
MAX_ROOM_HEIGHT = 10


class Generator:
    def __init__(self):
        self.map = []

    def generate(self):
        # get map boundaries
        self._get_map()
        # get a room by its size and position
        # check if position in map
        # check if position not on another map
        # place room in the map
        # do this until reaching max room count
        return self.map

    def _get_map(self):
        for row in range(HEIGHT):
            _row = []
            for col in range(WIDTH):
                if col == 0 or col == WIDTH - 1 or row == 0 or row == HEIGHT - 1:
                    _row.append(1)
                    continue
                _row.append(False)
            self.map.append(_row)

    def _get_a_random_room(self):
        room_start_x_pos = random.randint(0, WIDTH - MIN_ROOM_WIDTH)
        room_start_y_pos = random.randint(0, HEIGHT - MIN_ROOM_HEIGHT)

        room_width = random.randint(MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
        room_height = random.randint(MAX_ROOM_HEIGHT, MAX_ROOM_WIDTH)

        if self._is_not_overlapping_or_not_in_map_boundaries(room_start_x_pos, room_start_y_pos,
                                                             room_width, room_height):
            return room_start_x_pos, room_start_y_pos, room_width, room_height

        self._get_a_random_room()

    @staticmethod
    def _is_not_overlapping_or_not_in_map_boundaries(room_x, room_y, room_w, room_h):
        if room_x + room_w > WIDTH or room_y + room_h:
            return False
        return True

    def _place_room_in_map(self):
        for i in range(MAX_ROOMS):
            room = self._get_a_random_room()
            room_x, room_y = room[0], room[1]
            room_w, room_h = room[2], room[3]


MAP = Generator().generate()
print(MAP)
