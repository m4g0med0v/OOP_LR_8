#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу:
# Напишите простейший калькулятор, состоящий из двух текстовых полей, куда
# пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". Результат
# вычисления должен отображаться в метке. Если арифметическое действие
# выполнить невозможно (например, если были введены буквы, а не числа),
# то в метке должно появляться слово "ошибка".

import tkinter as tk


def calculate(operation: str) -> None:
    try:
        # Преобразуем введенные значения в числа
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        # Выполняем соответствующую операцию
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        # Отображаем результат
        label_result.config(text=f"Результат: {result}")
    except (ValueError, ZeroDivisionError):
        # Обрабатываем ошибки ввода или деления на ноль
        label_result.config(text="Ошибка")


# Создаем главное окно
window = tk.Tk()
window.title("Калькулятор")

# Создаем рамки для группировки элементов
top_frame = tk.Frame(window)
middle_frame = tk.Frame(window)
bottom_frame = tk.Frame(window)

# Поля ввода для чисел
entry1 = tk.Entry(top_frame)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(top_frame)
entry2.grid(row=0, column=2, padx=5, pady=5)

# Кнопки для выполнения операций
button_add = tk.Button(middle_frame, text="+", command=lambda: calculate("+"))
button_add.grid(row=1, column=0, padx=5, pady=5)

button_sub = tk.Button(middle_frame, text="-", command=lambda: calculate("-"))
button_sub.grid(row=1, column=1, padx=5, pady=5)

button_mul = tk.Button(middle_frame, text="*", command=lambda: calculate("*"))
button_mul.grid(row=1, column=2, padx=5, pady=5)

button_div = tk.Button(middle_frame, text="/", command=lambda: calculate("/"))
button_div.grid(row=1, column=3, padx=5, pady=5)

# Метка для отображения результата
label_result = tk.Label(bottom_frame, text="Результат: ")
label_result.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

# Размещаем рамки в основном окне
top_frame.pack()
middle_frame.pack()
bottom_frame.pack()

if __name__ == "__main__":
    # Запускаем главный цикл приложения
    window.mainloop()
