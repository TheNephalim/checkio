import re

def checkio(text):

    letter_list = re.findall("[a-zA-Z]+?", text.lower())
    letter_set = set(letter_list)

    counts = [(letter, text.lower().count(letter)) for letter in letter_set]
    sorted_counts = sorted(counts, key=get_key)

    max_value = max(sorted_counts, key=get_value)

    result = max_value[0]

    #replace this f
    return result

def get_key(item):
    return item[0]

def get_value(item):
    return item[1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")