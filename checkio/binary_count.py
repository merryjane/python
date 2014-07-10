#!/usr/bin/env python3

def checkio(number):
	bin_number = bin(number)
	str_bin_number = str(bin_number)[2:] # whitout '0b' prefix
	result = str_bin_number.count('1')
	return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
