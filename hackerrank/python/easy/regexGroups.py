import re

regex = r"([a-zA-Z0-9])\1"
m = re.search(r"([a-zA-Z0-9])\1", input().strip())
print(m.group()[0] if m else -1)
