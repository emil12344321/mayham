
"""
This file has all objects of the game and the class system for them


All objects are sublasses of the base class pygame.sprite.sprite
this class has these properties:

sprite.alive -> checks which group it belongs to
sprite.remove -> removes from group
sprite.update -> updates behaviour
sprite.add -> adds to group
sprite.kill -> removes from all groups

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

import pygame
import math
from config import WIDTH, HEIGHT, BULLETSPEED

class Obstacle(pygame.sprite.Sprite):
    """A static rectangular obstacle that ships can collide with."""

    def __init__(self, x: int, y: int, size: tuple[int, int], color: tuple[int, int, int]):
        super().__init__()

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the obstacle on screen."""
        screen.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    """
    The bullet class for the game
    Initializes the bullet and updates it
    """

    def __init__(self, x: float, y: float, angle: float, owner: pygame.sprite.Sprite, radius: int = 4):
        super().__init__()

        self.x = x
        self.y = y
        self.angle = angle
        self.owner = owner
        self.speed = BULLETSPEED
        self.radius = radius

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "orange", (self.radius, self.radius), self.radius)

        self.rect = self.image.get_rect(center=(round(self.x), round(self.y)))

        radians = math.radians(self.angle)
        self.vx = -math.sin(radians) * self.speed
        self.vy = -math.cos(radians) * self.speed

    def update(self, players, obstacles: pygame.sprite.Group) -> None:
        """
        Handles bullet collision with obstacles and the player
        """
        self.x += self.vx
        self.y += self.vy

        self.rect.center = (round(self.x), round(self.y))


        # collision
        for player in players:
            if player != self.owner and pygame.sprite.collide_circle(self, player):
                from src.game_events import bullet_hit_player
                bullet_hit_player(self, player)  # reduserer needs.health

        ## outside boundaries
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

        if pygame.sprite.spritecollideany(self, obstacles):
            self.kill()

class Fuel(pygame.sprite.Sprite):
    """
    Class for fuel cans
    Spawn in random places at the map and can be picked up by one of the players
    The Fuel can is represented by a red box
    """
    def __init__(self, x: int, y: int, size: tuple[int, int], color: tuple[int, int, int]):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen: pygame.Surface) -> None:
            """Draw the Fuel on screen."""
            screen.blit(self.image, self.rect)



class Ship(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, speed_x: int = 3, size: tuple[int, int] = (40, 20)):
        super().__init__()


        ## constants of player
        ###pos
        self.x = x
        self.y = y

        ### vx, vy for velocity in direction
        self.vx = 0.0
        self.vy = 0.0

        self.angle = 0.0

        self.original_image = pygame.Surface(size, pygame.SRCALPHA)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(round(self.x), round(self.y)))

    def update_rect(self) -> None:
        self.rect = self.image.get_rect(center=(round(self.x), round(self.y)))


    def move(self) -> None:
        self.x += self.vx
        self.y += self.vy
        self.update_rect()


