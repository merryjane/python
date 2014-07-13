#!/usr/bin/env python3

def checkio(data):
    if len(data) < 10:
        return False
    
    counter_digit = 0
    counter_upper = 0
    counter_lower = 0

    for i in data:
        if i.isdigit():
            counter_digit += 1
        elif i.isalpha():
            if i.isupper():
                counter_upper += 1
            else:
                counter_lower += 1
        else:
            return False
            break

    if counter_digit >= 1 and counter_upper >= 1 and counter_lower >= 1:
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

