while True:
    try:
        disciplinas = int(input())

        ira = 0
        somatoriaNotas = 0
        somatoriaCargas = 0
        for i in range(disciplinas):
            nota, cargaHr = [int(x) for x in input().split()]
            somatoriaNotas += nota * cargaHr
            somatoriaCargas += cargaHr

        ira = somatoriaNotas / (somatoriaCargas * 100)

        print(f'{ira:.4f}')
    except EOFError:
        break
