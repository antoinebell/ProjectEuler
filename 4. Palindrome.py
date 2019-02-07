if __name__ == "__main__":

    biggest_plaindrome = 0

    for i in range(100, 1000, 1):
        for j in range(100, 1000, 1):
            result = i * j
            result_str = str(result)

            length = len(result_str)

            if length == 5:
                left_part = result_str[0] + result_str[1] + result_str[2]
                right_part = result_str[2] + result_str[3] + result_str[4]
                right_part = right_part[::-1]
            elif length == 6:
                left_part = result_str[0] + result_str[1] + result_str[2]
                right_part = result_str[3] + result_str[4] + result_str[5]
                right_part = right_part[::-1]

            if left_part == right_part:
                if result > biggest_plaindrome:
                    biggest_plaindrome = result

    print("Biggest Palindrome :", str(biggest_plaindrome))

