N = int(input())

for i in range(0, N):
    K = int(input())

    for b in range(0, K):
        feed = int(input())
        if(feed == 1):  # Feedback Elogios
            print('Rolien')
        elif(feed == 2):  # Feedback Bugs
            print('Naej')
        elif(feed == 3):  # Feedback Duvidas
            print('Elehcim')
        elif(feed == 4):  # Feedback Sugestoes
            print('Odranoel')
