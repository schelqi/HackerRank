def solve(s):
    return " ".join([sub.capitalize() for sub in s.split(" ")])

if __name__ == '__main__':
    s = input().strip()
    print(solve(s))

