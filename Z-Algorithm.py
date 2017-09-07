'''
Chase Austvold, Carsen Ball, Bradley White
Homework #1: Z-Algorithm and Pattern Matching
CSCI 451/551
September 12, 2017
'''


# TODO: Implement the Z-Algorithm with pattern matching(separate file)
def ZAlgorithm(s):
    # creates local variables l,r,k and an array to hold the z scores
    # creates an array from the input string
    l = 0
    r = 0
    k = 1
    z_scores = [0] * len(s)
    s_list = list(s)
    #print(s_list)

    # Will decide what case to use based on l,k,r
    def driver(self):
        # if statement to decide what case to chose
        if self.k > self.r:
            run_z.case_1()
        else:
            run_z.case_2()

    # case 1, k > r
    def case_1(self):
        count = 0
        char_k = self.input_string[self.k]

        # compares the char at k + count with the char at count
        while ord(char_k) == ord(self.input_string[count]):
            count += 1
            char_k = self.input_string(self.k + count)

        # update values
        self.z_scores[self.k] = count
        self.l = self.k
        self.r = self.k + count
        run_z.driver()

    # case 2a, K <= R && Z_k < length of Beta
    # case 2b, k <= r && Z_k >= length of Beta
    # Beta is the string from [k,r]
    def case_2(self):
        beta = self.input_string[self.k, self.r + 1]
        if (self.z_scores[self.k] < len(beta)):
            # case 2a
            pass
        else:
            # case 2b
            pass


if __name__ == "__main__":
    input_text = input("Enter your desired string: ")
    ZAlgorithm(input_text)
