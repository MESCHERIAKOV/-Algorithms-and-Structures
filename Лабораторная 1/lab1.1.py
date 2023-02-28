"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Очередь идет слева направо (начало - слева, конец - справа)
        """
        self._my_list = []

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._my_list.append(elem)  # Сложность O(1)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if len(self._my_list) == 0:
            raise IndexError("Очередь пустая")

        element = self._my_list[0]

        del self._my_list[0]  # Сложность O(1)

        return element

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Индекс должен быть целым числом")
        elif not 0 <= ind <= len(self._my_list):
            raise IndexError("Индекс не в границах очереди")

        return self._my_list[ind] # Сложность O(1)

    def clear(self) -> None:
        """ Очистка очереди. """
        self._my_list.clear() # Сложность O(n)

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self._my_list) # Сложность O(1)
