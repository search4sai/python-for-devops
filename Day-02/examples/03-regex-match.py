import re

text = "The quick brown fox"
pattern = r"brown"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
