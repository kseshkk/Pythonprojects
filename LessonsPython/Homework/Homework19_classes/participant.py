class Participant:
    _name: str
    _school_class: str
    _score: int

    def __init__(self, name: str, school_class: str):
        self._name = name
        self._school_class = school_class
        self._score = 0

    
    def get_status(self):
        if self._score == 0:
            return "нет баллов"
        elif self._score >= 50:
            return "лидер"
        else:
            return "участник"

    def add_points(self, points: int):
        if points >= 0:
            self._score += points
        
    def remove_points(self, points: int):
        if points > 0:
            self._score -= points


    def get_role(self):
        return "участник"
    
    def __str__(self):
        return f"Имя: {self._name}, {self._school_class} класс - {self._score} баллов, роль: {self.get_status()}"

    def __repr__(self):
        return f"Participant(name='{self._name}', school_class='{self._school_class}', score={self._score})"