import datetime
while True:
    try:
        hr, minuto = [int(x) for x in input().split(':')]
        acorda = datetime.datetime(2021, 5, 20, hr, minuto)
        chega = acorda + datetime.timedelta(0, 60 * 60)
        feira = datetime.datetime(2021, 5, 20, 8, 0)
        if chega > feira:
            atrasoMax = chega - feira
            minutos = atrasoMax.total_seconds() / 60
            print(f'Atraso maximo: {int(minutos)}')
        else:
            print('Atraso maximo: 0')

    except EOFError:
        break
