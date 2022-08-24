while True:
    try:
        n = input()
    except EOFError:
        break

    firstIdx = 0
    if n.find('_') != -1:
        itaIdx = n.find('_')
    else:
        itaIdx = -1

    if n.find('*') != -1:
        boldIdx = n.find('*')
    else:
        boldIdx = -1

    if itaIdx == -1 and boldIdx >= 0:
        firstIdx = boldIdx
    elif boldIdx == -1 and itaIdx >= 0:
        firstIdx = itaIdx
    elif itaIdx < boldIdx:
        firstIdx = itaIdx
    elif itaIdx > boldIdx:
        firstIdx = boldIdx

    res = ''
    if firstIdx > 0:
        res += n[:firstIdx]

    i = firstIdx
    keyIta = False
    keyBold = False
    while i < len(n):
        if n[i] == '_':
            if keyIta:
                res += '</i>'
                keyIta = False
            else:
                res += '<i>'
                keyIta = True
        elif n[i] == '*':
            if keyBold:
                res += '</b>'
                keyBold = False
            else:
                res += '<b>'
                keyBold = True
        else:
            res += n[i]

        i += 1

    print(res)
