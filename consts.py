import pygame
MAIN_CAR_IMAGE = pygame.image.load("./images/main_car.png")
RUNNING_STATE = 1
QUESTION_STATE = 2
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 854
BACKGROUND_COLOR = (51, 204, 51)
CAR_WIDTH = MAIN_CAR_IMAGE.get_width() / 1.5
CAR_HEIGHT = MAIN_CAR_IMAGE.get_height() / 1.5
INITIAL_CAR_POSITION = (5/8 * SCREEN_WIDTH, SCREEN_HEIGHT - CAR_HEIGHT)
ROAD_WIDTH = SCREEN_WIDTH - SCREEN_WIDTH / 2
ROAD_HEIGHT = SCREEN_HEIGHT
ROAD_POSITION = (SCREEN_WIDTH / 4, 0)
ROAD_COLOR = (95,95,95)