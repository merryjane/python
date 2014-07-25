#!/usr/bin/env python3

def look_for_neighbors(network,node):
    neighbors = set()
    
    for couples in network:
        if couples.split('-')[0] == node:
            neighbors.add(couples.split('-')[1])
        elif couples.split('-')[1] == node:
            neighbors.add(couples.split('-')[0])
    return neighbors

def check_connection(network, first, second):
    visited = set()
    visited.add(first)
    
    future = set()
    future.update(look_for_neighbors(network,first))

    for node in future:
        if node == second:
            return True
        else:
            visited.add(node)
            future.remove(node)

    print(future)
    print(visited)

check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3")


'''
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
'''
