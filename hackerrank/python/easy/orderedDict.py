from collections import OrderedDict
if __name__ == '__main__':
    data = OrderedDict()
    N = int(input())
    for _ in range(N):
        *item_name_arr, item_price = input().strip().split()
        item_name = ' '.join(item_name_arr)
        if item_name not in data.keys():
            data[item_name] = int(item_price)
        else:
            data[item_name] += int(item_price)

    for key, value in data.items():
        print(key, value)
