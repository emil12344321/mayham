"""
Base of the code project
This is the file to run for the project to run
The file has the main loop of the game

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

import pygame
from src.player import Player1, Player2
from config import FPS, HEIGHT, TITLE, WIDTH
from src.gui import create_center_obstacle, draw_frame
##from src.game_events import reverse_ships_if_edge_hit
from src.objects import Ship


def gameloop() -> None:
    """ Run the main game loop.

    The loop sets up pygame, loads assets, processes events, updates screen and renders the screen
    """

    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    obstacle = create_center_obstacle()

    player1 = Player1(WIDTH // 4, HEIGHT // 4)
    player2 = Player2(WIDTH // 3/4, HEIGHT // 3/4)
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ## make obstacle
        
        ## should probably be player1.update(keys) and player2.... 
        keys = pygame.key.get_pressed()

        player1.update(keys, obstacle)
        player2.update(keys, obstacle)


        

        screen.fill("black")
        obstacle.draw(screen)
        player1.draw(screen)
        player2.draw(screen)
        

        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    # run game
    gameloop()
