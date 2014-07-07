#!/usr/bin/env python3

def checkio(number):
	list_number = list(str(number))
	list_number_wo_nulls = []
	result = 1

	for i in list_number:
		if not i == '0':
			list_number_wo_nulls.append(i)
		else:
			continue

	for j in list_number_wo_nulls:
		result *= int(j)	

	return result
			
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
