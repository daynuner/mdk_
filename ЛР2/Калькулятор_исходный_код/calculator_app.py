"""Графический интерфейс калькулятора на основе библиотеки Tkinter."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

from calculator_core import CalculatorEngine


class CalculatorApp:
    """Окно калькулятора с двумя операндами и четырьмя командами памяти."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.engine = CalculatorEngine()
        self.root.title("Калькулятор")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self._build_interface()

    def _build_interface(self) -> None:
        main = tk.Frame(self.root, padx=14, pady=12)
        main.pack(fill="both", expand=True)

        tk.Label(main, text="КАЛЬКУЛЯТОР", font=("Arial", 16, "bold")).pack(pady=(0, 12))

        inputs = tk.Frame(main)
        inputs.pack(fill="x", pady=4)
        tk.Label(inputs, text="Число A", width=12, anchor="w").grid(row=0, column=0, padx=4, pady=4)
        tk.Label(inputs, text="Число B", width=12, anchor="w").grid(row=0, column=2, padx=4, pady=4)
        self.entry_a = tk.Entry(inputs, width=18, font=("Arial", 12))
        self.entry_b = tk.Entry(inputs, width=18, font=("Arial", 12))
        self.entry_a.grid(row=0, column=1, padx=4, pady=4)
        self.entry_b.grid(row=0, column=3, padx=4, pady=4)

        binary_frame = tk.LabelFrame(main, text="Операции с двумя числами", padx=8, pady=8)
        binary_frame.pack(fill="x", pady=7)
        binary_buttons = [
            ("Сложение (+)", "add"),
            ("Вычитание (-)", "subtract"),
            ("Умножение (×)", "multiply"),
            ("Деление (÷)", "divide"),
            ("Степень (Aʙ)", "power"),
        ]
        for index, (title, operation) in enumerate(binary_buttons):
            tk.Button(
                binary_frame,
                text=title,
                width=15,
                command=lambda op=operation: self.perform_binary(op),
            ).grid(row=index // 3, column=index % 3, padx=4, pady=4, sticky="ew")
        for column in range(3):
            binary_frame.grid_columnconfigure(column, weight=1)

        unary_frame = tk.LabelFrame(main, text="Операции над числом A", padx=8, pady=8)
        unary_frame.pack(fill="x", pady=7)
        tk.Button(
            unary_frame,
            text="Квадратный корень √A",
            command=lambda: self.perform_unary("sqrt"),
        ).pack(side="left", expand=True, fill="x", padx=4)
        tk.Button(
            unary_frame,
            text="Факториал A!",
            command=lambda: self.perform_unary("factorial"),
        ).pack(side="left", expand=True, fill="x", padx=4)

        memory_frame = tk.LabelFrame(main, text="Память", padx=8, pady=8)
        memory_frame.pack(fill="x", pady=7)
        memory_commands = [
            ("MS — сохранить", self.store_memory),
            ("MR — прочитать", self.recall_memory),
            ("M+ — добавить", self.add_memory),
            ("MC — очистить", self.clear_memory),
        ]
        for title, callback in memory_commands:
            tk.Button(memory_frame, text=title, command=callback).pack(
                side="left", expand=True, fill="x", padx=3
            )

        self.result_label = tk.Label(main, text="Результат: —", font=("Arial", 12, "bold"), anchor="w")
        self.result_label.pack(fill="x", pady=(9, 3))
        self.memory_label = tk.Label(
            main, text="Память: 0", font=("Arial", 10), anchor="w"
        )
        self.memory_label.pack(fill="x")

    @staticmethod
    def _format_number(value: int | float) -> str:
        if isinstance(value, float):
            return str(int(value)) if value.is_integer() else format(value, ".12g")
        return str(value)

    @staticmethod
    def _read_number(entry: tk.Entry, field_name: str) -> float:
        raw_value = entry.get().strip().replace(",", ".")
        if not raw_value:
            raise ValueError(f"Введите значение в поле «{field_name}».")
        try:
            return float(raw_value)
        except ValueError as error:
            raise ValueError(f"Поле «{field_name}» должно содержать число.") from error

    def _show_error(self, error: Exception) -> None:
        messagebox.showerror("Ошибка ввода или вычисления", str(error), parent=self.root)

    def _show_result(self, value: int | float) -> None:
        self.result_label.configure(text=f"Результат: {self._format_number(value)}")

    def perform_binary(self, operation: str) -> None:
        try:
            a = self._read_number(self.entry_a, "Число A")
            b = self._read_number(self.entry_b, "Число B")
            self._show_result(self.engine.calculate(operation, a, b))
        except (ValueError, TypeError, ZeroDivisionError, OverflowError) as error:
            self._show_error(error)

    def perform_unary(self, operation: str) -> None:
        try:
            a = self._read_number(self.entry_a, "Число A")
            self._show_result(self.engine.calculate(operation, a))
        except (ValueError, TypeError, ZeroDivisionError, OverflowError) as error:
            self._show_error(error)

    def _update_memory_label(self) -> None:
        self.memory_label.configure(text=f"Память: {self._format_number(self.engine.read_memory())}")

    def store_memory(self) -> None:
        try:
            self.engine.store_in_memory(self._read_number(self.entry_a, "Число A"))
            self._update_memory_label()
        except (ValueError, TypeError) as error:
            self._show_error(error)

    def recall_memory(self) -> None:
        self.entry_a.delete(0, tk.END)
        self.entry_a.insert(0, self._format_number(self.engine.read_memory()))
        self._update_memory_label()

    def add_memory(self) -> None:
        try:
            self.engine.add_to_memory(self._read_number(self.entry_a, "Число A"))
            self._update_memory_label()
        except (ValueError, TypeError) as error:
            self._show_error(error)

    def clear_memory(self) -> None:
        self.engine.clear_memory()
        self._update_memory_label()


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
