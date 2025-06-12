import re

# Let's define the consonants list
consonants = "bcdfghjklmnpqrstvwxyz"
# Let's define the vowels list
vowels = "aeiou"

regex = rf"(?<=[{consonants}])([{vowels}]{{2,}})[{consonants}]"

m = re.findall(regex, input(), flags=re.IGNORECASE)
print(*m if len(m) > 0 else [-1], sep="\n")
