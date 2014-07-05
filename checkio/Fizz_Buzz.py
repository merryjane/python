#!/usr/bin/env python3

def checkio(dig):
	if dig % 3 == 0 and dig % 5 == 0:
		return "Fizz Buzz"
	elif dig % 3 == 0:
		return "Fizz"
	elif dig % 5 == 0:
		return "Buzz"
	else:
		return str(dig)
		
if __name__ == '__main__':
	assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
	assert checkio(6) == "Fizz", "6 is divisible by 3"
	assert checkio(5) == "Buzz", "5 is divisible by 5"
	assert checkio(7) == "7", "7 is not divisible by 3 or 5"
