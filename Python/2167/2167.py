n = int(input())
rpms = [int(x) for x in input().split()]
indiceQueda = 0
for i in range(len(rpms) - 1):
    if rpms[i] > rpms[i + 1]:
        indiceQueda = i + 2
        break

print(indiceQueda)
