def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        sub = string[i:i+k]
        print(remove_duplicates(sub))

def remove_duplicates(sub):
    n = len(sub)
    res = sub[0]
    for i in range(1, n):
        if sub[i] not in sub[:i]:
            res += sub[i]
    return res

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)