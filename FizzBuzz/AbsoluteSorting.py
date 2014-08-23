def checkio(numbers_array):
    if len(numbers_array) < 0 and len(numbers_array) < 100:
        raise ValueError("Array length needs to be greater than 0 and less than 100")

    if not all(isinstance(x, int) for x in numbers_array):
        raise ValueError("All values of the array need to be an integer")

    if not all(-100 < x < 100 for x in numbers_array):
        raise ValueError("All values of the array must be greater than -100 and less than 100")

    result = [(abs(number), number) for number in numbers_array]
    sorted_result = [get_value(number_tuple) for number_tuple in sorted(result, key=get_key)]

    return sorted_result


def get_key(item):
    return item[0]

def get_value(item):
    return item[1]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"