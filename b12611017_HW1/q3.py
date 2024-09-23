check_num = int(input())
is_prime = 1
is_odd = 0

if(check_num % 2 == 0):
    is_odd = 0
else:
    is_odd = 1

for i in range(2, int(check_num ** 0.5) + 1):
    if check_num % i == 0:
        is_prime = 0
        break

if(check_num == 1):
    is_prime = 0
    is_odd = 1

if(is_prime == 0 and is_odd == 0):
    print("Not Prime,Even")

elif(is_prime == 1 and is_odd == 1):
    print("Prime,Odd")

elif(is_prime == 1 and is_odd == 0):
    print("Prime,Even")

elif(is_prime == 0 and is_odd == 1):
    print("Not Prime,Odd")