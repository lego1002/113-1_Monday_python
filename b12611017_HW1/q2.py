user_input = input().split(",")
character = user_input[0]
first = float(user_input[1])
second = float(user_input[2])

if(character == '+'):
    print("{:.2f}".format(first + second))
elif(character == '-'):
    print("{:.2f}".format(first - second))
elif(character == '*'):
    print("{:.2f}".format(first * second))
elif(character == "/"):
    if(second == 0):
        print("Error")
    else:
        print("{:.2f}".format(first / second))
