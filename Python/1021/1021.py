N = float(input())

nota100 = N // 100
nota50 = (N % 100) // 50
nota20 = ((N % 100) % 50) // 20
nota10 = (((N % 100) % 50) % 20) // 10
nota5 = ((((N % 100) % 50) % 20) % 10) // 5
nota2 = (((((N % 100) % 50) % 20) % 10) % 5) // 2
moeda1 = ((((((N % 100) % 50) % 20) % 10) % 5) % 2) // 1

moedas = int((((((((N % 100) % 50) % 20) % 10) % 5) % 2) % 1) * 100)
moeda50 = moedas // 50
moeda25 = (moedas % 50) // 25
moeda10 = ((moedas % 50) % 25) // 10
moeda05 = (((moedas % 50) % 25) % 10) // 5
moeda01 = ((((moedas % 50) % 25) % 10) % 5) // 1

print('NOTAS:')
print(f'{int(nota100)} nota(s) de R$ 100.00')
print(f'{int(nota50)} nota(s) de R$ 50.00')
print(f'{int(nota20)} nota(s) de R$ 20.00')
print(f'{int(nota10)} nota(s) de R$ 10.00')
print(f'{int(nota5)} nota(s) de R$ 5.00')
print(f'{int(nota2)} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{int(moeda1)} moeda(s) de R$ 1.00')
print(f'{int(moeda50)} moeda(s) de R$ 0.50')
print(f'{int(moeda25)} moeda(s) de R$ 0.25')
print(f'{int(moeda10)} moeda(s) de R$ 0.10')
print(f'{int(moeda05)} moeda(s) de R$ 0.05')
print(f'{int(moeda01)} moeda(s) de R$ 0.01')
