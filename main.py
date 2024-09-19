import time
import math
import pygame
import screen
import consts
from checks import distance_car_to_sign, check_answer, sign_appear

timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 400)
state = {
    "state": consts.OPENING_SCREEN_STATE,
    "is_window_open": True,
    "car_position": consts.INITIAL_CAR_POSITION,
    "car_speed": 1,
    "first_line_position": consts.INITIAL_LINE_POSITION,
    "movement": "",
    "timer": 0,
    "time_counter": 0,
    "last_time": consts.INITIAL_TIME,
    "times_for_question": consts.TIMES_FOR_QUESTION,
    "objects_position": {
        "sign_position": consts.SIGN_INITIAL_POSITION.copy()
    },
    "sign": "",
    "question_answer": [0, False],
    "score": 0
}


def main():
    pygame.init()
    while state["is_window_open"]:
        if state["state"] == consts.QUESTION_STATE:
            if state["question_answer"][1]:
                state['score'] += 50
                time.sleep(1.3)
                state["state"] = consts.HANDLING_SIGN_STATE
                state["question_answer"] = [0, False]
            state["question_answer"][1] = check_answer(state)
        elif math.floor(state["time_counter"]) in consts.TIMES_FOR_QUESTION:
            if state["state"] != consts.SIGN_STATE:
                state["sign"] = consts.SIGN_LIST[0]
                consts.SIGN_LIST.remove(state["sign"])
            state["state"] = consts.SIGN_STATE
        elif state["state"] == consts.SIGN_STATE:
            if distance_car_to_sign(state["car_position"][1], state["objects_position"]["sign_position"][1]):
                state["state"] = consts.QUESTION_STATE
        elif state['state'] == consts.HANDLING_SIGN_STATE:
            print()

        handle_user()
        set_time_counter()
        handle_object_position()
        screen.draw_game(state)


def handle_user():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif state["state"] == consts.OPENING_SCREEN_STATE:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    state['state'] = consts.RUNNING_STATE

        elif state["state"] != consts.QUESTION_STATE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    state["car_position"] = consts.CAR_POSITION_LEFT

                if event.key == pygame.K_RIGHT:
                    state["car_position"] = consts.INITIAL_CAR_POSITION

                if event.key == pygame.K_UP:
                    state["movement"] = "up"
                if event.key == pygame.K_DOWN:
                    state["movement"] = "down"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    state["movement"] = ""

                if event.key == pygame.K_DOWN:
                    state["movement"] = ""
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                state["question_answer"][0] = 1
                print(state["question_answer"][0])

            if event.key == pygame.K_2:
                state["question_answer"][0] = 2

            if event.key == pygame.K_3:
                state["question_answer"][0] = 3

            if event.key == pygame.K_4:
                state["question_answer"][0] = 4

        if state["movement"] == "up" and state["car_speed"] < 20:
            state["car_speed"] += 1

        if state["movement"] == "down" and state["car_speed"] > 0:
            state["car_speed"] -= 1




def handle_object_position():
    i = state["car_speed"] / 20
    if state["state"] == consts.SIGN_STATE or state["state"] == consts.HANDLING_SIGN_STATE:
        state["objects_position"]["sign_position"][1] = state["objects_position"]["sign_position"][1] + i
    if state["state"] != consts.QUESTION_STATE:
        if state["first_line_position"] + i >= consts.LINES_ONLY_SPACE:
            state["first_line_position"] = -consts.LINES_HEIGHT
        else:
            state["first_line_position"] = state["first_line_position"] + i
    if sign_appear(state["objects_position"]["sign_position"][1]):
        state["objects_position"]["sign_position"] = consts.SIGN_INITIAL_POSITION.copy()
        state["state"] = consts.RUNNING_STATE

def set_time_counter():
    if state["state"] != consts.QUESTION_STATE and state["state"] != consts.HANDLING_SIGN_STATE and state["state"] != consts.HANDLING_SIGN_STATE:
        now = time.time()
        state["time_counter"] += now - state["last_time"]
        state["last_time"] = now
    else:
        state["last_time"] = time.time()

main()

# play_again = True
# while play_again:
#     for event in pygame.event.get():
#         if event.type == event.KEYDOWN:
#             if event.key == event.K_y:
#                 main()
#
#             elif event.key == event.K_n:
#                 play_again = False
#
# pygame.quit()
