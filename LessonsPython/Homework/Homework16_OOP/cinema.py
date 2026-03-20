from movie import Movie
from session import Session

class Cinema:
    __cinema_name: str
    __session_list: list[Session]

    def __init__(self, cinema_name: str):
        self.__cinema_name = cinema_name
        self.__session_list = []

    def add_session(self, session: Session) -> None:
        self.__session_list.append(session)
        print("сеанс добавлен")

    def show_sessions(self) -> list[str]:
        all_sessions = []
        for session in self.__session_list:
            all_sessions.append(session.get_info())
        return all_sessions
    

    def find_session_by_number(self, index: int):
        if 1 <= index <= len(self.__session_list):
            return self.__session_list[index - 1]
        return None
    
    def book_ticket(self, session_index: int, seat_number: int) -> bool:
        current_session = self.find_session_by_number(session_index)

        if current_session == None:
            return False

        return current_session.book_seat(seat_number)
    

    def cancel_ticket(self, session_index, seat_number):
        current_session = self.find_session_by_number(session_index)

        if current_session == None:
            return False

        return current_session.cancel_booking(seat_number)
    
    def get_sessions_count(self) -> int:
        return len(self.__session_list)