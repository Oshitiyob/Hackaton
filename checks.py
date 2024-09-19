import consts
import random as r

def distance_car_to_sign(car_y, sign_y):
    if car_y - sign_y <= consts.SCREEN_HEIGHT / 1.5:
        return True
    return False


def check_answer(state):
    if state["question_answer"][0] == consts.ANSWERS[state["sign"]]:
        return True
    return False


def sign_appear(sign_position):
    if (sign_position - consts.SIGN_HEIGHT / 2) > consts.SCREEN_HEIGHT:
        return True
    return False


def random_seconds(number_amount):
    list_ = []
    for i in range(number_amount):
        x = r.randint(1, 100)
        list_.append(x)

    return list_


def random_screening(number_amount):
    list_ = []
    for i in range(number_amount):
        x = r.randint(1, consts.SCREEN_WIDTH)
        list_.append(x)

    return list_
