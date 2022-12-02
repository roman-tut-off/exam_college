# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    res = input('Введите число: ')
    res = sum_digit(res)
    print(res)





