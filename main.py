import pygame
import screen
import consts

state = {
    "state": consts.RUNNING_STATE,
    "is_window_open": True,
    "car_position": consts.INITIAL_CAR_POSITION,
    "car_speed": 0,
    "first_line_position": consts.INITIAL_LINE_POSITION,
    "movement": True
}

def main():
    pygame.init()
    i = 0.01
    while state["is_window_open"]:
        handle_user()
        if state["first_line_position"] + i >= consts.LINES_SPACE:
            state["first_line_position"] = -consts.LINES_HEIGHT
        else:
            state["first_line_position"] = state["first_line_position"] + i
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

main()