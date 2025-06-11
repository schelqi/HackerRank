import re
# solution valid for python 2
for _ in range(int(raw_input())):
    try:
        re.compile(raw_input().strip())
        print(True)
    except re.error:
        print(False)
