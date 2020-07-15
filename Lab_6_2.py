import lab6_str_func
list_of_elements = [1, 8, 9, 2, 1, 5, 6, 9, 4, 5]

value = 5
sequence = [9, 2]
print(f"Список елементів - {list_of_elements}")
print("\n")
print("--Виберіть дію--")
while True:
    choose = input("\t1 - Сортування;\n\t2 - Пошук елементу за значенням;\n\t3 - Пошук послідовності елементів;\
\n\t4 - Пошук перших п’яти мінімальних елементів;\n\t5 - Пошук перших п’яти максимальних елементів;\
\n\t6 - Пошук середнього арифметичного;\n\t7 - Отримати список без повторень.\nВаш вибір - ")
    if choose == '1':
        print("\n")
        print(lab6_str_func.sort_list(list_of_elements))
    elif choose == '2':
        print("\n")
        print(lab6_str_func.find_element(list_of_elements, value))
    elif choose == '3':
        print("\n")     print(lab6_str_func.find_sequence(list_of_elements, sequence))
    elif choose == '4':
        print("\n")
        print(lab6_str_func.find_5_min(list_of_elements))
    elif choose == '5':
        print("\n")
        print(lab6_str_func.find_5_max(list_of_elements))
    elif choose == '6':
        print("\n")
        print(lab6_str_func.get_avg(list_of_elements))
    elif choose == '7':
        print("\n")
   print(lab6_str_func.distinct_elements(list_of_elements))
lab6_str_func.py
def sort_list(unsorted_list):
    """
    Сортування
    :param unsorted_list: несортований список
    :return: сортований список
    """
    return f"Сортований список{sorted(unsorted_list)}"


def find_element(list_of_elements, find_element):
    """
    Пошук елементу за значенням
    :param list_of_elements: список елементів
    :param find_element: значення елементу
    :return: True/False
    """
    if find_element in list_of_elements:
        return f"Елемент -{find_element}- знайдено у списку"
    else:
        return f"Елемент -{find_element}- незнайдено у списку"
def find_sequence(list_of_elements, sequence):
    """
    Пошук послідовності елементів
    :param list_of_elements: список елементів
    :param sequence: шукану послідовність
    :return: True/False
    """
    if sequence[0] in list_of_elements:
        start_index = list_of_elements.index(sequence[0])
        for i in sequence[1:]:
            start_index += 1
            if i == list_of_elements[start_index]:
                continue
            else:
                return f"Послідовність -{sequence}- незнайдено у списку"
        return f"Послідовність -{sequence}- знайдено у списку"
    else:
        return f"Послідовність -{sequence}- незнайдено у списку"
def find_5_min(list_of_elements):
    """
    Пошук перших п’яти мінімальних елементів
    :param list_of_elements: список елементів
    """
    if len(list_of_elements) < 5:
        return "Список має менше пяти елементів!"
    else:
        sorted_list = sorted(list_of_elements.copy())
        return sorted_list[:5]
def find_5_max(list_of_elements):
    """
    Пошук перших п’яти максимальних елементів
    :param list_of_elements: список елементів
    """
    if len(list_of_elements) < 5:
        return "Список має менше пяти елементів!"
    else:
        sorted_list = sorted(list_of_elements.copy())
        max_5 = sorted_list[-5:].copy()
        max_5.reverse()
        return max_5
def get_avg(list_of_elements):
    """
    Пошук середнього арифметичного
    :param list_of_elements: список елементів
    :return: середнє арифметичне
    """
    return sum(list_of_elements)/len(list_of_elements)
def distinct_elements(list_of_elements):
    """
    Повернення списку, що сформований з початкового списку, але не містить повторів (залишається лише перший з однакових
    елементів)
    :param list_of_elements: список елементів
    :return: список без повторень
    """
    distinct_list = []
    for element in list_of_elements:
        if element not in distinct_list:
            distinct_list.append(element)
    return f"Список без повторень - {distinct_list}"
