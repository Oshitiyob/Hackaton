import time
import pygame

TIMES_FOR_QUESTION = [2, 20, 30, 50]
INITIAL_TIME = time.time()
RUNNING_STATE = 1
SIGN_STATE = 2
QUESTION_STATE = 3
HANDLING_SIGN_STATE = 4
ANSWER_STATE = 5
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 854
BACKGROUND_COLOR = (51, 204, 51)

# images
MAIN_CAR_IMAGE = pygame.image.load("./images/main_car.png")
SIGN_LIST = ["stop", "priority", "crossroad"]
SIGN_LIST_RANDOM = SIGN_LIST.copy()
CROSS_ROAD_IMAGE = pygame.image.load("./images/crossroadsign.png")
PRIORITY_SIGN_IMAGE = pygame.image.load("./images/prioritysign.png")
STOP_SIGN_IMAGE = pygame.image.load("./images/stopsign.png")
RIGHT_ANSWER_IMAGE = pygame.image.load("./images/right_answer.png")
WRONG_ANSWER_IMAGE = pygame.image.load("./images/wrong_answer.png")
OPENING_SCREEN = pygame.image.load("./images/opening_screen.png")

ANSWERS_WIDTH = WRONG_ANSWER_IMAGE.get_width() / 8
ANSWERS_HEIGHT = WRONG_ANSWER_IMAGE.get_height() / 8
INITIAL_POSITION_ANSWER_Y = 300
SPACE_BETWEEN_ANSWERS = SCREEN_WIDTH / 3.5

SIGNS_LIST_IMAGES = {
    "stop": STOP_SIGN_IMAGE,
    "priority":PRIORITY_SIGN_IMAGE,
    "crossroad": CROSS_ROAD_IMAGE
}
# QUESTIONS:
STOP_Q = pygame.image.load("./images/questions/stop sign.png")
PRIORITY_Q = pygame.image.load("./images/questions/priorety sign.png")
CROSS_ROAD_Q = pygame.image.load("./images/questions/crossroud sign.png")
URBAN_AREA_Q = pygame.image.load("./images/questions/urban area sign.png")

# question image size
QUESTION_WIDTH = SCREEN_WIDTH
QUESTION_HEIGHT = SCREEN_HEIGHT

QUESTIONS_LIST_IMAGES = {
    "stop": STOP_Q,
    "priority": PRIORITY_Q,
    "crossroad": CROSS_ROAD_IMAGE,
    "urban area": URBAN_AREA_Q
}

ANSWERS_OPTIONS = [1, 2, 3, 4]
ANSWERS = {
    'stop': 3,
    'priority': 4,
    'crossroad': 3,
    'urban area': 1
}


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