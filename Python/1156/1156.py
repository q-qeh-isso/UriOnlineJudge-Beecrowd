s = 0
div = 2
for i in range(1, 40, 2):
    if i == 1:
        s += i
    else:
        s += i / div
        div *= 2

print(f'{s:.2f}')
