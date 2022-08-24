t, d = map(int, input().split())

msg = ''
dif = d - t
if dif > 0:
    if dif <= 2 and t:
        msg = 'Parece o trabalho do meu filho!\n'
        correcao = d + 2
        if correcao <= 24:
            msg += 'TCC Apresentado!'
        else:
            msg += 'Fail! Entao eh nataaaaal!'
    elif dif >= 3:
        msg = 'Muito bem! Apresenta antes do Natal!'
else:
    msg = 'Eu odeio a professora!'

print(msg)
