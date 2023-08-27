n, m = map(int, input().split())    # n 책 개수 // m 최대 무게
if n != 0:
    books = list(map(int, input().split()))

    SUM = 0
    cnt = 1
    while books:
        book = books.pop(0)
        SUM += book
        if SUM > m:
            cnt += 1
            SUM = book
    print(cnt)

else: print(0)
