board = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    ]

def chess_to_index(chess_pos):
    column = ord(chess_pos[0]) - ord('a')
    row = 8 - int(chess_pos[1])
    return row, column

for row in board:
    print(' '.join(row))
print()

while True:
    start_pos = input("Enter the piece's starting position (e.g., 'a2'): ")
    end_pos = input("Enter the piece's ending position (e.g., 'a4'): ")

    try:
        start_row, start_col = chess_to_index(start_pos)
        end_row, end_col = chess_to_index(end_pos)

        if board[start_row][start_col] == '.':
            print("Error: No piece at the starting position.")
            break

        board[end_row][end_col] = board[start_row][start_col]
        board[start_row][start_col] = '.'

        for row in board:
            print(' '.join(row))
        print()

    except:
        print("Invalid input. Please enter a valid chess position (e.g., 'a2').")