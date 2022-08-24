x, y = input().split()
x = float(x)
y = float(y)
result = 'Q1'

if(x == 0 and y == 0):
    result = 'Origem'
elif((x > 0 or x < 0) and y == 0):
    result = 'Eixo X'
elif((y > 0 or y < 0) and x == 0):
    result = 'Eixo Y'
elif(x > 0):
    if(y > 0):
        result = 'Q1'
    else:
        result = 'Q4'
elif(x < 0):
    if(y > 0):
        result = 'Q2'
    else:
        result = 'Q3'

print(result)
