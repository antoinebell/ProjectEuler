if __name__ == "__main__":

    sum = 0

    fib1 = 1
    fib2 = 1
    temp = fib1

    while fib2<4000000:
        temp = fib1+fib2
        fib1 = fib2
        fib2 = temp
        if fib2 > 4000000:
            break;
        if fib2 % 2 == 0:
            sum += fib2
        print(fib2)

    print(sum)