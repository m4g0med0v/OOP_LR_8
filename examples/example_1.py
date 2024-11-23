from tkinter import Button, Entry, Label, Tk


# Функция-событие
def str_to_sort_list(event):
    s = ent.get()
    s = s.split()
    s.sort()
    lab["text"] = " ".join(s)


# Основное окно
root = Tk()

# Виджеты окна
ent = Entry(width=20)
but = Button(text="Преобразовать")
lab = Label(width=20, bg="black", fg="white")


# Регистранция события
but.bind("<Button-1>", str_to_sort_list)

# Расположение виджетов
ent.pack()
but.pack()
lab.pack()

# Запусе цикла
root.mainloop()
