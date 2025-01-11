from def_tic_tac import my_board, game_round, computer

print("Welcome to Tic Tac Toe!")
while True:
    try:
        answer = input('Would you like to play against a friend?(yes/no):').lower()
        if answer == 'yes':
            game_round(my_board())
            break
        if answer == 'no':
            computer(my_board())
            break
        else:
            print('Not part of the options...try again')
            continue
    except ValueError:
        print('Invalid text,try again')
        continue
