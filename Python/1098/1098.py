i = 0
j = 1
while i <= 2:
    for k in range(3):
        if i % 2 == 0 or i % 2 == 1 or i > 1.8:
            print(f'I={i:.0f} J={j + k:.0f}')
        else:
            print(f'I={i:.1f} J={j + k:.1f}')

    i += 0.2
    j += 0.2
