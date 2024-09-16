check_password = input()
len_of_pass = len(check_password)

if(len_of_pass < 6):
    print("weak")
elif(len_of_pass >= 6 and len_of_pass <= 10):
    print("Medium")
elif(len_of_pass > 10):
    print("strong")