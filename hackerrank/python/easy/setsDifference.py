if __name__ == '__main__':
    n = int(input())
    english_newspaper_subscriptions = set(map(int, input().strip().split(' ')))
    m = int(input())
    french_newspaper_subscriptions = set(map(int, input().strip().split(' ')))

    result = list(english_newspaper_subscriptions.difference(french_newspaper_subscriptions))
    # Output the total number of students who are subscribed to the English newspaper only.
    print(len(result))
