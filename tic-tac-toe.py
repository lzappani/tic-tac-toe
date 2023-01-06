# These are the sets of positions representing
# vertical, horizontal and diagonal lines
lines = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
         {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]

coord = [[1, 1], [1, 2], [1, 3],  # These are the coordinates for the 3 x 3 grid
         [2, 1], [2, 2], [2, 3],
         [3, 1], [3, 2], [3, 3]]


# This function checks the win state of each player
def check_lines(s):
    player_o = {i for i, x in enumerate(s) if x == "O"}
    player_x = {i for i, x in enumerate(s) if x == "X"}
    win_state_o = False
    win_state_x = False
    for i in range(len(lines)):
        win_state_o = lines[i].issubset(player_o) or win_state_o
        win_state_x = lines[i].issubset(player_x) or win_state_x
    return [win_state_o, win_state_x]


# This function evaluates a state of a grid, by calling the check_lines function
def evaluate(s):
    player_win = check_lines(s)
    if player_win == [True, False]:
        return 'O wins'
    elif player_win == [False, True]:
        return 'X wins'
    elif player_win == [False, False] and s.count(' ') == 0:
        return 'Draw'
    else:
        return False


# This function ensures that the move is valid
def read_move(s):
    while True:
        m = list(input().split())
        if (len(m) == 2 and len(m[0]) == 1 and len(m[1]) == 1
                and m[0].isdigit() and m[1].isdigit()):
            m = [int(element) for element in m]
            if m[0] in range(1, 4) and m[1] in range(1, 4):
                if s[coord.index(m)] == ' ':
                    return m
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


# Main body
state = list('_________')
state = [' ' if element == '_' else element for element in state]
player = 'X'
print('T I C   T A C   T O E')
print('Player X plays first')
print()
while True:
    screen = f'---------\n' \
             f'| {state[0]} {state[1]} {state[2]} |\n' \
             f'| {state[3]} {state[4]} {state[5]} |\n' \
             f'| {state[6]} {state[7]} {state[8]} |\n' \
             f'---------'
    print(screen)
    move = read_move(state)
    state = list(state)
    state[coord.index(move)] = player
    state = ''.join(state)
    state_eval = evaluate(state)
    if state_eval:
        screen = f'---------\n' \
                 f'| {state[0]} {state[1]} {state[2]} |\n' \
                 f'| {state[3]} {state[4]} {state[5]} |\n' \
                 f'| {state[6]} {state[7]} {state[8]} |\n' \
                 f'---------'
        print(screen)
        print(state_eval)
        break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
