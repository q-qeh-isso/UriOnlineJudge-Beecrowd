from datetime import datetime
while True:
    try:
        mes, dia = input().split()
        if len(mes) == 1:
            mes = '0' + mes
        if len(dia) == 1:
            dia = '0' + dia

        dtAtual = datetime(2016, int(mes), int(dia))
        dtNatal = datetime(2016, 12, 25)
        dif = (dtNatal - dtAtual).days
        if dif == 0:
            print('E natal!')
        elif dif == 1:
            print('E vespera de natal!')
        elif dif < 0:
            print('Ja passou!')
        else:
            print(f'Faltam {dif} dias para o natal!')

    except EOFError:
        break
