def check_prime(x):
    if(x == 1):
        return False
    if(x == 2):
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if(x % i == 0):
            return False
    return True

user_input = input().split(" ")
N1 = int(user_input[0])
N2 = int(user_input[1])
is_prime = []

for i in range(N1, N2 + 1):
    if check_prime(i):
        is_prime.append(i)

if(len(is_prime) == 0):
    print(0)
else:
    for i in range(len(is_prime)):
        if(i == len(is_prime) - 1):
            print(is_prime[i], end = "\n" )
        else:
            print(is_prime[i], end = ',')
