user_text = input()
count = 0
for c in user_text:
    if not c in (' !.,'):
        count = count + 1
print(count)