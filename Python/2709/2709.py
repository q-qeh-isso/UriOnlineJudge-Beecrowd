while True:
    try:
        m = int(input())
        moedas = []
        for i in range(m):
            moedas.append(int(input()))
        n = int(input())

        soma = 0
        for i in range(len(moedas) - 1, -1, -n):
            soma += moedas[i]

        ehPrimo = True
        if soma > 1:
            for i in range(2, soma):
                if soma % i == 0:
                    ehPrimo = False
                    break
        else:
            ehPrimo = False

        if ehPrimo:
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")

    except EOFError:
        break
