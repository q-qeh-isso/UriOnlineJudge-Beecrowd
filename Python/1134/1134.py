opt = 0
alcool = 0
gasolina = 0
diesel = 0
while opt != 4:
    opt = int(input())
    if opt == 4:
        break

    if opt == 1:
        alcool += 1
    elif opt == 2:
        gasolina += 1
    elif opt == 3:
        diesel += 1

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
