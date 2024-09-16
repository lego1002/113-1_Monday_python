user_input = input().split(", ")
character = user_input[0]
first = float(user_input[1])
second = float(user_input[2])

if(character == '+'):
    print(f"{first + second:.2f}")
elif(character == '-'):
    print(f"{first - second:.2f}")
elif(character == '*'):
    print(f"{first * second:.2f}")
elif(character == "/"):
    if(second == 0):
        print("Error")
    else:
        print(f"{first / second:.2f}")
