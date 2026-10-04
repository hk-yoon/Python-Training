import re
text = "sample_123"
match = re.search(r"\d+", text)
print(match.group())
sequence = "ATG123CGT456"
print(re.findall(r"\d+", sequence))
