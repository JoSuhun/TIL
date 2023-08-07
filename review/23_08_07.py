#
# def abc(level):
#     if level == 2:
#         return
#     abc(level+1)
#     abc(level+1)
#
# abc(0)


def abc(level):

    if level == 2:
        print('#', end='')
        return

    for i in range(2):
        abc(level + 1)

abc(0)



#
#
#
# def abc2(level):
#
#     if level == 2:
#         return
#
#     for i in range(2):
#         abc2(level+1)
#     print(level, end=' ')
#
# abc2(0)
