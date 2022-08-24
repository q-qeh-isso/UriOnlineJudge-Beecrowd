A, B = input().split()
A = int(A)
B = int(B)
result = 'Nao sao Multiplos'

if (A % B == 0 or B % A == 0):
    result = 'Sao Multiplos'

print(result)
