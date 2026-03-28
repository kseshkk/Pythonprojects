from decimal import Decimal
from courier import Courier


class FootCourier(Courier):
    _max_distance: float
    _speed: float

    def __init__(self, name: str, experience: int, rating: float, completed_orders: int, balance: Decimal, is_busy: bool, max_distance: float, speed: float):

        if max_distance < 0:
            raise ValueError
        
        if speed <= 0:
            raise ValueError

        super().__init__(name, experience, rating, completed_orders, balance, is_busy)
        self._max_distance = max_distance
        self._speed = speed

    def print_info(self) -> None:
        super().print_info()
        print(f"Максимальная дистанция: {self._max_distance} км")
        print(f"Скорость: {self._speed} км/ч")

    def calculate_salary_for_order(self, distance: float) -> float:
        fix_price = 120
        extra_price = 25
        return fix_price + extra_price * distance
    
    def deliver_order(self, distance: float) -> None:
        if distance > self._max_distance:
            print(f"Пеший курьер не может взять данный заказ. Максимальная дистанция - {self._max_distance}")
        else:
            self._completed_orders += 1
            salary = self.calculate_salary_for_order(distance)
            self._balance += Decimal(salary)

            print("Доставка выполнена")
            print(f"Оплата: {self.calculate_salary_for_order(distance):.2f} руб")


