n = int(input())
for i in range(n):
    placa = input()

    rodizio = ''
    if '-' in placa:
        letra, num = placa.split('-')
        if not (letra.isalpha() and letra.isupper() and len(letra) == 3 and num.isnumeric() and len(num) == 4):
            rodizio = 'FAILURE'
        else:
            last = int(num[-1])
            if last == 1 or last == 2:
                rodizio = 'MONDAY'
            elif last == 3 or last == 4:
                rodizio = 'TUESDAY'
            elif last == 5 or last == 6:
                rodizio = 'WEDNESDAY'
            elif last == 7 or last == 8:
                rodizio = 'THURSDAY'
            elif last == 9 or last == 0:
                rodizio = 'FRIDAY'
    else:
        rodizio = 'FAILURE'

    print(rodizio)
