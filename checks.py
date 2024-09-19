import consts


def distance_car_to_sign(car_y, sign_y):
    if car_y - sign_y <= consts.SCREEN_HEIGHT/2:
        return True
    else:
        return False



