from participant import Participant

class Captain(Participant):
    _team_name: str

    def __init__(self, name: str, school_class: str, team_name: str):
        super().__init__(name, school_class)
        self._team_name = team_name

    def add_points(self, points: int):
        if points > 0:
            self._score += points + 2

    def get_role(self):
        return f"Капитан команды - {self._team_name}"

    def __str__(self):
        return f"Имя: {self._name}, {self._school_class} класс - {self._score} баллов, роль: {self.get_role()}"