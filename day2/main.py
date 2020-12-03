from day2.Password import Password


def task1():
    count = 0
    for pw in passwords:
        if pw.is_correct_task1():
            count += 1
    return count


def task2():
    count = 0
    for pw in passwords:
        if pw.is_correct_task2():
            count += 1
    return count


if __name__ == '__main__':
    file = open("input.txt", "r")
    lines = file.read().split('\n')
    passwords = []

    for line in lines:
        parts = line.split(' ')
        lower = parts[0].split('-')[0]
        higher = parts[0].split('-')[1]
        char = parts[1][0]
        passphrase = parts[2]
        passwords.append(Password(int(lower), int(higher), char, passphrase))

    print(f'Answer task 1: {task1()}')
    print(f'Answer task 2: {task2()}')




