from collections import defaultdict


def update_board(board_numbers, board_taken, number):
    if number not in board_numbers:
        return False

    for x, y in board_numbers[number]:
        board_taken[x][y] = True
    del board_numbers[number]

    for idx1 in range(5):
        if all(board_taken[idx1][idx2] for idx2 in range(5)):
            return True
        if all(board_taken[idx2][idx1] for idx2 in range(5)):
            return True

    return False


def parse_input(input_rows):
    numbers = [int(number) for number in input_rows[0].split(",")]

    board_numbers_list = []
    board_taken_list = []
    for offset in range(2, len(input_rows), 6):
        board_numbers = defaultdict(list)
        board_taken = []
        for row in range(5):
            input_row = input_rows[offset + row].replace("  ", " ")
            for col, number in enumerate(input_row.strip().split(" ")):
                board_numbers[int(number)].append((row, col))
            board_taken.append([False] * 5)
        board_numbers_list.append(board_numbers)
        board_taken_list.append(board_taken)

    return board_numbers_list, board_taken_list, numbers


def solve(input_rows):
    board_numbers_list, board_taken_list, numbers = parse_input(input_rows)
    for number in numbers:
        for board_numbers, board_taken in zip(board_numbers_list, board_taken_list):
            if update_board(board_numbers, board_taken, number):
                unmarked_sum = sum(
                    number * len(pos) for number, pos in board_numbers.items()
                )
                return number * unmarked_sum


if __name__ == "__main__":
    import sys

    lines = open(sys.argv[1], "r").read().splitlines()
    print(solve(lines))
