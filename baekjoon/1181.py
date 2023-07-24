T = int(input())

words = [str(input()) for _ in range(T)]
words_set = list(set(words))


words_len = []
for word in words_set:
    words_len.append((len(word), word))

words_sorted = sorted(words_len)

for len_word, word in words_sorted:
    print(word)
