import pygame
import consts

screen = pygame.display.set_mode(
    (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))


def draw_game(state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_road()
    draw_player(state["car_position"])
    pygame.display.flip()


def draw_player(car_position):
    car_image = consts.MAIN_CAR_IMAGE
    car_image = pygame.transform.scale(car_image, [consts.CAR_WIDTH, consts.CAR_HEIGHT])
    screen.blit(car_image, car_image.get_rect(center=car_position))


def draw_road():
    rect_info = (consts.ROAD_POSITION[0], consts.ROAD_POSITION[1], consts.ROAD_WIDTH, consts.ROAD_HEIGHT)
    pygame.draw.rect(screen, consts.ROAD_COLOR, pygame.Rect(rect_info))

def draw_line():
    rect_info = (consts.ROAD_POSITION[0], consts.ROAD_POSITION[1], consts.ROAD_WIDTH, consts.ROAD_HEIGHT)
    pygame.draw.rect(screen, consts.ROAD_COLOR, pygame.Rect(rect_info))
def draw_lines():
    print()

