# pac-man

import pygame, math, random, pacmanclass, gridclass, ghostclass, copy

pygame.init()
clock = pygame.time.Clock()
fps = 75
size = [560, 640]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pacman!!!!")

level = 1

pacman = pacmanclass.Pacman()

blinky = ghostclass.Ghost((255, 0, 0), (11*20)+4, (12*20)+4, "right")
pinky = ghostclass.Ghost((255, 184, 255), (16*20)+4, (12*20)+4, "left")
inky = ghostclass.Ghost((0, 255, 255), (11*20)+4, (14*20)+4, "right")
clyde = ghostclass.Ghost((255, 184, 82), (16*20)+4, (14*20)+4, "left")

ghosts = [blinky, pinky, inky, clyde]

grid = gridclass.Grid()

def update_all():
    global level
    dots_left = grid.dots_left()
    if dots_left == 0:
        level += 1
        pacman.x = 280
        pacman.y = 330
        for ghost in ghosts:
            ghost.x = ghost.start_pos[0] * 20
            ghost.y = ghost.start_pos[1] * 20
        grid.grid = copy.deepcopy(grid.copygrid)
    pacman.move()
    pacman.clamping(grid)
    pacman.eat_check(ghosts, grid, fps)
    pacman.power_pellet_timer(ghosts)
    pacman.animation()
    
    pacman.draw(screen)

    grid.draw(screen)

    for ghost in ghosts:
        ghost.behaviours(pacman, grid)
        ghost.move()
        ghost.draw(screen)

running = True

while running:
    screen.fill((0, 0, 0))

    update_all()

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
