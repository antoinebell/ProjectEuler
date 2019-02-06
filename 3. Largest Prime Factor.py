def largestPrime(n):
    i = 2               #Number with which to start
    while i * i < n:
        while n % i == 0:
            n = n / i
    return n

if __name__ == "__main__":
    print(largestPrime(600851475143))