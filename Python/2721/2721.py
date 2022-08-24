n = sum([int(x) for x in input().split()])
renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

print(renas[(n % len(renas)) - 1])
