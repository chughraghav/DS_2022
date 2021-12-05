"""
You are given a list of numbers, and a target number k.
Return whether there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.

Try to do it in a single pass of the list.
"""



def check_add_to_target(list_numbers, target):
    for i in range(len(list_numbers) - 1):
        if (target - list_numbers[i]) in list_numbers[i + 1:]:
            return True
    return False


if __name__ == '__main__':
    input_list = [4, 7, 1, -3, 2]
    tar = 9
    print(check_add_to_target(input_list, tar))
