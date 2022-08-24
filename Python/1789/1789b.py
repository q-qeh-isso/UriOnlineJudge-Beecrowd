while True:
    try:
        l = int(input())
        lesmas = [int(x) for x in input().split()]
        lesmas.sort()
        maior = lesmas[-1]

        if(maior >= 20):
            print('3')
        elif(10 <= maior < 20):
            print('2')
        else:
            print('1')

    except EOFError:
        break
