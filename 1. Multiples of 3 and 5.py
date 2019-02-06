if __name__ == "__main__":

    indexes = []
    sum = 0

    for i in range(1, 1000, 1):
        if ((i % 3) == 0) or ((i % 5) == 0):
            indexes.append(i)

    for i in indexes:
        sum += i

    print(sum)