ehComplicado = False
while True:
    try:
        linha = input()
        if ehComplicado and linha != '':
            print()

        ehComplicado = True
        charsContados = {}
        for i in range(len(linha)):
            countChar = 0
            if linha[i] not in charsContados:
                countChar = linha.count(linha[i])
                charsContados[linha[i]] = countChar

        sortKeys = [v[0] for v in sorted(charsContados.items(), key=lambda kv: (-kv[1], kv[0]), reverse=True)]
        sortValues = [v[1] for v in sorted(charsContados.items(), key=lambda kv: (-kv[1], kv[0]), reverse=True)]

        for i in range(len(sortValues)):
            char = ord(sortKeys[i])
            print(char, sortValues[i])

    except EOFError:
        break
