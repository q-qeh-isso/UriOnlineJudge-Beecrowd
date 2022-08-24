N = int(input())

anos = N // 365
meses = (N - (anos * 365)) // 30
dias = N - ((anos * 365) + (meses * 30))

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
