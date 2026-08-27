import re

if __name__ == '__main__':
    credit_card_pattern = re.compile(r"^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$")
    consecutive_digits_pattern = re.compile(r"(\d)\1{3}")
    for _ in range(int(input())):
        credit_card_number = input().strip()
        if re.match(credit_card_pattern, credit_card_number):
            credit_card_number_modified = re.sub(r"-", "", credit_card_number)
            if re.search(consecutive_digits_pattern, credit_card_number_modified):
                print("Invalid")
            else:
                print("Valid")
        else:
            print("Invalid")
