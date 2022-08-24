andares = []
for i in range(3):
    andares.append(int(input()))

tempo = (andares[1] * 2) + (andares[2] * 4)
if andares[0] == andares[1] and andares[1] == andares[2]:
    tempo = (andares[0] * 2) + (andares[2] * 2)
else:
    t1 = (andares[1] * 2) + (andares[2] * 4)
    t2 = (andares[0] * 2) + (andares[2] * 2)
    t3 = (andares[0] * 4) + (andares[1] * 2)
    if t1 >= t2:
        tempo = t2
        if t2 >= t3:
            tempo = t3
    else:
        if t1 >= t3:
            tempo = t3

print(tempo)
