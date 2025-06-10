if __name__ == '__main__':
    x, result = map(int, input().strip().split(' '))
    expression = input()
    print(eval(expression) == result)