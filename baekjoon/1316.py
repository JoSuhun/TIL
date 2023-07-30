N = int(input())
words = list(input() for _ in range(N))

cnt = 0

for word in words:
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+2:]:
            cnt += 1
            break
print(len(words)-cnt)
