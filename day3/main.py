def task1():
    x_slope = 3
    y_slope = 1
    return count_trees(grid, x_slope, y_slope)


def task2():
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    product = 1
    for slope in slopes:
        product *= count_trees(grid, slope[0], slope[1])
    return product


def count_trees(forest, x_slope, y_slope):
    columns = len(forest[0])
    x = 0
    count = 0

    for y in range(0, len(forest), y_slope):
        if forest[y][x] == '#':
            count += 1
        x = (x + x_slope) % columns
    return count


if __name__ == '__main__':
    file = open("input.txt", "r")
    grid = file.read().split('\n')

    print(f'Answer task 1: {task1()}')
    print(f'Answer task 2: {task2()}')
