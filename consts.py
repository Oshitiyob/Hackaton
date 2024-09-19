import time
import pygame

TIMES_FOR_QUESTION = [5, 20, 30, 50]
INITIAL_TIME = time.time()
RUNNING_STATE = 1
SIGN_STATE = 2
QUESTION_STATE = 3
HANDLING_SIGN_STATE = 4
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 854
BACKGROUND_COLOR = (51, 204, 51)

# images
MAIN_CAR_IMAGE = pygame.image.load("./images/main_car.png")
SIGN_LIST = [0, 1, 2, 3]
SIGN_LIST_RANDOM = SIGN_LIST.copy()
CROSS_ROAD_IMAGE = pygame.image.load("./images/crossroadsign.png")
PRIORITY_SIGN_IMAGE = pygame.image.load("./images/prioritysign.png")
STOP_SIGN_IMAGE = pygame.image.load("./images/stopsign.png")
SIGNS_LIST_IMAGES = [STOP_SIGN_IMAGE, PRIORITY_SIGN_IMAGE, CROSS_ROAD_IMAGE]

# QUESTIONS:
STOP_Q = pygame.image.load("./images/questions/stop sign.png")
PRIORITY_Q = pygame.image.load("./images/questions/priorety sign.png")
CROSS_ROAD_Q = pygame.image.load("./images/questions/crossroad sign.png")
URBAN_AREA_Q = pygame.image.load("./images/questions/urban area sign.png")

# question image size
QUESTION_WIDTH = SCREEN_WIDTH
QUESTION_HEIGHT = SCREEN_HEIGHT

CAR_WIDTH = MAIN_CAR_IMAGE.get_width() / 1.5
CAR_HEIGHT = MAIN_CAR_IMAGE.get_height() / 1.5
INITIAL_CAR_POSITION = (5/8 * SCREEN_WIDTH, SCREEN_HEIGHT - CAR_HEIGHT)
ROAD_WIDTH = SCREEN_WIDTH - SCREEN_WIDTH / 2
ROAD_HEIGHT = SCREEN_HEIGHT
ROAD_POSITION = (SCREEN_WIDTH / 4, 0)
INITIAL_LINE_POSITION = 0
LINES_WIDTH = 10
LINES_HEIGHT = 50
LINES_COLOR = (255,255,255)
LINES_ONLY_SPACE = 30
LINES_SPACE = LINES_HEIGHT + LINES_ONLY_SPACE
LINES_POSITION_X = SCREEN_WIDTH / 2 - LINES_WIDTH / 2
ROAD_COLOR = (95, 95, 95)

# signs
SIGN_WIDTH = STOP_SIGN_IMAGE.get_width() / 3
SIGN_HEIGHT = STOP_SIGN_IMAGE.get_height() / 3
SIGN_INITIAL_POSITION = [7/8 * SCREEN_WIDTH, -SIGN_HEIGHT]