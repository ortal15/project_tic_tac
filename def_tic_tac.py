def my_board():
    return {
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ]
    }


board: dict = my_board()


def game_round(board: dict):
    names()
    while True:
        try:
            print('Pleas enter for "X" your wanted place')
            row: int = int(input("enter a row number:"))
            col: int = int(input("enter a col number:"))
            if row not in range(0, 2 + 1):
                print('not in range..')
                continue
            if col not in range(0, 2 + 1):
                print('not in range..')
                continue
            if board['board'][row][col] != '_':
                print('The place is full..')
                continue
            board['board'][row][col] = 'X'
            for i in board['board']:
                print(i)
            if check_win(board, 'X'):
                play_again()
                break
            if check_win(board, 'O'):
                play_again()
                break
            if is_full(board):
                print('It\'s a tie!')
                play_again()
                break
        except ValueError:
            print('Invalid text,try again')
        try:
            print('Pleas enter for "O" your wanted place')
            row: int = int(input("enter a row number:"))
            col: int = int(input("enter a col number:"))
            if board['board'][row][col] != '_':
                print('The place is full..')
                row: int = int(input("enter a row number:"))
                col: int = int(input("enter a col number:"))
            if row not in range(0, 2 + 1):
                print('not in range..')
                continue
            if col not in range(0, 2 + 1):
                print('not in range..')
                continue
            board['board'][row][col] = 'O'
            for i in board['board']:
                print(i)
            if check_win(board, 'O'):
                play_again()
                break
            if check_win(board, 'X'):
                play_again()
                break
            if is_full(board):
                print('It\'s a tie!')
                play_again()
                break
            continue
        except ValueError:
            print('Invalid text,try again')


def check_win(my_board: dict, search: str):
    board = my_board['board']
    for row in board:
        win: bool = True
        for shape in row:
            if shape != search:
                win = False
                break
        if win:
            print(search, 'won')
            return True
    for col in range(0, 2 + 1):
        win: bool = True
        for row in range(0, 2 + 1):
            if board[row][col] != search:
                win = False
                break
        if win:
            print(search, 'won')
            return True
    win: bool = True
    for index in range(0, 2 + 1):
        if board[index][index] != search:
            win: bool = False
            break
    if win:
        print(search, 'won')
        return True
    win = True
    for i in range(3):
        if board[i][2 - i] != search:
            win = False
            break
    if win:
        print(search, 'won')
        return True
    return False


def is_full(my_board: dict):
    board = my_board['board']
    for row in board:
        for cell in row:
            if cell == '_':
                return False
    print("tie")
    play_again()
    return True


def play_again():
    while True:
        try:
            end = input("Do you want to play again? (yes/no): ").lower()
            if end == "yes":
                answer = input('Would you like to play against a friend?(yes/no):').lower()
                if answer == 'yes':
                    return game_round(my_board())
                if answer == 'no':
                    return computer(my_board())
            if end == "no":
                print("Goodbye!")
                break
            else:
                print("You answered an unknown answer")
        except ValueError:
            print('Invalid text,try again')
            continue


import random


def names():
    while True:
        try:
            print('enter your name -')
            name1: str = input('player 1 name:')
            name2: str = input('player 2 name:')
            break
        except ValueError:
            print('Invalid text,try again')
            continue
    while True:
        try:
            shape = input(f'{name1} choose shape(if you want random , input - "Y"):').upper()
            if shape != 'X':
                if shape != 'O':
                    if shape != 'Y':
                        print('Not part of the options...try again')
                        continue
            if shape == 'O':
                print(f'{name2} is "X" and {name1} is "O"')
                break
            if shape == "Y":
                shape = random.choice("X" or "O")
                print(f'{name1} is {shape}')
                break
            else:
                print(f'{name1} is "X" and {name2} is "O"')
                break
        except ValueError:
            print('Invalid text,try again')
            continue


def computer(board: dict):
    while True:
        try:
            print('Pleas enter for "X" your wanted place')
            row: int = int(input("enter a row number:"))
            col: int = int(input("enter a col number:"))
            if row not in range(0, 2 + 1):
                print('not in range..')
                continue
            if col not in range(0, 2 + 1):
                print('not in range..')
                continue
            if board['board'][row][col] != '_':
                print('The place is full..')
                continue
            board['board'][row][col] = 'X'
            for i in board['board']:
                print(i)
            if check_win(board, 'X'):
                play_again()
                break
            if check_win(board, 'O'):
                play_again()
                break
            if is_full(board):
                print('It\'s a tie!')
                play_again()
                break
        except ValueError:
            print('Invalid text,try again')
        try:
            print('Pleas enter for "O" your wanted place')
            row: int = random.randint(0, 2)
            col: int = random.randint(0, 2)
            if board['board'][row][col] != '_':
                print('The place is full..')
                row: int = random.randint(0, 2)
                col: int = random.randint(0, 2)
            if row not in range(0, 2 + 1):
                print('not in range..')
                continue
            if col not in range(0, 2 + 1):
                print('not in range..')
                continue
            board['board'][row][col] = 'O'
            for i in board['board']:
                print(i)
            if check_win(board, 'O'):
                play_again()
                break
            if check_win(board, 'X'):
                play_again()
                break
            if is_full(board):
                print('It\'s a tie!')
                play_again()
                break
            continue
        except ValueError:
            print('Invalid text,try again')
