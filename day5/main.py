def binary_check(binary, lower, higher):
    for b in binary:
        middle = lower + (higher - lower) / 2
        if b == '1':
            lower = middle
        else:
            higher = middle
    return lower


def get_pass_value(bpass):
    bpass = bpass.replace('L', '0').replace('R', '1').replace('F', '0').replace('B', '1')
    row = binary_check(bpass[0:7], 0, 128)
    col = binary_check(bpass[-3:], 0, 8)
    return row * 8 + col


def task1(bpasses):
    highest = 0
    for bpass in bpasses:
        total = get_pass_value(bpass)
        highest = total if total > highest else highest
    return highest


def task2(bpasses):
    seat_list = []
    for bpass in bpasses:
        seat_list.append(get_pass_value(bpass))
    seat_list.sort()
    index = 1
    while seat_list[index] == seat_list[index + 1] - 1:
        index += 1
    return seat_list[index] + 1


if __name__ == '__main__':
    file = open("input.txt", "r")
    lines = file.read().split('\n')
    print(f'Answer task 1: {task1(lines)}')
    print(f'Answer task 2: {task2(lines)}')
