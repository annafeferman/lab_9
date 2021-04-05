from random import randint  # randint для заполнения массива
import timeit  # timeit для рассчета времени выполнения


class MainProgram:
    while True:  # зацикливаем программу
        class DataInput:
            while True:  # зацикливаем проверку на ошибки
                try:
                    old_list = []
                    length = int(input('Array length: '))
                    if length > 30:
                        for i in range(length):
                            old_list.append(randint(0, 100))
                    else:
                        inp = input(
                            'Want to input the array? Print "1". Want to use the example? Print anything else: ')
                        if inp == '1':
                            for i in range(length):
                                old_list.append(int(input(f'Input {i + 1} element: ')))
                        else:
                            for i in range(length):
                                old_list.append(randint(0, 100))
                    method = int(input('\nChoose which sort method you want to use.\n'  # выбор метода сортировки
                                       'Bubble sort - input "1"\n'
                                       'Selection sort - input "2"\n'
                                       'Insertion sort - input "3"\n'
                                       'Cocktail sort - input "4"\n'
                                       'Shell sort - input "5"\n'
                                       'Heap sort - input "6"\n'
                                       ''))
                    up_down = int(input('Ascending list - input "1"\n'  # выбор по возрастанию или по убыванию
                                        'Descending list - input "2"\n'
                                        ''))
                    break
                except (NameError, TypeError, ValueError):
                    print('Wrong value!')

        class SortingMethods:

            @staticmethod
            def bubble_sort_ascending(my_list):
                comparisons = 0
                changes = 0
                last_item = len(my_list) - 1
                for k in range(last_item):  # вложенным циклом перебираем все элементы массива
                    for j in range(last_item - k):
                        if my_list[j] > my_list[j + 1]:  # каждый элемент меньше следующего, меняем с ним местами в с.45
                            comparisons += 1
                            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                            changes += 1

                print('Comparisons_ascending: ', comparisons, '  Changes_ascending: ', changes)  # сравнения и обмены
                return my_list  # возвращаем отсортированный список

            # реализуем тот же метод, только для сортировки массива по убыванию, меняя в условии знак больше на знак меньше

            @staticmethod
            def bubble_sort_descending(my_list):
                comparisons = 0
                changes = 0
                last_item = len(my_list) - 1
                for k in range(last_item):
                    for j in range(last_item):
                        if my_list[j] < my_list[j + 1]:
                            comparisons += 1
                            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                            changes += 2
                print('Comparisons_descending: ', comparisons, '    Changes_descending: ', changes)
                return my_list

            @staticmethod
            def selection_sort_ascending(my_list):
                comparisons = 0
                changes = 0
                for i in range(len(my_list)):
                    min_index = i
                    for j in range(i + 1,
                                   len(my_list)):  # перебираем элементы массива вложенным циклом, сравнивая их значения
                        if my_list[j] < my_list[min_index]:  # где el[j] идет после el[i]
                            comparisons += 1
                            min_index = j
                    my_list[i], my_list[min_index] = my_list[min_index], my_list[
                        i]  # меняем, если найдено нужное значение
                    changes += 1

                print('Comparisons_ascending: ', comparisons, '  Changes_ascending: ',
                      changes)  # считаем сравнения и обмены
                return my_list

            # реализуем тот же метод, только для сортировки массива по убыванию

            @staticmethod
            def selection_sort_descending(my_list):
                comparisons = 0
                changes = 0
                for i in range(len(my_list)):
                    min_index = i
                    for j in range(i + 1, len(my_list)):
                        if my_list[j] > my_list[min_index]:
                            comparisons += 1
                            min_index = j
                    my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
                    changes += 1

                print('Comparisons_descending: ', comparisons, '  Changes_descending: ', changes)
                return my_list

            @staticmethod
            def insertion_sort_ascending(my_list):
                comparisons = 0
                changes = 0
                for i in range(1, len(my_list)):
                    k = my_list[i]  # присваиваем ключу значение номера элемента
                    min_index = i - 1  # начинаем отсчет с минимального номера
                    while min_index >= 0 and my_list[min_index] > k:  # сравниваем значение элемента с прерыдущим
                        comparisons += 2
                        my_list[min_index + 1] = my_list[min_index]  # меняем, если он больше
                        changes += 1
                        min_index -= 1
                    my_list[min_index + 1] = k

                print('Comparisons_ascending: ', comparisons, '  Changes_ascending: ',
                      changes)  # считаем сравнения и обмены
                return my_list

            # реализуем тот же метод, только для сортировки массива по убыванию

            @staticmethod
            def insertion_sort_descending(my_list):
                comparisons = 0
                changes = 0
                for i in range(1, len(my_list)):
                    k = my_list[i]
                    min_index = i - 1
                    while min_index >= 0 and my_list[min_index] < k:
                        comparisons += 2
                        my_list[min_index + 1] = my_list[min_index]
                        changes += 1
                        min_index -= 1
                    my_list[min_index + 1] = k

                print('Comparisons_descending: ', comparisons, '  Changes_descending: ', changes)
                return my_list

            @staticmethod
            def cocktail_sort_ascending(my_list):
                comparisons = 0
                changes = 0
                for i in range(len(my_list) // 2):
                    swap = False  # присваем значенрие фолз в начале каждой итерации
                    for j in range(1 + i, len(my_list) - i):
                        if my_list[j] < my_list[j - 1]:  # используем bubble sort
                            comparisons += 1
                            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                            changes += 1
                            swap = True
                    if not swap:  # если ничего не изменилось, прерываем цикл (элементы отсортированы)
                        break
                    swap = False
                    for j in range(len(my_list) - i - 1, i, -1):  # проходим цикл без последнего элемента
                        if my_list[j] < my_list[j - 1]:  # так как он уже на своем месте
                            comparisons += 1
                            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]  # меняем нужные элементы местами
                            changes += 1
                            swap = True
                    if not swap:  # если ничего не изменилось, прерываем цикл
                        break

                print('Comparisons_ascending: ', comparisons, '  Changes_ascending: ',
                      changes)  # считаем сравнения и обмены
                return my_list

            # реализуем тот же метод, только для сортировки массива по убыванию

            @staticmethod
            def cocktail_sort_descending(my_list):
                comparisons = 0
                changes = 0
                for i in range(len(my_list) // 2):
                    swap = False
                    for j in range(1 + i, len(my_list) - i):
                        if my_list[j] > my_list[j - 1]:
                            comparisons += 1
                            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                            changes += 1
                            swap = True
                    if not swap:
                        break
                    swap = False
                    for j in range(len(my_list) - i - 1, i, -1):
                        if my_list[j] > my_list[j - 1]:
                            comparisons += 1
                            my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
                            changes += 1
                            swap = True
                    if not swap:
                        break

                print('Comparisons_descending: ', comparisons, '  Changes_descending: ', changes)
                return my_list

            @staticmethod
            def shell_sort_ascending(my_list):
                comparisons = 0
                changes = 0
                n = len(my_list)
                gap = n // 2  # устанавливаем базовый шаг, деля длину массива на 2, потом он будет уменьшатся
                while gap > 0:  # цикл выполняется до тех пор, пока окончательно не уменьшится шаг
                    comparisons += 1
                    for i in range(gap, n):
                        temp = my_list[i]  # добавляем элемент, который уже отсортирован, во временную переменную
                        j = i  # добавляем отсортированные элементы на нужную позицию
                        while j >= gap and my_list[j - gap] > temp:
                            comparisons += 2
                            my_list[j] = my_list[j - gap]  # меняем элементы местами
                            changes += 1
                            j -= gap

                        my_list[j] = temp  # возвращаем значения из временной переменной на нужное место
                    gap //= 2

                print('Comparisons_ascending: ', comparisons, '  Changes_ascending: ',
                      changes)  # считаем сравнения и обмены
                return my_list

            # реализуем тот же метод, только для сортировки массива по убыванию

            @staticmethod
            def shell_sort_descending(my_list):
                comparisons = 0
                changes = 0
                n = len(my_list)
                gap = n // 2
                while gap > 0:
                    comparisons += 1
                    for i in range(gap, n):
                        temp = my_list[i]
                        j = i
                        while j >= gap and my_list[j - gap] < temp:
                            comparisons += 2
                            my_list[j] = my_list[j - gap]
                            changes += 1
                            j -= gap

                        my_list[j] = temp
                    gap //= 2

                print('Comparisons_ascending: ', comparisons, '  Changes_ascending: ', changes)
                return my_list

            # получив сортирующее бинарное дерево в преыдущей функции, используем его,
            # чтобы отсортировать элемента из массива,
            # для этого проходим по ним циклами в строках 261 - 266

            @staticmethod
            def heap_sort_ascending(my_list):
                def heapify_asc(my_list, n, i):
                    largest = i  # присваиваем значение самого большого элемента
                    left = 2 * i + 1  # разбиваем условно дерево на левую и правую части
                    right = 2 * i + 2

                    if left < n and my_list[i] < my_list[
                        left]:  # цикл сверяет значение левого и правого элемента каждой "подветки"
                        largest = left

                    if right < n and my_list[largest] < my_list[
                        right]:  # то же самое, если наибольшее значение - справа
                        largest = right

                    if largest != i:
                        my_list[i], my_list[largest] = my_list[largest], my_list[
                            i]  # меняем неотсортированные элементы,
                        # чтобы получить сортирующее бинарное дерево
                        heapify_asc(my_list, n, largest)
                    return my_list

                n = len(my_list)
                heapify_asc(my_list, n, 0)

                for i in range(n, -1, -1):
                    heapify_asc(my_list, n, i)

                for i in range(n - 1, 0, -1):
                    my_list[i], my_list[0] = my_list[0], my_list[i]
                    heapify_asc(my_list, i, 0)

                return my_list

            # реализуем тот же метод, только для сортировки массива по убыванию

            @staticmethod
            def heap_sort_descending(my_list):
                def heapify_desc(my_list, n, i):
                    smallest = i
                    left = 2 * i + 1
                    right = 2 * i + 2

                    if left < n and my_list[i] > my_list[left]:
                        smallest = left

                    if right < n and my_list[smallest] > my_list[right]:
                        smallest = right

                    if smallest != i:
                        my_list[i], my_list[smallest] = my_list[smallest], my_list[i]

                        heapify_desc(my_list, n, smallest)

                n = len(my_list)

                for i in range(n, -1, -1):
                    heapify_desc(my_list, n, i)

                for i in range(n - 1, 0, -1):
                    my_list[i], my_list[0] = my_list[0], my_list[i]
                    heapify_desc(my_list, i, 0)

                return my_list

        if 1 <= DataInput.method <= 6 and 1 <= DataInput.up_down <= 2:
            print('Old list: ', DataInput.old_list)  # выводим старый список
            # учитывая выбор пользователя, запускаем нужную функцию (строки 304 - 327)
            if DataInput.method == 1 and DataInput.up_down == 1:
                print('Ascending new list: ', SortingMethods.bubble_sort_ascending(DataInput.old_list).copy())
            elif DataInput.method == 1 and DataInput.up_down == 2:
                print('Descending new list: ', SortingMethods.bubble_sort_descending(DataInput.old_list).copy())
            elif DataInput.method == 2 and DataInput.up_down == 1:
                print('Ascending new list: ', SortingMethods.selection_sort_ascending(DataInput.old_list).copy())
            elif DataInput.method == 2 and DataInput.up_down == 2:
                print('Descending new list: ', SortingMethods.selection_sort_descending(DataInput.old_list).copy())
            elif DataInput.method == 3 and DataInput.up_down == 1:
                print('Ascending new list: ', SortingMethods.insertion_sort_ascending(DataInput.old_list).copy())
            elif DataInput.method == 3 and DataInput.up_down == 2:
                print('Descending new list: ', SortingMethods.insertion_sort_descending(DataInput.old_list).copy())
            elif DataInput.method == 4 and DataInput.up_down == 1:
                print('Ascending new list: ', SortingMethods.cocktail_sort_ascending(DataInput.old_list).copy())
            elif DataInput.method == 4 and DataInput.up_down == 2:
                print('Descending new list: ', SortingMethods.cocktail_sort_descending(DataInput.old_list).copy())
            elif DataInput.method == 5 and DataInput.up_down == 1:
                print('Ascending new list: ', SortingMethods.shell_sort_ascending(DataInput.old_list).copy())
            elif DataInput.method == 5 and DataInput.up_down == 2:
                print('Descending new list: ', SortingMethods.shell_sort_descending(DataInput.old_list).copy())
            elif DataInput.method == 6 and DataInput.up_down == 1:
                print('Ascending new list: ', SortingMethods.heap_sort_ascending(DataInput.old_list).copy())
            elif DataInput.method == 6 and DataInput.up_down == 2:
                print('Descending new list: ', SortingMethods.heap_sort_descending(DataInput.old_list).copy())

            print('Program execution time is ', timeit.timeit(number=100000))

            repeat = input('Input 1 if you want to restart the program. If you do not, input anything else: ')
            if repeat == '1':  # хочет повторить программу
                continue
            else:
                break
        else:
            print('You have probably entered a method that does not exist. You must choose an item from the list.'
                  ' For now, we suggest you restarting the program.')
            repeat = input('Input 1 if you want to restart the program. If you do not, input anything else: ')
            if repeat == '1':  # хочет повторить программу
                continue
            else:
                break


MainProgram()
