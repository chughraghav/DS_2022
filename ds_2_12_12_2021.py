"""
You are given an array of N integers. You have to find the Difference of Maximum and Minimum sum of exactly K numbers from the array.
If not possible then print -1

"""


def max_min_difference(list_numbers, k):
    sorted_list_numbers = sorted(list_numbers)

    if k > len(list_numbers):
        return -1

    min_sum = sum(sorted_list_numbers[:k])
    max_sum = sum(sorted_list_numbers[-k:])

    return max_sum - min_sum


if __name__ == '__main__':
    numbers = [1, 8, 2, 6, 4, 12]
    k = 3
    difference = max_min_difference(numbers, k)
    print(difference)
