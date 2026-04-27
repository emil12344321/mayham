""" 
This file has the player script of the game

"""

import math
import pygame

from config import GRAVITY, STARTING_FUEL, THRUST, WIDTH, HEIGHT
from src.objects import Ship, Obstacle

"""
Todo
make code more object oriented. could probably use the same 
class and some form of polymorhpism

"""


"""
Base player class, owns movement, physics, collison, rotation and drawing of player object
Player1, Player2 own controls (input) and colour
"""

class Player(Ship):
    def __init__(self, x, y, color, controls):
        super().__init__(x,y, size=(40,40))

        self.controls = controls
        self.color = color

        #player constants
        self.rotation_speed = 3
        self.thrust = THRUST
        self.gravity = GRAVITY
        self.fuel = STARTING_FUEL
        self.radius = 18

        # update player image
        self.original_image = self.create_ship_surface()
        self.image = self.original_image
        self.update_rect()


    def create_ship_surface(self) -> pygame.Surface:
        surface = pygame.Surface((40,40), pygame.SRCALPHA)
        pygame.draw.polygon(surface, self.color, [(20,0), (5,35),(35,35)])
        pygame.draw.rect(surface, "white", (17, 10, 6, 6))
        return surface
    
    def update(self, keys, obstacle: Obstacle) -> None:
        #rotation
        old_x = self.x
        old_y = self.y
            
        # gravity
        self.vy += self.gravity

        #movement
        self.move()

        #input
        self.handle_input(keys)

        # rotate playerimage
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.update_rect()

        # limits
        if self.x < 0:
            self.x = 0
            self.vx = 0

        if self.x > WIDTH:
            self.x = WIDTH
            self.vx = 0

        if self.y < 0:
            self.y = 0
            self.vy = 0

        if self.y > HEIGHT:
            self.y = HEIGHT
            self.vy = 0

        #collision
        if self.rect.colliderect(obstacle.rect):
            self.x = old_x
            self.y = old_y
            self.vx = -self.vx
            self.vy = -self.vy + 1
            self.update_rect()

    def handle_input(self, keys) -> None:
        if keys[self.controls["left"]]:
            self.angle += self.rotation_speed

        if keys[self.controls["right"]]:
            self.angle -= self.rotation_speed

        if keys[self.controls["up"]]:
            radians = math.radians(self.angle)
            self.vx -= (math.sin(radians) * self.thrust)/3
            self.vy -= math.cos(radians) * self.thrust
            # self.fuel -= 1


    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
class Player1(Player):
    def __init__(self, x: float, y: float) -> None:
        controls = {
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "up": pygame.K_UP,
            # add shoot later
        }

        super().__init__(x, y, "blue", controls)



class Player2(Player):
    def __init__(self, x: float, y: float) -> None:
        controls = {
            "left": pygame.K_a,
            "right": pygame.K_d,
            "up": pygame.K_w,
            # add shoot later
        }

        super().__init__(x, y, "red", controls)