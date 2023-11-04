import random
"""
This module implements some functions based on linear search algo
"""
from typing import List

def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве
    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if len(arr) == 0:
     raise ValueError()
    me = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < me:
            me = arr[i]
    return me


if __name__ == '__main__':
    print(min_search([-10, -9, 0]))
    print(min_search([0, 1, 2, 3]))
    print(min_search([i for i in range(3, 10)] + [1]))
    print(min_search([i for i in range(10, -3, -1)]))
    print(min_search([random.randint(-100, 100) for _ in range(300)]))