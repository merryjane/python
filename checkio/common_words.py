#!/usr/bin/env python3

def checkio(first, second):
	set_first = set(first.split(','))
	set_second = set(second.split(','))
	intersection = set_first & set_second
	result = ','.join(sorted(list(intersection)))
	
	return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
