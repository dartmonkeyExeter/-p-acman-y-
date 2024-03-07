# pac-man

import pygame, math

pygame.init()
clock = pygame.time.Clock()
fps = 75
size = [560, 640]
screen = pygame.display.set_mode(size)

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
            if grid.grid[int((self.y + self.radius) / 20)][int(self.x / 20)] == "#":
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

    def eat_check(self):
        current_array = list(grid.grid[int(self.y / 20)])  # Convert string to list
        if current_array[int(self.x / 20)] == ".":
            current_array[int(self.x / 20)] = " "
        if current_array[int(self.x / 20)] == "*":
            current_array[int(self.x / 20)] = " "
        grid.grid[int(self.y / 20)] = "".join(current_array)  # Convert list back to string

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
        self.eat_check()
        self.animation()

class Ghost:
    def __init__(self, color):
        self.x = 50
        self.y = 50
        self.direction = "right"
        self.speed = 2.4
        self.color = color
        self.radius = 20

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.radius * 2, self.radius * 2))

    def move(self):
        if self.direction == "right":
            self.x += self.speed
        if self.direction == "left":
            self.x -= self.speed
        if self.direction == "up":
            self.y -= self.speed
        if self.direction == "down":
            self.y += self.speed

    def update(self):
        self.draw()
        self.move()

pacman = Pacman()

blinky = Ghost((255, 0, 0))
pinky = Ghost((255, 184, 255))
inky = Ghost((0, 255, 255))
clyde = Ghost((255, 184, 255))

ghosts = [blinky, pinky, inky, clyde]

grid = Grid()

running = True

while running:
    screen.fill((0, 0, 0))
    
    pacman.update()
    for ghost in ghosts:
        ghost.update()
    grid.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            current_array = (int(pacman.x / 20), int(pacman.y / 20))
            if event.key == pygame.K_LEFT:
                pacman.direction = "left"
                pacman.x = current_array[0] * 20 + 10
                pacman.y = current_array[1] * 20 + 10
            if event.key == pygame.K_RIGHT:
                pacman.direction = "right"
                pacman.x = current_array[0] * 20 + 10
                pacman.y = current_array[1] * 20 + 10
            if event.key == pygame.K_UP:
                pacman.direction = "up"
                pacman.x = current_array[0] * 20 + 10
                pacman.y = current_array[1] * 20 + 10
            if event.key == pygame.K_DOWN:
                pacman.direction = "down"
                pacman.x = current_array[0] * 20 + 10
                pacman.y = current_array[1] * 20 + 10

    pygame.display.flip()
    clock.tick(fps)
