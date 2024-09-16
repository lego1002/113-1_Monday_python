user_info = input().split()
height = float(user_info[0])
weight = float(user_info[1])
bmi_value = weight / height / height
print(f"{bmi_value:.2f}")
