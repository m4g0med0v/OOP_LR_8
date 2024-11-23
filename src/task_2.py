#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу:
# Перепишите программу из пункта 8 так, чтобы интерфейс
# выглядел подругому.


import tkinter as tk


def display_color(color_code: str, color_name: str) -> None:
    entry_color.delete(0, tk.END)
    entry_color.insert(0, color_code)
    label_color_name.config(text=color_name)


# Создание окна
window = tk.Tk()
window.title("Цвета радуги")

color_frame = tk.Frame(window)
output_frame = tk.Frame(window)

# Словарь цветов
rainbow_colors = {
    "Красный": "#ff0000",
    "Оранжевый": "#ff7d00",
    "Желтый": "#ffff00",
    "Зеленый": "#00ff00",
    "Голубой": "#007dff",
    "Синий": "#0000ff",
    "Фиолетовый": "#7d00ff",
}

# Создание кнопок
for color_name, color_code in rainbow_colors.items():
    button = tk.Button(
        color_frame,
        bg=color_code,
        fg="white",
        command=lambda c=color_code, n=color_name: display_color(c, n),  # type: ignore[misc]
    )
    button.pack(fill=tk.X, ipadx=10, ipady=2, side=tk.LEFT)

# Текстовое поле для кода цвета
entry_color = tk.Entry(output_frame, font=("Arial", 14), justify="center")
entry_color.pack(padx=5, pady=10, side=tk.BOTTOM)

# Метка для названия цвета
label_color_name = tk.Label(output_frame, text="", font=("Arial", 16))
label_color_name.pack(padx=5, pady=10, side=tk.BOTTOM)


color_frame.pack(side=tk.BOTTOM)
output_frame.pack(side=tk.BOTTOM)

if __name__ == "__main__":
    # Запуск приложения
    window.mainloop()
