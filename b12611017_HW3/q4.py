x, y = map(int, input().split())

for i in range(1, y):
    if(x % 2 == 0):
        x = x / 2 + 1
    else:
        x = x * 5 - 3

print(int(x))
