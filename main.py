import pygame
import screen
from consts import *

state = {
    "state": RUNNING_STATE,
    "is_window_open": True
}


def main():
    handle_user()


def handle_user():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] == RUNNING_STATE:
            if state["movement"]:
                if event.key == pygame.K_SPACE:
                    state["movement"] = False
                    state["view_mines"] = True
                    continue

                if event.key == pygame.K_LEFT:
                    print("left")

                elif event.key == pygame.K_RIGHT:
                    print("right")

                elif event.key == pygame.K_UP:
                    print("up")

                elif event.key == pygame.K_DOWN:
                    print("down")
