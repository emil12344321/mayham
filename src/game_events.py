"""
Game event logic

This file contains the GameEvents class which handles bulletdamage, player death,
winner state and crash penalties

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

from __future__ import annotations
from config import BULLET_DAMAGE

import pygame

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

	return should_reverse