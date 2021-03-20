def _lines(board):
    yield from board  # the rows
    yield [board[i][i] for i in range(len(board))]  # one of the diagonals

def lines(board):
    yield from _lines(board)
    # rotate the board 90 degrees to get the columns and the other diagonal
    yield from _lines(list(zip(*reversed(board))))

def check_winner(board):
    for line in lines(board):
        if len(set(line)) == 1 and line[0] is not None:
            return line[0]
    return " "  # if we got this far, there's no winner

a = [['X', 'O', 'X'],
     ['O', 'X', 'O'],
     ['O', 'X', 'O']]

b = [['X', 'O', 'O'],
     ['O', 'X', 'O'],
     ['O', 'X', 'O']]

c = [['X', 'O', 'X'],
     ['O', 'X', 'O'],
     ['X', 'X', 'O']]

print(check_winner(a))
print(check_winner(b))
print(check_winner(c))