import re

regex = r".(#[a-f\d]{3,6})"

for _ in range(int(input())):
    row = input().strip()
    # print(row)
    m = re.finditer(regex, row, flags=re.IGNORECASE)
    for x in m:
        print(x.group(1))

