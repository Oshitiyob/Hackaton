import consts


def distance_car_to_sign(car_y, sign_y):
    if car_y - sign_y <= consts.SCREEN_HEIGHT / 1.5:
        return True
    return False


def check_answer(state):
    if state["question_answer"][0] == consts.ANSWERS[state["sign"]]:
        return True
    return False


def sign_appear(sign_position):
    if sign_position > consts.SCREEN_HEIGHT:
        return True
    return  False
