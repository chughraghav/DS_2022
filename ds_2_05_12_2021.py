"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""


def minimal_array_len(list_numbers, max_sum):
    i, j = 0, 1
    min_length = len(list_numbers)
    length = 1

    # subcase 1 where number greater than or equal to s is present in nums list. We return 1
    output_list = filter(lambda x: x >= max_sum, list_numbers)
    if len(list(output_list)) >= 1:
        return 1

    # subcase 2 where numbers present in list are smaller than s
    acc = list_numbers[i]  # initializing accumulator with num[i] i.e num[0]
    while i < len(list_numbers) - 1 and j < len(list_numbers):
        acc += list_numbers[j]
        length += 1

        if acc >= max_sum:
            if min_length > length:
                min_length = length
                if min_length == 2:
                    break

            length = 1
            i += 1
            j = i + 1
            acc = list_numbers[i]
        else:
            if j != len(list_numbers) - 1:
                j += 1
            else:
                i += 1
                j = i + 1
                acc = list_numbers[i]

    return min_length


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minimal_array_len(nums, s))
