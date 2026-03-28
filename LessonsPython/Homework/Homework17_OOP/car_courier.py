from decimal import Decimal
from courier import Courier

class CarCourier(Courier):
    _car_model: str
    _fuel: float
    _fuel_consumption: float

    def __init__(self, name: str, experience: int, rating: float, completed_orders: int, balance: Decimal, is_busy: bool, car_model: str, fuel: float, fuel_consumption: float):
        super().__init__(name, experience, rating, completed_orders, balance, is_busy)
        self._car_model = car_model
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    def print_info(self) -> None:
        super().print_info()
        print(f"Модель машины: {self._car_model}")
        print(f"Остаток топлива: {self._fuel:.2f} л")
        print(f"Расход топлива: {self._fuel_consumption} л")

    def calculate_salary_for_order(self, distance: float) -> float:
        fix_price = 200
        extra_price = 40
        return fix_price + extra_price * distance
    
    def deliver_order(self, distance: float) -> None:
        if self._fuel < 10:
            print("Топлива недостаточно. Доставка невозможна")
        else:
            self._fuel -= self._fuel_consumption * distance / 100
            self._completed_orders += 1
            salary = self.calculate_salary_for_order(distance)
            self._balance += Decimal(salary)

            print("Доставка выполнена")
            print(f"Оплата: {self.calculate_salary_for_order(distance):.2f} руб")


    def refuel(self, liters: float) -> None:
        self._fuel += liters
        print("Автомобиль заправлен")