from tkinter import Button, Label, Tk


def take():
    lab["text"] = "Выдано"


root = Tk()
Label(text="Пункт выдачи").pack()
Button(text="Взять", command=take).pack()
lab = Label(width=10, height=1)
lab.pack()
root.mainloop()
