s = input()
b = '0'
countOnes = s.count('1')
if countOnes % 2 != 0:
    b = '1'

s += b
print(s)
