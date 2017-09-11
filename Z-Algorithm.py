'''
Chase Austvold, Carsen Ball, Bradley White
Homework #1: Z-Algorithm
CSCI 451/551
September 12, 2017
'''

import timeit
from random import choice
from string import ascii_lowercase

#Accepts a string, and returns a list of the z scores
def Z_algorithm(s):
    #will hold the left and right side of the "box"
    l = 0
    r = 0
    #Will hold the z scores for all the indicies in the string
    z_scores = [0] * len(s)
    #Creates a list from the pattern
    s_list = list(s)

    #Increments by each index in the string, calculating the z score at that index
    for k in range(1, len(s)):
        # Case 1, Brute force prefix recognition
        if k > r:
            count = 0
            while (k + count) < len(s_list) and s_list[k + count] == s_list[count]:
                count += 1
            z_scores[k] = count
            if count > 0:
                l = k
                r = k + count - 1
        # Case 2, if we are within a "box"
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

    #Returns the Z scores at each index in the string
    return z_scores

def generate_string(length):
    #return ''.join(choice(ascii_lowercase) for i in range(length))
    return ''.join(choice('abc') for i in range(length))

if __name__ == "__main__":
    #Creates a random strings of length 2^i
    for i in range(2,50):
        length = 2**i
        s_input = generate_string(length)
        #Prints the iteration of the loop with the coresponding random string length
        print("Starting iteration {0} with string length {1}".format(i-1, length))
        #Calculates the time it takes to run the Z_algorithm
        time = timeit.timeit("Z_algorithm('{0}')".format(s_input),globals=globals(), number=1)
        #Prints the time taken to run the z_algorithm on the random string
        print("\tTime taken: {0}".format(time))