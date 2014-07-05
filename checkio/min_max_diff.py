#!/usr/bin/env python3

def checkio(*args):
	list_number = []
	for arg in args:
		list_number.append(arg)
	if list_number:
		min_value = min(list_number)
		max_value = max(list_number)
		abs_diff = abs(max_value - min_value)
	else:
		abs_diff = 0

	return abs_diff

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
