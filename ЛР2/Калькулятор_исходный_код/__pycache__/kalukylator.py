import math

mem = 0

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

def div(a, b):
    if b == 0: raise ValueError("Деление на ноль")
    return a / b

def power(a, b): return a ** b

def sqrt(a):
    if a < 0: raise ValueError("Корень из отрицательного")
    return math.sqrt(a)

def factorial(n):
    if not isinstance(n, int) or n < 0: raise ValueError("Некорректный факториал")
    return math.factorial(n)

# память
def mem_save(v):
    global mem; mem = v; return mem

def mem_read(): return mem

def mem_add(v):
    global mem; mem += v; return mem

def mem_clear():
    global mem; mem = 0; return mem
import unittest
import calculator as c

class TestCalc(unittest.TestCase):
    def setUp(self):
        c.mem_clear()

    def test_base(self):
        self.assertEqual(c.add(2, 3), 5)
        self.assertEqual(c.sub(5, 3), 2)
        self.assertEqual(c.mul(3, 4), 12)
        self.assertEqual(c.div(10, 2), 5)
        with self.assertRaises(ValueError): c.div(1, 0)

    def test_power_sqrt(self):
        self.assertEqual(c.power(2, 3), 8)
        self.assertEqual(c.sqrt(9), 3)
        with self.assertRaises(ValueError): c.sqrt(-4)

    def test_factorial(self):
        self.assertEqual(c.factorial(5), 120)
        self.assertEqual(c.factorial(0), 1)
        with self.assertRaises(ValueError): c.factorial(-1)

    def test_memory(self):
        self.assertEqual(c.mem_save(42), 42)
        self.assertEqual(c.mem_read(), 42)
        self.assertEqual(c.mem_add(8), 50)
        self.assertEqual(c.mem_clear(), 0)

if __name__ == "__main__":
    unittest.main()