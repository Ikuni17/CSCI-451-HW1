'''
Chase Austvold, Carsen Ball, Bradley White
Homework #1: Pattern Matching
CSCI 451/551
September 12, 2017
'''

import timeit
from random import choice
from string import ascii_lowercase

length = 0


def Z_algorithm(s):
    global length
    l = 0
    r = 0
    z_scores = [0] * len(s)
    s_list = list(s)
    pattern_locations = []

    for k in range(1, len(s)):
        # Case 1
        if k > r:
            count = 0
            while (k + count) < len(s_list) and s_list[k + count] == s_list[count]:
                count += 1
            z_scores[k] = count
            if count > 0:
                l = k
                r = k + count - 1
        # Case 2
        else:
            beta = s_list[k:(r + 1)]
            # Case 2a
            if z_scores[k - l] < len(beta):
                z_scores[k] = z_scores[k - l]
            # Case 2b
            else:
                count = r + 1
                while count < len(s_list) and s_list[count] == s_list[count - k]:
                    count += 1
                l = k
                r = count - 1
                z_scores[k] = count - k
        if z_scores[k] == length:
            pattern_locations.append(k - (length + 1))

    return pattern_locations


def pattern_matching(p, s):
    global length
    # p = 'aba'
    # s = 'abacabacabasfkdflksdjaba'
    length = len(p)
    patterns = Z_algorithm(p + '$' + s)
    #print('\tThe pattern exists at the indices {0}'.format(patterns))
    print('\tThe pattern exists {0} times'.format(len(patterns)))


def generate_string(length):
    # return ''.join(choice(ascii_lowercase) for i in range(length))
    return ''.join(choice('ac') for i in range(length))


def generate_pattern(length):
    return ''.join(choice('ac') for i in range(length))


if __name__ == "__main__":

    # Correct output should be [0,0,5,0,3,0,1,1,1]
    # print(Z_algorithm('abababaaa'))
    # timeit.timeit("Z_algorithm('abababaaa')",globals=globals(), number=1)

    for i in range(2, 50):
        length = 2 ** i
        s_input = generate_string(length)
        p_input = generate_pattern(i)
        print("Starting iteration {0} with string length {1} and pattern length {2}".format(i - 1, length, len(p_input)))
        time = timeit.timeit("pattern_matching('{0}', '{1}')".format(p_input, s_input), globals=globals(), number=1)
        print("\tTime taken: {0} seconds".format(time))
        # pattern_matching()
