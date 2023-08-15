import random

WIDTH = 64
HEIGHT = 64
ROOM_COUNT = 4
MIN_ROOM_WIDTH = 4
MAX_ROOM_WIDTH = 10
MIN_ROOM_HEIGHT = 4
MAX_ROOM_HEIGHT = 10


class Generate:
    MAP = []

    def generate(self):
        self._make_map()
        for _ in range(ROOM_COUNT):
            room = self._get_a_random_room()
            self._place_a_room(room)

        return self.MAP

    def _make_map(self):
        for row in range(HEIGHT):
            _row = []
            for col in range(WIDTH):
                if col == 0 or col == WIDTH - 1 or row == 0 or row == HEIGHT - 1:
                    _row.append(1)
                else:
                    _row.append(False)
            self.MAP.append(_row)

    def _get_a_random_room(self):
        room_start_x_pos = random.randint(0, WIDTH - MIN_ROOM_WIDTH)

        room_start_y_pos = random.randint(0, HEIGHT - MIN_ROOM_HEIGHT)

        room_width = random.randint(MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
        room_height = random.randint(MAX_ROOM_HEIGHT, MAX_ROOM_WIDTH)

        room = room_start_x_pos, room_start_y_pos, room_width, room_height

        if self._check_room_placement(room):
            return room
        else:
            self._get_a_random_room()

    @staticmethod
    def _check_room_placement(room):
        # checking if in boundaries
        if room[0] + room[2] > WIDTH and room[1] + room[3] > HEIGHT:
            return False
        return True

    def _place_a_room(self, room):
        for i in range(room[2]):
            for j in range(room[3]):
                self.MAP[room[0] + i][room[1] + j] = 1


mini_map = Generate().generate()
