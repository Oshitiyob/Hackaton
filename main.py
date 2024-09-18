import pygame
import screen
import consts

state = {
    "state": consts.RUNNING_STATE,
    "is_window_open": True,
    "car_position": consts.INITIAL_CAR_POSITION
}

def main():
    pygame.init()
    while state["is_window_open"]:
        hendle_user_events()
        screen.draw_game(state)

def hendle_user_events():
    print()


main()
