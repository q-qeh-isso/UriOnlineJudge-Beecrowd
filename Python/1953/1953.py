while True:
    try:
        n = int(input())
        EPR = 0
        EHD = 0
        INTRUSOS = 0

        # if(n <= 0):
        #    break

        for i in range(0, n):
            matricula, curso = input().split()

            if(curso == 'EPR'):
                EPR += 1
            elif(curso == 'EHD'):
                EHD += 1
            else:
                INTRUSOS += 1

        print(f'EPR: {EPR}')
        print(f'EHD: {EHD}')
        print(f'INTRUSOS: {INTRUSOS}')

    except EOFError:
        break
