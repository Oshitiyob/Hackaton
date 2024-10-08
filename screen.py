import pygame

import colors
import consts
from checks import distance_car_to_sign

screen = pygame.display.set_mode(
    (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))


def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_road()
    draw_road_lines(state["first_line_position"])
    draw_player(state["car_position"])
    drew_scoreboard(state['score'])
    drew_car_speed(state["car_speed"])
    if state['state'] == consts.OPENING_SCREEN_STATE:
        drew_opening_screen()
    if state["state"] == consts.SIGN_STATE or state["state"] == consts.HANDLING_SIGN_STATE:
        draw_sign(state["objects_position"]["sign_position"], state["sign"])
    if state["state"] == consts.QUESTION_STATE:
        draw_question(state["sign"])
        if state["question_answer"][0] in consts.ANSWERS_OPTIONS:
            draw_answer(state["question_answer"][0], state["question_answer"][1])
    pygame.display.flip()


def draw_player(car_position):
    car_image = consts.MAIN_CAR_IMAGE
    car_image = pygame.transform.scale(car_image, [consts.CAR_WIDTH, consts.CAR_HEIGHT])
    screen.blit(car_image, car_image.get_rect(center=car_position))


def draw_road():
    rect_info = (consts.ROAD_POSITION[0], consts.ROAD_POSITION[1], consts.ROAD_WIDTH, consts.ROAD_HEIGHT)
    pygame.draw.rect(screen, consts.ROAD_COLOR, pygame.Rect(rect_info))


def draw_line(line_position_y):
    rect_info = (consts.LINES_POSITION_X, line_position_y, consts.LINES_WIDTH, consts.LINES_HEIGHT)
    pygame.draw.rect(screen, consts.LINES_COLOR, pygame.Rect(rect_info))


def draw_road_lines(first_line_position_y):
    line_position_y = first_line_position_y
    while line_position_y < consts.SCREEN_HEIGHT:
        draw_line(line_position_y)
        line_position_y += consts.LINES_SPACE


def draw_sign(sign_position, sign):
    sign_image = consts.SIGNS_LIST_IMAGES[sign]
    sign_image = pygame.transform.scale(sign_image, [consts.SIGN_WIDTH, consts.SIGN_HEIGHT])
    screen.blit(sign_image, sign_image.get_rect(center=sign_position))


def draw_question(sign):
    question_image = consts.QUESTIONS_LIST_IMAGES[sign]
    question_image = pygame.transform.scale(question_image, [consts.QUESTION_WIDTH, consts.QUESTION_HEIGHT])
    screen.blit(question_image, (0, 0))


def draw_answer(number_to_draw, answer):
    if answer:
        answer_image = consts.RIGHT_ANSWER_IMAGE
    else:
        answer_image = consts.WRONG_ANSWER_IMAGE
    answer_image = pygame.transform.scale(answer_image, [consts.ANSWERS_WIDTH, consts.ANSWERS_HEIGHT])
    screen.blit(answer_image, answer_image.get_rect(center=(
    consts.SCREEN_WIDTH / 2, consts.INITIAL_POSITION_ANSWER_Y + (number_to_draw - 1) * consts.SPACE_BETWEEN_ANSWERS)))


def drew_opening_screen():
    opening_screen = pygame.transform.scale(consts.OPENING_SCREEN, [consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT])
    screen.blit(opening_screen, (0, 0))

def drew_scoreboard(score):
    font = pygame.font.SysFont('Pokemon GB.ttf', 30)
    scoreboard = font.render(f"score: {str(score)}", True, colors.BLACK)
    screen.blit(scoreboard, [10, 10])


def drew_car_speed(speed):
    font = pygame.font.SysFont('Pokemon GB.ttf', 30)
    font = font.render(f"speed: {str(round(speed * 4))}", True, colors.BLACK)
    screen.blit(font, [consts.SCREEN_WIDTH - font.get_width() - 10, 10])
