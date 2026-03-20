from movie import Movie

class Session:
    __movie: Movie
    __session_time: str
    __ticket_price: int
    __number_of_seats: int
    __list_of_occupied_seats: list[int]

    def __init__(self, movie: Movie, session_time: str, ticket_price: int, number_of_seats: int):
        self.__movie = movie
        self.__session_time = session_time
        self.__ticket_price = ticket_price
        self.__number_of_seats = number_of_seats
        self.__list_of_occupied_seats = []

    def show_free_seats(self) -> list[int]:
        return [seat for seat in range(1, self.__number_of_seats + 1) 
        if seat not in self.__list_of_occupied_seats]
    
    def book_seat(self, seat_number: int):
        if seat_number in self.__list_of_occupied_seats:
            print(f"место {seat_number} уже забронировано. Выберите другое")
            return False
        
        self.__list_of_occupied_seats.append(seat_number)
        print(f"место {seat_number} забронировано")
        return True
    
    def cancel_booking(self, seat_number: int):
        if seat_number not in self.__list_of_occupied_seats:
            print("Невозможно отменить бронь. Место свободно")
            return False
        
        if seat_number in self.__list_of_occupied_seats:
            self.__list_of_occupied_seats.remove(seat_number)
            print(f"Бронь на место {seat_number} отменена")
            return True
        

    def is_seat_free(self, seat_number: int) -> bool:
        return seat_number not in self.__list_of_occupied_seats

        # if seat_number not in self.__list_of_occupied_seats:
        #     print(f"место {seat_number} свободно")
        #     return True
        
        # if seat_number in self.__list_of_occupied_seats:
        #     print(f"место {seat_number} забронировано")
        #     return False
        
    def get_info(self) -> str:
        free_seats = len(self.show_free_seats())
        return f"{self.__session_time} | {self.__movie.get_info()} | цена: {self.__ticket_price} руб | свободных мест: {free_seats}"


    def get_total_seats(self) -> int:
        return self.__number_of_seats
