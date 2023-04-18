from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    val_init = 0

    matr = [[val_init for i in range(m)] for j in range(n)]
    matr[0][0] = 1
    for y in range(n):
        for x in range(m):
            if x == m - 1 and y == n - 1:
                break
            a_3 = True
            a_4 = True
            a_5 = True
            op = matr[y][x]
            if y == 0:
                pass
            if y == n - 1:
                a_4 = False
                a_5 = False
            if x == m - 1:
                a_3 = False
                a_4 = False
            if a_3:
                matr[y][x + 1] += op
            if a_4:
                matr[y + 1][x + 1] += op
            if a_5:
                matr[y + 1][x] += op
    return matr
if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
