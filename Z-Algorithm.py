'''
Chase Austvold, Carsen Ball, Bradley White
Homework #1: Z-Algorithm and Pattern Matching
CSCI 451/551
September 12, 2017
'''


def Z_algorithm(s):
    l = 0
    r = 0
    k = 1
    z_scores = [0] * len(s)
    s_list = list(s)

    for i in range(len(s)):
        # Case 1
        if k > r:
            count = 0
            while ord(s_list[k + count]) == ord(s_list[count]):
                count += 1
            z_scores[k] = count
            l = k
            r = k + count
        # Case 2
        else:
            beta = s_list[k:(r + 1)]
            # Case 2a
            if z_scores[k] < len(beta):
                k += 1
                z_scores[k] = z_scores[k - l]
            # Case 2b
            else:
                count = 0
                while ((r + 1 + count) < len(s_list)) and (
                            ord(s_list[r + 1 + count]) == ord(s_list[r - k + 1 + count])):
                    count += 1
                l = k
                r = r + count
                k += 1
                z_scores[k] = z_scores[r - k + 1] + count

    return z_scores


'''class ZAlgorithm():
    # creates local variables l,r,k and an array to hold the z scores
    # creates an array from the input string
    def __init__(self, input_text):
        self.l = 0
        self.r = 0
        self.k = 1
        self.z_scores = [0] * len(input_text)
        self.input_string = list(input_text)

    # Will decide what case to use based on l,k,r
    def driver(self):
        # if statement to decide what case to chose
        if self.k < len(self.input_string):
            if self.k > self.r:
                self.case_1()
            else:
                self.case_2()

    # case 1, k > r
    def case_1(self):
        count = 0
        char_k = self.input_string[self.k]

        # compares the char at k + count with the char at count
        while ord(char_k) == ord(self.input_string[count]):
            if self.k + count < (len(self.input_string) - 1):
                count += 1
                char_k = self.input_string[self.k + count]
            else:
                break

        # update values
        self.z_scores[self.k] = count
        self.l = self.k
        self.r = self.k + count
        self.driver()

    # case 2a, K <= R && Z_k < length of Beta
    # case 2b, k <= r && Z_k >= length of Beta
    # Beta is the string from [k,r]
    def case_2(self):
        beta = self.input_string[self.k:self.r + 1]
        if self.k < (len(self.input_string) - 1):
            if (self.z_scores[self.k] < len(beta)):
                # case 2a
                self.k += 1
                self.z_scores[self.k] = self.z_scores[self.k - self.l]
                self.driver()
            else:
                # case 2b
                count = 0
                char_k = self.input_string[self.r + 1]
                while ord(char_k) == ord(self.input_string[self.r - self.k + 1 + count]):
                    if self.k + count < (len(self.input_string) - 1):
                        count += 1
                        char_k = self.input_string[self.r + count + 1]
                    else:
                        break
                self.l = self.k
                self.r = self.r + count
                self.k += 1
                self.z_scores[self.k] = self.z_scores[self.r - self.k + 1] + count
                self.driver()

    def print_z_scores(self):
        print(self.z_scores)'''


if __name__ == "__main__":
    '''input_text = input("Enter your desired string: ")
    run_z = ZAlgorithm(input_text)
    run_z.driver()
    run_z.print_z_scores()'''
    print(Z_algorithm('abababaaa'))
