import pygame
from consts import *

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_game():
    draw_player()


def draw_player():
    pygame.init()
    car = MAIN_CAR_IMAGE
    pygame.image.load(car)
    pygame.transform.scale(car, [CAR_WIDTH, CAR_HEIGHT])
