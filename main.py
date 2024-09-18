import time
import math
import pygame
import screen
import consts
from checks import distance_car_to_sign
state = {
    "state": consts.RUNNING_STATE,
    "is_window_open": True,
    "car_position": consts.INITIAL_CAR_POSITION,
    "car_speed": 3,
    "first_line_position": consts.INITIAL_LINE_POSITION,
    "movement": True,
    "time_counter": 0,
    "first_time": consts.INITIAL_TIME,
    "times_for_question": consts.TIMES_FOR_QUESTION,
    "objects_position": {
        "stop_sign_position": consts.SIGN_INITIAL_POSITION
    }
}


def main():
    pygame.init()
    while state["is_window_open"]:
        if math.floor(state["time_counter"]) in consts.TIMES_FOR_QUESTION:
            state["state"] = consts.SIGN_STATE
            if distance_car_to_sign(state["car_position"][1], state["objects_position"]["stop_sign_position"][1]):
                state["state"] = consts.QUESTION_STATE


        handle_user()
        set_time_counter()
        handle_object_position()
        screen.draw_game(state)


def handle_user():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] == consts.RUNNING_STATE:
            if state["movement"]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state["movement"] = False
                        continue

                    if event.key == pygame.K_LEFT:
                        print("left")

                    elif event.key == pygame.K_RIGHT:
                        print("right")

                    elif event.key == pygame.K_UP:
                        print("up")

                    elif event.key == pygame.K_DOWN:
                        print("down")


def handle_object_position():
    i = state["car_speed"] / 10
    if state["state"] == consts.SIGN_STATE:
        state["objects_position"]["stop_sign_position"][1] = state["objects_position"]["stop_sign_position"][1] + i
    if state["state"] != consts.QUESTION_STATE:
        if state["first_line_position"] + i >= consts.LINES_ONLY_SPACE:
            state["first_line_position"] = -consts.LINES_HEIGHT
        else:
            state["first_line_position"] = state["first_line_position"] + i


def set_time_counter():
    if state["state"] == consts.RUNNING_STATE:
        state["time_counter"] = time.time() - state["first_time"]
    elif state["state"] == consts.SIGN_STATE:
        state["first_time"] = time.time() - state["first_time"] - state["time_counter"]


main()