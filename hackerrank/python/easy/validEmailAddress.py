import re

regex = r"^<[a-z][\w.\-]+@[a-z]+\.[a-z]{,3}>$"

for _ in range(int(input())):
    user_name, email = input().strip().split(' ')
    if re.match(regex, email):
        print(user_name, email)

