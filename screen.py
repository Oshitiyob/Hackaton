import pygame

import consts
from consts import *

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_player(state["car_position"])
    pygame.display.flip()


def draw_player(car_position):
    car_image = consts.MAIN_CAR_IMAGE
    car_image = pygame.transform.scale(car_image, [CAR_WIDTH, CAR_HEIGHT])
    screen.blit(car_image, car_position)
