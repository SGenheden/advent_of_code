def solve(number):
    number = str(number)
    if len(number) != 6:
        return False
    int_rep = list(map(int, number))
    double_digit = False
    for i, (first, second) in enumerate(zip(int_rep[:-1], int_rep[1:]), -1):
        prev = int_rep[i] if i >= 0 else -1
        next = int_rep[i + 3] if i + 3 < len(number) else -1
        if first == second and first != prev and first != next:
            double_digit = True
        if first > second:
            return False
    return double_digit


if __name__ == "__main__":
    n = 0
    for number in range(156218, 652527 + 1):
        if solve(number):
            n += 1
    print(f"There were {n} password that fitted the criteria")
