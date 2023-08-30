import random
import math

WIDTH = 80  # 90
HEIGHT = 150  # 160
ROOM_COUNT = 20
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
        self.connected_rooms = []


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

    def _ensure_indirect_reachability(self):
        room_to_neighbors = {room: [] for room in self.ROOMS}

        for room in self.ROOMS:
            for connected_room in room.connected_rooms:
                room_to_neighbors[room].append(connected_room)
                room_to_neighbors[connected_room].append(room)

        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for neighbor in room_to_neighbors[room]:
                dfs(neighbor)

        # Start DFS from a randomly chosen room
        start_room = random.choice(self.ROOMS)
        dfs(start_room)

        # Ensure all rooms are visited
        for room in self.ROOMS:
            if room not in visited:
                self._connect_two_rooms(room, random.choice(room_to_neighbors[room]))
                dfs(room)

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
        self.ROOMS.sort(key=lambda room: (room.x, room.y))

        for i in range(len(self.ROOMS)):
            current_room = self.ROOMS[i]

            nearest_rooms = self._find_nearest_rooms(current_room, self.ROOMS)

            for nearest_room in nearest_rooms:
                if len(current_room.connected_rooms) < 2 and len(nearest_room.connected_rooms) < 2:
                    self._connect_two_rooms(current_room, nearest_room)
                    current_room.connected_rooms.append(nearest_room)
                    nearest_room.connected_rooms.append(current_room)

        return self.MAP

    def _find_nearest_rooms(self, source_room, target_rooms):
        target_rooms = sorted(target_rooms, key=lambda room: self._calculate_distance(source_room, room))
        return target_rooms[1:3]  # Exclude the source room itself

    @staticmethod
    def _calculate_distance(room1, room2):
        return math.sqrt((room1.x - room2.x) ** 2 + (room1.y - room2.y) ** 2)

    def _connect_two_rooms(self, room1, room2):
        start_x = room1.x + room1.width // 2
        start_y = room1.y + room1.height // 2
        end_x = room2.x + room2.width // 2
        end_y = room2.y + room2.height // 2

        self._create_horizontal_corridor(start_x, end_x, start_y)
        self._create_vertical_corridor(end_x, start_y, end_y)

    def _create_horizontal_corridor(self, start_x, end_x, y):
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            self.MAP[x][y] = False

    def _create_vertical_corridor(self, x, start_y, end_y):
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            self.MAP[x][y] = False


mini_map = Generate().generate()
