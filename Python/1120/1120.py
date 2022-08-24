while True:
    dig, n = input().split()
    if dig == '0' and n == '0':
        break

    res = ''
    for i in n:
        if i != dig:
            res += i

    res = res.lstrip('0')
    if res == '0' or res == '' or res.count('0') == len(res):
        res = '0'

    print(res)
