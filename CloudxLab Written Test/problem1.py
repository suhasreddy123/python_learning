"""
Problem 1:
Write a function in your favorite programming language that takes two numbers m and n as parameters
and prints all possible strings of length n where each character is a digit from 0 to m.

Algotithm:
1. with n digit number and 0 to m possible digit values, total number of out comes is (m+1) power n
2. we can observe the outputs patterns like for first column 0 to m values will repeat by pow(m+ 1, bit_no)
here bit value is m. for second column bit_no is m-1 ans so on..
3.repeat the pattern by - total outcomes combination / pattern array length
4. transpose the array
5. convert each inner array to string representation by concatenating digits
"""
import numpy as np


def create_patterns(n, m):
    num_of_patterns = None
    final_set = []
    for bit_no in reversed(range(n)):
        data = []
        for element in range(m + 1):
            data = data + [element] * (pow(m+ 1, bit_no))

        # print("data=",data)
        current_pattern_len = len(data)
        if num_of_patterns is None:
            num_of_patterns = len(data)

        m_factor = int(num_of_patterns / current_pattern_len)

        # print(data)
        final_set.append(data * m_factor)

    np_data = np.array(final_set)
    np_data = np_data.transpose()

    final_array = []
    for a in np_data:
        x = a.tolist()
        final_array.append("".join([ str (s) for s in x ]))
    return final_array

if __name__ == '__main__':
    print(create_patterns(2, 1))
    print(create_patterns(2, 2))
    print(create_patterns(3, 2))
