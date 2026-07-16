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
            continue
        if not i.isdigit():
            print("Invalid input")
            return
        value = int(i)
        if value < 1 or value > 9:
            print("Out of range")
            return
        board.append(value)
    return board

def solve():
    return

def main():
    board = parse_board()
    print(solve(board))

main()