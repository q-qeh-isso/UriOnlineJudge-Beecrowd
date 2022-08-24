N = int(input())

horas = N // 60 // 60
minutos = (N - (horas * 60 * 60)) // 60
segundos = N - ((horas * 60 * 60) + (minutos * 60))


print(f'{horas}:{minutos}:{int(segundos)}')
