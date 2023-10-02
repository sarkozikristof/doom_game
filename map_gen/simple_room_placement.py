import random
import math

WIDTH = 50  # 90
HEIGHT = 50  # 160
ROOM_COUNT = 2
MIN_ROOM_WIDTH = 5
MAX_ROOM_WIDTH = 5
MIN_ROOM_HEIGHT = 5
MAX_ROOM_HEIGHT = 5


class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.connected_with = []


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

        # find the closest room to the input
        base_room = self.ROOMS[0]
        closest_room = self.find_the_closest_room(base_room)
        base_mid = self.find_room_middle_point(base_room)
        closest_mid = self.find_room_middle_point(closest_room)

        distance_x, distance_y = self.get_distance(base_mid, closest_mid)

        self.connect_middle_points(base_mid, closest_mid, distance_x, distance_y)
        # connect the two points

    @staticmethod
    def get_distance(base_mid, closest_mid):
        dist_x = base_mid[0] - closest_mid[0]
        dist_y = base_mid[1] - closest_mid[1]
        print(f'distance: {dist_x}, {dist_y}')
        return dist_x, dist_y

    def connect_middle_points(self, base_mid, closest_mid, distance_x, distance_y):
        b_x, b_y = base_mid
        c_x, c_y = closest_mid
        start_x = b_x
        start_y = b_y
        self.connect_horizontally(start_x, start_y, distance_x)

    def connect_horizontally(self, start_x, start_y, distance_x):
        if distance_x > 0:
            for step in range(distance_x):
                self.MAP[start_y][start_x - step - 1] = False
        else:
            for step in range(0, distance_x, -1):
                self.MAP[start_y][start_x - step + 1] = False

    def connect_vertically(self, start_x, start_y, distance):
        pass

    @staticmethod
    def find_room_middle_point(room: Room):
        middle_x = int(room.x + room.width / 2)
        middle_y = int(room.y + room.height / 2)

        return middle_x, middle_y

    def find_the_closest_room(self, room: Room) -> Room:
        closest_distance = float('inf')
        closest_room = None

        for other_room in self.ROOMS:
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
        while len(self.ROOMS) != ROOM_COUNT:
            room = self.get_room()
            if self.is_room_good_position(room):
                self.place_room(room)
                self.ROOMS.append(room)

    def place_room(self, room: Room):
        for width_step in range(room.width):
            for height_step in range(room.height):
                self.MAP[room.y + height_step][room.x + width_step] = False

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


mini_map = Generate().get_map()
