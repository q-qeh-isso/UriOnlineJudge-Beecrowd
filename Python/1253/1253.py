n = int(input())

for k in range(n):
    cod = input()
    key = int(input())

    res = ''
    for i in range(len(cod)):
        curr = ord(cod[i])
        if curr - key < 65:
            res += chr(90 - (key - (curr - 65)) + 1)
        else:
            res += chr(curr - key)

    print(res)
