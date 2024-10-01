user_binary = input()
decimal_result = 0

for i in range(len(user_binary)):
    decimal_result += int(user_binary[i]) * (2 ** (len(user_binary) - 1 - i))

print(decimal_result)
