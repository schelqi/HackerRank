import re

for _ in range(int(input())):
    # change && → and
    modified_input_1 = re.sub(r"(?<=(\s))&&\s", "and ", input())
    # change || → or
    modified_input_2 = re.sub(r"(?<=(\s))\|\|\s", "or ", modified_input_1)
    # print result
    print(modified_input_2)
