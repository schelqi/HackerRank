if __name__ == '__main__':

    scores_count = int(input())
    scores_no_duplicate = set(map(int, input().strip().split(' ')))
    scores = list(scores_no_duplicate)
    scores.sort(reverse=True)
    print(scores[1])

