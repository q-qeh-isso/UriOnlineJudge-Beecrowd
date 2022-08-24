n = int(input())

for i in range(1, n + 1):
    for k in range(2):
        if k == 1:
            print(i, i * i + 1, i * i * i + 1)
        else:
            print(i, i * i, i * i * i)
