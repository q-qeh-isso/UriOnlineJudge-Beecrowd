c = int(input())
lst = []
if c == 1:
    lst.append(1)
elif c == 2:
    lst.append(1)
    lst.append(1)
else:
    lst.append(1)
    lst.append(1)
    lst.append(2)

    for i in range(3, c):
        lst.append(lst[i - 1] + lst[i - 2])

lst.sort(reverse=True)
print(*lst, sep=' ')
