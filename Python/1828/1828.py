t = int(input())
for i in range(0, t):
    s, r = input().split()
    if s == r:
        print(f'Caso #{i + 1}: De novo!')
    elif ((s == 'tesoura' and r == 'papel') or
            (s == 'papel' and r == 'pedra') or
            (s == 'pedra' and r == 'lagarto') or
            (s == 'lagarto' and r == 'Spock') or
            (s == 'Spock' and r == 'tesoura') or
            (s == 'tesoura' and r == 'lagarto') or
            (s == 'lagarto' and r == 'papel') or
            (s == 'papel' and r == 'Spock') or
            (s == 'Spock' and r == 'pedra') or
            (s == 'pedra' and r == 'tesoura')):
        print(f'Caso #{i + 1}: Bazinga!')
    else:
        print(f'Caso #{i + 1}: Raj trapaceou!')
