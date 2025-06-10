
if __name__ == '__main__':
    # You are given a space separated list of integers.
    n = int(input())
    data = list((input().strip().split(' ')))
    # If all the integers are positive, then you need to check if any integer is a palindromic integer.
    all_positive_integers = [int(i) > 0 for i in data]
    any_palindromic_integer = [j == j[::-1] for j in data]
    print(all(all_positive_integers) and any(any_palindromic_integer))
