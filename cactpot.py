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
        return

    known_count = 0
    for i in board:
        if i is not None:
            known_count += 1
    return

def main():
    board = parse_board()
    print(solve(board))

main()