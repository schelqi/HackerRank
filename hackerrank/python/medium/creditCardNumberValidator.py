import re

for _ in range(int(input())):
    credit_card_number = input().strip()
    if re.match(r"^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}-?$", credit_card_number):
        credit_card_number_modified = re.sub(r"-", "", credit_card_number)
        if re.search(r"(\d)\1{3}", credit_card_number_modified):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
