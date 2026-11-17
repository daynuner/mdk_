"""Модульные и интеграционные тесты калькулятора (стандартный unittest)."""

import unittest

from calculator_core import (
    CalculatorEngine,
    add,
    divide,
    factorial,
    memory_add,
    memory_clear,
    memory_recall,
    memory_store,
    multiply,
    power,
    square_root,
    subtract,
)


class TestArithmeticFunctions(unittest.TestCase):
    """Модульные тесты отдельных арифметических функций."""

    def test_add(self):
        self.assertEqual(add(7, 5), 12)
        self.assertEqual(add(-7, 5), -2)

    def test_subtract(self):
        self.assertEqual(subtract(7, 5), 2)
        self.assertEqual(subtract(5, 7), -2)

    def test_multiply(self):
        self.assertEqual(multiply(7, 5), 35)
        self.assertEqual(multiply(-2, 4), -8)

    def test_divide(self):
        self.assertEqual(divide(15, 3), 5)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 5), 32)
        self.assertEqual(power(5, 0), 1)

    def test_power_rejects_complex_result(self):
        with self.assertRaises(ValueError):
            power(-4, 0.5)

    def test_square_root(self):
        self.assertEqual(square_root(81), 9)
        self.assertEqual(square_root(0), 0)

    def test_square_root_of_negative_number(self):
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(4.0), 24)

    def test_factorial_rejects_negative_and_fractional_values(self):
        with self.assertRaises(ValueError):
            factorial(-3)
        with self.assertRaises(ValueError):
            factorial(2.5)

    def test_functions_reject_boolean_values(self):
        with self.assertRaises(TypeError):
            add(True, 1)


class TestMemoryFunctions(unittest.TestCase):
    """Модульные тесты функций управления памятью."""

    def test_memory_store(self):
        self.assertEqual(memory_store(0, 15), 15)
        self.assertEqual(memory_store(15, -2), -2)

    def test_memory_recall(self):
        self.assertEqual(memory_recall(27), 27)

    def test_memory_add(self):
        self.assertEqual(memory_add(10, 5), 15)
        self.assertEqual(memory_add(-2, 5), 3)

    def test_memory_clear(self):
        self.assertEqual(memory_clear(123), 0)


class TestCalculatorIntegration(unittest.TestCase):
    """Интеграционные тесты взаимодействия операций и состояния памяти."""

    def setUp(self):
        self.calculator = CalculatorEngine()

    def test_binary_and_unary_operation_dispatch(self):
        self.assertEqual(self.calculator.calculate("add", 3, 4), 7)
        self.assertEqual(self.calculator.calculate("power", 2, 3), 8)
        self.assertEqual(self.calculator.calculate("sqrt", 49), 7)
        self.assertEqual(self.calculator.calculate("factorial", 4), 24)

    def test_two_argument_operation_requires_second_operand(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate("divide", 10)

    def test_memory_workflow(self):
        result = self.calculator.calculate("add", 12, 8)
        self.calculator.store_in_memory(result)
        self.calculator.calculate("multiply", 3, 4)
        self.calculator.add_to_memory(2)
        self.assertEqual(self.calculator.read_memory(), 22)
        self.assertEqual(self.calculator.clear_memory(), 0)
        self.assertEqual(self.calculator.read_memory(), 0)

    def test_unknown_operation_is_rejected(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate("modulo", 8, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
