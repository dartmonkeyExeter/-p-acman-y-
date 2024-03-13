import pygame

class Fruit:
    def __init__(self, sprite, fruit_score):
        self.sprite = sprite
        self.x = 280
        self.y = 330
        self.eaten = False
        self.initialise_timer = 10
        self.fruit_score = fruit_score

    def draw(self, screen, amount_of_fruits):
        if not self.eaten:
            screen.blit(self.sprite, (self.x - 20, self.y))
            self.initialise_timer -= 0.01
        if self.eaten:
            self.x = 300 + (amount_of_fruits * 20 * 2)
            self.y = 600 
    
    def eat_check(self, pacman):
        pacman_position_arr = [int(pacman.x) / 20, int(pacman.y) / 20]
        fruit_position_arr = [int(self.x) / 20, int(self.y) / 20]

        if pacman_position_arr == fruit_position_arr:
            self.eaten = True
            pacman.score += self.fruit_score
