import re

if __name__ == '__main__':

    pattern_and = re.compile(r"(?<=(\s))&&\s")
    pattern_or = re.compile(r"(?<=(\s))\|\|\s")

    for _ in range(int(input())):
        # change && → and
        modified_input_1 = re.sub(pattern_and, "and ", input())
        # change || → or
        modified_input_2 = re.sub(pattern_or, "or ", modified_input_1)
        # print result
        print(modified_input_2)
