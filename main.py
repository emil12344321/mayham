"""
Base of the code project
This is the file to run for the project to run
The file has the main loop of the game

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

"""
TODO list
make sure all functions and methods have type hints and doccstrings
clean up duplicate code from merges and unused code
check game feel against requirements, is accelerations implemented correctly?
add needs object and visual health + fuel
"""


import pygame
from src.player import Player1, Player2
from config import FPS, HEIGHT, TITLE, WIDTH

from src.gui import NeedsDisplay, create_center_obstacle, create_fuelcan

##from src.game_events import reverse_ships_if_edge_hit
from src.objects import Ship, Bullet



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
    player2 = Player2(WIDTH * 3 // 4, HEIGHT *3 // 4)
    needs_display = NeedsDisplay(player1, player2)

    players = pygame.sprite.Group()
    players.add(player1, player2)

    obstacles = pygame.sprite.Group()
    obstacles.add(obstacle)

    bullets = pygame.sprite.Group()

    fuel_cans = pygame.sprite.Group()


    all_sprites = pygame.sprite.Group()
    all_sprites.add(obstacle, player1, player2, fuel_cans)

    time_from_fuel_spawn = pygame.time.get_ticks()
    fuel_spawn_time = 10000

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ## make obstacle
        

        ## should probably be player1.update(keys) and player2.... 
        keys = pygame.key.get_pressed()

        players.update(keys, obstacles, players, bullets, fuel_cans)
        bullets.update(players, obstacles)

        current_time = pygame.time.get_ticks()

        if len(fuel_cans) == 0 and current_time - time_from_fuel_spawn > fuel_spawn_time:
            fuel = create_fuelcan()
            fuel_cans.add(fuel)
            all_sprites.add(fuel)
            time_from_fuel_spawn = current_time

        all_sprites.add(bullets)


        

        screen.fill("black")
        all_sprites.draw(screen)

        needs_display.draw(screen)
        

        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    # run game
    gameloop()

