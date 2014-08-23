def checkio(words_set):
    if (len(words_set) == 1):
        return False

    for word_to_test_1 in words_set:
        for word_to_test_2 in words_set:
            if not (len(word_to_test_1) == len(word_to_test_2)) and not (len(word_to_test_1) > len(word_to_test_2)):
                if word_to_test_2.find(word_to_test_1) >= 0:
                    if word_to_test_2.endswith(word_to_test_1):
                        return True

    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"