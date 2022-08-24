a, b, c = [int(i) for i in input().split()]
msg = ':)'
if a > b and c >= b:
    msg = ':)'
elif a < b and c <= b:
    msg = ':('
elif (a < b and b < c) and c - b < b - a:
    msg = ':('
elif (a < b and b < c) and c - b >= b - a:
    msg = ':)'
elif (a > b and b > c) and b - c < a - b:
    msg = ':)'
elif (a > b and b > c) and b - c >= a - b:
    msg = ':('
elif a == b and c > b:
    msg = ':)'
else:
    msg = ':('

print(msg)
