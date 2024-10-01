def check_prime(x):
    if(x == 1):
        return False
    if(x == 2):
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if(x % i == 0):
            return False
    return True

RANGE = input().split()
N1 = int(RANGE[0])
N2 = int(RANGE[1])

index = N1
result = []

while (index <= N2):
    if(check_prime(index)):
        result.append(index)
    index += 1

if(len(result) == 0):
    print(0)
else:
    print(",".join((str(x) for x in result)))
