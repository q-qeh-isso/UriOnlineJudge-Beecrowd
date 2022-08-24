n = int(input())
for k in range(n):
    m = input()
    txt = ''
    for i in m:
        if i.isalpha():
            txt += chr(ord(i) + 3)
        else:
            txt += i

    txt = txt[::-1]
    crip = ''
    for i in range(len(txt) // 2, len(txt)):
        crip += chr(ord(txt[i]) - 1)

    print(f'{txt[:(len(txt) // 2)]}{crip}')
