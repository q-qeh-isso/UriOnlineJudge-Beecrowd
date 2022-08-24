n = int(input())
copo = input()
copos = [0, 0, 0]
if copo == 'A':
    copos[0] = 1
elif copo == 'B':
    copos[1] = 1
elif copo == 'C':
    copos[2] = 1

for i in range(n):
    mov = int(input())
    if mov == 1:
        temp = copos[0]
        copos[0] = copos[1]
        copos[1] = temp
    elif mov == 2:
        temp = copos[1]
        copos[1] = copos[2]
        copos[2] = temp
    elif mov == 3:
        temp = copos[2]
        copos[2] = copos[0]
        copos[0] = temp

if 1 in copos:
    idx = copos.index(1)
    if idx == 0:
        print('A')
    elif idx == 1:
        print('B')
    else:
        print('C')
