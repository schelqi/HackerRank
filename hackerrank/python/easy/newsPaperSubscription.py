if __name__ == '__main__':
    n = int(input())
    english_newspaper_subscriptions = set(map(int, input().strip().split(' ')))
    m = int(input())
    french_newspaper_subscriptions = set(map(int, input().strip().split(' ')))

    result = list(english_newspaper_subscriptions.union(french_newspaper_subscriptions))
    # Output the total number of students who have at least one subscription.
    print(len(result))
