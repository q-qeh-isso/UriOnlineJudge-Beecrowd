num = float(input())
result = 'Fora de intervalo'

if(num >= 0 and num <= 25):
    result = 'Intervalo [0,25]'
elif(num >= 25 and num <= 50):
    result = 'Intervalo (25,50]'
elif(num >= 75 and num <= 100):
    result = 'Intervalo (75,100]'

print(result)
