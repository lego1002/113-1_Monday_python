def factorial(x):
    if(x == 1):
        return 1
    else:
        return(x * factorial(x - 1))
k, n = map(int, input().split(" "))



if(n < k):
    print("Error! k > n, please input again!")
else:
    answer = factorial(n) / factorial(n - k) / factorial(k)
    print(int(answer))