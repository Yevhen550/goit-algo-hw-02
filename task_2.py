from collections import deque


def is_palindrome(s):
    # Перетворити рядок на нижній регістр та видалити всі пробіли
    s = s.lower().replace(" ", "")

    # Створити двосторонню чергу
    d = deque(s)

    # Порівнювати символи з обох кінців черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


# Користувач вводить рядок і перевіряється чи є він паліндромом
while True:
    s = input("Введіть рядок: ")
    if s == "":
        break
    if is_palindrome(s):
        print("Цей рядок є паліндромом.")
    else:
        print("Цей рядок не є паліндромом.")
