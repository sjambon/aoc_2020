def task1():
    for number1 in numbers:
        for number2 in numbers:
            if int(number1) + int(number2) == 2020:
                return int(number1) * int(number2)


def task2():
    for number1 in numbers:
        for number2 in numbers:
            for number3 in numbers:
                if int(number1) + int(number2) + int(number3) == 2020:
                    return int(number1) * int(number2) * int(number3)


if __name__ == '__main__':
    file = open("input.txt", "r")
    numbers = file.read().split('\n')
    print(f'Answer task 1: {task1()}')
    print(f'Answer task 2: {task2()}')
