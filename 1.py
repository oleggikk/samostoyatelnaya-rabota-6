key = True
while key:
    a = []
    flag = True
    print('Сколько элементов вы хотите хранить в массиве? \nВведите целочисленное положительное значение: ')
    while flag:
        try:
            N = int(input())
        except ValueError:
            print("Ошибка, количество элементов массива должно быть положительным, целым и большим единицы.\nПовторите ввод: ")
        else:
            if N < 0:
                print('Вы ввели отрицательное значение.\nПовторите ввод: ')
            if N == 0:
                print('Массив не может состоять из нуля элементов. \nПовторите ввод: ')
            if N == 1:
                print('Выполение задачи невозможно для одного элемента. Минимальное количество элементов для выполения программы - два. \nПовторите ввод: ')
            if N > 1:
                flag = False
    print("Введите значения для ", N, " элементов, каждый с новой строки")
    for i in range(0, N):
        print('Введите целочисленное значение для ', i+1, 'элемента: ')
        flag = True
        while flag:
            try:
                k = int(input())
            except ValueError:
                print('Ошибка. Вы ввели не целое вещественное число или текст.\nВведите целочисленное значение для ', i+1, 'элемента: ')
            else:
                flag = False
        a.append(k)
    print('Введите значение для переменной DELTA')
    flag = True
    while flag:
        try:
            k = int(input())
        except ValueError:
            print('Ошибка. Значение переменной DELTA должно быть целым и неотрицательным.\nПовторите ввод: ')
        else:
            if k < 0:
                print('Вы ввели отрицательное значение. \nПовторите ввод: ')
            else:
                flag = False
    delta = k
    print('Ответ: ', a.count(min(a) + delta))
    print('Программа была выполнена. Хотете повторить программу с другими числами? Введите y или n, где y - да, n - нет')
    flag = True
    while flag:
        answer = input().lower()
        if answer == 'y' or answer == 'n':
            flag = False
        else:
            print('Введите y или n')
    if answer == 'n':
        key = False