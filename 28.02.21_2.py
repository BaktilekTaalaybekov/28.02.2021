import random
a = random.randint(1,21)
c = 0
b = c
for x in range(5):
    b = int(input())
    c = b
    if a == b:
        print("Класс! Вы угадали")
        break
    elif a > b:
        print("слишком мало")
    elif a < b:
        print("слишком много")

if a != c:
    print("Все, вы не выиграли.Игра завершилась")

