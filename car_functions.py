import pygame
import consts
import screen


def check_ac(state):
    state["car_speed"] = state["car_speed"] + 1
