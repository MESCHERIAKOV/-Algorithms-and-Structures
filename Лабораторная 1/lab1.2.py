def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    brackets_list = list()
    for sign in brackets_row:  # O(n)
        if sign == "(":
            brackets_list.append(sign)
        elif sign == ")":
            try:
                brackets_list.pop() # O(n)
            except IndexError:
                return False

    if len(brackets_list) != 0: # O(n)
        return False

    return True

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets('))))'))
    print(check_brackets('(())'))
    print(check_brackets('(())()'))
