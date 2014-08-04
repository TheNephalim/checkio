import math

def checkio(number):
    max_value = math.pow(10, 6)

    if number < 0 or number > max_value:
        raise("Invalid input", number)

    number_string = str(number)
    value = 1

    for i in number_string:
        if i != "0":
            value *= int(i)

    return value

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
