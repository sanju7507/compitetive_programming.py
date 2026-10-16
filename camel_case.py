n = int(input())
words = input().split(",")
pattern = input().strip()

def abbreviation(word):
    return ''.join(ch for ch in word if ch.isupper())
matches = []
for word in words:
    word = word.strip()
    abbr = abbreviation(word)
    if abbr.startswith(pattern):
        matches.append((abbr, word))
matches.sort(key=lambda x: (x[0], x[1]))
if matches:
    for _, word in matches:
        print(word)
else:
    print("No match found")
