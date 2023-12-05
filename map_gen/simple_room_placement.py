import random
import math

DIFFICULTY = 5  # 1 - 10
WIDTH = 60  # 90
HEIGHT = 60  # 160
ROOM_COUNT = 150
MIN_ROOM_WIDTH = 5
MAX_ROOM_WIDTH = 10
MIN_ROOM_HEIGHT = 5
MAX_ROOM_HEIGHT = 10


class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.connected_with = []
        self.is_spawn_room = False
        self.difficulty = DIFFICULTY


class Generate:
    def __init__(self):
        self.MAP = []
        self.ROOMS = []
        self.CONNECTED_ROOMS = []

    def get_map(self):
        self.generate_map_boundaries()
        self.generate_base_map()
        self.connect_rooms()

        return self.MAP

    def connect_rooms(self):
        if len(self.ROOMS) <= 1:
            return

        for room in self.ROOMS:
            if room in self.CONNECTED_ROOMS:
                continue
            closest_room = self.find_the_closest_room(room)
            base_mid = self.find_room_middle_point(room)
            closest_mid = self.find_room_middle_point(closest_room)
            distance_x, distance_y = self.get_distance(base_mid, closest_mid)

            self.connect_middle_points(base_mid, distance_x, distance_y)
            self.add_rooms_to_connected_rooms_list(room, closest_room)

    def add_rooms_to_connected_rooms_list(self, base_room, closest_room):
        if base_room not in self.CONNECTED_ROOMS:
            self.CONNECTED_ROOMS.append(base_room)
        if closest_room not in self.CONNECTED_ROOMS:
            self.CONNECTED_ROOMS.append(closest_room)

    @staticmethod
    def get_distance(base_mid, closest_mid):
        dist_x = base_mid[0] - closest_mid[0]
        dist_y = base_mid[1] - closest_mid[1]
        return dist_x, dist_y

    def connect_middle_points(self, base_mid, distance_x, distance_y):
        b_x, b_y = base_mid
        start_x = b_x
        start_y = b_y
        self.connect_horizontally(start_x, start_y, distance_x)

        start_x = b_x - distance_x
        start_y = b_y
        self.connect_vertically(start_x, start_y, distance_y)

    def connect_horizontally(self, start_x, start_y, distance_x):
        if distance_x > 0:
            for step in range(distance_x):
                self.MAP[start_x - step][start_y] = False
        else:
            for step in range(0, distance_x, -1):
                self.MAP[start_x - step][start_y] = False

    def connect_vertically(self, start_x, start_y, distance_y):
        if distance_y > 0:
            for step in range(distance_y):
                self.MAP[start_x][start_y - step] = False
        else:
            for step in range(0, distance_y, -1):
                self.MAP[start_x][start_y - step] = False

    @staticmethod
    def find_room_middle_point(room: Room):
        middle_x = int(room.x + room.width / 2)
        middle_y = int(room.y + room.height / 2)

        return middle_x, middle_y

    def find_the_closest_room(self, room: Room) -> Room:
        closest_distance = float('inf')
        closest_room = None

        searching_rooms = self.CONNECTED_ROOMS
        if not self.CONNECTED_ROOMS:
            searching_rooms = self.ROOMS

        for other_room in searching_rooms:
            if other_room != room:
                distance = self.calculate_distance(room, other_room)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_room = other_room

        return closest_room

    @staticmethod
    def calculate_distance(room1: Room, room2: Room):
        center1_x = room1.x + (room1.width // 2)
        center1_y = room1.y + (room1.height // 2)
        center2_x = room2.x + (room2.width // 2)
        center2_y = room2.y + (room2.height // 2)

        return math.sqrt((center1_x - center2_x) ** 2 + (center1_y - center2_y) ** 2)

    def generate_base_map(self):
        try_count = 0
        while len(self.ROOMS) != ROOM_COUNT and try_count < 500:
            print(try_count)
            room = self.get_room()
            if self.is_room_good_position(room):
                self.place_room(room)
                self.ROOMS.append(room)
            try_count += 1

    def place_room(self, room: Room):
        for width_step in range(room.width):
            for height_step in range(room.height):
                self.MAP[room.x + width_step][room.y + height_step] = False

    def is_room_good_position(self, room: Room) -> bool:
        if not self.is_out_of_map(room) and not self.is_overlapping_other_room(room):
            return True
        return False

    @staticmethod
    def is_out_of_map(room: Room) -> bool:
        if room.x + room.width >= WIDTH:
            return True
        if room.y + room.height >= HEIGHT:
            return True
        return False

    def is_overlapping_other_room(self, room: Room) -> bool:
        for width_step in range(-1, room.width + 1):
            for height_step in range(-1, room.height + 1):
                if not self.MAP[room.x + width_step][room.y + height_step]:
                    return True
        return False

    @staticmethod
    def get_room() -> Room:
        width = random.randint(MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
        height = random.randint(MIN_ROOM_HEIGHT, MAX_ROOM_HEIGHT)
        x = random.randint(1, WIDTH - width - 1)
        y = random.randint(1, HEIGHT - height - 1)

        return Room(x, y, width, height)

    def generate_map_boundaries(self) -> None:
        for col in range(WIDTH):
            row_ = []
            for row in range(HEIGHT):
                row_.append(1)
            self.MAP.append(row_)

    def is_there_a_one_connection_room(self) -> bool:
        for room in self.ROOMS:
            if len(room.connected_with) == 1:
                return True
        return False

    def get_one_connection_room(self) -> Room:
        for room in self.ROOMS:
            if len(room.connected_with) == 1:
                return room
