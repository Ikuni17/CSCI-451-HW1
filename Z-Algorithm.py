'''
Chase Austvold, Carsen Ball, Bradley White
Homework #1: Z-Algorithm and Pattern Matching
CSCI 451/551
September 12, 2017
'''
#TODO: Implement the Z-Algorithm with pattern matching(separate file)
class ZAlgorithm():
    #creates global variables l,r,k and an array to hold the z scores
    #creates an array from the input string
    def __init__(self, pattern):
        self.l = 0
        self.r = 0
        self.k = 0
        self.z_scores = []
        self.input_string = list(pattern)
    
    #Will decide what case to use based on l,k,r 
    def driver(self):
        #if statement to decide what case to chose
        pass
    
    #case 1, k > r    
    def case_1(self):
        print "case 1" 
    
    #case 2a, K <= R && Z_k < length of Beta
    #Beta is the string from [k,r]
    def case_2(self):
        print "case 2"
    
    #case 2b, k <= r && Z_k >= length of Beta    
    def case_3(self):
        print "case 3"
        
if __name__ == "__main__":
    run_z = ZAlgorithm("ababab")