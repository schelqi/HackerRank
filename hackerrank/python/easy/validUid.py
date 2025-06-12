# A valid UID must follow the rules below:
# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits .
# It should only contain alphanumeric characters ( a-z , A -Z  & 0 -9 ).
# No character should repeat.
# There must be exactly  characters in a valid UID.

import re

for _ in range(int(input())):
    uid = input().strip()
    if re.match(r"^[a-zA-Z0-9]{10}$", uid) \
            and re.search(r"[A-Z].*[A-Z]", uid) \
            and re.search(r"\d.*\d.*\d", uid)\
            and not re.search(r"([a-zA-Z0-9]).*\1", uid):
        print("Valid")
    else:
        print("Invalid")
