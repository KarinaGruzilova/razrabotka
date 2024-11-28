from tkinter import *
from tkinter import ttk  # Для стилей ttk
import tkinter.font as tkFont  # Для работы со шрифтами

def lb1():
    new_window = Toplevel(window)  # Создаем новое окно, связанное с основным
    new_window.title("Задача")  # Устанавливаем заголовок нового окна
    new_window.geometry('300x100')  # Устанавливаем размер нового окна
    new_label = Label(new_window, text="Приветствие", font=("Arial Bold", 12))  # Создаем метку в новом окне
    new_label.pack(pady=10)  # Размещаем метку в новом окне
    name = Label(new_window, text="Как вас зовут?", font=("Arial Bold", 12))
    name.pack(pady=0)

    # Поле для ввода имени
    entry1 = Entry(new_window)
    entry1.pack(pady=5)

    def privet():
        try:
            namepriv = entry1.get()
            result_label.config(text=f"Добро пожаловать {namepriv}")
        except ValueError:
            result_label.config(text="Ошибка: Введите буквы!")

    # Кнопка
    calculate_button = Button(new_window, text="Поприветствовать", command=privet)
    calculate_button.pack(pady=5)

    # Метка для вывода
    result_label = Label(new_window, text="", font=("Arial Bold", 12))
    result_label.pack(pady=5)
        

def lb2():
    new_window = Toplevel(window)  # Создаем новое окно, связанное с основным
    new_window.title("Задача")
    new_window.geometry('300x100')  
    new_label = Label(new_window, text="Задача:", font=("Arial Bold", 12)) 
    new_label.pack(pady=10)  # Размещаем метку в новом окне

    # Ввод первого числа
    entry1 = Entry(new_window)
    entry1.pack(pady=5)

    # Ввод второго числа
    entry2 = Entry(new_window)
    entry2.pack(pady=5)

    # Выбор операции
    operation = StringVar(new_window)
    operation.set("Сложение")  # Значение по умолчанию
    operation_menu = OptionMenu(new_window, operation, "Сложение", "Вычитание","Умнажение","Деление")
    operation_menu.pack(pady=5)

    def calculate():
        try:
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            if operation.get() == "Сложение":
                result = num1 + num2
            elif operation.get() == "Вычитание":
                result = num1 - num2
            elif operation.get() == "Умнажение":
                result = num1 * num2
            elif operation.get() == "Деление":
                if num2 != 0 :
                    result = num1 / num2
                else:
                    result_label.config(text="Ошибка: На ноль нельзя делить!")

            result_label.config(text=f"Результат: {result}")
        except ValueError:
            result_label.config(text="Ошибка: Введите числа!")

    # Кнопка "Рассчитать"
    calculate_button = Button(new_window, text="Рассчитать", command=calculate)
    calculate_button.pack(pady=10)

    # Метка для вывода результата
    result_label = Label(new_window, text="", font=("Arial Bold", 12))
    result_label.pack(pady=5)

    
def lb3():
    new_window = Toplevel(window)  # Создаем новое окно, связанное с основным
    new_window.title("Задача")
    new_window.geometry('300x100')  

    spisok = []
    result_label = Label(new_window, text="", font=("Arial Bold", 12))
    result_label.pack(pady=5)

    def spiski(label):
        nonlocal spisok
        spisok = [randint(0, 100) for i in range(10)]
        label.config(text=f"Список: {', '.join(map(str, spisok))}")
        return spisok


    def operation(func, label, *args):
        try:
            result = func(*args)
            label.config(text=f"Результат: {result}")
        except Exception as e:
            label.config(text=f"Ошибка: {e}")

    calculate_button = Button(new_window, text="Генерация списка:", command=lambda: spiski(result_label))
    calculate_button.pack(pady=5)

    sorted_button = Button(new_window, text="Сортировать", command=lambda: operation(lambda x: ', '.join(map(str, sorted(x))), result_label, spisok))
    sorted_button.pack(pady=5)

    minmax_button = Button(new_window, text="Найти max и min значения", command=lambda: operation(lambda x: f"Min: {min(x)}, Max: {max(x)}", result_label, spisok))
    minmax_button.pack(pady=5)

    summa_button = Button(new_window, text="Сумма значений", command=lambda: operation(sum, result_label, spisok))
    summa_button.pack(pady=5)

def lb4():
    new_window = tk.Toplevel()
    new_window.title("Задача")
    new_window.geometry('350x200')

    result_label = Label(new_window, text="", font=("Arial Bold", 12))
    result_label.pack(pady=5)

    def create_file(filename):
        try:
            with open(filename, 'w') as f:
                numbers = sample(range(1, 11), 10)
                f.write(' '.join(map(str, numbers)))
            result_label.config(text=f"Создан {filename}: {numbers}")
        except Exception as e:
            result_label.config(text=f"Ошибка: {e}")


    def calculate_average(filename):
        try:
            with open(filename, 'r') as f:
                numbers = [int(x) for x in f.read().split()]
                average = sum(numbers) / len(numbers) if numbers else 0
                result_label.config(text=f"Среднее {filename}: {average}")
        except FileNotFoundError:
            result_label.config(text="Ошибка: Файл не найден.")
        except ValueError:
            result_label.config(text="Ошибка: Неверные данные в файле.")
        except Exception as e:
            result_label.config(text=f"Ошибка: {e}")

    Button(new_window, text="Создать myfile.txt", command=lambda: create_file('myfile.txt')).pack(pady=5)
    Button(new_window, text="Создать myfile2.txt", command=lambda: create_file('myfile2.txt')).pack(pady=5)
    Button(new_window, text="Среднее (myfile.txt)", command=lambda: calculate_average('myfile.txt')).pack(pady=5)
    Button(new_window, text="Среднее (myfile2.txt)", command=lambda: calculate_average('myfile2.txt')).pack(pady=5)
    Button(new_window, text="Выбрать файл", command=lambda: calculate_average(fd.askopenfilename())).pack(pady=5)

class Animal:
    animals_count = 0

    def __init__(self, name, country, diet):
        self.name = name
        self.country = country
        self.diet = diet
        Animal.animals_count += 1

    def __str__(self):
        return f"Животное: {self.name}. Страна обитания: {self.country}. Рацион: {self.diet}"


class EndangeredAnimal(Animal):
    def __init__(self, name, country, diet, conservation_status, population):
        super().__init__(name, country, diet)
        self.conservation_status = conservation_status
        self.population = population

    def __str__(self):
        return f"{super().__str__()} Статус сохранения: {self.conservation_status}. Популяция: {self.population}"


def lb5():
    new_window = tk.Toplevel()
    new_window.title("Животные")
    new_window.geometry('450x300')

    animal_info_label = Label(new_window, text="", wraplength=400)
    animal_info_label.pack(pady=10)

    animals = [
        Animal("Тигр", "Азия", "Хищник"),
        Animal("Зебра", "Африка", "Травоядное"),
        EndangeredAnimal("Амурский тигр", "Россия", "Хищник", "На грани исчезновения", 500),
        EndangeredAnimal("Горная горилла", "Африка", "Травоядное", "Уязвимый вид", 10000)
    ]

    def display_animal_info(animal_list):
        animal_info_label.config(text="\n".join(map(str, animal_list)))
        animal_info_label.config(text=animal_info_label.cget("text") + f"\nВсего животных: {Animal.animals_count}")

    Button(new_window, text="Узнать о животных", command=lambda: display_animal_info(animals)).pack(pady=5)
    Button(new_window, text="Узнать о животных под угрозой", command=lambda: display_animal_info([a for a in animals if isinstance(a, EndangeredAnimal)])).pack(pady=5)

    display_animal_info(animals)
window = Tk()
window.geometry('700x250')
window.title("Лабораторные работы")
from random import randint
import tkinter as tk
from tkinter import Toplevel, Button, Label, ttk
from tkinter import filedialog as fd
from random import sample
import os

#1 Дизайн
window.configure(bg="#F8E8FF")

style = ttk.Style()
style.configure("TButton", background="#E6B8FF",
                 foreground="#9400D3",  
                 font=("Arial Bold", 14),
                 padding=10)  

style.map("TButton",
    foreground=[('active', '#FFFFFF'), ('pressed', '#FFFFFF')],  
    background=[('active', '#9400D3'), ('pressed', '#9400D3')]) 


lbl = Label(window, text="Лабораторные работы", font=("Arial Bold", 20), bg="#F8E8FF", fg="#9400D3")  
lbl.grid(column=0, row=0, padx=20, pady=20)

 

# 2 Кнопки
btn1 = ttk.Button(window, text="Лаба 1", command=lb1, style="TButton")
btn1.grid(column=0, row=1, padx=20, pady=10)

btn2 = ttk.Button(window, text="Лаба 2", command=lb2, style="TButton")
btn2.grid(column=0, row=2, padx=20, pady=10)

btn1 = ttk.Button(window, text="Лаба 3", command=lb3, style="TButton")
btn1.grid(column=1, row=1, padx=20, pady=10)

btn2 = ttk.Button(window, text="Лаба 4", command=lb4, style="TButton")
btn2.grid(column=1, row=2, padx=20, pady=10)

btn1 = ttk.Button(window, text="Лаба 5", command=lb5, style="TButton")
btn1.grid(column=2, row=1, padx=20, pady=10)

window.mainloop() #окно будет ждать любого взаимодействия с пользователем, пока не будет закрыто

