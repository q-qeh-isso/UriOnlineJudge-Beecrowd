count = 0
media = 0

while (True):
    num = int(input())

    if(num < 0):
        break

    media += num
    count += 1

media = media / count
print(f'{media:.2f}')
