d = int(input())
pts = 0
if 0 <= d <= 800:
    pts = 1
elif 800 < d <= 1400:
    pts = 2
elif 1400 < d <= 2000:
    pts = 3

print(pts)
