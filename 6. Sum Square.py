def sumSquares(n):
    #1^2 + 2^2 + ...
    sum = 0
    for i in range(1, n+1, 1):
        sum += pow(i, 2)

    return sum

def squaresSum(n):
    #(1+2)^2
    sum = 0
    for i in range(1, n+1, 1):
        sum += i

    return pow(sum, 2)

if __name__ == "__main__":
    print(squaresSum(100) - sumSquares(100))