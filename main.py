# pac-man

import pygame, math, random

pygame.init()
clock = pygame.time.Clock()
fps = 75
size = [560, 640]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pacman!!!!")

class Grid:
    def __init__(self):
        self.grid = [
    "############################",
    "#............##............#",
    "#*####.#####.##.#####.####*#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "     #.##### ## #####.#     ",
    "     #.##          ##.#     ",
    "     #.## ###--### ##.#     ",
    "######.## #      # ##.######",
    "      .   #      #   .        ",
    "######.## #      # ##.######",
    "     #.## ######## ##.#     ",
    "     #.##          ##.#     ",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#*..##................##..*#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]
    
        self.nodemap = [
    "############################",
    "#            ##            #",
    "# #### ##### ## ##### #### #",
    "# #### ##### ## ##### #### #",
    "#                          #",
    "# #### ## ######## ## #### #",
    "# #### ## ######## ## #### #",
    "#      ##    ##    ##      #",
    "###### ##### ## ##### ######",
    "     # ##### ## ##### #     ",
    "     # ##          ## #     ",
    "     # ## ###  ### ## #     ",
    "###### ## #      # ## ######",
    "          #      #            ",
    "###### ## #      # ## ######",
    "     # ## ######## ## #     ",
    "     # ##          ## #     ",
    "###### ## ######## ## ######",
    "###### ## ######## ## ######",
    "#            ##            #",
    "# #### ##### ## ##### #### #",
    "# #### ##### ## ##### #### #",
    "#   ##                ##   #",
    "### ## ## ######## ## ## ###",
    "### ## ## ######## ## ## ###",
    "#      ##    ##    ##      #",
    "# ########## ## ########## #",
    "# ########## ## ########## #",
    "#                          #",
    "############################"
]
    def draw(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                top_left = (x * 20, y * 20)
                top_right = (x * 20 + 20, y * 20)
                bottom_left = (x * 20, y * 20 + 20)
                bottom_right = (x * 20 + 20, y * 20 + 20) 
                if self.grid[y][x] == "#":
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if (i == 0 and j == 0) or (abs(i) == abs(j)):
                                continue
                            try:
                                if self.grid[y + i][x + j] != "#":
                                    if i == -1:
                                        pygame.draw.line(screen, (0,0,255), top_left, top_right, 2)
                                    if i == 1:
                                        pygame.draw.line(screen, (0,0,255), bottom_left, bottom_right, 2)
                                    if j == -1:
                                        pygame.draw.line(screen, (0,0,255), top_left, bottom_left, 2)
                                    if j == 1:
                                        pygame.draw.line(screen, (0,0,255), top_right, bottom_right, 2)
                            except IndexError:
                                pass
                if self.grid[y][x] == ".":
                    pygame.draw.circle(screen, (255, 255, 255), (x * 20 + 10, y * 20 + 10), 2)
                if self.grid[y][x] == "*":
                    pygame.draw.circle(screen, (255, 255, 255), (x * 20 + 10, y * 20 + 10), 5)

class Pacman:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.radius = 8
        self.color = (255, 255, 0)
        self.direction = "right"
        self.speed = 2.5
        self.direction_to_angle_dict = {"right": 0, "down": 90, "left": 180, "up": 270}
        self.animation_frame = 0
        self.animate_backwards = False
        self.moving = True
        self.power_pellet_clock = 0
        self.score = 0

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        start_angle = math.radians((-0 - self.animation_frame) + self.direction_to_angle_dict[self.direction])
        end_angle = math.radians((0 + self.animation_frame) + self.direction_to_angle_dict[self.direction])
        center = (self.x, self.y)
        vertices = [center]
        num_vertices = 30 
        angle_step = (end_angle - start_angle) / num_vertices
        for i in range(num_vertices + 1):
            angle = start_angle + i * angle_step
            x = center[0] + self.radius * math.cos(angle)
            y = center[1] + self.radius * math.sin(angle)
            vertices.append((x, y))

        pygame.draw.polygon(screen, (0, 0, 0), vertices)

    def move(self):
        if self.direction == "right":
            self.x += self.speed
        if self.direction == "left":
            self.x -= self.speed
        if self.direction == "up":
            self.y -= self.speed
        if self.direction == "down":
            self.y += self.speed

        if self.x > 560:
            self.x = 0
        if self.x < 0:
            self.x = 560

    def clamping(self):
        current_array = grid.grid[int(self.y / 20)]
        if self.direction == "right":
            if current_array[int((self.x + self.radius) / 20)] == "#":
                self.x -= self.speed
                self.moving = False
            else:
                self.moving = True
        if self.direction == "left":
            if current_array[int((self.x - self.radius) / 20)] == "#":
                self.x += self.speed
                self.moving = False
            else:
                self.moving = True
        if self.direction == "down":
            if grid.grid[int((self.y + self.radius) / 20)][int(self.x / 20)] == "#" or grid.grid[int((self.y + self.radius) / 20)][int(self.x / 20)] == "-":
                self.y -= self.speed
                self.moving = False
            else:
                self.moving = True
        if self.direction == "up":
            if grid.grid[int((self.y - self.radius) / 20)][int(self.x / 20)] == "#":
                self.y += self.speed
                self.moving = False
            else:
                self.moving = True

    def eat_check(self, ghost_list):
        current_array = list(grid.grid[int(self.y / 20)])  # Convert string to list
        ghost_positions = [(int(ghost.x / 20), int(ghost.y / 20)) for ghost in ghost_list]
        if current_array[int(self.x / 20)] == ".":
            current_array[int(self.x / 20)] = " "
            self.score += 10
        if current_array[int(self.x / 20)] == "*":
            current_array[int(self.x / 20)] = " "
            for ghost in ghost_list:
                ghost.edible = True
            self.power_pellet_clock = fps * 10
            self.score += 50
        
        grid.grid[int(self.y / 20)] = "".join(current_array)

        if ghost_positions.count((int(self.x / 20), int(self.y / 20))) > 0:
            if not ghost_list[ghost_positions.index((int(self.x / 20), int(self.y / 20)))].edible:
                self.x = 30
                self.y = 30
                self.score -= 100
                for ghost in ghost_list:
                    ghost.x = ghost.start_pos[0] * 20
                    ghost.y = ghost.start_pos[1] * 20
                    ghost.edible = False
                    ghost.path = None
            elif ghost_list[ghost_positions.index((int(self.x / 20), int(self.y / 20)))].edible:
                ghost_list[ghost_positions.index((int(self.x / 20), int(self.y / 20)))].x = ghost_list[ghost_positions.index((int(self.x / 20), int(self.y / 20)))].start_pos[0] * 20
                ghost_list[ghost_positions.index((int(self.x / 20), int(self.y / 20)))].y = ghost_list[ghost_positions.index((int(self.x / 20), int(self.y / 20)))].start_pos[1] * 20
                ghost_list[ghost_positions.index((int(self.x / 20), int(self.y / 20)))].edible = False
                ghost_list[ghost_positions.index((int(self.x / 20), int(self.y / 20)))].path = None
                self.score += 200

    def power_pellet_timer(self):
        if self.power_pellet_clock > 0:
            self.power_pellet_clock -= 1
        else:
            for ghost in ghosts:
                ghost.edible = False

    def animation(self):
        if self.moving:
            if self.animation_frame == 45:
                self.animate_backwards = True
            if self.animation_frame == 0:
                self.animate_backwards = False
            if self.animate_backwards:
                self.animation_frame -= 5
            else:
                self.animation_frame += 5

    def update(self):
        self.draw()
        self.move()
        self.clamping()
        self.eat_check(ghosts)
        self.power_pellet_timer()
        self.animation()

class Ghost:
    def __init__(self, color, x, y, starting_dir):
        self.x = x
        self.y = y
        self.direction = starting_dir
        self.speed = 2.4
        self.color = color
        self.radius = 8
        self.calculate_path = True
        self.path = []
        self.teleport_timer = 0
        self.edible = False
        self.start_pos = (int(x / 20), int(y / 20))

    def draw(self):
        if self.edible:
            pygame.draw.rect(screen, (0,0,255), (self.x, self.y, self.radius * 2, self.radius * 2))
        else: 
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.radius * 2, self.radius * 2))
    
    def BFS(self, start, end, grid):
        queue = {start: [[start]]}
        visited = {start: set()}
        all_paths = []
        while any(queue.values()):
            for ghost, path_queue in queue.copy().items():
                path = path_queue.pop(0)
                node = path[-1]
                if node == end:
                    all_paths.append(path)
                elif node not in visited[ghost]:
                    visited[ghost].add(node)
                    random.shuffle([(0, -1), (0, 1), (-1, 0), (1, 0)])
                    for adjacent in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        new_x = node[0] + adjacent[0]
                        new_y = node[1] + adjacent[1]
                        if (0 <= new_x < len(grid[0])) and (0 <= new_y < len(grid)) and grid[new_y][new_x] != "#":
                            new_path = list(path)
                            new_path.append((new_x, new_y))
                            if ghost not in queue:
                                queue[ghost] = []
                            queue[ghost].append(new_path)
        return all_paths

    def move(self):
        if self.path and self.teleport_timer == 0:
            next_node = self.path.pop(0)
            self.x = next_node[0] * 20
            self.y = next_node[1] * 20
    
    def update(self):
        if self.calculate_path and not self.edible:
            pacman_array = (int(pacman.x / 20), int(pacman.y / 20))
            ghost_array = (int(self.x / 20), int(self.y / 20))
            self.path = random.choice(self.BFS(ghost_array, pacman_array, grid.grid))
            self.calculate_path = False
        
        elif self.calculate_path and self.edible:
            pacman_array = (int(pacman.x / 20), int(pacman.y / 20))
            ghost_array = (int(self.x / 20), int(self.y / 20))
            self.path = random.choice(self.BFS(ghost_array, self.start_pos, grid.grid))
            self.calculate_path = False
        
        self.draw()
        self.move()
        self.behaviours()

    def behaviours(self):
        if random.randint(0, 100) == 0:
            self.calculate_path = True
        if self.path is None:
            self.calculate_path = True



pacman = Pacman()

blinky = Ghost((255, 0, 0), (11*20)+4, (12*20)+4, "right")
pinky = Ghost((255, 184, 255), (16*20)+4, (12*20)+4, "left")
inky = Ghost((0, 255, 255), (11*20)+4, (14*20)+4, "right")
clyde = Ghost((255, 184, 82), (16*20)+4, (14*20)+4, "left")

ghosts = [blinky, pinky, inky, clyde]

grid = Grid()

running = True

while running:
    screen.fill((0, 0, 0))

    pacman.update()
    for ghost in ghosts:
        ghost.update()
        ghost.teleport_timer += 1
        if ghost.teleport_timer == 15:
            ghost.teleport_timer = 0
    grid.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            current_array = (int(pacman.x / 20), int(pacman.y / 20))
            if event.key == pygame.K_LEFT and grid.grid[int(pacman.y / 20)][int((pacman.x - 20) / 20)] != "#":
                pacman.direction = "left"
                pacman.x = current_array[0] * 20 + 10
                pacman.y = current_array[1] * 20 + 10
            if event.key == pygame.K_RIGHT and grid.grid[int(pacman.y / 20)][int((pacman.x + 20) / 20)] != "#":
                pacman.direction = "right"
                pacman.x = current_array[0] * 20 + 10
                pacman.y = current_array[1] * 20 + 10
            if event.key == pygame.K_UP and grid.grid[int((pacman.y - 20) / 20)][int((pacman.x) / 20)] != "#":
                pacman.direction = "up"
                pacman.x = current_array[0] * 20 + 10
                pacman.y = current_array[1] * 20 + 10
            if event.key == pygame.K_DOWN and grid.grid[int((pacman.y + 20) / 20)][int(pacman.x / 20)] != "#" and grid.grid[int((pacman.y + 20) / 20)][int(pacman.x / 20)] != "-":
                pacman.direction = "down"
                pacman.x = current_array[0] * 20 + 10
                pacman.y = current_array[1] * 20 + 10

    pygame.display.flip()
    clock.tick(fps)
