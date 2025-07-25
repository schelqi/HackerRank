import re
def fun(s):
    # return True if s is a valid email, else return False
    regex = r"^[a-z0-9_-]+@[a-z0-9]+\.[a-z]{1,3}$"
    return bool(re.match(regex, s, re.IGNORECASE))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)