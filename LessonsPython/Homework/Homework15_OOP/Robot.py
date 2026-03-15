import random

class Robot:

    __energy: int
    __parts: int
    __status: bool

    MIN_LEVEL = 0
    MAX_LEVEL = 100

    __MIN_INCREASE = 10
    __MAX_INCREASE = 30

    __MIN_DECREASE = 10
    __MAX_DECREASE = 30

    __EVENT_CHANCE = 10


    def __init__(self, energy: int, parts: int, status: bool):
        self.__energy = energy
        self.__parts = parts
        self.__status = status

    def is_alive(self):
        return (self.__energy > self.MIN_LEVEL
                and self.__parts > self.MIN_LEVEL
                )

    def charge(self):
        increase_energy = random.randint(self.__MIN_INCREASE, self.__MAX_INCREASE)

        self.__energy += increase_energy

    def repair(self):
        increase_parts = random.randint(self.__MIN_INCREASE, self.__MAX_INCREASE)

        self.__parts += increase_parts

    def work(self):
        decrease_energy = random.randint(self.__MIN_DECREASE, self.__MAX_DECREASE)
        decrease_parts = random.randint(self.__MIN_DECREASE, self.__MAX_DECREASE)

        if self.__energy - decrease_energy < self.MIN_LEVEL:
            print("Недостаточно энергии для работы!")
            return

        if self.__parts - decrease_parts < self.MIN_LEVEL:
            print("Недостаточно запчастей для работы!")
            return

        self.__energy -= decrease_energy
        self.__parts -= decrease_parts

        print(f"Робот успешно поработал. Потрачено {decrease_energy} энергии и {decrease_parts} запчастей")

    def check_status(self):
        print("Текущее состояние робота")
        print(f"Уровень энергии: {self.__energy}")
        print(f"Уровень запчастей: {self.__parts}")
        status_text = "работает" if self.__status else "не работает"
        print(f"Состояние: {status_text}")

    def random_event(self):
        event_percent = random.randint(1, 100)
        if 1 <= event_percent <= self.__EVENT_CHANCE:
            event_number = random.randint(1, 2)
            print("Активировалось случайное событие")

            if event_number == 1:
                self.__parts = 0
                self.__status = False

                print("Робот сломался. Срочно почините его")

            if event_number == 2:
                increase = random.randint(self.__MIN_INCREASE, self.__MAX_INCREASE)
                self.__energy += increase

                print(f"Робот нашел дополнительную энергию. Энергия повышена на {increase}")


    def normalized_parameters(self):
        if self.__energy > self.MAX_LEVEL:
            self.__energy = self.MAX_LEVEL


        if self.__parts > self.MAX_LEVEL:
            self.__parts = self.MAX_LEVEL

