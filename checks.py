import consts
import questions


def distance_car_to_sign(car_y, sign_y):
    if car_y - sign_y <= consts.SCREEN_HEIGHT/2:
        return True
    else:
        return False


def check_answer(question_list, player_answer_int, sign):
    if questions.answers[sign][(player_answer_int-1)] == question_list[2]:
        return True
    else:
        return False


