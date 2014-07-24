#!/usr/bin/env python3

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def first_ten(number):
    return FIRST_TEN[number-1]
    
def second_ten(number):
    return SECOND_TEN[number-10]

def other_tens(number):
    return OTHER_TENS[number-2]

def checkio(number):
    if number < 10:
        return (first_ten(number))

    if number >= 10 and number < 20:
        return (second_ten(number))

    if number >= 20 and number < 100:
        number_str = str(number)
        first_number = int(number_str[0])
        second_number = int(number_str[1])
        if number % 10 == 0:
            return (other_tens(first_number))
        else:
            return (other_tens(first_number) + ' ' + first_ten(second_number))

    if number >= 100 and number < 1000:
        number_str = str(number)
        first_number = int(number_str[0])
        second_number = int(number_str[1])
        third_number = int(number_str[2])
        if number % 100 == 0:
            return (first_ten(first_number) + ' ' + HUNDRED)
        elif second_number == 0:
            return (first_ten(first_number) + ' ' + HUNDRED + ' ' + first_ten(third_number))
        elif second_number == 1:
            return (first_ten(first_number) + ' ' + HUNDRED + ' ' + second_ten(third_number))
        elif number % 10 == 0:
            return (first_ten(first_number) + ' ' + HUNDRED + ' ' + other_tens(second_number))
        else:
            return (first_ten(first_number) + ' ' + HUNDRED + ' ' + other_tens(second_number) + ' ' + first_ten(third_number))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
