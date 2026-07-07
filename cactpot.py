def parse_board():
    raw = input()
    parts = raw.split()

    if len(parts) != 9:
        print("Invalid input")
        return
    
    board = []
    for i in parts:
        if i == ".":
            board.append(None)
        if not i.isdigit():
            return
        value = int(i)
        if value < 1 or value > 9:
            return
        board.append(value)
    return

def solve():
    return

def main():
    board = parse_board()
    print(solve(board))

main()