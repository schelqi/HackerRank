def average(all_data_size, all_data):
    filtered_data = set(all_data)
    total = min(all_data_size, len(filtered_data))
    return sum(filtered_data)/total


if __name__ == '__main__':
    N = int(input())
    data = map(int, input().strip().split(' '))
    print(average(N, data))
