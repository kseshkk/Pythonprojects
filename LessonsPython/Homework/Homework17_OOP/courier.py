from decimal import Decimal

class Courier:
    _name: str
    _experience: int
    _rating: float
    _completed_orders: int
    _balance: Decimal
    _is_busy: bool

    def __init__(self, name: str, experience: int, rating: float, completed_orders: int, balance: Decimal, is_busy: bool) -> None:

        if len(name) == 0:
            raise ValueError
        
        if experience < 0:
            raise ValueError
        
        if rating < 0 or rating > 5:
            raise ValueError
        
        if completed_orders < 0:
            raise ValueError
        
        if balance < 0:
            raise ValueError

        self._name = name
        self._experience = experience
        self._rating = rating
        self._completed_orders = completed_orders
        self._balance = balance
        self._is_busy = is_busy

    def print_info(self) -> None:
        print("Основные характеристики курьера")
        print(f"Имя: {self._name}")
        print(f"Опыт работы: {self._experience} месяцев")
        print(f"Рейтинг: {self._rating}")
        print(f"Количество выполненных заказов: {self._completed_orders}")
        print(f"Заработанные деньги: {self._balance:.2f} руб")
        print(f"Статус: {'занят' if self._is_busy else 'не занят'}")

    def deliver_order(self, distance: float) -> None:
        raise NotImplementedError
    
    def calculate_salary_for_order(self, distance: float) -> float:
        raise NotImplementedError
    
    def finish_shift(self) -> None:
        self._is_busy = False
        print("Итог смены")
        print(f"Количество выполненных заказов: {self._completed_orders}")
        print(f"Заработанные деньги: {self._balance:.2f}")
