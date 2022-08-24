while True:
    pesquisadas = []
    pesquisa = []
    try:
        n = int(input())
        for i in range(n):
            pesquisadas.append(input())
        q = int(input())
        for i in range(q):
            pesquisa.append(input())

        for i in range(len(pesquisa)):
            encontradas = []
            for k in range(len(pesquisadas)):
                if pesquisa[i] == pesquisadas[k][:len(pesquisa[i])]:
                    encontradas.append(pesquisadas[k])

            largerWord = 0
            for i in range(len(encontradas)):
                if len(encontradas[i]) >= largerWord:
                    largerWord = len(encontradas[i])

            if len(encontradas) == 0:
                print(-1)
            else:
                print(len(encontradas), largerWord)

    except EOFError:
        break
