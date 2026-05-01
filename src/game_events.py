"""
Game event logic

This file contains the GameEvents class which handles bulletdamage, player death,
winner state and crash penalties

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

from __future__ import annotations
from config import BULLET_DAMAGE

import pygame

<<<<<<< HEAD
game_winner_player = None
game_winner_time = None
player_scores = {
    "Player1": 0,
    "Player2": 0,
}
=======
class GameEvents:
	"""Handle shared gameplay events
	
	Damage, death, winning
	"""

	def __init__(self) -> None:
		"""Create a game event handler, no winner at the start"""
		self.game_winner_player = None
		self.game_winner_time = None

	def bullet_hit_player(self, bullet, player) -> None:
		"""Updates the player health when hit by a bullet"""
		player.needs.health = max(0, player.needs.health - BULLET_DAMAGE)
		bullet.kill()

		if player.needs.health == 0 and player.is_alive:
			self.player_died(player, bullet.owner)

	def player_died(self, player, killer) -> None:
		"""Mark a player as dead and pass the killer to the winner handler."""
		player.is_alive = False
		player.kill()
		self.game_winner(killer)

	def get_game_winner(self):
		"""Return the winner if the game has ended."""
		return self.game_winner_player

	def game_winner(self, winner) -> None:
		"""Store the winner and when the game ended."""
		global game_winner_player, game_winner_time

		game_winner_player = winner
		game_winner_time = pygame.time.get_ticks()

	def get_game_winner_time(self):
		"""Return when the winner was decided."""
		return self.game_winner_time

	def reset_game_winner(self) -> None:
		"""Clear winner state before a new game starts."""
		global game_winner_player, game_winner_time

		game_winner_player = None
		game_winner_time = None


>>>>>>> origin/2player


def reverse_ship_if_obstacle_hit(ships: pygame.sprite.Group, obstacle: pygame.sprite.Sprite) -> bool:
	"""Reverse only ships that collide with the obstacle.

	Returns True if at least one ship changed direction this frame.
	"""
	hit_any_ship = False

	for ship in ships:
		if not hasattr(ship, "rect"):
			continue
		if not hasattr(ship, "reverse_direction"):
			continue
		if not hasattr(obstacle, "rect"):
			continue

		if ship.rect.colliderect(obstacle.rect):
			hit_any_ship = True

			# Push ship outside the obstacle before reversing to avoid oscillation.
			if hasattr(ship, "speed_x") and ship.speed_x >= 0:
				ship.rect.right = obstacle.rect.left
			else:
				ship.rect.left = obstacle.rect.right

			ship.reverse_direction()

	return hit_any_ship


def reverse_ships_if_edge_hit(ships: pygame.sprite.Group, screen_width: int) -> bool:
	"""Reverse all ships when any ship touches a horizontal edge.

	Returns True if a direction change was applied this frame.
	"""
	should_reverse = any(
		hasattr(ship, "hits_screen_edge") and ship.hits_screen_edge(screen_width)
		for ship in ships
	)

	if should_reverse:
		for ship in ships:
			if hasattr(ship, "reverse_direction"):
				ship.reverse_direction()

<<<<<<< HEAD
	return should_reverse


def bullet_hit_player(bullet, player) -> None:
    """bullet give damage"""
    from config import BULLET_DAMAGE

    player.needs.health = max(0, player.needs.health - BULLET_DAMAGE)
    bullet.kill()

    if player.needs.health == 0 and player.is_alive:
        player_died(player, bullet.owner)


def wall_or_obstacle_damage(player, killer) -> None:
    """Damage a player after hitting a wall or obstacle."""
    from config import WALL_DAMAGE

    player.needs.health = max(0, player.needs.health - WALL_DAMAGE)

    if player.needs.health == 0 and player.is_alive:
        player_died(player, killer)


def player_died(player, killer) -> None:
    """Mark a player as dead and pass the killer to the winner handler."""
    player.is_alive = False
    player.kill()
    game_winner(killer)


def game_winner(winner) -> None:
    """Store the winner, update score and when the game ended."""
    global game_winner_player, game_winner_time

    if game_winner_player is not None:
        return

    game_winner_player = winner
    game_winner_time = pygame.time.get_ticks()

    winner_name = winner.__class__.__name__
    if winner_name in player_scores:
        player_scores[winner_name] += 1


def get_game_winner():
    """Return the winner if the game has ended."""
    return game_winner_player


def get_game_winner_time():
    """Return when the winner was decided."""
    return game_winner_time


def get_scores():
    """Return a copy of the current player scores."""
    return player_scores.copy()


def reset_game_winner() -> None:
    """Clear winner state before a new game starts."""
    global game_winner_player, game_winner_time

    game_winner_player = None
    game_winner_time = None
=======
	return should_reverse
>>>>>>> origin/2player
