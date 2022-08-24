notas = 0
media = 0
while notas < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        notas += 1
        media += nota
    else:
        print('nota invalida')

print(f'media = {media/notas}')
