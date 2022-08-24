# from datetime import *
from datetime import date
while True:
    try:
        n, d = [int(x) for x in input().split()]
        datas = []
        mData = ''
        for i in range(d):
            data, pessoas = input().split(' ', 1)
            d, m, y = [int(x) for x in data.split('/')]
            dt = date(y, m, d)
            if pessoas.count('1') == n:
                mData = dt

            datas.append([dt, pessoas])
            # date = datetime.strptime(str_date, '%d/%m/%Y').date()

        combinado = False
        if len(datas) > 0:
            for i in range(len(datas)):
                if datas[i][1].count('1') == n:
                    combinado = True
                    if datas[i][0] <= mData:
                        mData = datas[i][0]

        if combinado:
            print(f'{mData.day}/{mData.month}/{mData.year}')
        else:
            print('Pizza antes de FdI')

    except EOFError:
        break
