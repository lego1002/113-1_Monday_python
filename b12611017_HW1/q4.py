entered_str = input()
sum = 0
for char in entered_str:
    if char.isdigit(): 
        sum += int(char)

print(f"{sum},{len(entered_str)}")