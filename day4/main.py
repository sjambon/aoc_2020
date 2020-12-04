import re


def is_valid_task1(passport):
    return passport.count("byr") == passport.count("iyr") == passport.count("eyr") == passport.count(
        "hgt") == passport.count("hcl") == passport.count("ecl") == passport.count("pid") == 1


def task1():
    count = 0
    for passport in passports:
        if is_valid_task1(passport):
            count += 1
    return count


def is_valid_field(key, value):
    if key == 'byr':
        if not 1920 <= int(value) <= 2002:
            return False
    if key == 'iyr':
        if not 2010 <= int(value) <= 2020:
            return False
    if key == 'eyr':
        if not 2020 <= int(value) <= 2030:
            return False
    if key == 'hgt':
        if value.endswith('cm'):
            part = int(value[:-2])
            if not 150 <= part <= 193:
                return False
        elif value.endswith('in'):
            part = int(value[:-2])
            if not 59 <= part <= 76:
                return False
        else:
            return False
    if key == 'hcl':
        if not re.match('^#[0-9a-f]{6}$', value):
            return False
    if key == 'ecl':
        colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if value not in colors:
            return False
    if key == 'pid':
        if not re.match('^[0-9]{9}$', value):
            return False
    return True


def is_valid_passport(passport):
    if not is_valid_task1(passport):
        return False

    values = passport.split(' ')
    for val in values:
        if not is_valid_field(val.split(':')[0], val.split(':')[1]):
            return False
    return True


def task2():
    count = 0
    for passport in passports:
        passport = passport.replace('\n', ' ')
        if is_valid_passport(passport):
            count += 1
    return count


if __name__ == '__main__':
    file = open("input.txt", "r")
    parts = file.read().split("\n\n")
    passports = [passport.replace(' ', '\n') for passport in parts]
    print(f'Answer task 1: {task1()}')
    print(f'Answer task 2: {task2()}')
