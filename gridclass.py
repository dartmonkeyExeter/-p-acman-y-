import pygame

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
        
        self.copygrid = [
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
    def draw(self, screen):
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

    def dots_left(self):
        dots = 0
        for row in self.grid:
            for char in row:
                if char == "." or char == "*":
                    dots += 1
        return dots

grid = Grid()
dots_left = grid.dots_left()