#!/usr/bin/env python3

def checkio(words):
	splited = words.split()
	words_counter = 0 
	result = False
	for word in splited:
		if word.isalpha():
			words_counter += 1
			if words_counter == 3:
				result = True
				break
		else:
			words_counter = 0 
	return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
