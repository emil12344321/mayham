"""GUI helpers for creating and drawing game visuals.

Authors: Irjan Evertsen and Emil Olsen-Kristiansen
"""

from __future__ import annotations

import pygame

from config import HEIGHT, OBSTACLE_COLOR, OBSTACLE_SIZE, WIDTH
from src.objects import Obstacle


def create_center_obstacle() -> Obstacle:
	"""Create a static obstacle centered in the game window."""
	return Obstacle(
		x=(WIDTH - OBSTACLE_SIZE[0]) // 2,
		y=(HEIGHT - OBSTACLE_SIZE[1]) // 2,
		size=OBSTACLE_SIZE,
		color=OBSTACLE_COLOR,
	)


def draw_frame(screen: pygame.Surface, ships: pygame.sprite.Group, obstacle: Obstacle) -> None:
	"""Draw one frame of the game scene."""
	screen.fill("black")
	obstacle.draw(screen)
	ships.draw(screen)