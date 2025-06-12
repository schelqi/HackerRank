import re

whole_string = input()
sub_string = input()
# Let's define the regex
regex = rf"(?=({sub_string}))"

result = list(re.finditer(regex, whole_string))
x = len(sub_string) - 1

if len(result) > 0:
    for m in result:
        print((m.start(), m.start() + x))
else:
    print((-1, -1))
