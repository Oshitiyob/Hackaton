import pygame

import consts

state = {
    "state": consts.RUNNING_STATE,
    "is_window_open": False,
}

def main():
    pygame.init()
    while state["is_window_open"]:
        hendle_user_events()
def hendle_user_events():


