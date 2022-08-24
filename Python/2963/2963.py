n = int(input())
votes = []
for i in range(n):
    votes.append(int(input()))

big = votes[0]
for i in range(1, len(votes)):
    if votes[i] > big:
        big = votes[i]

if big > votes[0]:
    print('N')
else:
    print('S')
