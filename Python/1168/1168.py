n = int(input())

for k in range(n):
    num = input()
    leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6, 6]

    ledsQtd = 0
    for i in num:
        ledsQtd += leds[int(i)]

    print(ledsQtd, 'leds')
