while True:
    try:
        n = int(input())
        msg = 'vai ter copa!'
        if n != 0:
            msg = 'vai ter duas!'
        print(msg)

    except EOFError:
        break
