import time

import pygame

import car_functions
import screen
import consts

timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 500)
state = {
    "state": consts.RUNNING_STATE,
    "is_window_open": True,
    "car_position": consts.INITIAL_CAR_POSITION,
    "car_speed": 0,
    "first_line_position": consts.INITIAL_LINE_POSITION,
    "movement": False,
    "timer": 0
}


def main():
    pygame.init()
    while state["is_window_open"]:
        handle_user()
        handle_object_position()
        screen.draw_game(state)


def handle_user():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] == consts.RUNNING_STATE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

                if event.key == pygame.K_LEFT:
                    print("left")

                if event.key == pygame.K_RIGHT:
                    print("right")

                if event.key == pygame.K_UP:
                    state["movement"] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    state["movement"] = False

                if event.key == pygame.K_DOWN:
                    state["car_speed"] -= 1
                    print()

        if state["movement"]:
            state["car_speed"] += 1
            print(state["car_speed"])



def handle_object_position():
    state["car_speed"] = 1
    if state["first_line_position"] + state["car_speed"] >= consts.LINES_ONLY_SPACE:
        state["first_line_position"] = -consts.LINES_HEIGHT
    else:
        state["first_line_position"] = state["first_line_position"] + state["car_speed"]


main()
