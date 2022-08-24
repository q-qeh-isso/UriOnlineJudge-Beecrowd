joias = set()
while True:
    try:
        q = input()
        joias.add(q)

    except EOFError:
        break

print(len(joias))
