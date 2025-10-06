
def findDigits(n):
    digits = str(n)
    divisors = 0
    for digit_str in digits:
        digit = int(digit_str)
        if digit != 0 and n % digit == 0:
            divisors += 1
    return divisors

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(findDigits(n))
