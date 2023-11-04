def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом
    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:
        raise ValueError("Факториал считается не от отрицательных чисел")
    if n == 0:
        return 1
    c = [i+1 for i in range(n)]
    a = 1
    for i in c:
        a *= i
    return a


if __name__ == '__main__':
    print(factorial_iterative(6))