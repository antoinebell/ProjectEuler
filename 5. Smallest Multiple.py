def smallest_multiple():

    #ppcm(1...20)
    #not prime as "* primes"
    #1, 2, 3, 5, 7, 11, 13, 17, 19 = primes
    #4 = pow(2,2)
    #6 = 2x3
    #8 = pow(2,3)
    #9 = 3x3
    #10 = 2x5
    #12 = pow(2,2)*3
    #14 = 2x7
    #15 = 3x5
    #16 = pow(2,4)
    #18 = 2x9
    #20 = pow(2,2)*5

    #for each prime, take the biggest exponent

    smallest = pow(2, 4)*pow(3, 2)*5*7*11*13*17*19

    return smallest

if __name__ == "__main__":
    print(smallest_multiple())


