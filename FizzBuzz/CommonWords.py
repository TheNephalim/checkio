import types
import collections

def checkio(first, second):
    if not isinstance(first, str):
        raise "Invalid input"

    if not isinstance(second, str):
        raise "Invalid input"

    first_word_array = first.split(",")
    second_word_array = second.split(",")

    first_set = set(first_word_array)
    second_set = set(second_word_array)

    word_intersection = first_set.intersection(second_set)

    result = ""

    if len(word_intersection) > 0:
        result = ','.join(sorted(list(word_intersection)))

    return result


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"