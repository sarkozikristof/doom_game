import random
import math

WIDTH = 80  # 90
HEIGHT = 150  # 160
ROOM_COUNT = 4
MIN_ROOM_WIDTH = 10
MAX_ROOM_WIDTH = 20
MIN_ROOM_HEIGHT = 10
MAX_ROOM_HEIGHT = 20


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

    def get_map(self):
        self.generate_map_boundaries()
        self.generate_base_map()
        self.connect_rooms()

        return self.MAP

    def connect_rooms(self):
        # find the closest room to the input
        base_room = self.ROOMS[0]
        closest_room = self.find_the_closest_room(base_room)
        # find the two points (middle of the room)
        # base_middle, closest_middle = self.find_rooms_middle_point(base_room, closest_room)
        # connect the two points

    @staticmethod
    def find_rooms_middle_point(base_room: Room, closest_room: Room):
        pass

    def find_the_closest_room(self, room: Room) -> Room:
        closest_distance = float('inf')  # Initialize with a large value
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

    def create_horizontal_corridor(self):
        pass

    def create_vertical_corridor(self):
        pass

    def generate_base_map(self):
        while len(self.ROOMS) != ROOM_COUNT:
            room = self.get_room()
            if self.is_room_good_position(room):
                self.place_room(room)
                self.ROOMS.append(room)

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


mini_map = Generate().get_map()
