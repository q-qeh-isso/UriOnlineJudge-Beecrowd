A = []
for i in range(100):
    A.append(input())

for b in range(len(A)):
    if(float(A[b]) <= 10):
        print(f'A[{b}] = {float(A[b]):.1f}')
