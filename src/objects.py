""" 
This file has all objects of the game and the class system for them


All objects are sublasses of the base class pygame.sprite.sprite
this class has these properties:

sprite.alive -> checks which group it belongs to
sprite.remove -> removes from group
sprite.update -> updates behaviour
sprite.add -> adds to group
sprite.kill -> removes from all groups
"""

import pygame



class Ship(pygame.sprite.Sprite):

    # constuctor, pass in x and y coordinates
    def __init__(self, width, height):
        ## call parent constructor
        pygame.sprite.Sprite.__init__(self)