import random

class Robot:

    __energy: int
    __parts: int
    __status: str

    MIN_LEVEL = 0
    MAX_LEVEL = 100

    __MIN_INCREASE = 10
    __MAX_INCREASE = 100

    def __init__(self, energy: int, parts: int, status: str):
        self.__energy = energy
        self.__parts = parts
        self.__status = status

    def charge(self):
        increase_energy = random.randint(self.__MIN_INCREASE, self.__MAX_INCREASE)

        self.__energy += increase_energy



