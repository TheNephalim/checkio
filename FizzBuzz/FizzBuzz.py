#Your optional code here
#You can import some modules or create additional functions


def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    results = ""

    #replace this for solution
    if (divisibleByFive(number) and divisibleByThree(number)) :
        return "Fizz Buzz"
    elif (divisibleByThree(number)):
        return "Fizz"
    elif (divisibleByFive(number)):
        return "Buzz"
    else:
        return str(number)


def divisibleByThree(number):
    if ((number % 3) == 0) :
        return True
    else:
        return False

def divisibleByFive(number) :
    if ((number % 5) == 0) :
        return True
    else:
        return False

#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"

