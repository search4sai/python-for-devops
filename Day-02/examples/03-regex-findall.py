import re

text = "The quick brown fox"
pattern = "brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
