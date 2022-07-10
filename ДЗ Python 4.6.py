from itertools import count

print("<<Бесконечный итератор целых чисел, начиная с указанного>>")
n = int(input("Введите целое число:"))

for i in count(n):
    print(i, end=' ')

    from itertools import cycle

    list = [23, 4, 6, 44, 42, 2, 4, 6, 7, 45]
    for i in cycle(list):
        print(i, end=' ') 