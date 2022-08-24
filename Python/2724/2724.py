n = int(input())
for p in range(n):
    t = int(input())

    fPerigosas = []
    jExp = []
    for i in range(t):
        fPerigosas.append(input())
    u = int(input())
    for i in range(u):
        juvForm = input()
        jExp.append(juvForm)

        ehBomba = False
        for k in range(len(fPerigosas)):
            if fPerigosas[k] in juvForm:
                formula = juvForm.index(fPerigosas[k])
                word = juvForm[formula:formula + len(fPerigosas[k])]
                if formula == 0 and len(juvForm) == len(fPerigosas[k]):
                    ehBomba = True
                    break
                elif formula == len(juvForm) - len(fPerigosas[k]):
                    ehBomba = True
                    break
                elif word[-1].isdecimal() and juvForm[formula + len(word)].isalpha() and juvForm[formula + len(word)].isupper():
                    ehBomba = True
                    break
                elif word[-1].isalpha() and juvForm[formula + len(word)].isalpha() and juvForm[formula + len(word)].isupper():
                    ehBomba = True
                    break

        if ehBomba:
            print('Abortar')
        else:
            print('Prossiga')

    if p != n - 1:
        print()
