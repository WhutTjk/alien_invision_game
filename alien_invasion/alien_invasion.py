import pygame
import sys

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """初始化游戏"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 创建飞船
    ship = Ship(screen)

    pygame.display.set_caption("Alian Invision")

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, ship, screen)


run_game()
