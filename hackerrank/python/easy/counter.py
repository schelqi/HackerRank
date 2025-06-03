from collections import Counter

if __name__ == '__main__':
    total_sales = 0
    shoes_count = int(input())
    shoes_size = list(map(int, input().strip().split(' ')))
    shoes_counter = Counter(shoes_size)

    N = int(input())

    for _ in range(N):
        shoes_size, shoe_price = map(int, input().strip().split(' '))
        if shoes_counter[shoes_size] > 0:
            total_sales += shoe_price
            shoes_counter[shoes_size] -= 1

    print(total_sales)
