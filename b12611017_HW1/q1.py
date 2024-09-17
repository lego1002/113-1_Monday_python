user_info = input().split()
height = float(user_info[0])
weight = float(user_info[1])
bmi_value = weight / height / height
print("{:.2f}".format(bmi_value))

