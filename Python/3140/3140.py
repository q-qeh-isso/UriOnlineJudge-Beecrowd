grava = False
while True:
    try:
        n = input()
    except EOFError:
        break

    if '<body>' in n:
        grava = True
        continue
    elif '</body>' in n:
        grava = False

    if grava and ('<body>' not in n) and ('</body>' not in n):
        print(n)
