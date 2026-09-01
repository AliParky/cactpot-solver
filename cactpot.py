payout_by_sum = {
    6: 10000,
    7: 36,
    8: 720,
    9: 360,
    10: 80,
    11: 252,
    12: 108,
    13: 72,
    14: 54,
    15: 180,
    16: 72,
    17: 180,
    18: 119,
    19: 36,
    20: 306,
    21: 1080,
    22: 144,
    23: 1800,
    24: 3600
}

LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

def parse_board():
    raw = input("Enter 9 cells (use . for unknown), e.g. '1 . . 4 . . . . .':")
    parts = raw.split()

    if len(parts) != 9:
        print("Expected exactly 9 space-separated values (use . for unknown)")
        return
    
    board = []
    for i in parts:
        if i == ".":
            board.append(None)
            continue
        if not i.isdigit():
            print("Invalid input")
            return
        value = int(i)
        if value < 1 or value > 9:
            print("Out of range (1-9)")
            return
        board.append(value)
    return board

def solve(board):
    if board is None:
        return "Cannot solve"

    if len(board) != 9:
        return "Cannot solve: Board must have 9 cells"

    known_count = 0
    for i in board:
        if i is not None:
            known_count += 1

    if known_count < 4:
        for i, j in enumerate(board):
            print(i, j)
            row = i // 3 + 1
            col = i % 3 + 1
            if j is None:
                return f"Reveal next: r{row}, c{col}"

    if known_count == 4:
        best_line = None
        for line in LINES:
            values = [board[i] for i in line]
        return "Choose a line to scratch"
        
    return

def main():
    board = parse_board()
    print(solve(board))

main()