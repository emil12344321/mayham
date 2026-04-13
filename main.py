""" 
Base of the code project
This is the file to run for the project to run
The file has the main loop of the game

"""

import pygame

from config import FPS, HEIGHT, TITLE, WIDTH
##from src.game_events import reverse_ships_if_edge_hit
from src.objects import Ship
from src.player import Player


def gameloop() -> None:
    """ Run the main game loop.

    The loop sets up pygame, loads assets, processes events, updates screen and renders the screen
    """

    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    player = Player(WIDTH // 2, HEIGHT // 2)
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        ## should probably be player1.update(keys) and player2.... 
        keys = pygame.key.get_pressed()

        player.update(keys)

        

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    # run game
    gameloop()

