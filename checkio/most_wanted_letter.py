#!/usr/bin/env python3

def checkio(text):
    list_alpha = []
    for i in text:
        if i.isalpha():
            list_alpha.append(i.lower())
        else:
            continue

    dict_alpha = {}    
    for alpha in list_alpha:
        dict_alpha[alpha] = int(list_alpha.count(alpha))
#    print(dict_alpha)

    value = 0
    result_alpha = '' 
    for key in sorted(dict_alpha):
        if dict_alpha[key] > value:
            value = dict_alpha[key]
            result_alpha = key
#    print(result_alpha)
    return result_alpha

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
