'''
Chase Austvold, Carsen Ball, Bradley White
Homework #1: Pattern Matching
CSCI 451/551
September 12, 2017
'''

import timeit
from random import choice
from string import ascii_lowercase

#Holds the length of the pattern that we are looking for
length = 0

#Accepts a pattern p, and string s
#Prints how many times the pattern exists in the string
def pattern_matching(p, s):
    global length

    #Sets length to the length of the pattern
    length = len(p)
    #Calls the Z_aglorithm, using the randomly generated pattern and string, seperated by $
    patterns = Z_algorithm(p + '$' + s)

    print('\tThe pattern exists {0} times'.format(len(patterns)))

#Acepts a string with a prefix seperated by a $, followed by the string that we are looking for the patterns within
def Z_algorithm(s):
    global length
    #Holds the left and right side of the "box"
    l = 0
    r = 0
    #Holds the z scores for all the indicies in the string
    z_scores = [0] * len(s)
    s_list = list(s)
    #Holds every index that the pattern exists in the randomly generated string
    pattern_locations = []

    #Iterates for the length of the string s, calculating z scores at each index
    for k in range(1, len(s)):
        # Case 1, Brute force
        if k > r:
            count = 0
            while (k + count) < len(s_list) and s_list[k + count] == s_list[count]:
                count += 1
            z_scores[k] = count
            if count > 0:
                l = k
                r = k + count - 1
        # Case 2, if we are within a 'box'
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
        #If the z score at the index k is equal to the lenght of the pattern,
        #Then a pattern exists at the index k - (length of the pattern + 1)
        if z_scores[k] == length:
            #Adds the index of the pattern to our list
            pattern_locations.append(k - (length + 1))

    return pattern_locations



#Generates a random string
def generate_string(length):
    # return ''.join(choice(ascii_lowercase) for i in range(length))
    return ''.join(choice('ac') for i in range(length))

#Generates a random pattern to find in the random string
def generate_pattern(length):
    return ''.join(choice('ac') for i in range(length))


if __name__ == "__main__":

    #Iterates multiple times, to generate multiple random strings and patterns to test
    for i in range(2, 50):
        length = 2 ** i
        s_input = generate_string(length)
        p_input = generate_pattern(i)
        #Prints the pattern and string length at the certain iteration of the loop
        #Prints the number of occurences of the pattern
        print("Starting iteration {0} with string length {1} and pattern length {2}".format(i - 1, length, len(p_input)))
        #Prints the time it takes to find the patterns in the particular string
        time = timeit.timeit("pattern_matching('{0}', '{1}')".format(p_input, s_input), globals=globals(), number=1)
        print("\tTime taken: {0} seconds".format(time))
