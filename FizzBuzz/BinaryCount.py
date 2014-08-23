import math

def checkio(number):

    if type(number) != int:
        raise "input is not valid"

    if math.pow(2,36) < number or number <= 0:
        raise "Input is not valid"

    binary_string = bin(number)

    unities = binary_string.count("1")

    return unities

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
