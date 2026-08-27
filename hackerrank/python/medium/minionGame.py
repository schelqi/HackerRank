def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if stuart_score == kevin_score:
        print("Draw ")
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Kevin", kevin_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)
