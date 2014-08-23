def count_words(text, words):
    counter = 0

    if len(text) > 256:
        return 0

    if not all(3 <= len(w) and w.islower() and w.isalpha for w in words):
        return 0

    for word in words:
        if text.lower().find(word) >= 0:
            counter += 1

    return counter


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"