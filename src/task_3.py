#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу:
# Напишите программу, состоящую из однострочного и многострочного текстовых
# полей и двух кнопок "Открыть" и "Сохранить". При клике на первую должен
# открываться на чтение файл, чье имя указано в поле класса Entry , а
# содержимое файла должно загружаться в поле типа Text . При клике на вторую
# кнопку текст, введенный пользователем в экземпляр Text , должен сохраняться
# в файле под именем, которое пользователь указал в однострочном текстовом
# поле. Файлы будут читаться и записываться в том же каталоге, что и файл
# скрипта, если указывать имена файлов без адреса. Для выполнения практической
# работы вам понадобится функция open языка Python и методы файловых объектов
# чтения и записи. Освежить знания о файлах можно из материала лабораторной
# работы 9.


import tkinter as tk
from tkinter import messagebox


def open_file() -> None:
    file_name = entry_file_name.get()  # Получаем имя файла из поля Entry
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)  # Очищаем поле Text
            text_area.insert(tk.END, file.read())  # Загружаем содержимое файла
    except FileNotFoundError:
        messagebox.showerror("Ошибка", f"Файл '{file_name}' не найден.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")


def save_file() -> None:
    file_name = entry_file_name.get()  # Получаем имя файла из поля Entry
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(
                text_area.get("1.0", tk.END)
            )  # Сохраняем содержимое поля Text в файл
        messagebox.showinfo("Успех", f"Файл '{file_name}' успешно сохранен.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")


# Создаем главное окно
window = tk.Tk()
window.title("Работа с файлами")

# Однострочное текстовое поле для ввода имени файла
entry_file_name = tk.Entry(window, width=50)
entry_file_name.pack(pady=5)

# Кнопка "Открыть"
button_open = tk.Button(window, text="Открыть", command=open_file)
button_open.pack(pady=5)

# Многострочное текстовое поле для содержимого файла
text_area = tk.Text(window, width=60, height=20, wrap=tk.WORD)
text_area.pack(pady=5)

# Кнопка "Сохранить"
button_save = tk.Button(window, text="Сохранить", command=save_file)
button_save.pack(pady=5)


if __name__ == "__main__":
    # Запуск приложения
    window.mainloop()
