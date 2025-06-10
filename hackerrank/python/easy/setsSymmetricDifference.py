if __name__ == '__main__':
    n = int(input())
    english_newspaper_subscriptions = set(map(int, input().strip().split(' ')))
    m = int(input())
    french_newspaper_subscriptions = set(map(int, input().strip().split(' ')))

    result = list(english_newspaper_subscriptions.symmetric_difference(french_newspaper_subscriptions))
    # Output total number of students who have subscriptions to the English or the French newspaper but not both.
    print(len(result))
