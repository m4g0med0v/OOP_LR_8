#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу:
# Виджеты Radiobatton и Checkbutton поддерживают большинство свойств оформления
# внешнего вида, которые есть у других элементов графического интерфейса. При
# этом у Radiobutton есть особое свойство indicatoron . По-умолчанию он равен
# единице, в этом случае радиокнопка выглядит как нормальная радиокнопка.
# Однако если присвоить этой опции ноль, то виджет Radiobutton становится
# похожим на обычную кнопку по внешнему виду. Но не по смыслу. Напишите
# программу, в которой имеется несколько объединенных в группу радиокнопок,
# индикатор которых выключен ( indicatoron=0 ). Если какая-нибудь кнопка
# включается, то в метке должна отображаться соответствующая ей информация.
# Обычных кнопок в окне быть не должно.

import tkinter as tk


def update_phone() -> None:
    label_phone.config(text=f"Номер телефона: {phonebook[selected_name.get()]}")


# Создаем главное окно
window = tk.Tk()
window.title("Телефонная книга")

# Словарь с именами и номерами телефонов
phonebook = {
    "Алексей": "+7-900-123-45-67",
    "Мария": "+7-901-234-56-78",
    "Иван": "+7-902-345-67-89",
    "Ольга": "+7-903-456-78-90",
}

# Переменная для хранения выбранного имени
selected_name = tk.StringVar()
selected_name.set("")  # По умолчанию ничего не выбрано

# Левая колонка для отображения номера телефона
frame_left = tk.Frame(window, padx=10, pady=10)
frame_left.pack(side=tk.LEFT, fill=tk.BOTH)

label_phone = tk.Label(frame_left, text="Номер телефона:", font=("Arial", 14))
label_phone.pack()

# Правая колонка для радиокнопок
frame_right = tk.Frame(window, padx=10, pady=10)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH)

# Создание радиокнопок
for name in phonebook:
    rb = tk.Radiobutton(
        frame_right,
        text=name,
        value=name,
        variable=selected_name,
        command=update_phone,
        indicatoron=False,  # Отключаем индикатор
        width=15,
        pady=5,
    )
    rb.pack(anchor="w", pady=2)


if __name__ == "__main__":
    # Запуск приложения
    window.mainloop()
