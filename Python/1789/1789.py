while True:
    try:
        l = int(input())
        lesmas = [int(x) for x in input().split()]
        maior = 0
        for i in range(len(lesmas)):
            if lesmas[i] > maior:
                maior = lesmas[i]

        if(maior >= 20):
            print('3')
        elif(10 <= maior < 20):
            print('2')
        else:
            print('1')

    except EOFError:
        break