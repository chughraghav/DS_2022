"""
Squares in Rectangle

Given dimensions of rectangle, you need to find least possible squares that can make complete rectangle.

Input format:
- First line will contain two integers, length L and breath B of rectangle(not in order)


"""

def calculate_squares(length, breath, square_dict):
    if breath > length:
        length, breath = breath, length

    if breath == 1 or length - breath == 0:
        value = square_dict.get(breath, 0)
        square_dict[breath] = value + length
        return square_dict

    value = square_dict.get(breath, 0)
    square_dict[breath] = value + 1

    return calculate_squares(length - breath, breath, square_dict)


if __name__ == '__main__':
    length = 12
    breath = 7
    square_dict = dict()
    calculate_squares(length, breath, square_dict)
    print(square_dict)
