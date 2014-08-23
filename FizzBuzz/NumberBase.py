import re

def checkio(str_number, radix):
    match_obj = re.match("\A[A-Z0-9]+\Z", str_number)

    if not match_obj:
        return -1

    if len(str_number) == 0 or len(str_number) > 10:
        return -1

    if radix < 2 or radix > 36:
        return -1

    try:
        result = int(str_number, base=radix)
    except ValueError:
        return -1

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"