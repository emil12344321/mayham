
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



class Ship(pygame.sprite.Sprite):

    # constructor, pass in x and y coordinates
    def __init__(self, x: int, y: int, speed_x: int = 3, size: tuple[int, int] = (40, 20)):
        # Call parent constructor.
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

