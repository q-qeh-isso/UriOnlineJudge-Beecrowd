s, t, f = [int(x) for x in input().split()]
chegada = (s + t + f) % 24
if chegada == 24:
    chegada = 0
print(chegada)
