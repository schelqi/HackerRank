import re

regex = r"^[7-9]\d{9}$"

for _ in range(int(input())):
    if re.match(regex, input().strip()):
        print("YES")
    else:
        print("NO")
