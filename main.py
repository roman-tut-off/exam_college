
"""" Функция принимает число и возвращает сумму цифр  """
def sum_digit(number):
    try:
        number = int(number)
        sum = 0
        while number > 0:
            sum += number % 10
            number = number // 10
        return sum
    except:
        raise TypeError('Type Error. Input is not int')


"""" Вызов функции сложения чисел """
if __name__ == '__main__':
    res = input('Введите число: ')
    res = sum_digit(res)
    print(res)





