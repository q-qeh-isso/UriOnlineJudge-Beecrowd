x = int(input())
z = 0

count = 0
while True:
    z = int(input())
    if z > x:
        break

soma = 0
while soma < z:
    if soma + x < z:
        soma += x
        count += 1
    else:
        count += 1
        break
    x += 1

print(count)
