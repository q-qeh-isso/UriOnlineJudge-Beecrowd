while True:
    try:
        dodo, leo, pepper = input().split()
        if ((dodo == 'papel' and leo == 'pedra' and pepper == 'pedra') or
            (dodo == 'pedra' and leo == 'tesoura' and pepper == 'tesoura') or
            (dodo == 'tesoura' and leo == 'papel' and pepper == 'papel')):
            print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
        elif ((leo == 'papel' and pepper == 'pedra' and dodo == 'pedra') or
            (leo == 'pedra' and pepper == 'tesoura' and dodo == 'tesoura') or
            (leo == 'tesoura' and pepper == 'papel' and dodo == 'papel')):
            print("Iron Maiden's gonna get you, no matter how far!")
        elif ((pepper == 'papel' and leo == 'pedra' and dodo == 'pedra') or
            (pepper == 'pedra' and leo == 'tesoura' and dodo == 'tesoura') or
            (pepper == 'tesoura' and leo == 'papel' and dodo == 'papel')):
            print('Urano perdeu algo muito precioso...')
        else:
            print('Putz vei, o Leo ta demorando muito pra jogar...')

    except EOFError:
        break
