import random

number = random.randint(1, 100)
while True:
    try:
        user = int(input("Угадайте число от 1 до 100:"))
        if user == number:
            print("Вы угадали число!")
            break
        elif user > number:
            print("Загаданное число меньше")
        else:
            print("Загаданное число больше")
    except ValueError as e:
        print("Вы не ввели число!")