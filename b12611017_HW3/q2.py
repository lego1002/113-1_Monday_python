#base_path = "/home/lego/Desktop/examples/"
q, a = map(str, input().split(","))
result = None

try:
    #with open(base_path + q, "r") as question:
    with open(q, "r") as question:
        calculation = question.readline().strip()
    parts = calculation.split(" ")

    if(len(parts) != 3):
        if(len(parts) == 2):
            if(parts[0] in ["+", "-", "*", "/"] and parts[1].isdigit()):
                print("Number1 lost")
            else:
                print("Operator lost")
    else:
        num1_str, operator, num2_str = parts
        num1 = float(num1_str)
        num2 = float(num2_str)

        if(operator == '+'):
            result = num1 + num2
        elif(operator == '-'):
            result = num1 - num2
        elif(operator == '*'):
            result = num1 * num2
        elif(operator == '/'):
            if(num2 == 0):
                print("Cannot divide by zero")
            else:
                result = num1 / num2

except FileNotFoundError:
    print("File not found")

#output_file_path = base_path + a
output_file_path = a

with open(output_file_path, "w") as answer:
    if(result is not None):
        answer.write(str(result))
        print("Successfully")
    else:
        pass

print("Execution completed")
