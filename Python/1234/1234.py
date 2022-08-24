while True:
    try:
        sent = input()
        sent = sent.lower()
    except EOFError:
        break

    i = 0
    new = ''
    chaveia = True
    while i < len(sent):
        if sent[i] == ' ':
            new += sent[i]
        elif sent[i].isalpha():
            if chaveia:
                new += sent[i].upper()
                chaveia = False
            else:
                new += sent[i]
                chaveia = True
        else:
            new += sent[i]

        i += 1

    print(new)
