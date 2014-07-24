#!/usr/bin/env python3

def checkio(game_result):
    # rows
    if game_result[0][0] == game_result[0][1] == game_result[0][2] != '.':
        return game_result[0][2]
    elif game_result[1][0] == game_result[1][1] == game_result[1][2] != '.':
        return game_result[1][2]
    elif game_result[2][0] == game_result[2][1] == game_result[2][2] != '.':
        return game_result[2][2]
    # columns
    elif game_result[0][0] == game_result[1][0] == game_result[2][0] != '.':
        return game_result[2][0]
    elif game_result[0][1] == game_result[1][1] == game_result[2][1] != '.':
        return game_result[2][1]
    elif game_result[0][2] == game_result[1][2] == game_result[2][2] != '.':
        return game_result[2][2]
    # diagonals
    elif game_result[0][0] == game_result[1][1] == game_result[2][2] != '.':
        return game_result[2][2]
    elif game_result[0][2] == game_result[1][1] == game_result[2][0] != '.':
        return game_result[2][0]
    else:
        return 'D'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio([
        "O.X",
        "...",
        "XOO"]) == "D", "Drow when dots"
