from random import randint  # randint для заполнения массива
import timeit  # timeit для рассчета времени выполнения


class DataInput:

    def arrayInput(self):
        while True:
            try:
                oldList = []
                length = int(input('Array length: '))
                if length > 30:
                    for i in range(length):
                        oldList.append(randint(0, 100))
                else:
                    inp = input(
                        'Want to input the array? Print "1". Want to use the example? Print anything else: ')
                    if inp == '1':
                        for i in range(length):
                            oldList.append(int(input(f'Input {i + 1} element: ')))
                    else:
                        for i in range(length):
                            oldList.append(randint(0, 100))
                break
            except (NameError, TypeError, ValueError):
                print('Wrong value!')
        return oldList

    def getMethod(self):
        while True:
            try:
                method = int(input('\nChoose which sort method you want to use.\n'  # выбор метода сортировки
                                   'Bubble sort - input "1"\n'
                                   'Selection sort - input "2"\n'
                                   'Insertion sort - input "3"\n'
                                   'Cocktail sort - input "4"\n'
                                   'Shell sort - input "5"\n'
                                   ''))
                break
            except (NameError, TypeError, ValueError):
                print('Wrong value!')
        return method

    def getUpDown(self):
        while True:
            try:
                upDown = int(input('\nAscending list - input "1"\n'
                                   'Descending list - input "2"\n'
                                   ''))
                break
            except (NameError, TypeError, ValueError):
                print('Wrong value!')
        return upDown


class BubbleSort:


    def sortedArray(self, my_list, up_down):
        comparisons = 0
        changes = 0
        last_item = len(my_list) - 1
        for k in range(last_item):  # вложенным циклом перебираем все элементы массива
            for j in range(last_item - k):
                if (up_down == 1 and my_list[j] > my_list[j + 1]) or (up_down == 2 and my_list[j] < my_list[j + 1]):
                    comparisons += 1
                    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                    changes += 1

        print('Sorted list: ', my_list)
        print('Comparisons: ', comparisons, '  Changes: ', changes)  # сравнения и обмены
        print('This is bubble sort')


class SelectionSort:


    def sortedArray(self, my_list, up_down):
        comparisons = 0
        changes = 0
        for i in range(len(my_list)):
            min_index = i
            for j in range(i + 1, len(my_list)):
                if (up_down == 1 and my_list[j] < my_list[min_index]) or (up_down == 2 and my_list[j] > my_list[min_index]):
                    comparisons += 1
                    min_index = j
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
            changes += 1

        print('Sorted list: ', my_list)
        print('Comparisons: ', comparisons, '  Changes: ', changes)  # сравнения и обмены
        print('This is selection sort')


class InsertionSort:


    def sortedArray(self, my_list, up_down):
        comparisons = 0
        changes = 0
        for i in range(1, len(my_list)):
            k = my_list[i]  # присваиваем ключу значение номера элемента
            min_index = i - 1  # начинаем отсчет с минимального номера
            while (up_down == 1 and min_index >= 0 and my_list[min_index] > k) or (
                    up_down == 2 and min_index >= 0 and my_list[
                min_index] < k):  # сравниваем значение элемента с прерыдущим
                comparisons += 2
                my_list[min_index + 1] = my_list[min_index]  # меняем, если он больше
                changes += 1
                min_index -= 1
            my_list[min_index + 1] = k

        print('Sorted list: ', my_list)
        print('Comparisons: ', comparisons, '  Changes: ', changes)  # сравнения и обмены
        print('This is insertion sort')


class CocktailSort:


    def sortedArray(self, my_list, up_down):
        comparisons = 0
        changes = 0
        for i in range(len(my_list) // 2):
            swap = False  # присваем значенрие фолз в начале каждой итерации
            for j in range(1 + i, len(my_list) - i):
                if (up_down == 1 and my_list[j] < my_list[j - 1]) or (up_down == 2 and my_list[j] > my_list[j - 1]):  # используем bubble sort
                    comparisons += 1
                    my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                    changes += 1
                    swap = True
            if not swap:  # если ничего не изменилось, прерываем цикл (элементы отсортированы)
                break
            swap = False
            for j in range(len(my_list) - i - 1, i, -1):  # проходим цикл без последнего элемента
                if (up_down == 1 and my_list[j] < my_list[j - 1]) or (up_down == 2 and my_list[j] > my_list[j - 1]):  # так как он уже на своем месте
                    comparisons += 1
                    my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]  # меняем нужные элементы местами
                    changes += 1
                    swap = True
            if not swap:  # если ничего не изменилось, прерываем цикл
                break

        print('Sorted list: ', my_list)
        print('Comparisons: ', comparisons, '  Changes: ', changes)  # сравнения и обмены
        print('This is cocktail sort')


class ShellSort:


    def sortedArray(self, my_list, up_down):
        comparisons = 0
        changes = 0
        n = len(my_list)
        gap = n // 2  # устанавливаем базовый шаг, деля длину массива на 2, потом он будет уменьшатся
        while gap > 0:  # цикл выполняется до тех пор, пока окончательно не уменьшится шаг
            comparisons += 1
            for i in range(gap, n):
                temp = my_list[i]  # добавляем элемент, который уже отсортирован, во временную переменную
                j = i  # добавляем отсортированные элементы на нужную позицию
                while (up_down == 1 and j >= gap and my_list[j - gap] > temp) or (up_down == 2 and j >= gap and my_list[j - gap] < temp):
                    comparisons += 2
                    my_list[j] = my_list[j - gap]  # меняем элементы местами
                    changes += 1
                    j -= gap

                my_list[j] = temp  # возвращаем значения из временной переменной на нужное место
            gap //= 2

        print('Sorted list: ', my_list)
        print('Comparisons: ', comparisons, '  Changes: ', changes)  # сравнения и обмены
        print('This is shell sort')


def SortMethod():
    method = DataInput.getMethod(DataInput)
    if method == 1:
        return BubbleSort
    elif method == 2:
        return SelectionSort
    elif method == 3:
        return InsertionSort
    elif method == 4:
        return CocktailSort
    else:
        return ShellSort


def RunProgram():
    while True:
        oldList = DataInput.arrayInput(DataInput)
        sortMethod = SortMethod()
        upDown = DataInput.getUpDown(DataInput)
        print('\nOld list: ', oldList)
        b = sortMethod()
        b.sortedArray(oldList, upDown)
        print('Program execution time is ', timeit.timeit(number=100000))
        repeat = input('\nInput 1 if you want to restart the program. If you do not, input anything else: ')
        if repeat == '1':  # хочет повторить программу
            continue
        else:
            break


RunProgram()