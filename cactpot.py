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
                return f"{row}, {col}"
        
    return

def main():
    board = parse_board()
    print(solve(board))

main()