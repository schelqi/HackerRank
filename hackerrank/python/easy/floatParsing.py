import re
if __name__ == '__main__':
    regex = r"[+-]?\d*\.\d+$"
    n = int(input())
    for _ in range(n):
        number = input().strip()
        if re.match(regex, number):
            print(True)
        else:
            print(False)
