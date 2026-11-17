"""Логика калькулятора: арифметические операции и работа с памятью."""

from __future__ import annotations

import math
from typing import Union

Number = Union[int, float]


def _check_number(value: Number, name: str = "значение") -> None:
    """Проверяет, что передан числовой аргумент (bool не считается числом)."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} должно быть целым или вещественным числом")


def add(a: Number, b: Number) -> Number:
    """Возвращает сумму двух чисел."""
    _check_number(a, "Первый аргумент")
    _check_number(b, "Второй аргумент")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Возвращает разность двух чисел."""
    _check_number(a, "Первый аргумент")
    _check_number(b, "Второй аргумент")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Возвращает произведение двух чисел."""
    _check_number(a, "Первый аргумент")
    _check_number(b, "Второй аргумент")
    return a * b


def divide(a: Number, b: Number) -> float:
    """Делит первое число на второе; деление на ноль запрещено."""
    _check_number(a, "Делимое")
    _check_number(b, "Делитель")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """Возводит число в степень, возвращая только вещественный результат."""
    _check_number(base, "Основание")
    _check_number(exponent, "Показатель степени")
    result = base ** exponent
    if isinstance(result, complex):
        raise ValueError("Результат операции не является вещественным числом")
    return result


def square_root(value: Number) -> float:
    """Возвращает квадратный корень неотрицательного числа."""
    _check_number(value)
    if value < 0:
        raise ValueError("Нельзя извлечь квадратный корень из отрицательного числа")
    return math.sqrt(value)


def factorial(value: Number) -> int:
    """Вычисляет факториал неотрицательного целого числа."""
    _check_number(value)
    if value < 0 or not float(value).is_integer():
        raise ValueError("Факториал определён только для неотрицательных целых чисел")
    return math.factorial(int(value))


def memory_store(current_memory: Number, value: Number) -> Number:
    """Сохраняет значение в памяти, заменяя прежнее."""
    _check_number(current_memory, "Текущее значение памяти")
    _check_number(value, "Сохраняемое значение")
    return value


def memory_recall(current_memory: Number) -> Number:
    """Возвращает значение, хранящееся в памяти."""
    _check_number(current_memory, "Текущее значение памяти")
    return current_memory


def memory_add(current_memory: Number, value: Number) -> Number:
    """Прибавляет значение к содержимому памяти."""
    _check_number(current_memory, "Текущее значение памяти")
    _check_number(value, "Добавляемое значение")
    return current_memory + value


def memory_clear(current_memory: Number) -> Number:
    """Очищает память и возвращает нулевое значение."""
    _check_number(current_memory, "Текущее значение памяти")
    return 0


class CalculatorEngine:
    """Класс-координатор, связывающий операции и состояние памяти."""

    def __init__(self) -> None:
        self._memory: Number = 0

    def calculate(self, operation: str, a: Number, b: Number | None = None) -> Number:
        """Выполняет операцию по коду: add/subtract/multiply/divide/power/sqrt/factorial."""
        binary_operations = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
            "power": power,
        }
        unary_operations = {
            "sqrt": square_root,
            "factorial": factorial,
        }

        if operation in binary_operations:
            if b is None:
                raise ValueError("Для выбранной операции необходимо указать два числа")
            return binary_operations[operation](a, b)
        if operation in unary_operations:
            return unary_operations[operation](a)
        raise ValueError(f"Неизвестная операция: {operation}")

    def store_in_memory(self, value: Number) -> Number:
        self._memory = memory_store(self._memory, value)
        return self._memory

    def read_memory(self) -> Number:
        return memory_recall(self._memory)

    def add_to_memory(self, value: Number) -> Number:
        self._memory = memory_add(self._memory, value)
        return self._memory

    def clear_memory(self) -> Number:
        self._memory = memory_clear(self._memory)
        return self._memory
