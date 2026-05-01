"""GUI helpers for creating and drawing game visuals.

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

from __future__ import annotations

import pygame
import random

from config import HEIGHT, OBSTACLE_COLOR, OBSTACLE_SIZE, WIDTH, FUEL_COLOR, FUEL_SIZE
from src.objects import Obstacle, Fuel


def create_center_obstacle() -> Obstacle:
	"""Create a static obstacle centered in the game window."""
	return Obstacle(
		x=(WIDTH - OBSTACLE_SIZE[0]) // 2,
		y=(HEIGHT - OBSTACLE_SIZE[1]) // 2,
		size=OBSTACLE_SIZE,
		color=OBSTACLE_COLOR,
	)

def create_fuelcan() -> Fuel:
	"""Create fuel can in random position"""
	obstacle_rect = pygame.Rect(
		(WIDTH - OBSTACLE_SIZE[0]) // 2,
		(HEIGHT - OBSTACLE_SIZE[1]) // 2,
		OBSTACLE_SIZE[0],
		OBSTACLE_SIZE[1],
	)

	while True:
		fuel = Fuel(
			x=random.randint(0, WIDTH - FUEL_SIZE[0]),
			y=random.randint(0, HEIGHT - FUEL_SIZE[1]),
			size=FUEL_SIZE,
			color=FUEL_COLOR,
		)

		if not fuel.rect.colliderect(obstacle_rect):
			return fuel


def draw_frame(screen: pygame.Surface, ships: pygame.sprite.Group, obstacle: Obstacle) -> None:
	"""Draw one frame of the game scene."""
	screen.fill("black")
	obstacle.draw(screen)
	ships.draw(screen)


class NeedsDisplay:
	"""Display health and fuel for both players."""

	def __init__(self, player1, player2) -> None:
		self.player1 = player1
		self.player2 = player2
		self.font = pygame.font.SysFont(None, 28)
		self.player1_color = (80, 160, 255)
		self.player2_color = (255, 90, 90)

	def draw(self, screen: pygame.Surface) -> None:
		"""Draw player health and fuel values on the screen."""
		player1_text = self._create_player_text("Player 1", self.player1)
		player2_text = self._create_player_text("Player 2", self.player2)

		self._draw_text(screen, player1_text, self.player1_color, (20, 20))
		self._draw_text(screen, player2_text, self.player2_color, (WIDTH - 20, 20), align_right=True)

	def _create_player_text(self, label: str, player) -> str:
		return f"{label}  Health: {player.needs.health}  Fuel: {player.needs.fuel}"

	def _draw_text(self, screen: pygame.Surface, text: str, color, position, align_right: bool = False) -> None:
		text_surface = self.font.render(text, True, color)
		text_rect = text_surface.get_rect()
		if align_right:
			text_rect.topright = position
		else:
			text_rect.topleft = position
		screen.blit(text_surface, text_rect)


class WinnerAnnouncement:
	"""Display the winning player in a centered box."""

	def __init__(self, winner) -> None:
		self.winner = winner
		self.font = pygame.font.SysFont(None, 100)
		self.box_color = (25, 25, 25)
		self.border_color = (255, 255, 255)
		self.text_color = (255, 255, 255)

	def draw(self, screen: pygame.Surface) -> None:
		"""Draw the winner announcement."""
		winner_name = winner_to_text(self.winner)
		text_surface = self.font.render(f"Winner is {winner_name}", True, self.text_color)
		text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

		box_rect = text_rect.inflate(130, 110)
		pygame.draw.rect(screen, self.box_color, box_rect)
		pygame.draw.rect(screen, self.border_color, box_rect, 3)
		screen.blit(text_surface, text_rect)


def winner_to_text(winner) -> str:
	"""Return a readable winner name."""
	return winner.__class__.__name__
