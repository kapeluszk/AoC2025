import numpy as np
from fontTools.misc.cython import returns

data_matrix = np.loadtxt('/home/kapelusz/PycharmProjects/AoC2025/day 6/test.txt', dtype=str)
data_matrix = data_matrix.transpose()

def part1(data) -> int:
    sum = 0
    for row in data:
        partial_result = 0
        sign = row[-1]
        if sign == '*':
            partial_result = 1
            for char in row[:-1]:
                partial_result *= int(char)
        else:
            for char in row[:-1]:
                partial_result += int(char)
        sum += partial_result

    return sum


import numpy as np


def part2_helper(row, operator) -> int:
    longest_string = len(max(row, key=len))

    helper_matrix = np.full((len(row), longest_string), -1)

    i = 0
    for char in row:
        char_list = list(char)
        offset = longest_string - len(char_list)

        for j in range(len(char_list)):
            helper_matrix[i][j + offset] = int(char_list[j])
        i += 1

    helper_matrix = helper_matrix.transpose()
    if operator == "*":
        result = 1
    else:
        result = 0

    print(helper_matrix)

    for row in helper_matrix:
        num_str = ""
        for val in row:
            if val != -1:
                num_str += str(val)

        if num_str:
            number = int(num_str)
            if operator == "*":
                result *= number
            else:
                result += number

    return result


def part2(data) -> int:
    total_sum = 0
    for row in data:
        sign = row[-1]
        data_rows = row[:-1]
        total_sum += part2_helper(data_rows, sign)

    return total_sum


# print("part 1:  ",part1(data_matrix))
print("part 2:  ",part2(data_matrix))