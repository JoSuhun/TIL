T = int(input())

words = [str(input()) for _ in range(T)]
words_set = list(set(words))


words_sorted = []
for word in words_set:
    words_sorted.append((len(word), word))

result = sorted(words_sorted)

for len_word, word in result:
    print(word)
