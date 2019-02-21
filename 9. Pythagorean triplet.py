def triplet():
    n = 1000

    for a in range(1, n, 1):
        for b in range(1, n-a, 1):
            c = n-a-b
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                return a*b*c

if __name__ == "__main__":
    print(triplet())
