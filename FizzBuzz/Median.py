import math

def checkio(data):
    if not isinstance(data, list):
        raise ValueError("Data is not a list")

    if not len(data) > 1 or not len(data) <= 1000:
        raise ValueError("Length of array is not between 1 and 1000")

    if not all(0 <= x < 10 ** 6 for x in data):
        raise ValueError("Values of data in array are not correct")

    sorted_array = sorted(data)
    result = 0

    if (len(sorted_array) % 2) != 0:
        middle = math.floor(len(sorted_array) / 2)
        result = sorted_array[middle]
        print(result)
    else:
        middle_one = math.floor(len(sorted_array) / 2) - 1
        middle_two = middle_one + 1

        result = (sorted_array[middle_one] + sorted_array[middle_two]) / 2

    #replace this for solution
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")