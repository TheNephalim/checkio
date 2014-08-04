def checkio(words):
    word_list = str.split(words, " ")
    counter = 0

    for i in range(0,len(word_list)):
        if counter == 3:
            break
        else:
            if not str.isalpha(word_list[i]):
                counter = 0
            else:
                counter = counter + 1

    if counter == 3:
        return True

    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
