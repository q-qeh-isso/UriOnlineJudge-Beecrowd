firstCase = True
while True:
    n = int(input())
    if n == 0:
        break

    lst = []
    bigLen = 0
    for u in range(n):
        temp = input()
        lst.append(temp)
        if len(temp) > bigLen:
            bigLen = len(temp)

    if not firstCase:
        print()

    for i in range(len(lst)):
        print(lst[i].rjust(bigLen))

    firstCase = False
