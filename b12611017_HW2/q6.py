from datetime import datetime

def calculate_date_difference(date_input):
    try:
        date1_str, date2_str = date_input.split(",")
        date1 = datetime.strptime(date1_str.strip(), "%Y-%m-%d")
        date2 = datetime.strptime(date2_str.strip(), "%Y-%m-%d")
        date_difference = abs((date2 - date1).days)
        return date_difference

    except ValueError:
        return("Invalid")

date_input = input()
result = calculate_date_difference(date_input)
print(result)
