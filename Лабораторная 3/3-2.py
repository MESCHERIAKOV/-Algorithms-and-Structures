from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if container == []:
        return list()
    if len(container) == 1:
        return container
    malkom = [0] * (len(container) + 1)
    for i in container:
        malkom[i] += 1

    container = []

    for i in range(len(malkom)):
        #if i > 0:
        for j in range(malkom[i]):
            container.append(i)

    return container