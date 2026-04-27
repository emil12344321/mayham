""" 
This file has the player script of the game

"""



## should have :
"""
player pos (self.x and self.y)
velocity
angle (self.angle)
ship image (self.image)
hitbox (self.x, self.y)
update()
draw()
"""

        

import math
import pygame

from config import GRAVITY, STARTING_FUEL, THRUST, WIDTH, HEIGHT
from src.objects import Ship, Obstacle



class Player1(Ship):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x,y, (40,40))


        #pplayer constants
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
        pygame.draw.polygon(surface, "blue", [(20,0), (5,35),(35,35)])
        pygame.draw.rect(surface, "white", (17, 10, 6, 6))
        return surface

    def update(self, keys, obstacle: Obstacle) -> None:
        #rotation
        old_x = self.x
        old_y = self.y

        if keys[pygame.K_LEFT]:
            self.angle += self.rotation_speed

        if keys[pygame.K_RIGHT]:
            self.angle -= self.rotation_speed

        #thrust // add fuel later
        if keys[pygame.K_UP]:
            radians = math.radians(self.angle)
            self.vx -= (math.sin(radians) * self.thrust)/3
            self.vy -= math.cos(radians) * self.thrust

        # gravity
        self.vy += self.gravity


        """ To do:
        player should have a function shoot, which takes pygame.K_SPACE and uses it to create objects
        these objects should be able to interact with the player to do damage
        before this is done gui for health and fuel should be added aswell as the obstacle
        lastly player 2 should be added
        """

        #movement
        self.move()

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


    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

class Player2(Ship):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x,y, (40,40))


        #pplayer constants
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
        pygame.draw.polygon(surface, "red", [(20,0), (5,35),(35,35)])
        pygame.draw.rect(surface, "white", (17, 10, 6, 6))
        return surface

    def update(self, keys, obstacle: Obstacle) -> None:
        #rotation
        old_x = self.x
        old_y = self.y

        if keys[pygame.K_a]:
            self.angle += self.rotation_speed

        if keys[pygame.K_d]:
            self.angle -= self.rotation_speed

        #thrust // add fuel later
        if keys[pygame.K_w]:
            radians = math.radians(self.angle)
            self.vx -= (math.sin(radians) * self.thrust)/3
            self.vy -= math.cos(radians) * self.thrust

        # gravity
        self.vy += self.gravity


        """ To do:
        player should have a function shoot, which takes pygame.K_SPACE and uses it to create objects
        these objects should be able to interact with the player to do damage
        before this is done gui for health and fuel should be added aswell as the obstacle
        lastly player 2 should be added
        """

        #movement
        self.move()

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


    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)


