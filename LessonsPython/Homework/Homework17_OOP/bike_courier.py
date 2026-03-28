from decimal import Decimal
from courier import Courier

class BikeCourier(Courier):
    _bike_type: str
    _stamina: int

    def __init__(self, name: str, experience: int, rating: float, completed_orders: int, balance: Decimal, is_busy: bool,bike_type: str, stamina: int):
        super().__init__(name, experience, rating, completed_orders, balance, is_busy)
        self._bike_type = bike_type
        self._stamina = stamina
        
    def print_info(self) -> None:
        super().print_info()
        print(f"Тип велосипеда: {self._bike_type}")
        print(f"Выносливость: {self._stamina}")


    def calculate_salary_for_order(self, distance: float) -> float:
        fix_price = 150
        extra_price = 30
        return fix_price + extra_price * distance

    def deliver_order(self, distance: float) -> None:
        if self._stamina < 10:
            print("Значение выносливости слишком маленькое. Курьер устал")
        else:
            self._completed_orders += 1
            self._stamina -= 10
            salary = self.calculate_salary_for_order(distance)
            self._balance += Decimal(salary)

            print("Доставка выполнена")
            print(f"Оплата: {self.calculate_salary_for_order(distance):.2f} руб")