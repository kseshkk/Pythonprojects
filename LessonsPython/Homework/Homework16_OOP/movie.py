class Movie:
    __name: str
    __duration: int
    __age_limit: int

    def __init__(self, name: str, duration: int, age_limit: int):
        self.__name = name
        self.__duration = duration
        self.__age_limit = age_limit


    def get_info(self):
        return f"{self.__name} - {self.__duration} мин, {self.__age_limit}+"