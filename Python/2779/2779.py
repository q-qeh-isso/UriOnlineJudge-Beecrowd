album = int(input())
figs = int(input())
compradas = []
for i in range(figs):
    compradas.append(int(input()))

sCompradas = set(compradas)
print(album - len(sCompradas))
