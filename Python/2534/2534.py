while True:
    try:
        n, m = [int(x) for x in input().split()]
        habitantes, res = [], []
        for i in range(n):
            habitantes.append(int(input()))
        for i in range(m):
            habitantes.sort(reverse=True)
            consulta = int(input())
            res.append(habitantes[consulta - 1])

        for i in range(len(res)):
            print(res[i])

    except EOFError:
        break
