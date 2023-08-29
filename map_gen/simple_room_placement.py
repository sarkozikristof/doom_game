import random

WIDTH = 70  # 90
HEIGHT = 70  # 160
ROOM_COUNT = 15
MIN_ROOM_WIDTH = 10
MAX_ROOM_WIDTH = 10
MIN_ROOM_HEIGHT = 10
MAX_ROOM_HEIGHT = 10


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

        self._connect_rooms_with_corridors()
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
        for width_step in range(-1, room.width + 1):
            for height_step in range(-1, room.height + 1):
                if not self.MAP[room.x + width_step][room.y + height_step]:
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

    def _connect_rooms_with_corridors(self):
        for i in range(1, len(self.ROOMS)):
            prev_room = self.ROOMS[i - 1]
            current_room = self.ROOMS[i]

            if current_room.x + current_room.width // 2 > prev_room.x + prev_room.width // 2:
                start_x = prev_room.x + prev_room.width // 2
                end_x = current_room.x + current_room.width // 2
            else:
                start_x = current_room.x + current_room.width // 2
                end_x = prev_room.x + prev_room.width // 2

            self._create_horizontal_corridor(start_x, end_x, current_room.y + current_room.height // 2)
            self._create_vertical_corridor(start_x, prev_room.y + prev_room.height // 2,
                                           current_room.y + current_room.height // 2)

        return self.MAP

    def _create_horizontal_corridor(self, start_x, end_x, y):
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            self.MAP[x][y] = False

    def _create_vertical_corridor(self, x, start_y, end_y):
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            self.MAP[x][y] = False
            

mini_map = Generate().generate()
